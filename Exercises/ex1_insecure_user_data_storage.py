# Exercise 1: Insecure User Data Storage
# ---------------------------------------
# This script demonstrates how NOT to store user data, especially sensitive
# information like usernames and passwords. As a software architect and security
# expert, you should identify architectural flaws (e.g., plain text storage) and
# propose secure alternatives such as password hashing, encryption, and proper
# database usage.

def storeuserdata(user_data):
   database = open('user_database.txt', 'a')
   database.write(str(user_data))
   database.close()

storeuserdata({'username': 'admin', 'password': '1234'})
