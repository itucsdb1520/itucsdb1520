Parts Implemented by Mehmet Aygün
=================================

The database is created in the "initialize_db.py" file with default values.In initialize_db.py corresponding tables CARS,ENGINES and CREATOR tables created.

.. code-block:: python

    cursor.execute("""DROP TABLE IF EXISTS CARS""")
    cursor.execute("""DROP TABLE IF EXISTS ENGINES""")
    cursor.execute("""DROP TABLE IF EXISTS CREATORS""")


    cursor.execute("""CREATE TABLE ENGINES(Id SERIAL PRIMARY KEY,Engine_Name CHAR(30), HorsePower CHAR(30)) """)
    cursor.execute("""CREATE TABLE CREATORS(Id SERIAL PRIMARY KEY,Name CHAR(30)) """)
    cursor.execute("""CREATE TABLE CARS (Image_Link TEXT, Name CHAR(30) UNIQUE PRIMARY KEY NOT NULL,Engine_ID INTEGER references ENGINES(Id) ON DELETE CASCADE,Creator_ID INTEGER references CREATORS(Id) ON DELETE CASCADE,Speed CHAR(30),BRAND_ID INTEGER references PILOTS(Id) ON DELETE CASCADE,PILOT_ID INTEGER references TEAMS(Id) ON DELETE CASCADE)""")



    cursor.execute("""CREATE TABLE ENGINES(Id SERIAL PRIMARY KEY,Engine_Name CHAR(30), HorsePower CHAR(30)) """)
    cursor.execute("""CREATE TABLE CREATORS(Id SERIAL PRIMARY KEY,Name CHAR(30)) """)
    cursor.execute("""CREATE TABLE CARS (Image_Link TEXT, Name CHAR(30) UNIQUE PRIMARY KEY NOT NULL,Engine_ID INTEGER references ENGINES(Id) ON DELETE CASCADE,Creator_ID INTEGER references CREATORS(Id) ON DELETE CASCADE,Speed CHAR(30),BRAND_ID INTEGER references PILOTS(Id) ON DELETE CASCADE,PILOT_ID INTEGER references TEAMS(Id) ON DELETE CASCADE)""")


Firstly we check if tables exist or not and if they exist we delete them.Our main table is CARS table which include image link,Name that primary key and not nullable,Engine ID references from ENGINES,CREATOR ID also references from CREATOR table, and we BRAND and PILOT ID's also they are referenced from their tables.


At CREATORS and ENGINES table primary keys are IDs.Since CARS table referenced other tables we have to create at end and delete in first,if we try to delete other tables before other tables we get errors since our referenced tables are gone and we got errors.For adding,deleting,updating,searching and listing implemented their corresponding operations in server.py and for show result or getting input car_add.html and  car_delete.html pages are used.



.. toctree::
   member2/add
   member2/delete
   member2/update
   member2/search
   member2/list