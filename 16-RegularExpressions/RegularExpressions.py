## Regular Expressions are to find chain of characters in a string!
import re

stri = 'Take up one idea. odd idea at a time'

searchresult = re.search(r'o\w\w', stri)   # search for pattern o + any alphanumeric character 0-9-A-Z + any alphanumeric character 0-9-A-Z  in the striing
print('Search o\w\w does:',searchresult.group())


searchresult = re.findall(r'o\w\w', stri)  ## finds all the striings with that pattern
print(searchresult)  ## group not needed

searchresult = re.match(r'T\w\w', stri)  ## match only searches at the end of the striing
print('Match T\w does: ',searchresult.group())


# split striing between some characters
stri = 'Take 1 up one 23 idea. odd idea 45 at a time'

rs = re.split(r'\d+', stri)   ## split the striing in between numbers   the + means more than one number d
print(rs)


# replace
stri = 'Take up one idea. odd idea at a time'

replace = re.sub(r'idea','hat',stri)
print('Sub does:',replace)


# Quantifiers
stri = 'Take up One idea. Only One idea at a time. nO Ordinary socks.'

searchresult = re.findall(r'O\w\w', stri)  ## finds all the repetitions of that pattern O + 2 characters.
print('Findall O\w does: ',searchresult)  ## group not needed

searchresult = re.findall(r'O\w+', stri)  ## finds all the repetitions of O + 1 or more characters before space. Hence why the O from nO is omitted.
print('Findall O\w+ does: ',searchresult)  ## group not needed

searchresult = re.findall(r'O\w*', stri)  ## finds all the repetitions of O + 0 or more characters before a space. Hence why the O from nO is included.
print('Findall O\w* does: ',searchresult)  ## group not needed

searchresult = re.findall(r'O\w?', stri)  ## finds all the repetitions of O + 0 or 1 repetition after O.
print('Findall O\w* does: ',searchresult)  ## group not needed

searchresult = re.findall(r'O\w{3}', stri)  ## finds all the repetitions of O + 3 non-space character.
print('Findall O\w* does: ',searchresult)  ## group not needed

searchresult = re.findall(r'O\w{0,3}', stri)  ## finds all the repetitions of O + 0 to 3 non-space character.
print('Findall O\w* does: ',searchresult)  ## group not needed

# reminder: w is for 0-9-A-Z, d is for 0-9

# Dates
stri = '23-02-218 Take up One idea. 22-1-2019. Only 1-2-18 One idea at a time 23-02-2180. 1-15-2019 nO Ordinary socks.'

findresult = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', stri)  # finds numbers
print('Findall \d{1,2}\d{1,2}\d{4} does: ', findresult)


# Special characters
stri = 'Take up One idea. \u00a35001 \'Only One idea at a time. \u00a3500 nO Ordinary socks.'

searchresult = re.search(r'\'\w\w', stri)   # add \ to search for a special character
print('Search \'\w\w does:',searchresult.group())

searchresult = re.search(r'\u00a3\w', stri)   # add \ to search for a special character
print('Search \u00a3\w does:',searchresult.group())

searchresult = re.search(r'\u00a3\w*', stri)   # add \ to search for a special character
print('Search \u00a3\w* does:',searchresult.group())

findresult = re.findall(r'\u00a3\w*', stri)   # add \ to search for a special character
print('Findall \u00a3\w* does:',findresult)

searchresult = re.search(r'^T\w\w', stri)   # ^ is to search from the beggining of the string
print('Search ^T\w\w does:',searchresult.group())



