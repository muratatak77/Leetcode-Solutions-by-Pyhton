'''
​### Implement strStr()

​
Return the index of the first occurrence of needle in haystack, or `-1` if `needle` is not part of `haystack`.
​
**Clarification:**

For the purpose of this problem, we will return 0 when `needle` is an empty string.

**Example 1:**
​
```
Input: haystack = "hello", needle = "ll"
Output: 2
​
```
​
**Example 2:**
​
```
Input: haystack = "aaaaa", needle = "bba"
Output: -1
​
```
​
**Example 3:**
​
```
Input: haystack = "", needle = ""
Output: 0
​
```
# Input: haystack = "hello", needle = "ll"
i,j = 0,0 ,  "h"
i,j = 0,1 ,  "he" I will match is needle . we can return i

i,j = 0,2 ,  'hel' 
		1,2 , 'el' : 
		1,3 , 'ell'
		2,3 , 'll'
		


# edge cases

if not haystack:
	return 0

if len(haystack) == 0:
	return 0

for i in range(len(haystack)):
	for j in range(i, len(haystack)):
		if len(needle) < len(j-i)+1:
			i+=1
		if s[i..j] == needle:
			return i
			
			
 ### Valid Palindrome
 
 
 Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters.
 
 
 ```
 s: noon
 
 return True
 
 ```
 
 ```
 
 s: hello
 
 return False
 ```
 
 
 ```
 
 s: ''
 
 return True
 ```
 
 ```
 
 s: 'h'
 
 return True
 ```
 # n o o n 
 # middle = len(s) // 2
 # middle = 2 
 # start = middle - 1 > 1 > -1 > 0
 # end = middle > 2 > 3 
 
'''


def isValid(s):
	 
	#edge cases
	if s is None:
		return False
		 
	if not s:
		return True
		
	if len(s) == 1:
		return True
		 
	#4 // 2 = 2
	middle = len(s) // 2

	start = middle - 1  #1
	end = middle #2

	while start > -1 and end < len(s):
		print("start : ", s[start])
		print("end : ", s[end])

		if s[start] != s[end]:
			return False
			 
		start -= 1 #0
		end += 1 #3
	
	return True

s = 'noon'
res = isValid(s)
print("res : ", res)


	