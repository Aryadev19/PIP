greeting = 'Good Morning. Have a Good Day!!'

print(greeting.count('Good')) # output --> 2

print(greeting.find('a')) # output --> 15

print(greeting.rfind('a')) # output --> 27

print(greeting.capitalize()) # output --> good morning. have a good day!!

print(greeting.lower()) # output --> GOOD MORNING. HAVE A GOOD DAY!!

print(greeting.upper()) # output --> gOOD mORNING. hAVE A gOOD dAY!!

print(greeting.swapcase()) # output --> False

print(greeting.istitle()) # output --> Sweet Morning. Have a Sweet Day!!

print(greeting.replace('Good', 'Sweet')) # output --> Good Morning. Have a Good Day!!

print(greeting.strip()) # output --> ['Good', 'Morning.', 'Have', 'a', 'Good', 'Day!!']

print(greeting.split()) # output --> ('Good Morning', '.', ' Have a Good Day!!')

print(greeting.partition('.')) # output --> False

print(greeting.startswith('good')) # output --> True

print(greeting.endswith('!!')) # output --> studen

