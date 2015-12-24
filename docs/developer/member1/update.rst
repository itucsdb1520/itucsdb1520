Update
^^^^^^

The Update operations in "server.py".
Update operation for pilot:
It gets id and other informations from user to Update.

.. code-block:: python

     if request.method =='POST':
        Id = request.form['id']
        new_name = request.form['N_name']
        new_surname = request.form['N_surname']
        new_age = request.form['N_age']
        new_team = request.form['N_team']
        new_country = request.form['N_country']

And it Updates the values with:

.. code-block:: python

   with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE PILOTS SET( Name, Surname, Age, Team, Country) = ( %s, %s, %s, %s, %s) WHERE Id = %s"""

            cursor.execute(query, (new_name, new_surname, new_age, new_team, new_country, Id))
            connection.commit()


The pilot Updated.

Update operation for team:
It gets id and other informations from user to Update.

.. code-block:: python

    if request.method =='POST':
        Id = request.form['id']
        new_team = request.form['N_team']


And it Updates the values with:

.. code-block:: python

          with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE TEAMS SET( Teams) = ( %s) WHERE Id = %s"""

            cursor.execute(query, (new_team, Id))
            connection.commit()

The team Updated.

Update operation for country:
It gets id and other informations from user to Update.

.. code-block:: python

     if request.method =='POST':
        Id = request.form['id']
        new_country = request.form['N_country']


And it Updates the values with:

.. code-block:: python

           with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """UPDATE COUNTRIES SET( Countries) = ( %s) WHERE Id = %s"""

            cursor.execute(query, (new_country, Id))
            connection.commit()

The country Updated.