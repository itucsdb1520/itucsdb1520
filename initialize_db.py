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
    cursor.execute("""DROP TABLE IF EXISTS TRACKS""")
    cursor.execute("""DROP TABLE IF EXISTS SEASONS""")
    cursor.execute("""CREATE TABLE TRACKS (Circuit CHAR(50) UNIQUE PRIMARY KEY NOT NULL, Map TEXT, Type CHAR(20), Direction CHAR(20), Location CHAR(50), Length CHAR(20), GrandsPrixHeld INTEGER)""")
    cursor.execute("""CREATE TABLE SEASONS (Id SERIAL PRIMARY KEY NOT NULL, Circuit_Name CHAR(50)references TRACKS(Circuit) ON DELETE CASCADE, Season CHAR(10))""")
    cursor.execute("""INSERT INTO TRACKS (Circuit, Map, Type, Direction, Location, Length, GrandsPrixHeld) VALUES ('Istanbul Park', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/Istanbul_park.svg/225px-Istanbul_park.svg.png', 'Race Circuit', 'Anti-clockwise', 'Istanbul, Turkey', '5.338 km', 7)""")
    cursor.execute("""INSERT INTO SEASONS (Circuit_Name, Season) VALUES ('Istanbul Park', '2005-2011')""")
