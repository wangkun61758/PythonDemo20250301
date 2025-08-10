import os.path


def test1():
    dict1 = {'name': '韩梅梅', 'age': 11, 'car': 'jeep'}
    list1 = []
    list2 = []
    for k, v in dict1.items():
        list1.append(k)
        list2.append(v)
    dict2 = dict({list1[i]: list2[i] for i in range(len(list1))})
    dict3 = {list1[j]: list2[j] for j in range(len(list1))}
    print(dict3)
    print(dict2)
    if not os.path.exists('../../resources/dict'):
        os.makedirs('../../resources/dict')
    with open('../../resources/dict/dict1.yaml', 'w', encoding='utf-8') as file:
        file.write(str(dict1))
