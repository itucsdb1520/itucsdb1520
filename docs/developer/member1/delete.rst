Delete
^^^^^^
The delete operations in "server.py".
Delete operation for pilot:
It gets id from user to delete.

.. code-block:: python

     if request.method =='POST':
        id = request.form['id']

And it deletes the values with:

.. code-block:: python

   with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM PILOTS WHERE Id = '""" +id + """' """
            cursor.execute(query)
            connection.commit()

The pilot deleted.

Delete operation for team:
It gets id from user to delete.

.. code-block:: python

    if request.method =='POST':
        Team = request.form['team']


And it deletes the values with:

.. code-block:: python

          with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM TEAMS WHERE TEAMS.Id = %s """
            cursor.execute(query, ([Team]))

The team deleted.

Delete operation for country:
It gets id from user to delete.

.. code-block:: python

     if request.method =='POST':
        Country = request.form['N_country']


And it deletes the values with:

.. code-block:: python

           with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """DELETE FROM COUNTRIES WHERE COUNTRIES.Id = %s """
            cursor.execute(query, ([Country]))

The country deleted.