nums = [1,2,3,4,5]

for num in nums:
    print(num)

for num in nums:
    if num ==3:
        print('found!')
        break #stop at this interation and only print out the number before 3
    print(num)

for num in nums:
    if num ==3:
        print('found!')
        continue # found and continue iterating.
    print(num)

#combination of numbs and abc
for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(10):
    print(i)

x = 0

while x<10:
    if x ==5:
        break
    print(x)
    x+=1
