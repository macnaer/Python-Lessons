if __name__ == "__main__":
    Users


class Users:

    def __init__(self, first_name, last_name, username, email, password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__username = username
        self.__email = email
        self.__password = password

    def show_user_info(self):
        print("First name: ", self.__first_name, "\nLast name: ",
              self.__last_name, "\nUsername : ", self.__username, "\nPassword : *******")

    def save_user(self):

        f = open('db.txt', 'a')
        f.write(self.__first_name + "#" + self.__last_name + "#" +
                self.__username + "#" + self.__email + "#" + self.__password+"\n")
        f.close()

    def show_all_users(self):
        users = []
        with open('db.txt', 'r') as shwo_user_db:
            item = shwo_user_db.readline()
            item = item.strip()
            item = item.split("#")
            users.append(item)
        return users
