# import requests
# import json
# import sqlite3
# # 1
# url = 'https://ghibliapi.herokuapp.com/films'
# r = requests.get(url)
# print(r.status_code)
# print(r.text)
# print(r.headers)
#
# # 2
#
# r_json = r.json()
# r_loads = json.loads(r.text)
# with open('anime.json','w') as f:
#     json.dump(r_loads,f,indent=4)
#
# # 3
# print("სტუდიო ghibli-ს ფილმების ჩამონათვალი: ")
# for each in r_loads:
#     title = each['title']
#     release_time = each['release_date']
#     print("სახელი: ",title,"გამოსვლის წელი: ",release_time)
#
# 4
"""მოცემული პროგრამით იქმნება sqlite მონაცემთა ბაზაში ცხრილი ghibli,
რომელსაც გააჩნია ხუთი სვეტი.
ამის შემდეგ კი json-დან წამოღებული ინფორმაცია ემატება შექმნილ ცხრილში. ეს ინფორმაციაა:
ghibli-ს სტუდიოს თითოეული ფილმის სახელი,რეჟისორი,პროდიუსერი და გამოსვლის თარიღი."""
#
# conn = sqlite3.connect('ghibli.sqlite')
# c = conn.cursor()
# c.execute('''CREATE TABLE IF NOT EXISTS ghibli (
#           id INTEGER PRIMARY KEY AUTOINCREMENT,
#           title VARCHAR(50),
#           director VARCHAR(40),
#           producer VARCHAR(40),
#           release_date INTEGER)''')
# conn.commit()
#
# movie_rows = []
# for each in r_loads:
#     title = each['title']
#     director = each['director']
#     producer = each['producer']
#     release_date = each['release_date']
#     row = (title,director,producer,release_date)
#     movie_rows.append(row)
#
# c.executemany('INSERT INTO ghibli (title,director,producer,release_date) VALUES (?,?,?,?)',movie_rows)
# conn.commit()
# conn.close()
