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


app = Flask(__name__)

class Brand:
    def __init__(self, name, description, year):
        self.name = name
        self.description = description
        self.year = year

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
    return render_template('pilots.html', current_time=now.ctime())

@app.route('/pilot_add_del')
def pilot_add_del():
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
    return render_template('pilot_add_del.html', pilots=pilots, current_time=now.ctime())

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


    return redirect(url_for('pilot_add_del'))

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


    return redirect(url_for('pilot_add_del'))

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
    return render_template('brand.html', the_brand=the_brand, current_time=now.ctime())

@app.route('/brands_db')
def brands_db():
    now = datetime.datetime.now()
    brands_list = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT * FROM BRANDS"""
            print(query)
            cursor.execute(query)

            for record in cursor:
                brands_list.append(record)

            connection.commit()
            print(brands_list)
    return render_template('brands_db.html', brands_list=brands_list, current_time=now.ctime())


@app.route('/add_brand', methods = ['GET','POST'])
def add_brand():
    if request.method =='POST':
        brand_name = request.form['brand-name']
        description = request.form['description']
        foundation = request.form['foundation']
        imagelink = request.form['imagelink']
        website = request.form['website']
        industry = request.form['industry']
        
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO BRANDS (Name, Comment, Foundation, Image, Industry, Website) VALUES ('""" 
            query = query + brand_name + """', '"""+ description + """', """+ foundation + """, '"""
            query = query + imagelink + """' , '""" + industry + """' , '""" + website+ """')"""
            cursor.execute(query)
            connection.commit()
    

    return redirect(url_for('brands_db'))

@app.route('/delete_brand', methods = ['GET','POST'])
def delete_brand():
    now = datetime.datetime.now()
    if request.method =='POST':
        brand_id = request.form['delete']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM BRANDS WHERE Id = '""" +brand_id + """' """
            cursor.execute(query)
            connection.commit()


    return redirect(url_for('brands_db'))

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
