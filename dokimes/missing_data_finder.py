import pandas as pd
from x_set_creator import sensor_data
from y_set_creator_dmg_percentage import new_damage_data


print(len(new_damage_data))
print(len(sensor_data))

'''

data = pd.concat([sensor_data, new_damage_data]).drop_duplicates(keep=False)

print('o arithmos twn hello einai posa data leipoun')
for data in sensor_data['sensor_index_number']:
    if data not in new_damage_data['damage_index_number']:
        print("hello")

print('o arithmos twn hello einai posa data leipoun')
for data in new_damage_data['damage_index_number']:
    if data not in sensor_data['sensor_index_number']:
        print("hello")


'''


#for i in range(0,len(new_damage_data)):
#    if new_damage_data['damage_index_number'][i] not in sensor_data['sensor_index_number']:
#        print('hello')

#print(new_damage_data)

#if new_damage_data['damage_index_number'] not in sensor_data['sensor_index_number']:
#    print('he')
# to programma checkarei poia indeces einai koina kai stis duo listes
# an kapoio den einai koino to afairei
#meta kanei to sensor_data apo lista csv se lista me timeseries
#for i in range(0,len(new_damage_data)):
#    if new_damage_data['damage_index_number'][i] !=sensor_data['']

