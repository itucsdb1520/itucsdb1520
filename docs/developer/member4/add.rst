Adding Operations for Tracks, Grands Prix and Seasons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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