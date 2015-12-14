def initialize_db_function(cursor):

    #Database for the counter
    cursor.execute("""DROP TABLE IF EXISTS COUNTER""")
    cursor.execute("""CREATE TABLE COUNTER (N INTEGER)""")
    cursor.execute("""INSERT INTO COUNTER (N) VALUES (0)""")


    #Database for the users
    cursor.execute("""DROP TABLE IF EXISTS USERS""")
    cursor.execute("""CREATE TABLE USERS (Username CHAR(20) UNIQUE PRIMARY KEY NOT NULL, Password CHAR(20) )""")

    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('user','user')""")
    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('admin','admin')""")
    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('aliercccan','pass')""")
    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('ebru','pass')""")
    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('fatih','pass')""")

    #Database for the admins
    cursor.execute("""DROP TABLE IF EXISTS ADMINS""")
    cursor.execute("""CREATE TABLE ADMINS(Username CHAR(20) UNIQUE PRIMARY KEY NOT NULL, Password CHAR(20) )""")

    cursor.execute("""INSERT INTO USERS (Username, Password) VALUES ('admin','admin')""")
    cursor.execute("""INSERT INTO ADMINS (Username, Password) VALUES ('aliercccan','pass')""")
    cursor.execute("""INSERT INTO ADMINS (Username, Password) VALUES ('ebru','pass')""")
    cursor.execute("""INSERT INTO ADMINS (Username, Password) VALUES ('fatih','pass')""")

    #database for the pilots
    cursor.execute("""DROP TABLE IF EXISTS FOUNDERS, BRANDS""")
    cursor.execute("""DROP TABLE IF EXISTS PILOTS, COUNTRIES CASCADE""")
    cursor.execute("""DROP TABLE IF EXISTS TEAMS CASCADE""")

    cursor.execute("""CREATE TABLE COUNTRIES (Id SERIAL PRIMARY KEY NOT NULL, Countries CHAR(25) Unique)""")
    cursor.execute("""CREATE TABLE TEAMS (Id SERIAL PRIMARY KEY NOT NULL, Teams CHAR(25) Unique)""")
    cursor.execute("""CREATE TABLE PILOTS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Surname CHAR(25), Age INTEGER, Team INTEGER references TEAMS(Id), Country INTEGER references COUNTRIES(Id) )""")


    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('MERCEDES')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('FERRARI')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('WILLIAMS')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('RED BULL RACING')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('FORCE INDIA')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('LOTUS')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('TORO ROSSO')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('SAUBER')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('MCLAREN')""")
    cursor.execute("""INSERT INTO TEAMS ( Teams) VALUES ('MARUSSIA')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Great Britain')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Germany')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Finland')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Brazil')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Russia')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Australia')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Mexico')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('France')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Netherlands')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Venezuela')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Spain')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Sweden')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('United States')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Japan')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Italy')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('Switzerland')""")
    cursor.execute("""INSERT INTO COUNTRIES ( Countries) VALUES ('China')""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Lewis','Hamilton', 30, 1, 1)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Nico','Rosberg', 30, 1, 2)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Sebastian','Vettel', 28, 2 ,2)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Kimi','Raikkonen', 36, 2, 3)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Valtteri','Bottas', 26, 3, 3)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Felipe','Massa', 24, 3, 4)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Daniil','Kvyat', 21, 4, 5)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Daniel','Ricciardo', 26, 4, 6)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Sergio','Perez', 25, 5, 7)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Nico','Hulkenberg', 28, 5, 2)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Romain','Grosjean', 29, 6, 8)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Max','Verstappen', 18, 7, 9)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Felipe','Nasr', 23, 8, 4)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Pastor','Maldonado', 30, 6, 10)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Carlos','Sainz', 21, 7, 11)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Jenson','Button', 35, 9, 1)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Fernando','Alonso', 34, 9, 11)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Marcus','Ericsson', 25, 8, 12)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Roberto','Merhi', 24, 10, 11)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Alexander','Rossi', 24, 10, 13)""")
    cursor.execute("""INSERT INTO PILOTS ( Name, Surname, Age, Team, Country) VALUES ('Will','Stevens', 24, 10, 1)""")




    #database for the brands
    cursor.execute("""CREATE TABLE BRANDS (Id SERIAL PRIMARY KEY NOT NULL, Name CHAR(25), Comment CHAR(75), Foundation INTEGER, Image Char(50), Industry CHAR(20), Website CHAR(25), CountryId INTEGER References COUNTRIES(Id))""")
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Shell', 'One of the biggest petrochemistry companies in the world', 1907, 'shell_logo.svg', 'Oil Distribution', 'www.shell.com', 9)""")
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Kaspersky', 'An Antivirus Company founded in Moskov', 1997, 'Kaspersky_lab_logo.svg', 'Computer Security', 'www.kaspersky.com', 5) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Pirelli', 'A Tire Company, founded in Milano as a plastic manufacturer', 1872, 'Pirelli_logo.svg', 'Auto and Parts', 'www.pirelli.com', 15) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('UPS', 'A Parcel Service founded as post company in Seattle', 1907, 'UPS.svg', 'Courier', 'www.ups.com', 13)""")
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Santander', '(Formerly Sovereign Bank) A subsidiary of Spanish Santander Group', 1875, 'Banco_Santander.svg', 'National Banks', 'www.santanderbank.com', 11) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Alfa Romeo', 'An automobile manufacturer founded by an aristocrat family', 1910, 'Alfa_Romeo.svg', 'Automotive', 'www.alfaromeo.com', 15) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Hublot', 'A clock manufacturer company', 1980, 'Hublot_logo.svg', 'Watchmaking', 'www.hublot.com', 16) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Weichai', 'A Manufacturer and salesman of diesel engines', 2002, 'Weichai_Logo.svg', 'Automotive', 'www.weichai.com', 17)""")
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('OMR', 'A car and motor manufacturer company', 1919, 'OMR_logo.png', 'Automotive', 'www.omrautomotive.com', 15) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Mahle', 'An automotive parts manufacturer and one of the largest part suppliers', 1920, 'Mahle_logo.svg', 'Automotive', 'www.mahle.com', 2) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Telcel', 'A wireless telecommunication company, originally named as Radio Movil Dipsa', 1984, 'Telcel_logo.svg', 'Telecommunication', 'www.telcel.com', 7) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Brembo', 'A manufacturer of automotive brake systems especially for high-end cars', 1961, 'Brembo_logo.svg', 'Automotive', 'www.brembo.com', 15) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('NGK Spark Plug', 'A manufacturer and saler of spark plugs and combustion engines', 1936, 'Ngk_logo_rund.svg', 'Spark Plugs', 'www.ngkntk.co.jp', 14) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('Magneti Marelli', 'A company which deals with development and manufacturing of systems', 1919, 'Marelli_logo.png', 'Automotive', 'www.magnetimarelli.com', 15) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('SKF', 'A leading bearing and seals manufacturing company', 1907, 'SKF_logo.svg', 'Manufacturing', 'www.skf.com', 12) """)
    cursor.execute("""INSERT INTO BRANDS (Name, Comment, Foundation,  Image, Industry, Website, CountryId) VALUES ('HAAS', 'A machine and CNC tools manufacturer founded in California', 1983, 'Haas_logo.jpg', 'Manufacturing', 'www.haascnc.com', 13) """)
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
    cursor.execute("""DROP TABLE IF EXISTS CREATORS""")


    cursor.execute("""CREATE TABLE ENGINES(Id SERIAL PRIMARY KEY,Engine_Name CHAR(30), HorsePower CHAR(30)) """)
    cursor.execute("""CREATE TABLE CREATORS(Id SERIAL PRIMARY KEY,Name CHAR(30)) """)
    cursor.execute("""CREATE TABLE CARS (Image_Link TEXT, Name CHAR(30) UNIQUE PRIMARY KEY NOT NULL,Engine_ID INTEGER references ENGINES(Id) ON DELETE CASCADE,Creator_ID INTEGER references CREATORS(Id) ON DELETE CASCADE,Speed CHAR(30),BRAND_ID INTEGER references PILOTS(Id) ON DELETE CASCADE,PILOT_ID INTEGER references TEAMS(Id) ON DELETE CASCADE)""")


    cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('R13','300')""")
    cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('H15','320')""")
    cursor.execute("""INSERT INTO ENGINES (Engine_Name , HorsePower) VALUES ('T15','350')""")


    cursor.execute("""INSERT INTO CREATORS (Name) VALUES ('John Wick')""")
    cursor.execute("""INSERT INTO CREATORS (Name) VALUES ('Xio Hua')""")
    cursor.execute("""INSERT INTO CREATORS (Name) VALUES ('Alfred Long')""")

    cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Creator_ID,Speed,BRAND_ID,PILOT_ID) VALUES ('http://www.f1fanatic.co.uk/wp-content/uploads/2008/01/ferrari_f2008_launch_4.jpg','MH13',2,2,'300',2,1)""")
    cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Creator_ID,Speed,BRAND_ID,PILOT_ID) VALUES ('http://www.autoguide.com/auto-news/wp-content/uploads/2013/07/honda-f1.jpg','V15',3,1,'300',3,2)""")
    cursor.execute("""INSERT INTO CARS (Image_Link,Name,Engine_ID,Creator_ID,Speed,BRAND_ID,PILOT_ID) VALUES ('http://www.sport-wall.com/wp-content/uploads/2015/03/Formula-1-Renault-F1-Car-680x425.jpg','RT3',3,1,'300',3,2)""")








    #database for the tracks
    cursor.execute("""DROP TABLE IF EXISTS SEASONS""")
    cursor.execute("""DROP TABLE IF EXISTS TRACKS""")
    cursor.execute("""DROP TABLE IF EXISTS GRANDS_PRIX""")
    cursor.execute("""DROP TABLE IF EXISTS LOCATION""")

    cursor.execute("""CREATE TABLE LOCATION (Id SERIAL PRIMARY KEY NOT NULL, Location CHAR(50))""")
    cursor.execute("""CREATE TABLE GRANDS_PRIX (Id SERIAL PRIMARY KEY NOT NULL, GrandsPrix CHAR(30), No_of_Races INTEGER)""")
    cursor.execute("""CREATE TABLE TRACKS (Circuit CHAR(50) UNIQUE PRIMARY KEY NOT NULL, Map TEXT, Type CHAR(20), Direction CHAR(20), Location_Id INTEGER references LOCATION(Id) ON DELETE CASCADE, Length CHAR(20), GP_Id INTEGER references GRANDS_PRIX(Id) ON DELETE CASCADE, GrandsPrixHeld INTEGER)""")
    cursor.execute("""CREATE TABLE SEASONS (Id SERIAL PRIMARY KEY NOT NULL, Circuit_Name CHAR(50) references TRACKS(Circuit) ON DELETE CASCADE, Season CHAR(15))""")

    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('German Grand Prix', 61)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Turkish Grand Prix', 7)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Austrian Grand Prix', 28)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('European Grand Prix', 22)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('French Grand Prix', 58)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('British Grand Prix', 66)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Luxembourg Grand Prix', 2)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Malaysian Grand Prix', 17)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Monaco Grand Prix', 62)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Moroccan Grand Prix', 1)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Spanish Grand Prix', 45)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Swiss Grand Prix', 6)""")
    cursor.execute("""INSERT INTO GRANDS_PRIX ( GrandsPrix, No_of_Races) VALUES ('Australian Grand Prix', 31)""")

    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Istanbul, Turkey')""")
    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Nurburg, Germany')""")
    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Liverpool, United Kingdom')""")
    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Melbourne, Australia')""")
    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Montmelo, Spain')""")
    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Monte Carlo, Monaco')""")
    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Dijon, France')""")
    cursor.execute("""INSERT INTO LOCATION ( Location) VALUES ('Zeltweg, Austria')""")


    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_Id, Length, GP_Id, GrandsPrixHeld) VALUES ('Istanbul Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Istanbul_park.svg/225px-Istanbul_park.svg.png', 'Race Circuit', 'Anti-clockwise', 1, '5.338 km', 2, 7)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_Id, Length, GP_Id, GrandsPrixHeld) VALUES ('Nurburgring', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Circuit_N%C3%BCrburgring-2002-GP.svg/225px-Circuit_N%C3%BCrburgring-2002-GP.svg.png', 'Race circuit', 'Clockwise', 2, '5.148 km', 1, 40)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_Id, Length, GP_Id, GrandsPrixHeld) VALUES ('Aintree', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Circuit_Aintree.svg/225px-Circuit_Aintree.svg.png', 'Road circuit', 'Clockwise', 3, '4.828 km', 6, 5)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_Id, Length, GP_Id, GrandsPrixHeld) VALUES ('Albert Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Albert_Lake_Park_Street_Circuit_in_Melbourne%2C_Australia.svg/225px-Albert_Lake_Park_Street_Circuit_in_Melbourne%2C_Australia.svg.png', 'Street circuit', 'Clockwise', 4, '5.303 km', 13, 20)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_Id, Length, GP_Id, GrandsPrixHeld) VALUES ('Circuit de Barcelona-Catalunya', 'https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Catalunya.svg/225px-Catalunya.svg.png', 'Race circuit', 'Clockwise', 5, '4.655 km', 11, 25)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_Id, Length, GP_Id, GrandsPrixHeld) VALUES ('Circuit de Monaco', 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Monte_Carlo_Formula_1_track_map.svg/225px-Monte_Carlo_Formula_1_track_map.svg.png', 'Street circuit', 'Clockwise', 6, '3.337 km', 9, 62)""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location_Id, Length, GP_Id, GrandsPrixHeld) VALUES ('Dijon-Prenois', 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Dijon-Prenois_Circuit.svg/225px-Dijon-Prenois_Circuit.svg.png', 'Race circuit', 'Clockwise', 7, '3.886 km', 5, 6)""")

    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Istanbul Park', '2005-2011')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '1995-2007')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '2013')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Nurburgring', '1971-1976')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Circuit de Barcelona-Catalunya', '1991-2015')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Circuit de Monaco', '1950')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Circuit de Monaco', '1955-2015')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Dijon-Prenois', '1981-1982')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Aintree', '1961-1962')""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season ) VALUES ('Albert Park', '1996-2015')""")

