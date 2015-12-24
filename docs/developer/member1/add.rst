Add
^^^
The add operations in "server.py".
Add operation for pilot:
It gets values from user

.. code-block:: python

     if request.method =='POST':
        name = request.form['name']
        surname = request.form['surname']
        age = request.form['age']
        team = request.form['team']
        country = request.form['country']

And it inserts the values with:

.. code-block:: python

   with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """INSERT INTO PILOTS (Name, Surname, Age, Team, Country) VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(query, (name, surname, age, team, country))
            connection.commit()

The pilot added.

Add operation for team:
It gets values from user

.. code-block:: python

     if request.method =='POST':
        Team = request.form['team']


And it inserts the values with:

.. code-block:: python

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """INSERT INTO TEAMS ( Teams) VALUES (%s)"""
            cursor.execute(query,([Team]))
            connection.commit()

The team added.

Add operation for country:
It gets values from user

.. code-block:: python

      if request.method =='POST':
        Country = request.form['country']


And it inserts the values with:

.. code-block:: python

         with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """INSERT INTO COUNTRIES ( Countries) VALUES (%s)"""
            cursor.execute(query,([Country]))
            connection.commit()

The country added.
