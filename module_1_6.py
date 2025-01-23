my_dict = {"Вера": 1990,"Надежда": 1985,"Любовь": 2000}
print('Dict:',my_dict)
print('Existing value for "Вера": ',my_dict.get("Вера"))
print('Not existing value for "Ольга": ',my_dict.get("Ольга", 'Key not found'))
my_dict["Анна"] = 1995
my_dict["Ольга"] = 1980
removed_value = my_dict.pop("Надежда", 'Key not found')
print('Deleted value for "Надежда":', removed_value)
print('Modified dictionary: ',my_dict)
my_set = {1, 0.5, 'Python', 'True'}
print('Set:', my_set)
my_set.add((42,15,18))
my_set.add(False)
my_set.discard('True')
print('Modified set:', my_set)
