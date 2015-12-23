Deleting Operations for Tracks, Grands Prix and Seasons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^




.. code-block:: html

   <form action="/track_delete" method="post">
   <h3> Delete a Track </h3>
   <div><label for='circuit_name'> Circuit Name : </label> <input type="text" name="circuit_name"></input></div>
   <div class =button""><input type="submit" value="Delete"></input></div>
   </form>





.. code-block:: python

   if request.method =='POST':
        circuit_name = request.form['circuit_name']
        with dbapi2.connect(app.config['dsn']) as connection:
            cursor = connection.cursor()
            query =  """DELETE FROM TRACKS WHERE Circuit=%s"""
            cursor.execute(query,([circuit_name]))
            connection.commit()