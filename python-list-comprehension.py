
'''
ref : https://www.geeksforgeeks.org/python-list-comprehension/
 
 List Comprehension 
  - single line
  - creating new lists from other iterables like tuples, strings, arrays, lists, etc
  - consist of brackets containing the expression -> executed for each element -> using for loop to iterate over each item.
  
  Syntax 
  - newList = [ expression(element) for element in oldList if condition ] 
'''

# Regular For Loop
def forLoop():
	List=[] 
	
	for i in "This is a for loop":
		List.append(i)
	print('For Loop: {0}'.format(List))

# List Comprehension 
def listComp():
	List=[]	

	List=[i for i in 'This is list comprehension!']
	print('ListComp: {0}'.format(List))

def nestedForLoop():
	List=[]	

	for i in range(3):
		# Creates 3 empty lists
		List.append([])

		# Creates 5 elements in each empty list
		for j in range(5):
			List[i].append(j)

		# [[0,1,2,3,4],[0,1,2,3,4],[0,1,2,3,4]]
	print('nestedForLoop: {0}'.format(List))

def nestedListComp():
	List=[]	

	# the leftmost expression is passed into the loop to the left
	#       [nested loop (left)]  first for loop
	List = [[j for j in range(5)] for i in range(3)] 
	print('nestedListComp: {0}'.format(List))




forLoop()
listComp()
nestedForLoop()
nestedListComp()