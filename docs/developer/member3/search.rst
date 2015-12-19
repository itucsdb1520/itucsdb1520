Search Brands and Founders
^^^^^^^^^^^^^^^^^^^^^^^^^^

The search function is common for all entities. In the main bar, where the search string is entered, there is also a field for selecting entities so that search can be specifically made for any entity.
When the search button is pressed, the string and field is sent as a form. Then python code takes the field and runs proper code. In the brands, the field is set as 4.

.. code-block:: python

   elif area == '4':
      search = "%" + search + "%"
      query = """SELECT * FROM BRANDS WHERE Name ILIKE %s"""
      cursor.execute(query, ([search]))
      for record in cursor:
        query_list.append(record)

      query = """SELECT * FROM BRANDS WHERE Industry ILIKE %s"""
      cursor.execute(query, ([search]))
      for record in cursor:
        query_list.append(record)

      query = """SELECT * FROM BRANDS WHERE Comment ILIKE %s"""
      cursor.execute(query, ([search]))
      for record in cursor:
        query_list.append(record)

      query_list = list(set(query_list))
      #remove duplicate elements in the list
      connection.commit()

The keyword is searched by adding "%" both in front and at end. This allows the string to be searched in between. The same string is searched through the brands table in 3 different columns.
Name, Industry and Comment sections are searched since the meaningful data is stored in those columns. Each match is added to the list and finally, by using "set" function the list is converted
to a set in order to remove duplicate elements. This list is printed in the search.html file.
