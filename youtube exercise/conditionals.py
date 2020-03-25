language = 'java'

if language == 'python':
    print('language is python')
elif language == 'java':
    print('language is java')
elif language == 'javascript':
    print('language is js')
else:
    print('no match')

user = 'Admin'
logged_in = False

if user =='Admin' and logged_in:
    print('admin page')
else:
    print('bad credentials')

if user =='Admin' or logged_in:
    print('either or')
else:
    print('bad credentials')

if not logged_in:
    print('please log in')
else:
    print('welcome')

a =[1,2,3]
b=[1,2,3]

print(a == b)
print(id(a))
print(id(b))
print(a is b) #-->False, because ID of a and b in memory are different.

condition = {}

if condition:
    print('evaluated to True')
else:
    print('evaluated to False')
#False Values: -- the below shows python will evaluate as false.
# False
# None
# 0
# any empty sequence. for example, ''str, []list, ()tupe. but [None] --> True :)
# any emply mapping. for example {}dictionary
