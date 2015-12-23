Searching Operations for Tracks, Grands Prix and Seasons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




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


