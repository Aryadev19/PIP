vehicles = {'Bicycle', 'Scooter', 'Car', 'Bike', 'Truck', 'Bus', 'Rickshaw'}
heavyVehicles = {'Truck', 'Bus'}
lightVehicles = {'Rickshaw', 'Scooter', 'Bike', 'Bicycle'}

# lytVehicles = vehicles - heavyVehicles
# print(lytVehicles) #output--> {'Car', 'Scooter', 'Bicycle', 'Bike', 'Rickshaw'}

# hvyVehicles = vehicles - lightVehicles
# print(hvyVehicles) #output--> {'Truck', 'Bus', 'Car'}

# averageWeightVehicles = lightVehicles & heavyVehicles
# print(averageWeightVehicles) #output--> returns a empty set

# transport = lightVehicles | heavyVehicles
# print(transport) #output--> {'Bus', 'Bicycle', 'Truck', 'Rickshaw', 'Scooter', 'Bike'}

# transport.add('Car')
# print(transport) #output--> {'Truck', 'Car', 'Bus', 'Scooter', 'Bicycle', 'Rickshaw', 'Bike'}

# for i in vehicles:
#     print(i) #outupt-->Bicycle Scooter Bike Rickshaw Car Bus Truck

# print(len(vehicles)) #output--> 7

# print(min(vehicles)) #output--> Bicycle

# set.union(vehicles, lightVehicles, heavyVehicles)
# print(vehicles) #output--> {'Car', 'Bicycle', 'Truck', 'Rickshaw', 'Bike', 'Scooter', 'Bus'}
