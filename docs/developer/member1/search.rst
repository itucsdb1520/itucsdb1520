Search
^^^^^^

Searching operation in "server.py" of code:
.. code-block:: python
   elif area == '2':
   search = "%" + search +"%"
                query = """  SELECT PILOTS.Name, PILOTS.Surname, TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (PILOTS.Name LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)

                query = """  SELECT PILOTS.Name, PILOTS.Surname,  TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (PILOTS.Surname LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)

                query = """  SELECT PILOTS.Name, PILOTS.Surname, TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (COUNTRIES.Countries LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)


                query = """  SELECT PILOTS.Name, PILOTS.Surname, TEAMS.Teams,COUNTRIES.Countries FROM PILOTS, COUNTRIES, TEAMS WHERE (TEAMS.Teams LIKE %s) AND (PILOTS.Country = COUNTRIES.Id AND PILOTS.Team = TEAMS.Id) """
                cursor.execute(query, ([search]))
                for klm in cursor:
                    query_list.append(klm)


                query_list = list(set(query_list))
                print(query_list)
                connection.commit()
                return render_template('search.html', current_time= now.ctime(), query_list = query_list, table = 2)


