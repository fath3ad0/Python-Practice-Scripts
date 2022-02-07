'''
 ref: https://realpython.com/python-lambda/

 Lambda Expressions aka Anonymous Functions
  - structure -> <lambda key word> <arg>: <body>


Function Definitions Examples:  
 Regular Function (Imperative Style):
 	- def identify(x): 
 		 return x+1

 Lambda Style (Functional):  	
 	- lamba x: x+1
 	- add_one = lambda x: x+1


Invoking
 Passing Arguments using parenthesis
 	- Pass the value of 2 to x 
 		- (lambda x: x + 1)(2) => 3
 
 Passing Argument using function names
 	- Pass the lambda expression into a varable name
 		- (add_one = lambda x:x+1) -> add_one(2) => 3 

 Multiple arguments separated by comma:
 	- full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
 	- full_name('guido', 'van rossum')

'''

# One Example: 
sayHello = lambda x1,x2: print('{0} {1}!!'.format(x1,x2))
sayHello('Hello', 'World')

# Regular For Loop 
for x in range(2):
	for y in range(2):
		(lambda v1,v2: print('({0},{1})'.format(v1,v2)))(x,y)


# List comprehension
testfunc = lambda v1,v2: print('({0},{1})'.format(v1,v2))

# Nested list compression - testfunc takes the values of x and y and applies function logic
[[testfunc(x,y) for y in range(2)] for x in range(2)]