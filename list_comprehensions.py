fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    if f.startswith('p'):
        expr = f.upper()
        f0.append(expr)
print(f"{f0 = }\n")

#    [ expr for  var in iterable if condition]
f1 = [f.upper() for f in fruits if f.startswith('p')]  
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits]
print(f"{f2 = }\n")

f3 = [f for f in fruits if f.startswith('p')]  
print(f"{f3 = }\n")

nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

n1 = [x * 1000.0 for x in nums]
print(f"{n1 = }\n")

num_strs = [str(x) for x in nums]
print(f"{num_strs = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [p[-1] for p in people]  # returns list
print(f"{dobs = }\n")

dobs_gen = (p[-1] for p in people)  # returns generator
print(f"{dobs_gen = }")
for dob in dobs_gen:
    print(dob)

