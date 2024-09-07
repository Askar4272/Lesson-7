my_dict = {'Askar':19.05, 'Janat':10.04,'Anna':21.07,'Sasha':12.05}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Askar'])
print('Not existing value: ', my_dict.get('Dima'))
my_dict.update({'Alex': 17.10,'Foma':13.01})
a = my_dict.pop('Askar')
print('Deleted value: ', a)
print('Modified dictionary: ', my_dict)
print()
my_set = {1, 2, 3, 'яблоко','яблоко',2,1}
print('Set: ', my_set)
(my_set.add(80))
print('Modified set: ', my_set)