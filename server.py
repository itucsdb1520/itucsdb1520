import datetime
import os
import psycopg2 as dbapi2

from flask import Flask
from flask import render_template
from flask import url_for
from mercurial.fileset import methods
from flask.globals import request
from flask import request

from flask import request





app = Flask(__name__)


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

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

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
        print("The car : '" + car_name + "'" + engine_name + "'"+ speed_limit + "'"+ zero_hundred + "'")
        now = datetime.datetime.now()
        return render_template('home.html', current_time=now.ctime())
    else:
         now = datetime.datetime.now()
         return render_template('car_add.html')


with app.test_request_context():
    print(url_for('about'))
    print(url_for('brand', the_brand = 'Shell'))
    print(url_for('brands', next='/'))


if __name__ == '__main__':
    PORT = int(os.getenv('VCAP_APP_PORT', '5000'))
    app.run(host='0.0.0.0', port=int(PORT))