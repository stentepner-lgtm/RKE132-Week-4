# Kui klient on kulutanud vähemalt 5000 €, siis tema staatus on Platinum.
# Kui klient on kulutanud vähemalt 1000 €, siis staatus on Gold.
# Kui klient on kulutanud vähemalt 500 €, siis staatus on Silver.
# Kui klient on kulutanud vähemalt 100 €, siis staatus on Bronze.
# Kui vähem kui 100 €, siis on ta Tavaline klient.

spent = int(input("Kui palju oled kulutanud? "))

# if spent >= 5000:
#     print("Staatus: Platinum")
# elif spent >= 1000:
#     print("Staatus: Gold")
# elif spent >= 500:
#     print("Staatus: Silver")
# elif spent >= 100:
#     print("Staatus: Bronze")
# else:
#     print("Staatus: Tavaline klient")


if spent < 100:
    print("Staatus: Tavaline klient")
elif spent >=100 and spent < 500:
    print("Staatus: Bronze")
elif spent >= 500 and spent < 1000:
    print("Staatus: Silver")
elif spent >= 1000 and spent < 5000:
    print("Staatus: Gold")
else:
    print("Staatus: Platinum")