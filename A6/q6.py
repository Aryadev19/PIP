address = 'B-6, Lodhi road, Delhi'

print(len(address)) # output --> 22

print(address[17:-1]) # output --> Delh

print(address[-len(address): len(address)]) # output -->B-6, Lodhi road, Delhi

print(address[:-12] + address[-12:]) # output --> B-6, Lodhi road, Delhi

print(address.find('delhi')) # output --> -1

print(address.swapcase()) # output --> b-6, lODHI ROAD, dELHI

print(address.split(',')) # output --> ['B-6', ' Lodhi road', ' Delhi']

print(address.isalpha()) # output --> False








