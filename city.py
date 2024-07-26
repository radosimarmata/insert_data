import json
import mysql.connector
from datetime import datetime
import requests

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

cursor = db.cursor()

provinsi_url = 'https://radosimarmata.github.io/data-indonesia/provinsi.json'
response = requests.get(provinsi_url)
provinsi_data = response.json()

for provinsi in provinsi_data:
  provinsi_id = provinsi['id']
  provinsi_nama = provinsi['nama']

  kabupaten_url = f'https://radosimarmata.github.io/data-indonesia/kabupaten/{provinsi_id}.json'

  response = requests.get(kabupaten_url)

  if response.status_code == 200:
    kabupaten_data = response.json()

    for kabupaten in kabupaten_data:
      kota = kabupaten['nama']
      long = str(kabupaten['longitude'])
      lat = str(kabupaten['latitude'])
      created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

      sql = "INSERT INTO city (kota, provinsi, `long`, lat, created_at) VALUES (%s, %s, %s, %s, %s)"
      val = (kota, provinsi_nama, long, lat, created_at)
      cursor.execute(sql, val)
  else:
    print(f"File kabupaten untuk provinsi ID {provinsi_id} {provinsi_nama} tidak ditemukan.")

# Commit dan tutup koneksi
db.commit()
cursor.close()
db.close()

print("Data berhasil dimasukkan ke dalam tabel city.")