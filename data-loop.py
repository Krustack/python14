student=[
{"name": "Joseph","score":85}, #e={"name": "Joseph","score":85}
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for e in student:
    if e['score'] >= 80:
        for key,vale in e.items():
            print(key,vale)
            print('ได้เกรด4')
    elif e['score'] >= 70:
        for key,vale in e.items():
            print(key,vale)
            print('ได้เกรด4')
    elif e['score'] >= 60:
        for key,vale in e.items():
            print(key,vale)
            print('ได้เกรด4')