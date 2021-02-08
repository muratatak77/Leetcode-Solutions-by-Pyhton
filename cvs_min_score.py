def merge_cvs(list1, list2):

	if not list1 and not list2:
		return []

	merge_list = []

	for l1 in list1:
		obj = {}
		user_id = l1['user_id']
		age = l1['age']
		min_score_1 = l1['min_score']

		obj['user_id'] = user_id
		obj['age'] = age
		obj['min_score'] = min_score_1

		for l2 in list2:

			if l2['user_id'] == user_id:
				obj['state'] = l2['state']
				min_score_2 = l2['min_score']
				if min_score_2 < min_score_1:
					obj['min_score'] = min_score_2
				break

		merge_list.append(obj)


	if merge_list is None or len(merge_list) == 0:
		return ""

	print('user_id','age','state','min_score')
	for item in merge_list:
		print(item['user_id'],item['age'],item['state'], item['min_score'])


list1 = [
{'user_id': 1, 'age': 23, 'min_score': 6},
{'user_id': 6, 'age': 54, 'min_score': 300},
{'user_id': 2, 'age': 39, 'min_score': 40}
]



list2 = [
{'user_id': 1, 'state': "CA", 'min_score': 12},
{'user_id': 6, 'state': "AK", 'min_score': 44},
{'user_id': 2, 'state': "WA", 'min_score': 100}
]


merge_cvs(list1, list2)
