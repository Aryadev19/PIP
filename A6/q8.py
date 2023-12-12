import re

string1 = 'Python Programming Language'

match1 = re.search('......m?', string1)
print(match1.group()) #Output--> Python
match2 = re.search('......m{1,2}', string1)
print(match2.group()) #Output--> Programm
match3 = re.search('.*Language$', string1)
print(match3.group()) #Output--> Python Programming Language
match4 = re.search('\w*\s\w*', string1)
print(match4.group()) #Output--> Python Programming
match5 = re.search('.*', string1)
print(match5.group()) #Output--> Python Programming Language



string2 = 'Car Number DL5645'

match1 = re.search('\w\w?\d{1,4}', string2)
print(match1.group()) #Output--> DL5645
match2 = re.search('.*5', string2)
print(match2.group()) #Output--> Car Number DL5645
match3 = re.search('.*5?', string2)
print(match3.group()) #Output--> Car Number DL5645
match4 = re.search('\d{3}', string2)
print(match4.group()) #Output--> 564
match5 = re.search('^ C.*5$', string2)
print(match5.group()) #Output--> AttributeError: 'NoneType' object has no attribute 'group'



string3 = 'cdcccdcddd343344aabb'

match1 = re.search('(c|d)*\d*(a|b)*', string3)
print(match1.group()) #Output--> cdcccdcddd343344aabb
match2 = re.search('(cd)*d', string3)
print(match2.group()) #Output--> d
match3 = re.search('(cc|cd)*(3|4)*(aa|bb)', string3)
print(match3.group()) #Output--> 343344aa
match4 = re.search('(cc|cd|dd)*(3|4)*(aa|bb)', string3)
print(match4.group()) #Output--> cdcccdcddd343344aa
match5 = re.search('(cc|cd|dd)*(3|4)*(aa|bb)*', string3)
print(match5.group()) #Output--> cdcccdcddd343344aabb

