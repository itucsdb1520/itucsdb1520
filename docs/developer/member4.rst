Parts Implemented by Müşerref Ebru Özaltın
==========================================


**Grands_Prix**, **Location**, **Tracks**, **Seasons** tables are created in **initialize_db.py**.

**Grands_Prix** table consists of 3 columns which are Id, GrandsPrix and No_Of_Races.
*Id* is the serial primary key of this table, so it can not be NULL.

**Location** table consists of 2 columns: *Id* and *Location*. *Id* is the serial primary key, so it can not be NULL.

**Tracks** table uses some attributes of **Grands_Prix** and **Location** tables, so these tables are created before **Tracks** table. **Tracks** table consists of 8 columns: *Circuit, Map, Type, Direction, Location_Id, Current_Length, GP_Id* and *Grands Prix Held*.
The primary key for this table is *Circuit* and it can not be NULL as in the description of the table.
*GP_Id* and *Location_Id* are foreign keys and each *Circuit* must have a *GP_Id* attribute from **Grands_Prix** table and a *Location_Id* from **Location** table.

**Seasons** table consists of 2 columns: *Season* and *Circuit*. *Season* is the primary key, so it can not be NULL. *Circuit* is the foreign key.

.. code-block:: python
   cursor.execute("""CREATE TABLE GRANDS_PRIX (Id SERIAL PRIMARY KEY NOT NULL, GrandsPrix CHAR(30), No_of_Races INTEGER)""")

In *server.py* file, database operations for these tables are implemented by several functions.



.. toctree::
   member4/tracks
   member4/add
   member4/delete
   member4/update
   member4/search