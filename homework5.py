immutable_var=(3,5,7,'home',True)
print(immutable_var)
#кортеж – это неизменяемая упорядоченная коллекция
mutable_list=[1,2,'home','love']
mutable_list[1]=3
print(mutable_list)
mutable_list.append('life')
print(mutable_list)
mutable_list.remove('home')
print(mutable_list)
