def initialize_db_function(cursor):

    #Database for the counter
    cursor.execute("""DROP TABLE IF EXISTS COUNTER""")
    cursor.execute("""CREATE TABLE COUNTER (N INTEGER)""")
    cursor.execute("""INSERT INTO COUNTER (N) VALUES (0)""")


    #Database for the users

    cursor.execute("""DROP TABLE IF EXISTS USERS""")
    cursor.execute("""CREATE TABLE USERS (Username CHAR(20) UNIQUE PRIMARY KEY NOT NULL, Password CHAR(20) )""")

    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('aliercccan','pass')""")
    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('ebru','pass')""")
    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('fatih','pass')""")

    #Database for the admins

    cursor.execute("""DROP TABLE IF EXISTS ADMINS""")
    cursor.execute("""CREATE TABLE ADMINS(Username CHAR(20) UNIQUE PRIMARY KEY NOT NULL, Password CHAR(20) )""")

    cursor.execute("""INSERT INTO ADMINS (Username, Password) VALUES ('aliercccan','pass')""")
    cursor.execute("""INSERT INTO ADMINS (Username, Password) VALUES ('ebru','pass')""")
    cursor.execute("""INSERT INTO ADMINS (Username, Password) VALUES ('fatih','pass')""")

    #database for the brands

    cursor.execute("""DROP TABLE IF EXISTS FOUNDERS""")
    cursor.execute("""DROP TABLE IF EXISTS BRANDS""")
    cursor.execute("""CREATE TABLE BRANDS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Comment CHAR(75), Foundation INTEGER, Image Char(50), Industry CHAR(20), Website CHAR(25))""")
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Shell', 'One of the biggest petrochemistry companies in the world', 1907, 'shell_logo.svg', 'Oil Distribution', 'www.shell.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Kaspersky', 'An Antivirus Company founded in Moskov', 1997, 'Kaspersky_lab_logo.svg', 'Computer Security', 'www.kaspersky.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Pirelli', 'A Tire Company, founded in Milano as a plastic manufacturer', 1872, 'Pirelli_logo.svg', 'Auto and Parts', 'www.pirelli.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('UPS', 'A Parcel Service founded as post company in Seattle', 1907, 'UPS.svg', 'Courier', 'www.ups.com')""")
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Santander', '(Formerly Sovereign Bank) A subsidiary of Spanish Santander Group', 1875, 'Banco_Santander.svg', 'National Banks', 'www.santanderbank.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Alfa Romeo', 'An automobile manufacturer founded by an aristocrat family', 1910, 'Alfa_Romeo.svg', 'Automotive', 'www.alfaromeo.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Hublot', 'A clock manufacturer company', 1980, 'Hublot_logo.svg', 'Watchmaking', 'www.hublot.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Weichai', 'A Manufacturer and salesman of diesel engines', 2002, 'Weichai_Logo.svg', 'Automotive', 'www.weichai.com')""")
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('OMR', 'A car and motor manufacturer company', 1919, 'OMR_logo.png', 'Automotive', 'www.omrautomotive.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Mahle', 'An automotive parts manufacturer and one of the largest part suppliers', 1920, 'Mahle_logo.svg', 'Automotive', 'www.mahle.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Telcel', 'A wireless telecommunication company, originally named as Radio Movil Dipsa', 1984, 'Telcel_logo.svg', 'Telecommunication', 'www.telcel.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Brembo', 'A manufacturer of automotive brake systems especially for high-end cars', 1961, 'Brembo_logo.svg', 'Automotive', 'www.brembo.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('NGK Spark Plug', 'A manufacturer and saler of spark plugs and combustion engines', 1936, 'Ngk_logo_rund.svg', 'Spark Plugs', 'www.ngkntk.co.jp') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('Magneti Marelli', 'A company which deals with development and manufacturing of systems', 1919, 'Marelli_logo.png', 'Automotive', 'www.magnetimarelli.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('SKF', 'A leading bearing and seals manufacturing company', 1907, 'SKF_logo.svg', 'Manufacturing', 'www.skf.com') """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website) VALUES ('HAAS', 'A machine and CNC tools manufacturer founded in California', 1983, 'Haas_logo.jpg', 'Manufacturing', 'www.haascnc.com') """)
    cursor.execute("""CREATE TABLE FOUNDERS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Surname CHAR(25), Brand_Id INTEGER references BRANDS(Id) ON DELETE CASCADE)""")
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Marcus', 'Samuel', 1) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Yevgeni', 'Kasperski', 2) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Giovanni Battista', 'Pirelli', 3) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('James E.', 'Casey', 4) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Jose Antonio', 'Alvarez', 5) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Alexandre', 'Darracq', 6) """) #more than one will be implemented later
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Carlo', 'Crocco', 7) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Tan', 'Xuguang', 8) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Marco', 'Righi', 9) """)  #more than one, will be implemented later
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Ernst', 'Mahle', 10) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('America', 'Movil', 11) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Emilio', 'Bombassei', 12) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Shinichi', 'Odo', 13) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Ercole', 'Marelli', 14) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Sven', 'Wingqvist', 15) """)
    cursor.execute("""INSERT INTO FOUNDERS (Name, Surname, Brand_Id) VALUES ('Gene Francis', 'Haas', 16) """)

    #database for the cars
    cursor.execute("""DROP TABLE IF EXISTS CARS""")
    cursor.execute("""DROP TABLE IF EXISTS ENGINES""")

    cursor.execute("""CREATE TABLE ENGINES(Id SERIAL PRIMARY KEY,Engine_Name CHAR(30), HorsePower CHAR(30)) """)
    cursor.execute("""CREATE TABLE CARS (Image_Link TEXT, Name CHAR(30) UNIQUE PRIMARY KEY NOT NULL,Engine_ID INTEGER references ENGINES(Id) ON DELETE CASCADE,Speed CHAR(30),BRAND CHAR(50),PILOT CHAR(50) )""")

    cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('R13','300')""")
    cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('H15','320')""")
    cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('T15','350')""")

    cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.parrola.com/wp-content/uploads/2013/01/mclaren-mercedes-formula-1.jpg','V13',1,'300','Mercedes','Fernando Alonso')""")
    cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.f1fanatic.co.uk/wp-content/uploads/2008/01/ferrari_f2008_launch_4.jpg','MH13',2,'320','Ferrari','James Hamilton' )""")
    cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.autoguide.com/auto-news/wp-content/uploads/2013/07/honda-f1.jpg','V15',1,'330','Honda','Torro Rosso')""")
    cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Speed,BRAND,PILOT) VALUES ('http://www.sport-wall.com/wp-content/uploads/2015/03/Formula-1-Renault-F1-Car-680x425.jpg','RT3',3,'350','Renault','Jason Button')""")



    #database for the pilots
    cursor.execute("""DROP TABLE IF EXISTS COUNTRIES""")
    cursor.execute("""DROP TABLE IF EXISTS PILOTS""")
    cursor.execute("""CREATE TABLE PILOTS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Surname CHAR(25), Age INTEGER )""")
    cursor.execute("""CREATE TABLE COUNTRIES (Id SERIAL PRIMARY KEY NOT NULL, Countries CHAR(25),ForeignKey INTEGER references PILOTS(Id ))""")



  #database for the tracks
    cursor.execute("""DROP TABLE IF EXISTS COUPLING_T_GP""")
    cursor.execute("""DROP TABLE IF EXISTS GRANDS_PRIX""")
    cursor.execute("""DROP TABLE IF EXISTS SEASONS""")
    cursor.execute("""DROP TABLE IF EXISTS TRACKS""")


    cursor.execute("""CREATE TABLE TRACKS (Circuit CHAR(50) UNIQUE PRIMARY KEY NOT NULL, Map TEXT, Type CHAR(20), Direction CHAR(20), Location CHAR(50), Length CHAR(20), GrandsPrixHeld INTEGER)""")
    cursor.execute("""CREATE TABLE SEASONS (Id SERIAL PRIMARY KEY, Circuit_Name CHAR(50) references TRACKS(Circuit) ON DELETE CASCADE, Season CHAR(15))""")
    cursor.execute("""CREATE TABLE GRANDS_PRIX (Id INTEGER PRIMARY KEY, GrandsPrix CHAR(30), No_of_Races INTEGER)""")
    cursor.execute("""CREATE TABLE COUPLING_T_GP ( Id SERIAL PRIMARY KEY, Circuit_Name CHAR(50) references TRACKS(Circuit) ON DELETE CASCADE, GP_Id INTEGER references GRANDS_PRIX(Id) ON DELETE CASCADE)""")


    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Adelaide Street Circuit','https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/Adelaide_%28long_route%29.svg/225px-Adelaide_%28long_route%29.svg.png', 'Street Circuit', 'Clockwise', 'Adelaide, Australia', '3.780 km', 11)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Ain-Diab Circuit', 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Ain-Diab.svg/225px-Ain-Diab.svg.png', 'Road circuit', 'Clockwise', 'Casablanca, Morocco', '7.618 km ', 1)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Aintree', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Circuit_Aintree.svg/225px-Circuit_Aintree.svg.png', 'Road circuit', 'Clockwise', 'Liverpool, United Kingdom', '4.828 km', 5)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Albert Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Albert_Lake_Park_Street_Circuit_in_Melbourne%2C_Australia.svg/225px-Albert_Lake_Park_Street_Circuit_in_Melbourne%2C_Australia.svg.png', 'Street circuit', 'Clockwise', 'Melbourne, Australia', '5.303 km', 20)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Brands Hatch', 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Brands_Hatch.svg/225px-Brands_Hatch.svg.png', 'Race circuit', 'Clockwise', 'Kent, United Kingdom', '3.703 km', 14)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Circuit de Barcelona-Catalunya', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Catalunya.svg/225px-Catalunya.svg.png', 'Race circuit', 'Clockwise', 'Montmelo, Spain', '4.655 km', 25)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Circuit de Monaco', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Monte_Carlo_Formula_1_track_map.svg/225px-Monte_Carlo_Formula_1_track_map.svg.png', 'Street circuit', 'Clockwise', 'Monte Carlo, Monaco', '3.337 km', 62)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Dijon-Prenois', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Dijon-Prenois_Circuit.svg/225px-Dijon-Prenois_Circuit.svg.png', 'Race circuit', 'Clockwise', 'Dijon, France', '3.886 km', 6)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Istanbul Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Istanbul_park.svg/225px-Istanbul_park.svg.png', 'Race Circuit', 'Anti-clockwise', 'Istanbul, Turkey', '5.338 km', 7)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Nurburgring', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Circuit_N%C3%BCrburgring-2002-GP.svg/225px-Circuit_N%C3%BCrburgring-2002-GP.svg.png', 'Race circuit', 'Clockwise', 'Nurburg, Germany', '5.148 km', 40)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Red Bull Ring', 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Circuit_Red_Bull_Ring.svg/225px-Circuit_Red_Bull_Ring.svg.png', 'Race circuit', 'Clockwise', 'Zeltweg, Austria', '4.326 km', 27)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Sepang International Circuit', 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Sepang.svg/225px-Sepang.svg.png', 'Race circuit', 'Clockwise', 'Kuala Lumpur, Malaysia', '5.543 km', 17)""")

    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Ain-Diab Circuit', '1958')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Aintree', '1955')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Aintree', '1957')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Aintree', ' 1959')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Aintree', '1961-1962')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Albert Park', '1996-2015')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Brands Hatch', '1964')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Brands Hatch', '1966')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Brands Hatch', '1968')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Brands Hatch', '1970')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Brands Hatch', '1972')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Brands Hatch', '1974')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Brands Hatch', '1976-1986')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Circuit de Barcelona-Catalunya', '1991-2015')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Circuit de Monaco', '1950')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Circuit de Monaco', '1955-2015')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Dijon-Prenois', '1974')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Dijon-Prenois', '1979')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Dijon-Prenois', '1981-1982')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Istanbul Park', '2005-2011')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '1951-1954')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '1956-1958')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '1961-1969')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '1971-1976')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '1995-2007')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '2013')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Red Bull Ring', '1997-2003')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Red Bull Ring', '2014-2015')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Sepang International Circuit', '1999-2015')""")

    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (1, 'Abu Dhabi Grand Prix', 7)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (2, 'Argentine Grand Prix', 20)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (3, 'Australian Grand Prix', 31)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (4, 'Austrian Grand Prix', 28)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (5, 'European Grand Prix', 22)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (6, 'French Grand Prix', 58)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (7, 'German Grand Prix', 61)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (8, 'British Grand Prix', 66)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (9, 'Luxembourg Grand Prix', 2)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (10, 'Malaysian Grand Prix', 17)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (11, 'Monaco Grand Prix', 62)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (12, 'Moroccan Grand Prix', 1)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (13, 'Spanish Grand Prix', 45)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (14, 'Swiss Grand Prix', 6)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( Id, GrandsPrix, No_of_Races) VALUES (15, 'Turkish Grand Prix', 7)""")

    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Adelaide Street Circuit', 3)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Ain-Diab Circuit', 12)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Aintree', 8)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Albert Park', 3)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Brands Hatch', 8)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Brands Hatch', 5)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Circuit de Barcelona-Catalunya', 13)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Circuit de Monaco', 11)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Dijon-Prenois', 6)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Dijon-Prenois', 14)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Istanbul Park', 15)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Nurburgring', 7)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Nurburgring', 5)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Nurburgring', 9)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Red Bull Ring', 4)""")
    cursor.execute("""INSERT INTO COUPLING_T_GP (Circuit_Name, GP_Id ) VALUES ('Sepang International Circuit', 10)""")