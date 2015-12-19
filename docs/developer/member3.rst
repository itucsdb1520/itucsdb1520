Parts Implemented by Muhammet Sadık Uğursoy
===========================================

The database is created in the "initialize_db.py" file with default values. The brands and founders tables are implemented while countries table which is already created by another member is used. The brands tuples consist of 8 columns: id, name, comment, foundation, image, industry, website and countryId.
The primary key is "id" and the foreign key is countryId in this table. Brand's own id is given automatically so it is guaranteed that it is not NULL. Foundation can not be NULL because of the definition of it on the HTML and country id can not be NULL because of the reference validation. Other fields can be NULL.

The brands database is dependent to countries tables. Each brand has to have a country id value from the countries table. In the interface, adding a country is made by entering the name of the country, however since the brands table holds the country id as an integer, the entered name is not directly added to that table.
It has been searched in the countries table by the country name and when a match is found, its id is returned and added to the brands tuple. There is a cascade relation between a brand and a founder: when a brand is deleted, the corresponding founder is removed as well since it would not make sense to hold a founder that has not founded a brand in the database.
This case is not hold for countries table since it is used by another table: pilots.

Founders database is dependen on the brands. It uses a brand id as a reference thus deleting a founder does not delete the brand since a brand can exist if there is no founder. A founder is not feasible if there is no brand it has founded so deleting the brand will cause the founder to be deleted as well. This is provided by "ON DELETE CASCADE" in the table definition.

.. code-block:: python
   cursor.execute("""CREATE TABLE FOUNDERS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Surname CHAR(25), Brand_Id INTEGER references BRANDS(Id) ON DELETE CASCADE)""")



.. toctree::

   member3/add
   member3/delete
   member3/update
   member3/search
