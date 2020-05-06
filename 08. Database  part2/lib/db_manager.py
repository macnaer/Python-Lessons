import mysql.connector
import requests
from lib.settings import COVID19_URL
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
        self.__cursor.execute("CREATE DATABASE IF NOT EXISTS COVID19")
        self.__cursor.execute("USE COVID19")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS Global (id INT AUTO_INCREMENT PRIMARY KEY, NewConfirmed INT(10), TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT (10))")
        self.__cursor.execute(
            "CREATE TABLE IF NOT EXISTS Countries (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(12), Slug VARCHAR(255), NewConfirmed INT(10),TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT (10), Date DATE)")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Update data\n2. Login\n3. Edit\n4. Delete\n5. Show all users\n6. Search by username\n7. Search by email\n0. Exit\n====>> "))
            if choice == 1:
                answer = self.__update_covid_data()
                print(answer)
            elif choice == 2:
                print("Login")
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choise")

    def __update_covid_data(self):
        covid_data = requests.get(COVID19_URL)
        covid_data = covid_data.json()
        return covid_data

    def __register(self):
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        re_password = input("Retype password: ")

        if password != re_password:
            return "Password dont match"

        self.__cursor.execute(
            "SELECT * FROM users WHERE username='" + username + "'")
        result = self.__cursor.fetchone()
        if result != None:
            return "User exists"
        else:
            sql = "INSERT INTO users (username, email, password) VALUES (%s, %s,%s)"
            val = (username, email, password)
            self.__cursor.execute(sql, val)
            self.__db.commit()
            return "User created"
