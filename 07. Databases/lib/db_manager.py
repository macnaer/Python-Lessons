import mysql.connector
if __name__ == "__main__":
    db_manager


class db_manager:

    def __init__(self, host, user, passwd):
        self.__db = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd
        )
        self.__cursor = self.__db.cursor()
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS pythonlogin")
        self.__cursor.execute("USE pythonlogin")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Register\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search by username\n7. Search by email\n0. Exit\n====>>"))
            if choice == 1:
                print("Register")
            elif choice == 2:
                print("Login")
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choise")
