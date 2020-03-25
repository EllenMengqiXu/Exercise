courses = ['History', 'Math', 'Physics', 'ComSci']
print(len(courses))

print(courses[3])
print(courses[-1]) #last item, negative is more convenient.

print(courses[2:])

courses.append('Art') #add new item at last
print(courses)
courses.insert(1,'Art') #insert new item by defining it's position
print(courses)

courses = ['History', 'Math', 'Physics', 'ComSci']
courses2 = ['Music', 'Education']
courses.insert(0, courses2)
print(courses[0]) #this print whole courses2, not what we want

courses = ['History', 'Math', 'Physics', 'ComSci']
courses.extend(courses2) #add new item from another list at last
print(courses)

courses = ['History', 'Math', 'Physics', 'ComSci']
courses.remove('Math')
print(courses)

courses = ['History', 'Math', 'Physics', 'ComSci']
popped = courses.pop() #remove the last item
print(popped)

courses = ['History', 'Math', 'Physics', 'ComSci']
courses.reverse()
print(courses)


nums = [1,5,4,3]
courses.sort(reverse=True) #sort descending from Z to A
nums.sort(reverse =True) #sort descending
print(courses)
print(nums)

courses = ['History', 'Math', 'Physics', 'ComSci']
nums = [1,5,4,3]
sorted_crs = sorted(courses)
print(sorted_crs)

print(min(nums))
print(max(nums))
print(sum(nums))

courses = ['History', 'Math', 'Physics', 'ComSci']
print(courses.index('ComSci'))
print('Math' in courses)

list_rp = ['USA_ABM Named Accounts - Leads', 'USA_ABM Prioritized Accounts - Display', 'USA_Select Leads','EMEA_ABM Named Accounts - Leads', 'USA_Audience Targeting','USA_ABM Trending Accounts - Display','USA_ABM Prioritized Accounts - Leads', 'USA_HQL- ABM','EMEA_HQL- ABM', 'USA_ABM Trending Accounts - Leads','USA_ABM Direct - Lead Gen', 'USA_ABM Named Accounts - Display','APAC_ABM Named Accounts - Leads','USA_ABM Install Base Named Accounts - Leads','EMEA_Category Leads', 'APAC_HQL- ABM','EMEA_ABM Prioritized Accounts - Leads','EMEA_ABM Prioritized Accounts - Display','APAC_ABM Named Accounts - Display', 'USA_HQL- Non-ABM','EMEA_Select Leads', 'USA_ABM Direct - Display','EMEA_ABM Trending Accounts - Display', 'APAC_Select Leads','EMEA_ABM Trending Accounts - Leads','EMEA_ABM Named Accounts - Display','APAC_ABM Prioritized Accounts - Leads','APAC_ABM Trending Accounts - Leads','EMEA_ABM Install Base Named Accounts - Branding','EMEA_Audience Targeting','USA_ABM Install Base Named Accounts - Branding','EMEA_HQL- Non-ABM', 'APAC_Confirmed Call Back (HQL)','EMEA_ABM Install Base Named Accounts - Leads','APAC_ABM Trending Accounts - Display','APAC_ABM Prioritized Accounts - Display']

print(type(list_rp))
list_str = ', '.join(list_rp)

print(type(list_str))

for index,RP_name in enumerate(list_rp,start =1):
    print(index,RP_name)

    #enumerate gave us the power to i ndex and we can define which number to start.

courses = ['History', 'Math', 'Physics', 'ComSci']
courses_str = ', '.join(courses)
print(courses_str)

newlist = list_str.split(', ')
print(newlist)

#tuple are not mutable -- not changeable

tuple1  = ('History', 'Math', 'Physics', 'ComSci' , 'Math')
print(tuple1)

set1 = {'History', 'Math', 'Physics', 'ComSci'}
set2 = {'History', 'Music', 'Arts', 'ComSci'}
print(set1)
print(set2)
#print('Math' in set1)
#common element
print(set1.intersection(set2))
#in set 1 but not in set 2
print(set1.difference(set2))
#for both sets
print(set1.union(set2))

#slicing

my_list = ['a','b','c','d','e','f','g']
          # 0,  1,  2,  3,  4,  5,  6
          # -7, -6, -5,  -4, -3, -2, -1
#list[start:end:step]

print(my_list[1:-1]) #negative label is more convenient so you don't need to count how many item you list has.
print(my_list[1:-1:2])

print(my_list[::-1]) #reverse the list
print(my_list[-1:1:-2])

#string example

sample_url = 'https://www.youtube.com/'
print(sample_url)

#reverse url
print(sample_url[::-1])

#get the top level doain
print(sample_url[-4:-1])
#get url without http://
print(sample_url[12:-1])
#print url without http:// and top domain
print(sample_url[12:-5])


