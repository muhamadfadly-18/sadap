import requests

ip = "192.168.1.3"  # Ganti dengan IP hasil tangkapan kamu

# NOTE: IP lokal (192.168.x.x) tidak bisa dilacak ke lokasi publik
# Ini contoh untuk IP publik

response = requests.get(f"http://ip-api.com/json/{ip}")
data = response.json()

if data['status'] == 'success':
    print("Lokasi:")
    print(f"Negara : {data['country']}")
    print(f"Kota   : {data['city']}")
    print(f"ISP    : {data['isp']}")
    print(f"Lat    : {data['lat']}")
    print(f"Lon    : {data['lon']}")
else:
    print("Gagal melacak IP.")
