#Flowchart suhu dan kelembaban

# batas suhu dan kelembapan
suhu_min = 20
suhu_max = 30
kelembapan_min = 20
kelembapan_max = 60

# loop utama
while True:
    # simulasi pembacaan sensor
    s_suhu = float(input("Masukkan nilai suhu: "))
    s_kelembapan = float(input("Masukkan nilai kelembapan: "))

    # pengendalian suhu
    if s_suhu < suhu_min:
        pemanas = "ON"
        pendingin = "OFF"
    elif s_suhu > suhu_max:
        pemanas = "OFF"
        pendingin = "ON"
    else:
        pemanas = "OFF"
        pendingin = "OFF"

    # pengendalian kelembapan
    if s_kelembapan < kelembapan_min:
        pengering = "ON"
        pelembab = "OFF"
    elif s_kelembapan > kelembapan_max:
        pengering = "OFF"
        pelembab = "ON"
    else:
        pengering = "OFF"
        pelembab = "OFF"

    # tampilkan status
    print(f"\nStatus:")
    print(f"Suhu: {s_suhu}°C → Pemanas: {pemanas}, Pendingin: {pendingin}")
    print(f"Kelembapan: {s_kelembapan}% → Pengering: {pengering}, Pelembab: {pelembab}")
    print("-" * 45)