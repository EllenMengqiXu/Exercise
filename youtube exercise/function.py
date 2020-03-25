def test():
    pass #we don't want anything for now maybe come back later, but the func won't throw any erro.

def hello_func():
    print('hello function.')

hello_func()

def hello_func():
    return 'hello function.'

print(hello_func())
print(hello_func().upper())

def greet(greeting):
    return '{} Function'.format(greeting)

print(greet('hi'))

def maturality(age):
    if age <30:
        return '{} years old is young man.'.format(age)
    else:
        return '{} years old is old man.'.format(age)
print(maturality(29))

def greet(greeting, name='you'): #default as you
    return '{}, {}'.format(greeting, name)

print(greet('hi', 'John'))



def student_info(*args, **kwargs): #posational arguments and keyword arguments
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name':'John', 'age':22}
student_info(courses, info) # --> nothing
student_info(*courses, **info)

#example

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 ==0 and (year % 100 != 0 or year % 400 ==0)
def days_in_month(year, month):
    if not 1<=month<=12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2017, 6))
