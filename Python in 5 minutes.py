# hello python

# if statements
x = 11
if (x > 10):
    print ('Hello in If')
else:
    print ('Hello in Else')
# Arrays
a = [1,2,3,'(',5]
for items in a:
    print (items)

# Maps  aka dictionaries

hm = {} # initialize

# add item into dictionary
hm['name'] = 'brain'
hm['state'] = 'florida'
hm['age'] = 37

for k,v in hm.items():
    print(k, '->', v)

# Functions
def my_fun():
    print ("Hello I m in Function :)")

# return mutlitple values in functions
def square(n1, n2): # return as pair
    return n1**2, n2**2

my_fun()
print (square(10,50))
print (square(1,5)) 