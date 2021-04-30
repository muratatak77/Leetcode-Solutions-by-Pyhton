# Name Matching # # At Checkr, one of the most important  aspects of our work is accurately matching records # to candidates. 
# One of the ways that we do this is by comparing the name on a given record # to a list of known aliases for the candidate. 
# In this exercise, we will implement a # `name_match` method that accepts the list of known aliases as well as the name returned # on a record.
#  It should return True if the name matches any of the aliases and False otherwise. 

 # # The name_match method will be required to pass the following tests: 


 # # 1. Exact match 
 # known_aliases = ['Alphonse Gabriel Capone', 'Al Capone'] 
 # name_match(known_aliases, 'Alphonse Gabriel Capone') => True 
 # name_match(known_aliases, 'Al Capone') => True 
 # name_match(known_aliases, 'Alphonse Francis Capone') => False 



 # # # 2. Middle name missing (on alias) 
 # # known_aliases = ['Alphonse Capone'] # 
 # name_match(known_aliases, 'Alphonse Gabriel Capone') => True 
 # name_match(known_aliases, 'Alphonse Francis Capone') => True 
 # name_match(known_aliases, 'Alexander Capone') => False 
 # 
 # if len(alias_split) == 2 and len(name_splits) == 3
 # 		
 # 		if alias_split[0] == name_splits[0] and alias_split[1] == name_splits[2]
 # 			return True
 # 		
 # if len(alias_split) == 2 and len(name_splits) == 2
 # 
 # 
 # if len(alias_split) == 3 and len(name_splits) == 3
 #		

 # if len(alias_split) == 3 and len(name_splits) == 2
 # 
 #  	if alias_split[0] == name_splits[0] and alias_split[2] == name_splits[1]
 # 			return True
 # 

 # # # 3. Middle name missing (on record name) 
 # # known_aliases = ['Alphonse Gabriel Capone'] 
 # name_match(known_aliases, 'Alphonse Capone') => True 
 # name_match(known_aliases, 'Alphonse Francis Capone') => False 
 # name_match(known_aliases, 'Alexander Capone') => False 


 # # # 4. More middle name tests # These serve as a sanity check of your implementation of cases 2 and 3 
 # # known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone'] 
 # name_match(known_aliases, 'Alphonse Gabriel Capone') => True 
 # name_match(known_aliases, 'Alphonse Francis Capone') => True 
 # name_match(known_aliases, 'Alphonse Edward Capone') => False 


 # # # 5. Middle initial matches middle name # # known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone'] 
 # name_match(known_aliases, 'Alphonse G Capone') => True 
 # name_match(known_aliases, 'Alphonse Francis Capone') => True 
 # name_match(known_aliases, 'Alphonse E Capone') => False 
 # name_match(known_aliases, 'Alphonse Edward Capone') => False 
 # name_match(known_aliases, 'Alphonse Gregory Capone') => False 


 # # # Bonus: Transposition # # Transposition (swapping) of the first name and middle name is relatively common. 
 # In order to accurately match the name returned from a record we should take this 
 # into account. # # All of the test cases implemented previously also apply to the transposed name. 

 # # # 6. First name and middle name can be transposed # # 'Gabriel Alphonse Capone' is a valid transposition of 'Alphonse Gabriel Capone' 
 # # known_aliases = ['Alphonse Gabriel Capone'] 
 # name_match(known_aliases, 'Gabriel Alphonse Capone') => True 
 # name_match(known_aliases, 'Gabriel A Capone') => True 
 # name_match(known_aliases, 'Gabriel Capone') => True 
 # name_match(known_aliases, 'Gabriel Francis Capone') => False

  # # # 7. Last name cannot be transposed 
  # # 'Alphonse Capone Gabriel' is NOT a valid transposition of 'Alphonse Gabriel Capone' # 'Capone Alphonse Gabriel' is NOT a valid transposition of 'Alphonse Gabriel Capone' 

  # # known_aliases = ['Alphonse Gabriel Capone'] 
  # name_match(known_aliases, 'Alphonse Capone Gabriel') => False 
  # name_match(known_aliases, 'Capone Alphonse Gabriel') => False 
  # name_match(known_aliases, 'Capone Gabriel') => False

def function():
	pass


def name_match(known_aliases, name):
	#edge cases
	if not known_aliases:
		return False
	if not name:
		return False

	#eaxt match 
	if name in known_aliases:
		return True


	for alias in known_aliases:
		alias_splits = alias.split(" ")
		name_splits = name.split(" ")

		# print("alias_splits : ", alias_splits)
		# print("name_splits : ", name_splits)

		#last name matching
		if alias_splits[-1] != name_splits[-1]:
			return False

		#middle name check
		if len(alias_splits) == 2 and len(name_splits) == 3:
			if alias_splits[0] == name_splits[0] and alias_splits[1] == name_splits[2]:
				return True

		# elif len(alias_splits) == 2 and len(name_splits) == 2:
			# pass

		# elif len(alias_splits) == 3 and len(name_splits) == 3:
			# if alias_splits == name_splits:
				# return True
		# ['Alphonse Gabriel Capone'] 
		# 'Alphonse Capone'
		# 
		# 
		# 
			# known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone'] 
			# name_match(known_aliases, 'Alphonse G Capone') => True 
			 # name_match(known_aliases, 'Alphonse Francis Capone') => True 
			 # name_match(known_aliases, 'Alphonse E Capone') => False 
			 # name_match(known_aliases, 'Alphonse Edward Capone') => False 
			 # name_match(known_aliases, 'Alphonse Gregory Capone') => False 
			 # 
		elif len(alias_splits) == 3 and len(name_splits) == 3:
			
			if len(name_splits[1]) == 1:
				if name_splits[1] == alias_splits[1][0]:
					return True

			if len(alias_splits[1]) == 1:
				if alias_splits[1] == name_splits[1][0]:
					return True

		elif len(alias_splits) == 3 and len(name_splits) == 2:
			if alias_splits[0] == name_splits[0] and alias_splits[2] == name_splits[1]:
				return True



	return False


# known_aliases = ['Alphonse Gabriel Capone', 'Al Capone'] 
# name_match(known_aliases, 'Al Capone') => True 
# we need just true cases and first names




# known_aliases = ['Alphonse Capone'] # 
# name_match(known_aliases, 'Alphonse Gabriel Capone') => True 
# name_match(known_aliases, 'Alphonse Francis Capone') => True 
# we need just true cases and first names



# known_aliases = ['Alphonse Gabriel Capone'] 
# name_match(known_aliases, 'Alphonse Capone') => True
# name_match(known_aliases, 'Gabriel Capone') => True 
# we need just true cases and first and middle names



# known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone'] 
# name_match(known_aliases, 'Alphonse G Capone') => True 
# name_match(known_aliases, 'Alphonse Francis Capone') => True 

# known_aliases = ['Alphonse Gabriel Capone'] 
# name_match(known_aliases, 'Gabriel Alphonse Capone') => True 
# name_match(known_aliases, 'Gabriel A Capone') => True 
# we need just alias first -  middle name , middle name of record name 

import unittest

class TestNameCheckMethods(unittest.TestCase):

	def test_case_1(self): 

		# # 1. Exact match 
		# known_aliases = ['Alphonse Gabriel Capone', 'Al Capone'] 
		# name_match(known_aliases, 'Alphonse Gabriel Capone') => True 
		# name_match(known_aliases, 'Al Capone') => True 
		# name_match(known_aliases, 'Alphonse Francis Capone') => False 
		print("start test_exact_match")
		known_aliases = ['Alphonse Gabriel Capone', 'Al Capone']
		self.assertTrue(name_match(known_aliases, 'Alphonse Gabriel Capone'))
		self.assertTrue(name_match(known_aliases, 'Al Capone'))
		self.assertFalse(name_match(known_aliases, 'Alphonse Francis Capone'))
		

	def test_case_2(self): 

		 # # # 2. Middle name missing (on alias) 
		 # # known_aliases = ['Alphonse Capone'] # 
		 # name_match(known_aliases, 'Alphonse Gabriel Capone') => True 
		 # name_match(known_aliases, 'Alphonse Francis Capone') => True 
		 # name_match(known_aliases, 'Alexander Capone') => False 
		print("start test_middle_name_missing")
		known_aliases = ['Alphonse Capone']
		self.assertTrue(name_match(known_aliases, 'Alphonse Gabriel Capone'))
		self.assertTrue(name_match(known_aliases, 'Alphonse Francis Capone'))
		self.assertFalse(name_match(known_aliases, 'Alexander Capone'))
		

	def test_case_3(self):

		 # # # 3. Middle name missing (on record name) 
		 # # known_aliases = ['Alphonse Gabriel Capone'] 
		 # name_match(known_aliases, 'Alphonse Capone') => True 
		 # name_match(known_aliases, 'Alphonse Francis Capone') => False 
		 # name_match(known_aliases, 'Alexander Capone') => False 
		print("start test_middle_name_missing")
		known_aliases = ['Alphonse Gabriel Capone'] 
		self.assertTrue(name_match(known_aliases, 'Alphonse Capone'))
		self.assertFalse(name_match(known_aliases, 'Alphonse Francis Capone') )
		self.assertFalse(name_match(known_aliases, 'Alexander Capone'))


	def test_case_4(self):
		 # # # 4. More middle name tests # These serve as a sanity check of your implementation of cases 2 and 3 
		 # # known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone'] 
		 # name_match(known_aliases, 'Alphonse Gabriel Capone') => True 
		 # name_match(known_aliases, 'Alphonse Francis Capone') => True 
		 # name_match(known_aliases, 'Alphonse Edward Capone') => False 
		known_aliases =['Alphonse Gabriel Capone', 'Alphonse Francis Capone'] 
		self.assertTrue(name_match(known_aliases, 'Alphonse Gabriel Capone'))
		self.assertTrue(name_match(known_aliases, 'Alphonse Francis Capone'))
		self.assertFalse(name_match(known_aliases, 'Alphonse Edward Capone'))

	def test_case_5(self):
		 # name_match(known_aliases, 'Alphonse G Capone') => True 
		 # name_match(known_aliases, 'Alphonse Francis Capone') => True 
		 # name_match(known_aliases, 'Alphonse E Capone') => False 
		 # name_match(known_aliases, 'Alphonse Edward Capone') => False 
		 # name_match(known_aliases, 'Alphonse Gregory Capone') => False 
		known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone'] 
		self.assertTrue(name_match(known_aliases, 'Alphonse G Capone'))
		self.assertTrue(name_match(known_aliases, 'Alphonse Francis Capone'))
		self.assertFalse(name_match(known_aliases, 'Alphonse E Capone'))
		self.assertFalse(name_match(known_aliases, 'Alphonse E Capone'))
		self.assertFalse(name_match(known_aliases, 'Alphonse Gregory Capone'))

unittest.main()  

# known_aliases = ['Alphonse Gabriel Capone', 'Al Capone'] 
# res1 = name_match(known_aliases, 'Al Capone')
# print("res1 :", res1)


# known_aliases = ['Alphonse Capone']
# res2= name_match(known_aliases, 'Alphonse Gabriel Capone')

# print("res2 :", res2)




# # # # 2. Middle name missing (on alias) 
# known_aliases = ['Alphonse Capone'] # 
# name_match(known_aliases, 'Alphonse Gabriel Capone') #=> True 
# name_match(known_aliases, 'Alphonse Francis Capone') #=> True 
# name_match(known_aliases, 'Alexander Capone') #=> False 




 
 

