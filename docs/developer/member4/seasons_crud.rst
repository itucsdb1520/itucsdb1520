CRUD Operations for Seasons
^^^^^^^^^^^^^^^^^^^^^^^^^^^

After clicking the "CRUD operations for Seasons", the new page will be shown to apply add, delete and update operations on **Seasons** table.

*************
Add Operation
*************

This code is for adding a new tuple in **Seasons** table.

.. code-block:: html

   <form action="/season_add" method="post">
   <h3> Season Adding </h3>
   <div><label for='circuit'>Circuit name : </label> <input type="text" name="circuit"></input></div>
   <div><label for='seasons'> Season :</label> <input type="text" name="seasons"></input></div>

   <div class =button""><input type="submit" value="Add"></input></div>

   </form>


.. code-block:: python

   if request.method =='POST':
        circuit = request.form['circuit']
        seasons = request.form['seasons']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO SEASONS ( Circuit_Name, Season) VALUES (%s,%s)"""
            print(query)

            cursor.execute(query,(circuit, seasons))
            connection.commit()



****************
Delete Operation
****************

The delete operation for **Seasons** table is done by *Season*.

.. code-block:: html

   <form action="/season_delete" method="post">
   <h3> Delete a Season </h3>
   <div><label for='seasons'> Season : </label> <input type="text" name="seasons"></input></div>
   <div class =button""><input type="submit" value="Delete"></input></div>

   </form>


.. code-block:: python

   if request.method =='POST':
        seasons = request.form['seasons']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM SEASONS WHERE Season=%s"""
            cursor.execute(query,([seasons]))
            connection.commit()



****************
Update Operation
****************

For updating some attributes of a tuple from **Seasons** table, first the current name of season must be written.
The tuple whose Season name is equal to given name will be found after that all the attributes of this tuple will be changed with the new ones.

.. code-block:: html

   <form action="/season_update" method="post">
   <h3> Update an existing Season</h3>

   <div><label for='oldseason'> Old season: </label> <input type="text" name="oldseason"></input></div>
   <div><label for='seasons'> Season : </label> <input type="text" name="seasons"></input></div>
   <div><label for='circuit'> Circuit Name :</label> <input type="text" name="circuit"></input></div>

   <div class =button""><input type="submit" value="Update"></input> </div>

   </form>


.. code-block:: python
   if request.method =='POST':
        oldseason = request.form['oldseason']
        seasons = request.form['seasons']
        circuit = request.form['circuit']

        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query = """UPDATE SEASONS SET (Circuit_Name, Season ) = (%s,%s) WHERE Season=%s"""
            #print(query)

            cursor.execute(query,(circuit, seasons, oldseason))

            connection.commit()


