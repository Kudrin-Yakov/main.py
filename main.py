meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное"
            }


print(meme_dict.keys())
key = input('Напишите:  ')

print(meme_dict[key])

if key in meme_dict.keys():
    print(meme_dict[key])
else:
    print('Нет такого слова')
