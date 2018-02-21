from pymongo import MongoClient
class DB(object
	):

	db = None
	def __init__(self):
		try:
			clint = MongoClient("mongodb://localhost:27017/")
			print("Connected to DB.")
			self.db = clint.project

		except pymongo.errors.ConnectionFailure as e:
			
			print("CANNOT CONNECT TO DB ... Something is wrong Cou")
			die()
	# insert One Record
	def insertOne(self,data,coll):
		col = self.db[coll]
		try:
			i_id = col.insert_one(data).inserted_id
			return True

		except Exception as e:
			print("Cannot insert into the Database")
			return False
	
	# insert many record
	def insert(self,coll,data):
		col = self.db[coll]
		try:
			col.insert(data)
			return True
		except Exception as e:
			print('Error occuted in insert function')
			print(e)
			return False


	# Search By ID
	def findone(self,coll,key,val):
		try:
			col = self.db[coll]
			data = col.find_one({key:val},{"is_deleted":False})
			if data is None :
				data = {"error" : 1}
			return data
		except Exception as e:
				print("Error Occuted at Search function")
				# print(e)
				exit()
	def find(self,coll,key,val):
		try:
			col = self.db[coll]
			data = col.find({key:val},{"is_deleted":False})
			if data is None:
				data = [{"error":1}]
			return data
		except Exception as e:
			raise e
	def delete(self,coll):
		try:
			col = self.db[coll]
			col.update_many({},{"$set":{"is_deleted":True}})
			print("delete")
			return True
		except Exception as e:
			print(e)
			return False
	def hardDrop(self,coll):
		try:
			col = self.db[coll]
			# col.
		except Exception as e:
			# raise e