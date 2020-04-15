
from lib.person import Users


user = Users("John", "Snow",
             "j_snow", "js@gmaol.com",
             "jonh's_secret")
user.show_user_info()
user.save_user()


user2 = Users("Bran", "Stark", "bs", "stark@winter.com", "passBran")
# user2.show_user_info()
user2.save_user()


users = user.show_all_users()
print(users)
