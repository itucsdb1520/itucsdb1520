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


def add_countries():
    now = datetime.datetime.now()
    if request.method =='POST':
        countries = request.form['countries']
        ForeignKey = request.form['ForeignKey']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO PILOTS (Countries, ForeignKey) VALUES ('""" +Countries +"""', """+ ForeignKey + """)"""
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


@app.route('/delete_countries', methods = ['GET','POST'])
def delete_countries():
    now = datetime.datetime.now()
    if request.method =='POST':
        id = request.form['id']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM COUNTRIES WHERE Id = '""" +id + """' """
            cursor.execute(query)
            connection.commit()


    return redirect(url_for('pilots'))



@app.route('/cars')
def cars():
    now = datetime.datetime.now()
    cars_list = []
    engine_list = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,ENGINES.HorsePower,CARS.Speed,CARS.BRAND,CARS.PILOT FROM CARS,ENGINES WHERE (CARS.Engine_ID = ENGINES.Id )"""


            cursor.execute(query)

            for record in cursor:
                cars_list.append(record)
            connection.commit()

            query = """SELECT Engine_Name,HorsePower FROM ENGINES"""
            cursor.execute(query)
            for record in cursor:
                engine_list.append(record)

    return render_template('cars.html', engine_list = engine_list, cars_list=cars_list, current_time=now.ctime())


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

#listing of brands
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



#about page
@app.route('/about')
def about():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())

#statistics page may be implemented in future
@app.route('/statistics')
def statistics():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())

@app.route('/car_add',methods = ['GET','POST'])
def car_add():
    if request.method =='POST':
        image_link = request.form['image_link']
        car_name = request.form['car_name']
        engine_id = request.form['engine_id']
        speed_limit = request.form['speed_limit']
        brand = request.form['brand']
        pilot = request.form['pilot']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO CARS (Image_Link, Name, Engine_ID,Speed, BRAND, PILOT) VALUES (%s,%s,%s,%s,%s,%s)"""
            print(query)

            cursor.execute(query,(image_link,car_name,engine_id,speed_limit,brand,pilot))
            connection.commit()

        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')


@app.route('/engine_add',methods = ['GET','POST'])
def engine_add():
    if request.method =='POST':
        engine_name = request.form['engine_name']
        horsepower = request.form['horsepower']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO ENGINES (Engine_Name, HorsePower) VALUES (%s,%s)"""
            print(query)

            cursor.execute(query,(engine_name,horsepower))
            connection.commit()

        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')


@app.route('/car_delete',methods = ['GET','POST'])
def car_delete():
    if request.method =='POST':
        car_name = request.form['car_name']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM CARS WHERE Name=%s"""
            cursor.execute(query,([car_name]))
            connection.commit()
        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_delete.html')


@app.route('/engine_delete',methods = ['GET','POST'])
def engine_delete():
    if request.method =='POST':
        engine_name = request.form['engine_name']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM ENGINES WHERE Engine_Name=%s"""
            cursor.execute(query,([engine_name]))
            connection.commit()
        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_delete.html')

#the search method
@app.route('/search', methods = ['GET','POST'])
def search():
    now = datetime.datetime.now()
    if request.method == 'POST':
        search = request.form['input_text']
        area = request.form['search_area']
        #print(search)
        #print(area)

        query_list = []

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            if area == '0':
                #Search all
                query = """ """

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 0)
            elif area == '1':
                #search cars
                search = "%" +search + "%"
                query = """ SELECT * FROM CARS WHERE Name LIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 1)
            elif area == '2':
                #search pilots
                query = """ """

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 2)
            elif area == '3':
                #search tracks
                query = """ """

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 3)
            elif area == '4':
                #search brands
                search = "%" + search + "%"
                query = """SELECT * FROM BRANDS WHERE Name LIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT * FROM BRANDS WHERE Industry LIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT * FROM BRANDS WHERE Comment LIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query_list = list(set(query_list))
                #remove duplicate elements in the list
                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 4)

            else:
                query = """ """
                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = [])

#these are for testing will be edited later
@app.route('/initdb')
def initialize_database():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        #Database for the counter
        cursor.execute("""DROP TABLE IF EXISTS COUNTER""")
        cursor.execute("""CREATE TABLE COUNTER (N INTEGER)""")
        cursor.execute("""INSERT INTO COUNTER (N) VALUES (0)""")


        #Database for the admins



        #Database for the users


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
        cursor.execute("""DROP TABLE IF EXISTS ENGINES""")

        cursor.execute("""CREATE TABLE ENGINES(Id SERIAL PRIMARY KEY,Engine_Name CHAR(30), HorsePower CHAR(30)) """)
        cursor.execute("""CREATE TABLE CARS (Image_Link TEXT, Name CHAR(30) UNIQUE PRIMARY KEY NOT NULL,Engine_ID INTEGER references ENGINES(Id),Speed CHAR(30),BRAND CHAR(50),PILOT CHAR(50) )""")

        cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('R13','300')""")
        cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('H15','320')""")
        cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('T15','350')""")

        cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.parrola.com/wp-content/uploads/2013/01/mclaren-mercedes-formula-1.jpg','V13',1,'300','Mercedes','Fernando Alonso')""")
        cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.f1fanatic.co.uk/wp-content/uploads/2008/01/ferrari_f2008_launch_4.jpg','MH13',2,'320','Ferrari','James Hamilton' )""")
        cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.autoguide.com/auto-news/wp-content/uploads/2013/07/honda-f1.jpg','V15',1,'330','Honda','Torro Rosso')""")
        cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.sport-wall.com/wp-content/uploads/2015/03/Formula-1-Renault-F1-Car-680x425.jpg','RT3',3,'350','Renault','Jason Button')""")



        #database for the pilots
        cursor.execute("""DROP TABLE IF EXISTS PILOTS""")
        cursor.execute("""CREATE TABLE PILOTS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Surname CHAR(25), Age INTEGER )""")
        cursor.execute("""DROP TABLE IF EXISTS COUNTRIES""")
        cursor.execute("""CREATE TABLE COUNTRIES (Id SERIAL PRIMARY KEY NOT NULL, Countries CHAR(25),ForeignKey references PILOTS(Id )""")





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
