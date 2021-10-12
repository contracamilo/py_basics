def run():
    mi_dic = {
        'key1': 1,
        'key2': 2,
        'key3': 3
    }

    print(mi_dic)
    print(mi_dic['key1'])

    for item in mi_dic.keys():
        print(item)

    for item in mi_dic.values():
        print(item)

    for i, k in mi_dic.items():
        print(i, k)


if __name__ == '__main__':
    run()
