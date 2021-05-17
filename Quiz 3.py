import requests
import json
import sqlite3
city = input("Enter City: ")
key = 'e3a2d1cecff0019df57b6934a5520b25'
cnt = 7
url = f'api.openweathermap.org/data/2.5/forecast/daily?q={city}&cnt={cnt}&appid={key}'
r = requests.get(url)
print(r.text)
print(r.status_code)
print(r.headers)
a = r.text
res = json.loads(a)
result = json.dumps(res, indent=6)
print(result["id"])
print(result["weather"])
print(result["temp"])

conn = sqlite3.connect("weather.sqlite")
cursor = conn.cursor()
cursor.execute("CREATE TABLE Pressure(Air_Pressure INT), INSERT INTO Pressure(Air_Pressure) VALUES(1013, 926, 1211)")
conn.commit()
conn.close()






