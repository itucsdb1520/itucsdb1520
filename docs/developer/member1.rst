Parts Implemented by Fatih Demirel
==================================

Created pilots, countries, and teams tables in "initialize_db.py".
At the beginning the database has given values in "initialize_db.py".



Table of operations:

============== =============
OPERATION      SUB OPERATION
============== =============
pilots         name,
               surname,
               age,
               team,
               country
countries      id,
               country
teams          id,
               team
add pilot
add country
add team
delete pilot
delete country
delete team
update pilot
update country
update team
============== =============

The sub operations are not taken as a different variable, instead they are gatheren in the same "operation" variable. The sub operation string is splitted with a "-" from the main operation. In the pyton code, it there is a try catch mechanism to split the text.

.. code-block:: python
   splitted = operation.split('-', 1)
   operation = splitted[0]
   #print(splitted)
   try:
      sub_operation = splitted[1]
      make_sub_operation = True
   except:
      #print("Single String, not splitted")
      make_sub_operation = False

The main and sub operation is gathered by this piece of code and the flag is set whether if there will be a sub operation or not. The only sub operations are on the listing phase. After this part, the corresponding operation is done by if-elif-else statements.

.. toctree::
   member3/list
   member3/add
   member3/delete
   member3/update
   member3/search
