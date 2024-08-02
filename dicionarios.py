def dicionarios():
    dic = {'nome': 'Alex', 'idade': 38, 'filhos':['Link', 'Zelda']}
    print("dic['filhos']:", dic["filhos"])
    print(dic)

    dic["extra"] = {"a": 1, "b": 10}

    print(dic)
    print(dic.keys())
    print(dic.items())
    print(dic.values())
    return

if __name__ == '__main__':
    dicionarios()
