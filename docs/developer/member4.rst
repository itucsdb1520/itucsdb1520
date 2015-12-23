Parts Implemented by Müşerref Ebru Özaltın
==========================================


**GRANDS_PRIX**, **LOCATION**, **TRACKS** tables are created in **initialize_db.py**.
**GRANDS_PRIX** table consists of 3 columns which are Id, GrandsPrix and No_Of_Races.
*Id* is the serial primary key of this table, so it can not be NULL.

**LOCATION** table consists of 2 columns: Id and Location. *Id* is the serial primary key, so it can not be NULL.

**TRACKS** table uses some attributes of **GRANDS_PRIX** and **LOCATION** tables, so these tables are created before **TRACKS** table. **TRACKS** table consists of 8 columns: Circuit, Map, Type, Direction, Location_Id, Current_Length, GP_Id and Grands Prix Held.
The primary key for this table is *Circuit* and it can not be NULL as in the description of the table. Each *Circuit* must have a *GP_ID* attribute from **GRANDS_PRIX** table and a *Location_ID* from **LOCATION** table.



.. code-block:: python
   cursor.execute("""DROP TABLE IF EXISTS SEASONS""")
   cursor.execute("""DROP TABLE IF EXISTS TRACKS""")
   cursor.execute("""DROP TABLE IF EXISTS GRANDS_PRIX""")
   cursor.execute("""DROP TABLE IF EXISTS LOCATION""")

   cursor.execute("""CREATE TABLE LOCATION (Id SERIAL PRIMARY KEY NOT NULL, Location CHAR(50))""")
   cursor.execute("""CREATE TABLE GRANDS_PRIX (Id SERIAL PRIMARY KEY NOT NULL, GrandsPrix CHAR(30), No_of_Races INTEGER)""")
   cursor.execute("""CREATE TABLE TRACKS (Circuit CHAR(50) UNIQUE PRIMARY KEY NOT NULL, Map TEXT, Type CHAR(20), Direction CHAR(20), Location_Id INTEGER references LOCATION(Id) ON DELETE CASCADE, Length CHAR(20), GP_Id INTEGER references GRANDS_PRIX(Id) ON DELETE CASCADE, GrandsPrixHeld INTEGER)""")
   cursor.execute("""CREATE TABLE SEASONS (Id SERIAL PRIMARY KEY NOT NULL, Circuit_Name CHAR(50) references TRACKS(Circuit) ON DELETE CASCADE, Season CHAR(15))""")
