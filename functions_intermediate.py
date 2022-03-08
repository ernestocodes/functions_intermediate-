x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print (x)

students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

z[0]['y'] = 30
print (z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionaryA(some_list):
    for student in some_list:
        print (f"first_name - {student['first_name']}, last_name - {student['last_name']}")
iterateDictionaryA(students)

def iterateDictionaryB(some_list):
    for student in range(len(some_list)):
        for key, val in some_list[student].items():
            print(f"{key} - {val}")
iterateDictionaryB(students)

def iterateDictionary2(key_name, some_list):
    for student in some_list:
        print(student[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for x in some_dict:
        print(f"\n{len(some_dict[x])} {x.upper()}")
        for z in range(len(some_dict[x])):
            print (some_dict[x][z])
printInfo(dojo)
