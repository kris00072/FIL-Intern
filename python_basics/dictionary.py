userName=["bob","Mike","Rahul","Mehul"]
email=["bob@gmail.com","mikegmail.com","rahul@gmail.com","Mehulgmail.com"]

dictionary={userName:email for userName,email in zip(userName,email)if "@" in email}
print(dictionary)