# Создайте словарь содержащий данные о человеке.
# В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.

def human(name:str, age:int, gender:str, height:int, weight:float, foot:float):
    dict_human = {'name': name,
                  'age': age,
                  'gender': gender,
                  'height': height,
                  'weight': weight,
                  'foot': foot}
    dict_human.setdefault('foot_2', 44)
    dict_human.pop('age')
    return dict_human


# Добавьте в словарь ключ и значение размера ноги
# Удалите из словаря возраст.

# Выведите на экран все данные о человеке по ключам.
human_1 = human('pol', 25, 'man', 180, 75.5, 43)
print(human_1.get('name'))
print(human_1.get('age'))
print(human_1.get('gender'))
print(human_1.get('height'))
print(human_1.get('weight'))
print(human_1.get('foot'))


