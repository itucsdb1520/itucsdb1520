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

@app.route('/cars')
def cars():
    now = datetime.datetime.now()
    return render_template('cars.html', current_time=now.ctime())

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


@app.route('/about')
def about():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())

@app.route('/statistics')
def statistics():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())

"""
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

"""
            #query =  """INSERT INTO CARS (Image_Link, Name, Engine_Name,Speed,Zero_Hundred, BRAND, PILOT) VALUES
            #('"""+image_link+"""', '"""+car_name+"""', '"""+engine_name+"""', '"""+speed_limit+"""', '"""+zero_hundred+"""',
            # '"""+brand+"""', '"""+pilot+"""')"""
            ##print(query)
"""
            cursor.execute(query)
            connection.commit()

        #print("The car : '" + car_name + "'" + engine_name + "'"+ speed_limit + "'"+ zero_hundred + "'")
        now = datetime.datetime.now()
        return render_template('home.html', current_time=now.ctime())
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')

"""
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
        cursor.execute("""CREATE TABLE BRANDS (Id SERIAL PRIMARY KEY NOT NULL, Name TEXT, Comment TEXT)""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment) VALUES ('Shell', 'Asd')""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment) VALUES ('Pirelli', 'sadasdads')""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment) VALUES ('F-Zero', 'sdasda')""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment) VALUES ('Santander', 'Ssss')""")
        cursor.execute("""INSERT INTO BRANDS (Name, Comment) VALUES ('Kaspersky', 'aaaa')""")

        #database for the brands
        cursor.execute("""DROP TABLE IF EXISTS CARS""")
        cursor.execute("""CREATE TABLE CARS (Id SERIAL PRIMARY KEY NOT NULL, Image_Link TEXT, Name CHAR(30),Engine_Name CHAR(30),Speed INTEGER, Zero_Hundred INTEGER,BRAND CHAR(50),PILOT CHAR(50) )""")
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
