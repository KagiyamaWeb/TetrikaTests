import requests
import wikipediaapi
'''
В этом задании я использую wikipediaapi. Это сторонняя библиотека для простой работы с API википедии. Благодаря
ей я могу получить всех животных из Категории:Животные за одну простую функцию. 
Она устанавливается с помощью pip3 install wikipedia-api. 
Затем я прохожусь по названиям животных и записываю в словарь, сколько животных есть на первую букву.
'''
wiki_wiki = wikipediaapi.Wikipedia('ru')
animal_count = {}

def get_categorymembers(categorymembers, level=0, max_level=1):
        for c in categorymembers.values():
            if c.title[0] not in animal_count:
                animal_count[c.title[0]] = 1
            else:
                animal_count[c.title[0]] += 1    

cat = wiki_wiki.page("Категория:Животные_по_алфавиту")
get_categorymembers(cat.categorymembers)
 
for key in animal_count.keys():
    print(str(key) + ': ' + str(animal_count[key]))


