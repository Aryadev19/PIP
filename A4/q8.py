address = 'B-6, Lodhi road, Delhi'
list1 = [1, 2, 3]
list2 = ['a', 1, 'z', 26, 'd', 4]
tuple1 = ('a', 'e', 'i', 'o', 'u') 
tuple2 = ([2,4,6,8], [3,6,9], [4,8], 5) 
dict1 = {'apple': 'red', 'mango': 'yellow', 'orange': 'orange'}
dict2 = {
        'X': ['eng', 'hindi', 'maths','science'],
        'XII': ['english', 'physics','chemistry', 'maths']
        }

# list1[3] = 4 #output--> index out of range error

# print(list1 * 2) #output--> [1, 2, 3, 1, 2, 3]

# print(min(list2)) #output--> type error both int and str is present

# print(max(list1)) #output--> 3

# print(list(address)) #output--> ['B', '-', '6', ',', ' ', 'L', 'o', 'd', 'h', 'i', ' ', 'r', 'o', 'a', 'd', ',', ' ', 'D', 'e', 'l', 'h', 'i']


# list2.extend(['e', 5])
# print(list2) #output--> ['a', 1, 'z', 26, 'd', 4, 'e', 5]

# list2.append(['e', 5])
# print(list2) #output--> ['a', 1, 'z', 26, 'd', 4, ['e', 5]]

# names = ['rohan', 'mohan', 'gita']
# names.sort(key= len)
# print(names) #output--> ['gita', 'rohan', 'mohan']

# list3 = [(x * 2) for x in range(1, 11)]
# print(list3) #ouput--> [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# del list3[1:]
# print(list3) #output--> [2] (to get this output uncomment list3 from above)

# list4 = [ x+y for x in range(1,5) for y in range(1,5)]
# print(list4) #output--> [2, 3, 4, 5, 3, 4, 5, 6, 4, 5, 6, 7, 5, 6, 7, 8]

# tuple2[3] = 6 #output--> tuple does not support item assignment

# tuple2.append(5) #output--> no append method in tuple

# t1 = tuple2 +(5) #output--> cannot add int to tuple 

# ','.join(tuple1) #output--> ('a', 'e', 'i', 'o', 'u')

# print(list(zip(['apple', 'orange'], ('red','orange')))) #output--> [('apple', 'red'), ('orange', 'orange')]

# print(dict2['XII']) #output--> ['english', 'physics', 'chemistry', 'maths']

# dict2['XII'].append('computer science'),dict2 #output--> 'X': ['eng', 'hindi', 'maths', 'science'], 'XII': ['english', 'physics', 'chemistry', 'maths', 'computer science']

# print('red' in dict1) #output--> False

# print(list(dict1.items())) #output--> [('apple', 'red'), ('mango', 'yellow'), ('orange', 'orange')]

# print(list(dict2.keys())) #output--> ['X', 'XII']

# print(dict2.get('XI', 'None')) #output--> None

# dict1.update({'kiwi':'green'})
# print(dict1) #output--> {'apple': 'red', 'mango': 'yellow', 'orange': 'orange', 'kiwi': 'green'}