Updating Operations for Tracks, Grands Prix and Seasons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




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