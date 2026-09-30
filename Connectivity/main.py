import mysql.connector
# Connect to MySQL
dbConnection = mysql.connector.connect(host="localhost", user="root",  password="sakshi1805", database="tap")

dbCommand = dbConnection.cursor()

def  get_products():
    dbCommand.execute("SELECT * FROM products")
    result = dbCommand.fetchall()
    for row in result:
        print(row)


# DELETE
def delete_products():
    pid = int(input("Enter ID: "))
    sql = "DELETE FROM products WHERE pid=%s"   #Query
    dbCommand.execute(sql, (pid,))
    dbConnection.commit()
    print("Products deleted successfully")


# CREATE
def add_products():
    pid = int(input("Enter ID: "))
    pname = input("Enter Name: ")
    description = input("Enter Description: ")
    price = input(" Enter Price:")
    stock = input("Enter Stock:")

    sql = "INSERT INTO products (pid, pname, description,price,stock) VALUES (%s, %s, %s,%s,%s)"
    values = (pid, pname, description,price,stock)

    dbCommand.execute(sql, values)
    dbConnection.commit()
    print("Product added successfully")


# UPDATE
def update_products():
    pid = int(input("Enter PID: "))
    pname = input("Enter new PName: ")
    description = input("Enter new Description: ")
    price= input("Enter new Price: ")
    stock = input("Enter new Stock: ")
    

    sql = "UPDATE products SET pname=%s ,description=%s ,price=%s,stock=%s where pid=%s"
    values = (pid, pname, description,price,stock)

    dbCommand.execute(sql, values)
    dbConnection.commit()

    print("Products updated successfully")


#menu


while True:
    print("\n1. Add Product")
    print("2. Show Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_products()

    elif choice == "2":
        get_products()

    elif choice == "3":
        update_products()

    elif choice == "4":
        delete_products()

    elif choice == "5":
        break

    else:
        print("Invalid choice")

dbCommand.close()
dbConnection.close()



# Data Layer: MySQL database connection 
#             Creating database, inerting sample data,
#             Testing database using SQL commands, Join queires and Stored procedure 
#             from the prespective of DBA

# DAL "Data Access Layer"
#            from the perspective of a developer,
#            we will create a python application to connect to the database and
#            perform CRUD operations on the database.