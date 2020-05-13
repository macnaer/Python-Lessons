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
            "CREATE TABLE IF NOT EXISTS Countries (id INT AUTO_INCREMENT PRIMARY KEY, Country VARCHAR(255), CountryCode VARCHAR(12), Slug VARCHAR(255), NewConfirmed INT(10),TotalConfirmed INT(10), NewDeaths INT(10), TotalDeaths INT(10), NewRecovered INT(10), TotalRecovered INT (10), Date VARCHAR(255))")

    def menu(self):
        exit = False
        while not exit:
            choice = int(input(
                "1. Update data\n2. Serach by country\n3. Serach by country code\n4. Top 10 total confirmed0\n5. Show all users\n6. Search by username\n7. Search by email\n0. Exit\n====>> "))
            if choice == 1:
                answer = self.__update_covid_data()
                print(answer)
            elif choice == 2:
                answer = self.__search_by_countries()
                print(answer)
            elif choice == 3:
                answer = self.__search_by_country_code()
                print(answer)
            elif choice == 0:
                exit = True
                print("Bye!")
            else:
                print("Wrong choise")

    def __update_covid_data(self):
        covid_data = requests.get(COVID19_URL).json()
        self.__cursor.execute("TRUNCATE TABLE global;")
        sql = "INSERT into global (NewConfirmed,TotalConfirmed,NewDeaths,TotalDeaths,NewRecovered,TotalRecovered) VALUES(%s,%s,%s,%s,%s,%s)"
        value = (covid_data['Global']["NewConfirmed"], covid_data['Global']["TotalConfirmed"], covid_data['Global']["NewDeaths"],
                 covid_data['Global']["TotalDeaths"], covid_data['Global']["NewRecovered"], covid_data['Global']["TotalRecovered"])
        self.__cursor.execute(sql, value)

        self.__cursor.execute("TRUNCATE TABLE countries")
        for item in covid_data['Countries']:
            sql = "INSERT into countries(Country, CountryCode, Slug, NewConfirmed, TotalConfirmed, NewDeaths, TotalDeaths, NewRecovered, TotalRecovered, Date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (item["Country"], item["CountryCode"], item["Slug"], item["NewConfirmed"], item["TotalConfirmed"],
                      item["NewDeaths"], item["TotalDeaths"], item["NewRecovered"], item["TotalRecovered"], item["Date"])
            self.__cursor.execute(sql, values)

        self.__db.commit()
        return "Database updated!"

    def __search_by_countries(self):
        country = input("Enter country: ")
        self.__cursor.execute(
            "SELECT * FROM countries WHERE Country='" + country + "'")
        result = self.__cursor.fetchone()
        if result == None:
            return ("Country " + country + " not found")
        else:
            return result

    def __search_by_country_code(self):
        country = input("Enter country code: ").upper()
        self.__cursor.execute(
            "SELECT * FROM countries WHERE CountryCode='" + country + "'")
        result = self.__cursor.fetchone()
        if result == None:
            return ("Country code " + country + " not found")
        else:
            return result
