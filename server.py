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
from initialize_db import initialize_db_function

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
            query = """SELECT PILOTS.Name, PILOTS.Surname, PILOTS.Age, TEAMS.Teams, COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE PILOTS.Country=COUNTRIES.Id AND PILOTS.Team = TEAMS.Id;"""

            cursor.execute(query)

            for pilot in cursor:
                pilots.append(pilot)

            connection.commit()



    return render_template('pilots.html', pilots=pilots,  current_time=now.ctime())





@app.route('/add_pilot', methods = ['GET','POST'])
def add_pilot():
    now = datetime.datetime.now()
    pilots = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT PILOTS.Id, PILOTS.Name, PILOTS.Surname, PILOTS.Age, TEAMS.Teams, COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE PILOTS.Country=COUNTRIES.Id AND PILOTS.Team = TEAMS.Id;"""

            cursor.execute(query)

            for pilot in cursor:
                pilots.append(pilot)

            connection.commit()


    if request.method =='POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        team = request.form['team']
        country = request.form['country']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO PILOTS (Name, Surname, Age, Team, Country) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (name, surname, age, team, country))
            connection.commit()


    return render_template('add_pilot.html', pilots=pilots, current_time=now.ctime())

@app.route('/add_countries', methods = ['GET','POST'])
def add_countries():
    now = datetime.datetime.now()
    countries = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT COUNTRIES.Id, COUNTRIES.Countries FROM  COUNTRIES"""

            cursor.execute(query)

            for pilot in cursor:
                countries.append(pilot)

            connection.commit()
    if request.method =='POST':
        Country = request.form['country']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """INSERT INTO COUNTRIES ( Countries) VALUES (%s)"""
            cursor.execute(query,([Country]))
            connection.commit()


    return render_template('add_country.html',countries = countries, current_time=now.ctime())
@app.route('/delete_countries', methods = ['GET','POST'])
def delete_countries():
    now = datetime.datetime.now()

    countries = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT COUNTRIES.Id, COUNTRIES.Countries FROM  COUNTRIES"""

            cursor.execute(query)

            for pilot in cursor:
                countries.append(pilot)

            connection.commit()

    if request.method =='POST':
        Country = request.form['N_country']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM COUNTRIES WHERE COUNTRIES.Id = %s """
            cursor.execute(query, ([Country]))


        return render_template('add_country.html',countries = countries, current_time=now.ctime())


@app.route('/add_team', methods = ['GET','POST'])
def add_team():
    now = datetime.datetime.now()
    teams = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT TEAMS.Id, TEAMS.Teams FROM  TEAMS"""

            cursor.execute(query)

            for pilot in cursor:
                teams.append(pilot)

            connection.commit()
    if request.method =='POST':
        Team = request.form['team']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """INSERT INTO TEAMS ( Teams) VALUES (%s)"""
            cursor.execute(query,([Team]))
            connection.commit()


    return render_template('add_team.html',teams = teams, current_time=now.ctime())

@app.route('/delete_teams', methods = ['GET','POST'])
def delete_teams():
    now = datetime.datetime.now()

    teams = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT TEAMS.Id, TEAMS.Teams FROM  TEAMS"""

            cursor.execute(query)

            for pilot in cursor:
                teams.append(pilot)

            connection.commit()

    if request.method =='POST':
        Team = request.form['team']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM TEAMS WHERE TEAMS.Id = %s """
            cursor.execute(query, ([Team]))


        return render_template('add_team.html',teams = teams, current_time=now.ctime())



@app.route('/delete_pilot', methods = ['GET','POST'])
def delete_pilot():
    now = datetime.datetime.now()
    pilots = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT PILOTS.Id, PILOTS.Name, PILOTS.Surname, PILOTS.Age, TEAMS.Teams, COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE PILOTS.Country=COUNTRIES.Id AND PILOTS.Team = TEAMS.Id;"""

            cursor.execute(query)

            for pilot in cursor:
                pilots.append(pilot)

            connection.commit()
    if request.method =='POST':
        id = request.form['id']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM PILOTS WHERE Id = '""" +id + """' """
            cursor.execute(query)
            connection.commit()


    return render_template('add_pilot.html', pilots=pilots, current_time=now.ctime())




@app.route('/update_pilot', methods = ['GET','POST'])
def update_pilot():
    now = datetime.datetime.now()
    pilots = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT PILOTS.Id, PILOTS.Name, PILOTS.Surname, PILOTS.Age, TEAMS.Teams, COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE PILOTS.Country=COUNTRIES.Id AND PILOTS.Team = TEAMS.Id;"""

            cursor.execute(query)

            for pilot in cursor:
                pilots.append(pilot)

            connection.commit()

    if request.method =='POST':
        Id = request.form['id']
        new_name = request.form['N_name']
        new_surname = request.form['N_surname']
        new_age = request.form['N_age']
        new_team = request.form['N_team']
        new_country = request.form['N_country']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE PILOTS SET( Name, Surname, Age, Team, Country) = ( %s, %s, %s, %s, %s) WHERE Id = %s"""

            cursor.execute(query, (new_name, new_surname, new_age, new_team, new_country, Id))
            connection.commit()


    return render_template('add_pilot.html', pilots=pilots, current_time=now.ctime())


@app.route('/update_countries', methods = ['GET','POST'])
def update_countries():
    now = datetime.datetime.now()
    countries = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT COUNTRIES.Id, COUNTRIES.Countries FROM  COUNTRIES"""

            cursor.execute(query)

            for pilot in cursor:
                countries.append(pilot)

            connection.commit()

    if request.method =='POST':
        Id = request.form['id']
        new_country = request.form['N_country']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE COUNTRIES SET( Countries) = ( %s) WHERE Id = %s"""

            cursor.execute(query, (new_country, Id))
            connection.commit()


    return render_template('add_country.html',countries = countries, current_time=now.ctime())



@app.route('/update_teams', methods = ['GET','POST'])
def update_teams():
    now = datetime.datetime.now()
    teams = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT TEAMS.Id, TEAMS.Teams FROM  TEAMS"""

            cursor.execute(query)

            for pilot in cursor:
                teams.append(pilot)

            connection.commit()
    if request.method =='POST':
        Id = request.form['id']
        new_team = request.form['N_team']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE TEAMS SET( Teams) = ( %s) WHERE Id = %s"""

            cursor.execute(query, (new_team, Id))
            connection.commit()


    return render_template('add_team.html',teams = teams, current_time=now.ctime())






@app.route('/cars')
def cars():
    now = datetime.datetime.now()
    cars_list = []
    engine_list = []
    creator_list = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,CREATORS.Name,ENGINES.HorsePower,CARS.Speed,TEAMS.Teams,PILOTS.Name,PILOTS.Surname FROM CARS,ENGINES,CREATORS,PILOTS,TEAMS WHERE (CARS.Engine_ID = ENGINES.Id ) AND (CARS.Creator_ID = CREATORS.Id) AND (CARS.BRAND_ID = TEAMS.Id) AND (CARS.PILOT_ID = PILOTS.Id)"""


            cursor.execute(query)

            for record in cursor:
                cars_list.append(record)
            connection.commit()

            query = """SELECT Engine_Name,HorsePower FROM ENGINES"""
            cursor.execute(query)
            for record in cursor:
                engine_list.append(record)

            query = """SELECT Name FROM CREATORS"""
            cursor.execute(query)
            for record in cursor:
                creator_list.append(record)
    return render_template('cars.html', creator_list = creator_list , engine_list = engine_list, cars_list=cars_list, current_time=now.ctime())



@app.route('/tracks')
def tracks():
    now = datetime.datetime.now()
    tracks_list = []
    seasons_list = []
    grandsprix_list = []
    location_list = []
    with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT TRACKS.Circuit, TRACKS.Map, TRACKS.Type, TRACKS.Direction, LOCATION.Location, TRACKS.Length, GRANDS_PRIX.GrandsPrix, TRACKS.GrandsPrixHeld FROM TRACKS, GRANDS_PRIX, LOCATION WHERE (TRACKS.GP_Id = GRANDS_PRIX.Id) AND (LOCATION.Id = TRACKS.Location_Id)"""

            cursor.execute(query)

            for record in cursor:
                tracks_list.append(record)
            connection.commit()

            query = """SELECT Circuit_Name, Season FROM SEASONS"""
            cursor.execute(query)
            for record in cursor:
                seasons_list.append(record)

            query = """SELECT GrandsPrix, No_of_Races FROM GRANDS_PRIX"""
            cursor.execute(query)
            for record in cursor:
                grandsprix_list.append(record)

            query = """SELECT * FROM LOCATION"""
            cursor.execute(query)
            for record in cursor:
                location_list.append(record)


    return render_template('tracks.html', tracks_list = tracks_list, seasons_list = seasons_list, grandsprix_list = grandsprix_list, location_list = location_list, current_time=now.ctime())

@app.route('/tracks_add', methods = ['GET', 'POST'])
def tracks_add():

    tracks_list = []
    seasons_list = []
    grandsprix_list = []
    location_list = []

    if request.method =='POST':
        name = request.form['name']
        map_link = request.form['map_link']
        type = request.form['type']
        direction = request.form['direction']
        location_id = request.form['location_id']
        current_length = request.form['current_length']
        gp_id = request.form['gp_id']
        Grands_prix_held = request.form['Grands_prix_held']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query = """SELECT Id FROM GRANDS_PRIX WHERE Id=%s"""
            cursor.execute(query,(gp_id))

            for record in cursor:
                grandsprix_list.append(record)

            if len(grandsprix_list) == 0 or gp_id == '':
                return redirect(url_for('tracks'))

            query = """SELECT Id FROM LOCATION WHERE Id=%s"""
            cursor.execute(query,(location_id))

            for record in cursor:
                location_list.append(record)

            if len(location_list) == 0 or location_id == '':
                return redirect(url_for('tracks'))

            query = """SELECT Circuit FROM TRACKS WHERE circuit=%s"""
            cursor.execute(query,([name]))

            for record in cursor:
                tracks_list.append(record)

            if len(tracks_list) != 0:
                return redirect(url_for('tracks'))

            query = """INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_id, Length, GP_Id, GrandsPrixHeld) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            print(query)

            cursor.execute(query,(name, map_link, type, direction, location_id, current_length, gp_id, Grands_prix_held))
            connection.commit()

        return redirect(url_for('tracks'))
    else:
         now = datetime.datetime.now()
         return render_template('tracks_add.html')

@app.route('/track_delete',methods = ['GET','POST'])
def track_delete():
    if request.method =='POST':
        circuit_name = request.form['circuit_name']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM TRACKS WHERE Circuit=%s"""
            cursor.execute(query,([circuit_name]))
            connection.commit()
        return redirect(url_for('tracks'))
    else:
        now = datetime.datetime.now()
        return render_template('tracks_add.html')

@app.route('/track_update',methods = ['GET','POST'])
def track_update():
    if request.method =='POST':
        oldname = request.form['oldname']
        name = request.form['name']
        map_link = request.form['map_link']
        type = request.form['type']
        direction = request.form['direction']
        location_id = request.form['location_id']
        current_length = request.form['current_length']
        gp_id = request.form['gp_id']
        Grands_prix_held = request.form['Grands_prix_held']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query = """UPDATE TRACKS SET (Circuit, Map, Type, Direction, Location_id, Length, GP_Id, GrandsPrixHeld) = (%s,%s,%s,%s,%s,%s,%s,%s) WHERE Circuit=%s"""
            #print(query)

            cursor.execute(query,(name, map_link, type, direction, location_id, current_length, gp_id, Grands_prix_held, oldname))

            connection.commit()

        return redirect(url_for('tracks'))
    else:
        now = datetime.datetime.now()
        return render_template('tracks_add.html')


@app.route('/grandsprix_add',methods = ['GET','POST'])
def grandsprix_add():
    if request.method =='POST':
        gpname = request.form['gpname']
        no_of_races = request.form['no_of_races']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES (%s,%s)"""
            print(query)

            cursor.execute(query,(gpname, no_of_races))
            connection.commit()

        return redirect(url_for('tracks'))
    else:
         now = datetime.datetime.now()
         return render_template('grandsprix_add.html')

@app.route('/grandsprix_delete',methods = ['GET','POST'])
def grandsprix_delete():
    if request.method =='POST':
        gpname = request.form['gpname']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM GRANDS_PRIX WHERE GrandsPrix=%s"""
            cursor.execute(query,([gpname]))
            connection.commit()
        return redirect(url_for('tracks'))
    else:
        now = datetime.datetime.now()
        return render_template('grandsprix_add.html')

@app.route('/grandsprix_update',methods = ['GET','POST'])
def grandsprix_update():
    if request.method =='POST':
        oldname = request.form['oldname']
        gpname = request.form['gpname']
        no_of_races = request.form['no_of_races']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query = """UPDATE GRANDS_PRIX SET ( GrandsPrix, No_of_Races) = (%s,%s) WHERE GrandsPrix=%s"""
            #print(query)

            cursor.execute(query,(gpname, no_of_races, oldname))

            connection.commit()

        return redirect(url_for('tracks'))
    else:
        now = datetime.datetime.now()
        return render_template('grandsprix_add.html')








@app.route('/brands')
def brands():
    now = datetime.datetime.now()
    return render_template('brands.html', current_time=now.ctime())

@app.route('/brand/<the_brand>')
def brand(the_brand):
    now = datetime.datetime.now()
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        query = """SELECT * FROM BRANDS WHERE Name = %s"""
        cursor.execute(query, ([the_brand]))
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

    if operation == "listbrands":
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
            elif sub_operation == 'country':
                sort = "COUNTRIES.Countries"
            else:
                sort = "Id"

        with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """SELECT BRANDS.Id, BRANDS.Name, BRANDS.Comment, BRANDS.Foundation, BRANDS.Image,  BRANDS.Industry, BRANDS.Website, COUNTRIES.Countries FROM COUNTRIES INNER JOIN BRANDS ON BRANDS.CountryId = COUNTRIES.Id """
                if make_sub_operation == True:
                    query = query + """ ORDER BY """ + sort
                print(query)
                cursor.execute(query)

                for record in cursor:
                    brands_list.append(record)

                connection.commit()
        return render_template('brands_db.html', brands_list=brands_list, current_time=now.ctime(), table = 0)

    elif operation == "listfounders":
        founders_list = []
        if make_sub_operation == True:
            if sub_operation == 'name':
                sort = "Name"
            elif sub_operation == 'surname':
                sort = "Surname"
            else:
                sort = "Id"

        with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """SELECT * FROM FOUNDERS"""
                if make_sub_operation == True:
                    query = query + """ ORDER BY """ + sort
                print(query)
                cursor.execute(query)

                for record in cursor:
                    founders_list.append(record)

                connection.commit()
                print(founders_list)
        return render_template('brands_db.html', founders_list=founders_list, current_time=now.ctime(), table = 1)

    elif operation == "listjoint":
        joint_list = []
        if make_sub_operation == True:
            if sub_operation == 'fname':
                sort = "FOUNDERS.Name"
            elif sub_operation == 'surname':
                sort = "FOUNDERS.Surname"
            elif sub_operation == 'bname':
                sort = "BRANDS.Name"
            elif sub_operation == 'year':
                sort = "BRANDS.Foundation"
            elif sub_operation == 'industry':
                sort = "BRANDS.Industry"
            elif sub_operation == 'website':
                sort = "BRANDS.Website"
            elif sub_operation == 'description':
                sort = "BRANDS.Comment"
            else:
                sort = "FOUNDERS.Id"

        with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """SELECT FOUNDERS.Name, FOUNDERS.Surname, BRANDS.Name, BRANDS.Foundation, BRANDS.Industry, BRANDS.Website, BRANDS.Comment FROM FOUNDERS INNER JOIN BRANDS ON BRANDS.Id = FOUNDERS.Brand_Id"""
                if make_sub_operation == True:
                    query = query + """ ORDER BY """ + sort
                print(query)
                cursor.execute(query)

                for record in cursor:
                    joint_list.append(record)

                connection.commit()
                #print(joint_list)
        return render_template('brands_db.html', joint_list=joint_list, current_time=now.ctime(), table = 2)

    elif operation == "add_brand":
        #print("On the add")
        if request.method =='POST':
            brand_name = request.form['brand-name']
            description = request.form['description']
            foundation = request.form['foundation']
            imagelink = request.form['imagelink']
            website = request.form['website']
            industry = request.form['industry']
            country = request.form['country']

            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()

                query = """SELECT Id FROM COUNTRIES WHERE COUNTRIES.countries = '""" + country + """'"""
                cursor.execute(query)

                countryid = None
                for record in cursor:
                    countryid = record

                print(countryid[0])
                query = """INSERT INTO BRANDS (Name, Comment, Foundation, Image, Industry, Website, CountryId) VALUES (%s, %s, %s, %s, %s, %s, %s);"""
                cursor.execute(query, (brand_name,description,foundation,imagelink,industry,website, countryid[0]))
                connection.commit()


        return redirect(url_for('brands_db', operation = 'listbrands'))

    elif operation == "add_founder":
        #print("On the add")
        if request.method =='POST':
            founder_name = request.form['founder-name']
            founder_surname = request.form['founder-surname']
            brand_id = request.form['brand-id']

            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES (%s, %s, %s);"""
                cursor.execute(query, (founder_name,founder_surname,brand_id))
                connection.commit()


        return redirect(url_for('brands_db', operation = 'listfounders'))

    elif operation == "delete_brand":
        #print("On delete")
        if request.method == 'POST':
            brand_id = request.form['delete']
            print(brand_id)
            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM BRANDS WHERE Id = %s ", ([brand_id]))
                connection.commit()

        return redirect(url_for('brands_db', operation = 'listbrands'))

    elif operation == "delete_founder":
        #print("On delete")
        if request.method == 'POST':
            founder_id = request.form['delete']

            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM FOUNDERS WHERE Id = %s ", ([founder_id]))
                connection.commit()
        return redirect(url_for('brands_db', operation = 'listfounders'))

    elif operation == "edit_brand":
        if request.method == 'POST':
            new_name = request.form['brand-name']
            new_description = request.form['description']
            new_foundation = request.form['foundation']
            new_imagelink = request.form['imagelink']
            new_website = request.form['website']
            new_industry = request.form['industry']
            new_country = request.form['country']
            edit = request.form['edit']
            print(new_country)


            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()

                query = """SELECT Id FROM COUNTRIES WHERE COUNTRIES.countries = '""" + new_country + """'"""
                cursor.execute(query)

                countryid = None
                for record in cursor:
                    countryid = record
                print(countryid[0])
                query = """UPDATE BRANDS SET (Name, Comment, Foundation,  Image, Industry, Website, CountryId) = (%s, %s,%s,%s,%s,%s,%s) WHERE ID = %s;"""
                cursor.execute(query, (new_name, new_description, new_foundation, new_imagelink, new_industry, new_website, countryid[0], edit))
                connection.commit()


        return redirect(url_for('brands_db', operation = 'listbrands'))

    elif operation == "edit_founder":
        if request.method == 'POST':
            new_name = request.form['founder-name']
            new_surname = request.form['founder-surname']
            edit = request.form['edit'] #id

            with dbapi2.connect(app.config['dsn']) as connection:
                cursor = connection.cursor()
                query = """UPDATE FOUNDERS SET (Name, Surname) = (%s,%s) WHERE ID = %s;"""
                cursor.execute(query, (new_name, new_surname, edit))
                connection.commit()


        return redirect(url_for('brands_db', operation = 'listfounders'))

#about page
@app.route('/about')
def about():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())



#Login page
@app.route('/login')
def login():
    now = datetime.datetime.now()
    return render_template('login.html', current_time=now.ctime())


#Sign in page
@app.route('/signUp')
def signUp():
    now = datetime.datetime.now()
    return render_template('signUp.html', current_time=now.ctime())


#statistics page may be implemented in future
@app.route('/statistics')
def statistics():
    now = datetime.datetime.now()
    return render_template('about.html', current_time=now.ctime())

@app.route('/car_add',methods = ['GET','POST'])
def car_add():
    engine_list = []
    name_list = []
    if request.method =='POST':
        image_link = request.form['image_link']
        car_name = request.form['car_name']
        engine_id = request.form['engine_id']
        creator_id = request.form['creator_id']
        speed_limit = request.form['speed_limit']
        brand = request.form['brand']
        pilot = request.form['pilot']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()


            query = """SELECT Id FROM ENGINES WHERE Id=%s"""
            cursor.execute(query,(engine_id))

            for record in cursor:
                engine_list.append(record)


            if len(engine_list) == 0 or engine_id =='':
                return redirect(url_for('home'))

            query = """SELECT Name FROM CARS WHERE Name=%s"""
            cursor.execute(query,([car_name]))

            for record in cursor:
                name_list.append(record)

            if len(name_list) != 0:
                return redirect(url_for('home'))

            query =  """INSERT INTO CARS (Image_Link, Name, Engine_ID,Creator_ID,Speed, BRAND_ID, PILOT_ID) VALUES (%s,%s,%s,%s,%s,%s,%s)"""
            print(query)

            cursor.execute(query,(image_link,car_name,engine_id,creator_id,speed_limit,brand,pilot))
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

@app.route('/creator_add',methods = ['GET','POST'])
def creator_add():
    if request.method =='POST':
        name = request.form['creator_name']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO CREATORS (Name) VALUES ('"""+name+"""')"""
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
    engine_list =[]
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

@app.route('/creator_delete',methods = ['GET','POST'])
def creator_delete():

    if request.method =='POST':
        creator_name = request.form['creator_name']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """DELETE FROM CREATORS WHERE Name=%s"""
            cursor.execute(query,([creator_name]))
            connection.commit()
        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_delete.html')

@app.route('/car_update',methods = ['GET','POST'])
def car_update():
    if request.method =='POST':
        car_name_up =request.form['car_name_up']
        image_link = request.form['image_link']
        car_name = request.form['car_name']
        engine_id = request.form['engine_id']
        creator_id = request.form['creator_id']
        speed_limit = request.form['speed_limit']
        brand = request.form['brand']
        pilot = request.form['pilot']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """UPDATE CARS SET (Image_Link, Name, Engine_ID,Creator_ID,Speed, BRAND_ID, PILOT_ID) = (%s,%s,%s,%s,%s,%s,%s) WHERE Name=%s"""
            #print(query)

            cursor.execute(query,(image_link,car_name,engine_id,creator_id,speed_limit,brand,pilot,car_name_up))

            connection.commit()

        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')

@app.route('/engine_update',methods = ['GET','POST'])
def engine_update():
    if request.method =='POST':
        engine_name_up =request.form['engine_name_up']
        engine_name =request.form['engine_name']
        horse_power =request.form['horse_power']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """UPDATE ENGINES SET (Engine_Name , HorsePower ) = (%s,%s) WHERE Engine_Name=%s"""
            #print(query)

            cursor.execute(query,(engine_name,horse_power,engine_name_up))

            connection.commit()

        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')

@app.route('/creator_update',methods = ['GET','POST'])
def creator_update():
    if request.method =='POST':
        creator_name_up =request.form['creator_name_up']
        creator_name =request.form['creator_name']


        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """UPDATE CREATORS SET Name = %s WHERE Name=%s"""
            #print(query)

            cursor.execute(query,(creator_name,creator_name_up))

            connection.commit()

        return redirect(url_for('home'))
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')


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
                #coming up next

                query = """ """

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 0)
            elif area == '1':
                #search cars
                search = "%" +search + "%"
                query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,CREATORS.Name,ENGINES.HorsePower,CARS.Speed,TEAMS.Teams,PILOTS.Name,PILOTS.Surname FROM CARS,ENGINES,CREATORS,PILOTS,TEAMS WHERE (CARS.Engine_ID = ENGINES.Id ) AND (CARS.Creator_ID = CREATORS.Id) AND (CARS.BRAND_ID = TEAMS.Id) AND (CARS.PILOT_ID = PILOTS.Id) AND (CARS.Name ILIKE %s)"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,CREATORS.Name,ENGINES.HorsePower,CARS.Speed,TEAMS.Teams,PILOTS.Name,PILOTS.Surname FROM CARS,ENGINES,CREATORS,PILOTS,TEAMS WHERE (CARS.Engine_ID = ENGINES.Id ) AND (CARS.Creator_ID = CREATORS.Id) AND (CARS.BRAND_ID = TEAMS.Id) AND (CARS.PILOT_ID = PILOTS.Id) AND (ENGINES.Engine_Name ILIKE %s) """
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,CREATORS.Name,ENGINES.HorsePower,CARS.Speed,TEAMS.Teams,PILOTS.Name,PILOTS.Surname FROM CARS,ENGINES,CREATORS,PILOTS,TEAMS WHERE (CARS.Engine_ID = ENGINES.Id ) AND (CARS.Creator_ID = CREATORS.Id) AND (CARS.BRAND_ID = TEAMS.Id) AND (CARS.PILOT_ID = PILOTS.Id) AND (CREATORS.Name ILIKE %s)"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,CREATORS.Name,ENGINES.HorsePower,CARS.Speed,TEAMS.Teams,PILOTS.Name,PILOTS.Surname FROM CARS,ENGINES,CREATORS,PILOTS,TEAMS WHERE (CARS.Engine_ID = ENGINES.Id ) AND (CARS.Creator_ID = CREATORS.Id) AND (CARS.BRAND_ID = TEAMS.Id) AND (CARS.PILOT_ID = PILOTS.Id) AND (PILOTS.Name ILIKE %s)"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,CREATORS.Name,ENGINES.HorsePower,CARS.Speed,TEAMS.Teams,PILOTS.Name,PILOTS.Surname FROM CARS,ENGINES,CREATORS,PILOTS,TEAMS WHERE (CARS.Engine_ID = ENGINES.Id ) AND (CARS.Creator_ID = CREATORS.Id) AND (CARS.BRAND_ID = TEAMS.Id) AND (CARS.PILOT_ID = PILOTS.Id) AND (PILOTS.Surname ILIKE %s)"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT CARS.Image_Link,CARS.Name,ENGINES.Engine_Name,CREATORS.Name,ENGINES.HorsePower,CARS.Speed,TEAMS.Teams,PILOTS.Name,PILOTS.Surname FROM CARS,ENGINES,CREATORS,PILOTS,TEAMS WHERE (CARS.Engine_ID = ENGINES.Id ) AND (CARS.Creator_ID = CREATORS.Id) AND (CARS.BRAND_ID = TEAMS.Id) AND (CARS.PILOT_ID = PILOTS.Id) AND (TEAMS.Teams ILIKE %s)"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query_list = list(set(query_list))

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 1)
            elif area == '2':
                #search pilots
                search = "%" + search +"%"
                query = """  SELECT PILOTS.Name, PILOTS.Surname, TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (PILOTS.Name LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)

                query = """  SELECT PILOTS.Name, PILOTS.Surname,  TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (PILOTS.Surname LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)

                query = """  SELECT PILOTS.Name, PILOTS.Surname, TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (COUNTRIES.Countries LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)


                query = """  SELECT PILOTS.Name, PILOTS.Surname, TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (TEAMS.Teams LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)


                query_list = list(set(query_list))
                print(query_list)
                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 2)
            elif area == '3':
                #search tracks
                search = "%" +search + "%"
                query = """SELECT TRACKS.Circuit, TRACKS.Type, TRACKS.Direction, LOCATION.Location, TRACKS.Length, GRANDS_PRIX.GrandsPrix, TRACKS.GrandsPrixHeld FROM TRACKS, GRANDS_PRIX, LOCATION WHERE (TRACKS.GP_Id = GRANDS_PRIX.Id AND TRACKS.Location_Id = LOCATION.Id) AND (TRACKS.Circuit LIKE %s)"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query_list = list(set(query_list))

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 3)
            elif area == '8':
                #search grands_prix
                search = "%" +search + "%"
                query = """SELECT GrandsPrix, No_of_Races FROM GRANDS_PRIX WHERE GrandsPrix ILIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query_list = list(set(query_list))

                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 8)
            elif area == '4':
                #search brands
                print(search)
                search = "%" + search + "%"
                query = """SELECT * FROM BRANDS WHERE Name ILIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT * FROM BRANDS WHERE Industry ILIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT * FROM BRANDS WHERE Comment ILIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query_list = list(set(query_list))
                #remove duplicate elements in the list
                connection.commit()
                print(query_list)
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 4)

            elif area == '7':
                #search founders
                search = "%" + search + "%"
                query = """SELECT * FROM FOUNDERS WHERE Name ILIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query = """SELECT * FROM FOUNDERS WHERE Surname ILIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)


                query_list = list(set(query_list))
                #remove duplicate elements in the list
                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 7)

            else:
                query = """ """
                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = [])

#these are for testing will be edited later
@app.route('/initdb')
def initialize_database():
    with dbapi2.connect(app.config['dsn']) as connection:
        cursor = connection.cursor()
        initialize_db_function(cursor)
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
