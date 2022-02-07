
'''
Binary Search -> recursive/iterative search
	- recursive -> slower -> allocating space/frames
	- iterative 


Steps: 
	1. Sort the array 
	2. establish the middle element 
	3. compare value with middle 
	4. if value is less than mid -> evaluate the first half of array until value is found. 
		-> else -> evaluate the second half



'''
# This function will keep calling itself (recursive) until the value of mid = the value we're looking for 

def binaryRecursiveSearch(arr, val):
		#Verify the array has values 
		if len(arr)>1: 

			# Sort array 
			vArr=sorted(arr)
			
			# Establish first and last value 
			first=vArr[0]
			last=len(vArr)-1 
			
			# Add and divide by 2 to obtain middle value. 
			#  // -> keeps the whole number component
			#     -> otherwise, float number may be returned
			mid=(first+last)//2

			#Checks if the middle value is the value we need. 
			if val == arr[mid]: 
				retVal=arr[mid]
				return retVal
			else:

				# if not check to see if the value is less than or greater than the middle value. 
				# return the function so that its called with the array truncated at the appropriate side. 
				if val < arr[mid]:
					return binarySearch(arr[:mid], val)
				else:
					return binarySearch(arr[mid:], val)
		else:
			return "Array is empty" 

#Example Array
arr=[2,3,5,10,11,12]
#Val 
x=10

result = binarySearch(arr, x )
print("Result: " , result)