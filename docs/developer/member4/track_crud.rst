CRUD Operations for Tracks
^^^^^^^^^^^^^^^^^^^^^^^^^^

After clicking the "CRUD operations for Tracks", the new page will be shown to apply add, delete and update operations on **Tracks** table.

*************
Add Operation
*************

This code is for adding a new tuple in **tracks** table. Circuit name must be filled because of being primary key. Location is added by its id, so the location with the given id have to be exist in **location** table.
The same situation is valid for the id of the Grands Prix.

.. code-block:: html

   <form action="/tracks_add" method="post">
   <h3> Tracks Adding </h3>
   <div><label for='name'>Circuit name : </label> <input type="text" name="name"></input></div>
   <div><label for='map_link'> Map :</label> <input type="text" name="map_link"></input></div>
   <div><label for='type'> Type :</label> <input type="text" name="type"></input></div>
   <div><label for='direction'> Direction :</label> <input type="text" name="direction"></input></div>
   <div><label for='location_id'> Location :</label> <input type="number" name="location_id"></input></div>
   <div><label for='current_length'> Current Length :</label> <input type="text" name="current_length"></input></div>
   <div><label for='gp_id'> Grands Prix :</label> <input type="number" name="gp_id"></input></div>
   <div><label for='Grands_prix_held'> Grands Prix Held :</label> <input type="text" name="Grands_prix_held"></input></div>

   <div class =button""><input type="submit" value="Add"></input></div>

   </form>


.. code-block:: python

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


****************
Delete Operation
****************

The delete operation for **tracks** table is done by *Circuit* name.

.. code-block:: html

   <form action="/track_delete" method="post">
   <h3> Delete a Track </h3>
   <div><label for='circuit_name'> Circuit Name : </label> <input type="text" name="circuit_name"></input></div>
   <div class =button""><input type="submit" value="Delete"></input></div>
   </form>


.. code-block:: python

   if request.method =='POST':
        circuit_name = request.form['circuit_name']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM TRACKS WHERE Circuit=%s"""
            cursor.execute(query,([circuit_name]))
            connection.commit()


****************
Update Operation
****************

For updating some attributes of a tuple from **tracks** table, first the current name of circuit must be written.
The tuple whose Circuit name is equal to given name will be found after that all the attributes of this tuple will be changed with the new ones.


.. code-block:: html

   <form action="/track_update" method="post">
   <h3> Update an existing track</h3>

   <div><label for='oldname'>Current name of Circuit : </label> <input type="text" name="oldname"></input></div>
   <div><label for='name'> Circuit name : </label> <input type="text" name="name"></input></div>
   <div><label for='map_link'> Map :</label> <input type="text" name="map_link"></input></div>
   <div><label for='type'> Type :</label> <input type="text" name="type"></input></div>
   <div><label for='direction'> Direction :</label> <input type="text" name="direction"></input></div>
   <div><label for='location_id'> Location :</label> <input type="number" name="location_id"></input></div>
   <div><label for='current_length'> Current Length :</label> <input type="text" name="current_length"></input></div>
   <div><label for='gp_id'> Grands Prix :</label> <input type="number" name="gp_id"></input></div>
   <div><label for='Grands_prix_held'> Grands Prix Held :</label> <input type="text" name="Grands_prix_held"></input></div>

   <div class =button""><input type="submit" value="Update"></input> </div>

   </form>


.. code-block:: python

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



****************
Search Operation
****************

The search operation for **tracks** table is done by circuit name. If any match(es) is found, result(s) will be shown.


.. code-block:: html

   {% elif table == 3%}
                {% for name, type, direction, location, current_length, gp_id, Grands_prix_held in query_list %}

                    <tr>
                        <td class="name">{{ name }} </td>
                        <td class="type">{{ type }} </td>
                        <td class="direction">{{ direction }} </td>
                        <td class="location">{{ location }} </td>
                        <td class="current_length">{{ current_length }} </td>
                        <td class="gp_id">{{ gp_id }} </td>
                        <td class="Grands_prix_held">{{ Grands_prix_held }} </td>
                    </tr>

                {% endfor %}


.. code-block:: python

   elif area == '3':
                #search tracks
                search = "%" +search + "%"
                query = """SELECT TRACKS.Circuit, TRACKS.Type, TRACKS.Direction, LOCATION.Location, TRACKS.Length, GRANDS_PRIX.GrandsPrix, TRACKS.GrandsPrixHeld FROM TRACKS, GRANDS_PRIX, LOCATION WHERE (TRACKS.GP_Id = GRANDS_PRIX.Id AND TRACKS.Location_Id = LOCATION.Id) AND (TRACKS.Circuit LIKE %s)"""
                cursor.execute(query, ([search]))
                for record in cursor:
                    query_list.append(record)

                query_list = list(set(query_list))

                connection.commit()
