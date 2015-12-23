CRUD Operations for Grands Prix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After clicking the "CRUD operations for Grands Prix", the new page will be shown to apply add, delete and update operations on **Grands_Prix** table.

*************
Add Operation
*************

This code is for adding a new tuple in **Grands_Prix** table.

.. code-block:: html

   <form action="/grandsprix_add" method="post">
   <h3> Grands Prix Adding </h3>
   <div><label for='gpname'>Grands Prix name : </label> <input type="text" name="gpname"></input></div>
   <div><label for='no_of_races'> No of Races :</label> <input type="text" name="no_of_races"></input></div>

   <div class =button""><input type="submit" value="Add"></input></div>

   </form>


.. code-block:: python

   if request.method =='POST':
        gpname = request.form['gpname']
        no_of_races = request.form['no_of_races']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()

            query =  """INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES (%s,%s)"""
            print(query)

            cursor.execute(query,(gpname, no_of_races))
            connection.commit()



****************
Delete Operation
****************

The delete operation for **Grands_Prix** table is done by *GrandsPrix* name.

.. code-block:: html

   <form action="/grandsprix_delete" method="post">
   <h3> Delete a Grands Prix </h3>
   <div><label for='gpname'> Grands Prix name : </label> <input type="text" name="gpname"></input></div>
   <div class =button""><input type="submit" value="Delete"></input></div>

   </form>


.. code-block:: python

   if request.method =='POST':
        gpname = request.form['gpname']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM GRANDS_PRIX WHERE GrandsPrix=%s"""
            cursor.execute(query,([gpname]))
            connection.commit()


****************
Update Operation
****************

For updating some attributes of a tuple from **Grands_Prix** table, first the current name of Grands Prix must be written.
The tuple whose Grands Prix name is equal to given name will be found after that all the attributes of this tuple will be changed with the new ones.

.. code-block:: html

   <form action="/grandsprix_update" method="post">
   <h3> Update an existing Grands Prix</h3>

   <div><label for='oldname'>Current name of Grands Prix : </label> <input type="text" name="oldname"></input></div>
   <div><label for='gpname'>Grands Prix name : </label> <input type="text" name="gpname"></input></div>
   <div><label for='no_of_races'> No of Races :</label> <input type="text" name="no_of_races"></input></div>

   <div class =button""><input type="submit" value="Update"></input> </div>

   </form>


.. code-block:: python

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



****************
Search Operation
****************

The search operation for **Grands_Prix** table is done by Grands Prix name. If any match(es) is found, result(s) will be shown.


.. code-block:: html

   {% elif table == 8%}
                {% for gpname, no_of_races in query_list %}

                    <tr>
                        <td class="gpname">{{ gpname }} </td>
                        <td class="no_of_races">{{ no_of_races }} </td>
                    </tr>

                {% endfor %}


.. code-block:: python

   elif area == '8':
                #search grands_prix
                search = "%" +search + "%"
                query = """SELECT GrandsPrix, No_of_Races FROM GRANDS_PRIX WHERE GrandsPrix ILIKE %s"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query_list = list(set(query_list))

                connection.commit()
