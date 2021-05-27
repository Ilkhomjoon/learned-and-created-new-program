# -*- coding: utf-8 -*-
"""
Created on Thu May 27 14:12:39 2021

@author: Ilhomjon
"""

davlatlar = {
            'o`zbekiston':{'poytaxt':'toshkent',
                            'til':'o`zbek',
                            'din':'islom',
                            'pul birligi':'so`m',
                            'axoli':35_054_874
                            },
             'rossiya':{'poytaxt':'moskva',
                            'til':'rus',
                            'din':'aralash',
                            'pul birligi':'rubl',
                            'axoli':835_054_874},
             'angliya':{'poytaxt':'london',
                            'til':'ingliz',
                            'din':'xiristiyan',
                            'pul birligi':'funt',
                            'axoli':385_054_874},
             'amerika':{'poytaxt':'vashington',
                            'til':'ingliz',
                            'din':'aralash',
                            'pul birligi':'dollor',
                            'axoli':835_054_874},
             'xitoy':{'poytaxt':'pekin',
                            'til':'xitoy',
                            'din':'aralash',
                            'pul birligi':'iyen',
                            'axoli':1_535_054_874}
    }

user = input("Davlat nomini kiriting: \n>>>").lower()

if user in davlatlar:
    x = davlatlar[user]
    print(f"{user.title()}ning poytaxti {x['poytaxt'].title()}"
          f"\nTili: {x['til']} tilida"
          f"\nDini: {x['din']} dinida"
          f"\nPul birligi: {x['pul birligi']}"
          f"\nAxolisi: {x['axoli']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
          
        

# for key, value in davlatlar.items():
#     print(f"\n{key.title()}ning poytaxti {value['poytaxt'].title()}"
#           f"\nTili: {value['til']} tilida"
#           f"\nDini: {value['din']} dinida"
#           f"\nPul birligi: {value['pul birligi']}"
#           f"\nAxolis: {value['axoli']}")
    