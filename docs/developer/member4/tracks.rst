Tracks Page
^^^^^^^^^^^

In **tracks.html** page, there are 3 tables; list of circuits, list of seasons and list of Grands Prix.

The first table, *list of circuits* is created by merging **tracks, location**, and **grands_prix** tables. *Circuit, Map, Type, Direction, Current_length* and *Grands_Prix_Held*
attributes are taken from **tracks** table, *Location* attribute are taken from **location** table and *GrandsPrix* attribute is taken from **Grands_Prix** table.


.. code-block:: html

   <table id="track-table">
        <caption>List of All Circuits</caption>
         <tr>
            <th id="name"> Circuit </th>
            <th id="map_link"> Map </th>
            <th id="type"> Type </th>
            <th id="direction"> Direction </th>
            <th id="location_id"> Location </th>
            <th id="current_length"> Current Length </th>
            <th id="gp_id"> Grands Prix name </th>
            <th id="Grands_prix_held"> Grands Prix Held </th>

         </tr>

         {% for id in tracks_list %}
         <tr>

            <td>{{ id[0] }} </td>
            <td> <img src={{ id[1] }} style="width:250px;height:125spx;"></td>
            <td>{{ id[2] }} </td>
            <td>{{ id[3] }} </td>
            <td>{{ id[4] }} </td>
            <td>{{ id[5] }} </td>
            <td>{{ id[6] }} </td>
            <td>{{ id[7] }} </td>

         </tr>
         {% endfor %}
      </table>

      <br><br><br><br>

      <table id="season-table">
        <caption>List of All Seasons</caption>
         <tr>

            <th id="Circuit_name">Circuit</th>
            <th id="Season"> Season</th>
         </tr>

         {% for id in seasons_list %}
         <tr>
            <td>{{ id[0] }} </td>
            <td>{{ id[1] }} </td>

         </tr>
         {% endfor %}
      </table>

      <br><br><br><br>

      <table id="grandsprix-table">
        <caption>List of All Grands Prix</caption>
         <tr>

            <th id="gp_name">Grands Prix</th>
            <th id="races"> Number Of Races</th>
         </tr>

         {% for id in grandsprix_list %}
         <tr>
            <td>{{ id[0] }} </td>
            <td>{{ id[1] }} </td>

         </tr>
         {% endfor %}
      </table>


Here is the python code for these tables. *Circuits* are listed alphabetically by their names with using **ORDER BY** keyword. *Seasons* are listed alphabetically by circuit names
and *Grands Prix* is listed alphabetically by their names with using this keyword.

.. code-block:: python

   tracks_list = []
   seasons_list = []
   grandsprix_list = []

   with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query = """SELECT TRACKS.Circuit, TRACKS.Map, TRACKS.Type, TRACKS.Direction, LOCATION.Location, TRACKS.Length, GRANDS_PRIX.GrandsPrix, TRACKS.GrandsPrixHeld FROM TRACKS, GRANDS_PRIX, LOCATION WHERE (TRACKS.GP_Id = GRANDS_PRIX.Id) AND (LOCATION.Id = TRACKS.Location_Id) ORDER BY TRACKS.Circuit"""

            cursor.execute(query)

            for record in cursor:
                tracks_list.append(record)
            connection.commit()

            query = """SELECT Circuit_Name, Season FROM SEASONS ORDER BY Circuit_Name"""
            cursor.execute(query)
            for record in cursor:
                seasons_list.append(record)

            query = """SELECT GrandsPrix, No_of_Races FROM GRANDS_PRIX ORDER BY GrandsPrix"""
            cursor.execute(query)
            for record in cursor:
                grandsprix_list.append(record)



