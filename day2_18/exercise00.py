list_name = ["悟空", "八戒", "唐僧"]
list_age = [25, 23, 21]
dict_person = {list_name[i]:list_age[i] for i in range(len(list_name))}
print(dict_person)
combat = zip(list_name,list_age)
dict_combat = {dict(item) for item in combat}
print(dict_combat)
dict_person_plus = dict(zip(list_name,list_age))
print(dict_person_plus)