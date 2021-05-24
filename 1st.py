"""
Ilkhomjon Ibragimov

o`rganish jarayonida yaratgan kodlari

bu dastur orqali siz davlatlarning poytaxtlari nima ekanligini bilib olishingiz mumkin!

24-05-2021 | 1:10 PM"
"""



country = {
    "o`zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'sungapur',
    'italiya':'rim'}

user = input("Qaysi davlatni poytaxtini nima eknaligini bilmoqchisiz?\n>>> ").lower()
x = country.get(user)

if x == None:
    print(F"Uzur, Biz siz so`ragan {user} davlatining poytaxti nima ekanligini bilmyamiz")
else:
    print(F"Siz izlagan {user.title()} davlatining poytaxti {x.title()} shaxri!")