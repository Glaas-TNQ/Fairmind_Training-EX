def storeuserdata(user_data):
   database = open('user_database.txt', 'a')
   database.write(str(user_data))
   database.close()

storeuserdata({'username': 'admin', 'password': '1234'})
