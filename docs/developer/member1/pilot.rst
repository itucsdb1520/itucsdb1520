Pilot
^^^^^


.. code-block:: python

   <table>

         <tr>
            <th > NAME</th>
            <th > SURNAME</th>
            <th > AGE </th>
            <th>  TEAM </th>
            <th > COUNTRY</th>
         </tr>
         {% for name, surname, age, team, country in pilots %}
         <tr>
            <td>{{ name }} </td>
            <td>{{ surname }} </td>
            <td>{{ age }} </td>
            <td>{{ team }} </td>
            <td>{{ country }} </td>
         </tr>
         {% endfor %}
      </table>

 This code in "pilots.html" shows values on page.

.. code-block:: python
      pilots = []
         with dbapi2.connect(app.config['dsn']) as connection:
                 cursor = connection.cursor()
                 query = """SELECT PILOTS.Name, PILOTS.Surname, PILOTS.Age, TEAMS.Teams, COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE PILOTS.Country=COUNTRIES.Id AND PILOTS.Team = TEAMS.Id;"""

                 cursor.execute(query)

                 for pilot in cursor:
                 pilots.append(pilot)

               connection.commit()

 This code selects values from tables in "server.py".
