' list of countries: '
country_lst= ['spain', 'catalunya', 'uk', 'italy']
print(country_lst[2])

country_lst.append('france')
print(country_lst)

country_lst.remove(country_lst[1])
del(country_lst[1])
print(country_lst)

country_lst.insert(2,'germany')
print(country_lst)


' set of countries: '
country_set= {'spain', 'uk', 'italy'}
print(country_set)

country_set.update(['france'])
print(country_set)

country_set.remove('uk')
print(country_set)

country_set.update(['germany'])
print(country_set)