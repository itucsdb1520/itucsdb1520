import datetime
import os
import json
import re
import psycopg2 as dbapi2


from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request

import mimetypes

mimetypes.add_type('image/svg+xml', '.svg')

app = Flask(__name__)

class Brand:
    def __init__(self, name, description, year, image_link, website, industry):
        self.name = name
        self.description = description
        self.year = year
        self.image_link = image_link
        self.website = website
        self.industry = industry

class Car:
    def __init__(self, car_name, engine_name, speed_limit, zero_hundred, brand, pilot):
        self.car_name = car_name
        self.engine_name = engine_name
        self.speed_limit = speed_limit
        self.zero_hundred = zero_hundred
        self.brand = brand
        self.pilot = pilot



def get_elephantsql_dsn(vcap_services):
    """Returns the data source name for ElephantSQL."""
    parsed = json.loads(vcap_services)
    uri = parsed["elephantsql"][0]["credentials"]["uri"]
    match = re.match('postgres://(.*?):(.*?)@(.*?)(:(\d+))?/(.*)', uri)
    user, password, host, _, port, dbname = match.groups()
    dsn = """user='{}' password='{}' host='{}' port={}
             dbname='{}'""".format(user, password, host, port, dbname)
    return dsn

@app.route('/')
@app.route('/home')
def home():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/pilots')
def pilots():
    now = datetime.datetime.now()
    pilots = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM PILOTS"""
            print(query)
            cursor.execute(query)

            for pilot in cursor:
                pilots.append(pilot)

            connection.commit()
            print(pilots)
    return render_template('pilots.html', pilots=pilots, current_time=now.ctime())





@app.route('/add_pilot', methods = ['GET','POST'])
def add_pilot():
    now = datetime.datetime.now()
    if request.method =='POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO PILOTS (Name, Surname, Age) VALUES ('""" +name +"""', '"""+ surname + """', """+ age + """)"""
            print(query)
            cursor.execute(query)
            connection.commit()


    return redirect(url_for('pilots'))

@app.route('/delete_pilot', methods = ['GET','POST'])
def delete_pilot():
    now = datetime.datetime.now()
    if request.method =='POST':
        id = request.form['id']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM PILOTS WHERE Id = '""" +id + """' """
            cursor.execute(query)
            connection.commit()


    return redirect(url_for('pilots'))

@app.route('/cars')
def cars():
    now = datetime.datetime.now()
    cars_list = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM CARS"""

            cursor.execute(query)

            for record in cursor:
                cars_list.append(record)
            connection.commit()
            print(cars_list)
    return render_template('cars.html', cars_list=cars_list, current_time=now.ctime())


@app.route('/tracks')
def tracks():
    now = datetime.datetime.now()
    return render_template('tracks.html', current_time=now.ctime())

@app.route('/brands')
def brands():
    now = datetime.datetime.now()
    return render_template('brands.html', current_time=now.ctime())

@app.route('/brand/<the_brand>')
def brand(the_brand):
    now = datetime.datetime.now()

    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT * FROM BRANDS WHERE Name = '""" + the_brand + """' """
        cursor.execute(query)
        connection.commit()

        brand_info = []

        brand_info = cursor.fetchone()
        print(brand_info)

        if not brand_info:
            name = "NONAME"
            description = "NO DESCRIPTION"
            year = 1800
            image_link = "no_logo.svg"
            industry = "NO INDUSTRY"
            website = "itucsdb1520.mybluemix.net"
        else:
            name = brand_info[1].strip()
            description = brand_info[2].strip()
            year = brand_info[3]
            image_link = brand_info[4].strip()
            industry = brand_info[5].strip()
            website = brand_info[6].strip()

    return render_template('brand.html', name=name, description=description, year=year, image_link=image_link, industry=industry, website=website, current_time=now.ctime())

@app.route('/brands_db/<operation>' , methods = ['GET','POST'])
def brands_db(operation):
    now = datetime.datetime.now()
    splitted = operation.split('-', 1)
    operation = splitted[0]

    print(splitted)
    try:
        sub_operation = splitted[1]
        make_sub_operation = True
    except:
        print("Single String, not splitted")
        make_sub_operation = False

    if operation == "list":
        #print("On the list")
        brands_list = []
        if make_sub_operation == True:
            if sub_operation == 'name':
                sort = "Name"
            elif sub_operation == 'industry':
                sort = "Industry"
            elif sub_operation == 'year':
                sort = "Foundation"
            elif sub_operation == 'website':
                sort = "Website"
            elif sub_operation == 'image':
                sort = "Image"
            elif sub_operation == 'comment':
                sort = "Comment"
            else:
                sort = "Id"

        with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """SELECT * FROM BRANDS"""
                if make_sub_operation == True:
                    query = query + """ ORDER BY """ + sort
                print(query)
                cursor.execute(query)

                for record in cursor:
                    brands_list.append(record)

                connection.commit()
                #print(brands_list)
        return render_template('brands_db.html', brands_list=brands_list, current_time=now.ctime())

    elif operation == "add":
        #print("On the add")
        if request.method =='POST':
            brand_name = request.form['brand-name']
            description = request.form['description']
            foundation = request.form['foundation']
            imagelink = request.form['imagelink']
            website = request.form['website']
            industry = request.form['industry']

            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO BRANDS (Name, Comment, Foundation, Image, Industry, Website) VALUES (%s, %s, %s, %s, %s, %s);"""
                cursor.execute(query, (brand_name,description,foundation,imagelink,industry,website))
                connection.commit()


        return redirect(url_for('brands_db', operation = 'list'))

    elif operation == "delete":
        #print("On delete")
        if request.method == 'POST':
            brand_id = request.form['delete']
            print(brand_id)
            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM BRANDS WHERE Id = %s ", ([brand_id]))
                connection.commit()

    elif operation == "edit":
        print("EDIT")
        if request.method == 'POST':

            new_name = request.form['brand-name']
            new_description = request.form['description']
            new_foundation = request.form['foundation']
            new_imagelink = request.form['imagelink']
            new_website = request.form['website']
            new_industry = request.form['industry']
            edit = request.form['edit']

            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """UPDATE BRANDS SET (Name, Comment, Foundation,  Image, Industry, Website) = (%s,%s,%s,%s,%s,%s) WHERE ID = %s;"""
                cursor.execute(query, (new_name, new_description, new_foundation, new_imagelink, new_industry, new_website, edit))
                connection.commit()

    return redirect(url_for('brands_db', operation = 'list'))


@app.route('/about')
def about():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())

@app.route('/statistics')
def statistics():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())

@app.route('/car_add',methods = ['GET','POST'])
def car_add():
    if request.method =='POST':
        image_link = request.form['image_link']
        car_name = request.form['car_name']
        engine_name = request.form['engine_name']
        speed_limit = request.form['speed_limit']
        zero_hundred = request.form['0_100_kmh']
        brand = request.form['brand']
        pilot = request.form['pilot']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO CARS (Image_Link, Name, Engine_Name,Speed,Zero_Hundred, BRAND, PILOT) VALUES
            ('"""+image_link+"""', '"""+car_name+"""', '"""+engine_name+"""', """+speed_limit+""", """+zero_hundred+""",
             '"""+brand+"""', '"""+pilot+"""')"""
            print(query)

            cursor.execute(query)
            connection.commit()

        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')


@app.route('/car_delete',methods = ['GET','POST'])
def car_delete():
    if request.method =='POST':
        id = request.form['id']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM CARS WHERE Id="""+id+""""""


            cursor.execute(query)
            connection.commit()
        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_delete.html')




#these are for testing will be edited later
@app.route('/initdb')
def initialize_database():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        #Database for the counter
        cursor.execute("""DROP TABLE IF EXISTS COUNTER""")
        cursor.execute("""CREATE TABLE COUNTER (N INTEGER)""")
        cursor.execute("""INSERT INTO COUNTER (N) VALUES (0)""")


        #database for the brands
        cursor.execute("""DROP TABLE IF EXISTS BRANDS""")
        cursor.execute("""CREATE TABLE BRANDS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Comment CHAR(75), Foundation INTEGER, Image Char(50), Industry CHAR(20), Website CHAR(25))""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Shell', 'One of the biggest petrochemistry companies in the world', 1907, 'shell_logo.svg', 'Oil Distribution', 'www.shell.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Kaspersky', 'An Antivirus Company founded in Moskov', 1997, 'Kaspersky_lab_logo.svg', 'Computer Security', 'www.kaspersky.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Pirelli', 'A Tire Company, founded in Milano as a plastic manufacturer', 1872, 'Pirelli_logo.svg', 'Auto and Parts', 'www.pirelli.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('UPS', 'A Parcel Service founded as post company in Seattle', 1907, 'UPS.svg', 'Courier', 'www.ups.com')""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Santander', '(Formerly Sovereign Bank) A subsidiary of Spanish Santander Group', 1875, 'Banco_Santander.svg', 'National Banks', 'www.santanderbank.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Alfa Romeo', 'An automobile manufacturer founded by an aristocrat family', 1910, 'Alfa_Romeo.svg', 'Automotive', 'www.alfaromeo.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Hublot', 'A clock manufacturer company', 1980, 'Hublot_logo.svg', 'Watchmaking', 'www.hublot.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Weichai', 'A Manufacturer and salesman of diesel engines', 2002, 'Weichai_Logo.svg', 'Automotive', 'www.weichai.com')""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('OMR', 'A car and motor manufacturer company', 1919, 'OMR_logo.png', 'Automotive', 'www.omrautomotive.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Mahle', 'An automotive parts manufacturer and one of the largest part suppliers', 1920, 'Mahle_logo.svg', 'Automotive', 'www.mahle.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Telcel', 'A wireless telecommunication company, originally named as Radio Movil Dipsa', 1984, 'Telcel_logo.svg', 'Telecommunication', 'www.telcel.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Brembo', 'A manufacturer of automotive brake systems especially for high-end cars', 1961, 'Brembo_logo.svg', 'Automotive', 'www.brembo.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('NGK Spark Plug', 'A manufacturer and saler of spark plugs and combustion engines', 1936, 'Ngk_logo_rund.svg', 'Spark Plugs', 'www.ngkntk.co.jp') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Magneti Marelli', 'A company which deals with development and manufacturing of systems', 1919, 'Marelli_logo.png', 'Automotive', 'www.magnetimarelli.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('SKF', 'A leading bearing and seals manufacturing company', 1907, 'SKF_logo.svg', 'Manufacturing', 'www.skf.com') """)
        cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('HAAS', 'A machine and CNC tools manufacturer founded in California', 1983, 'Haas_logo.jpg', 'Manufacturing', 'www.haascnc.com') """)
        
        
        #database for the cars
        cursor.execute("""DROP TABLE IF EXISTS CARS""")
        cursor.execute("""CREATE TABLE CARS (Id SERIAL PRIMARY KEY NOT NULL, Image_Link TEXT, Name CHAR(30),Engine_Name CHAR(30),Speed INTEGER, Zero_Hundred INTEGER,BRAND CHAR(50),PILOT CHAR(50) )""")

        #database for the pilots
        cursor.execute("""DROP TABLE IF EXISTS PILOTS""")
        cursor.execute("""CREATE TABLE PILOTS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Surname CHAR(25), Age INTEGER )""")
        
        



        connection.commit()
    return redirect(url_for('home'))

@app.route('/counter')
def counter_page():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        cursor.execute("""UPDATE COUNTER SET N = N + 1""")
        connection.commit()

        cursor.execute("""SELECT N FROM COUNTER""")



        count = cursor.fetchone()[0]
    return "This page was accessed %d times." % count

#end of test

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

#with app.test_request_context():
    #print(url_for('about'))
    #print(url_for('brand', the_brand = 'Shell'))
    #print(url_for('brands', next='/'))


if __name__ == '__main__':
    VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
    if VCAP_APP_PORT is not None:
        port, debug = int(VCAP_APP_PORT), False
    else:
        port, debug = 5000, True

    VCAP_SERVICES = os.getenv('VCAP_SERVICES')
    if VCAP_SERVICES is not None:
        app.config['dsn'] = get_elephantsql_dsn(VCAP_SERVICES)
    else:
        app.config['dsn'] = """user='vagrant' password='vagrant'
                               host='localhost' port=54321 dbname='itucsdb'"""

    app.run(host='0.0.0.0', port=port, debug=debug)
