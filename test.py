from libs.DB import DB

con = DB()
data = [
		{'name' :'rohit','email':'gade.rohitreddy@gmail.com','password':12345,"is_deleted":False},		
		{'name' :'ram','email':'ram@gmail.com','password':12345,"is_deleted":False},
		{'name' :'ravi','email':'ravi@gmail.com','password':12345,"is_deleted":False},
		{'name' :'sai','email':'sai@gmail.com','password':12345,"is_deleted":False}
]

# con.delete('users')
cursor = con.find('users','password',12345)
for val in cursor:
	print(val)
