import json
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = db.cursor()

with open('D:/project/Learn/python/scraper_web/tokopedia_categories.json', 'r') as file:
  tokopedia_categories  = json.load(file)

for category in tokopedia_categories:
  category_name = category['title']
  print(category_name)
  sql = "INSERT INTO category (name) VALUES (%s)"
  val = (category_name,)
  cursor.execute(sql, val)

db.commit()
cursor.close()
db.close()

print("Data berhasil dimasukkan ke dalam tabel category.")