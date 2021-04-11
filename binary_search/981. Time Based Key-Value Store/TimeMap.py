from collections import defaultdict

class TimeMap:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.time_hash = defaultdict(list)
		

	def set(self, key: str, value: str, timestamp: int) -> None:
		self.time_hash[key].append((timestamp, value))
		print("			SET time_hash : ", self.time_hash)

	def get(self, key: str, timestamp: int) -> str:
		print("			GET key : ", key, " - timestamp : ", timestamp)

		if key not in self.time_hash:
			print("NO KEY return empty string....")
			return ""

		value_list = self.time_hash[key]
		print("			value_list : ", value_list)

		left = 0
		right = len(value_list) - 1

		#if last item less then the current time we can return directly val in the value_list
		if value_list[right][0] < timestamp:
			print("			Timestamp is grater then last item in the value_list. We can return last item value")
			return value_list[right][1]

		#if current times less then the first value in the time list , we can return empty string
		if timestamp < value_list[0][0]:
			print("			Timestamp is less then first item in the value_list. We can return empty string")
			return ""



		# if we have multiple items in the value_list, we need to search and return the one with the largest from the map
		# we can apply a binary search alg
		# 
		# 7
		# 1,2,3,6,8,9,10
		
		while left <= right:
			medium = left +(right-left)//2
			print("			MEDIUM item ", value_list[medium])
			#if we have match , we can return directly value
			if value_list[medium][0] == timestamp:
				print("			we can return directly ", timestamp ," from value_list : ", value_list[medium])
				return value_list[medium][1]
			#if we have value that it is between range , we can return this range
			if timestamp < value_list[medium][0] and timestamp > value_list[medium-1][0]:
				print("			we can return from range timestamp ", timestamp ," from value_list : ", value_list[medium])
				return value_list[medium-1][1]

			#if current timestamp less then medium value, we need to get back right position
			elif timestamp < value_list[medium][0]:
				right = medium - 1
				print("			we decremented right: ", right)
			#if timestamp grater than the medium value , we nee to move left pointer to the next item from medium 
			elif timestamp > value_list[medium][0]:
				left  = medium + 1
				print("			we incremented left : ", right)




# Your TimeMap object will be instantiated and called as such:

inputs_main = [  "set",          "get",    "get",    "set",           "get",    "get"]
inputs_values = [["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]

obj = TimeMap()

key = "foo"
value = "bar"
timestamp = 1
obj.set(key,value,timestamp)
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")

key = "foo"
timestamp = 1 
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")

key = "foo"
timestamp = 3
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")
key = "foo"
value = "bar2"
timestamp = 4
obj.set(key,value,timestamp)
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")


key = "foo"
value = "bar2"
timestamp = 5
obj.set(key,value,timestamp)
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")



key = "foo"
value = "bar2"
timestamp = 6
obj.set(key,value,timestamp)
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")

key = "foo"
timestamp = 67
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")

key = "foo"
timestamp = 0
get_value = obj.get(key,timestamp)
print("get_value : ", get_value)
print("===============================")
