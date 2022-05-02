import mysql.connector

def DataUpdate(name, location, destination, car_type, total_people, date, time):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",  
        passwd="",
        database="Cab_Booking"
    )

    mycursor = mydb.cursor()
    
    # sql='INSERT INTO Cab (Name) VALUES (\'{0}\');'.format(Name)
    sql = f"INSERT INTO Cab (name, location, destination, car_type, total_people, date, time) VALUES ('{name}', '{location}', '{destination}', '{car_type}', {total_people}, '{date}', '{time}');"
    # id=f"SELECT id FROM Cab WHERE name='{name}'"    
    # print(id) 
    mycursor.execute(sql)
    # x=mycursor.execute(id)
    # print(x) 
    mydb.commit()

def DataDelete(name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",  
        passwd="",
        database="Cab_Booking"
    )

    mycursor = mydb.cursor()
    
    sql = f"DELETE FROM Cab WHERE name = ('{name}');"
    mycursor.execute(sql) 
    mydb.commit()