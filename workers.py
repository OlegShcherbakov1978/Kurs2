from collections import OrderedDict


def workers():
    workers_list = {}

    while True:
        a = input('введите параметр (для окончания ввода введите "stop"): ')
        if a == "stop":
            break
        b = input('введите значение: ')
        workers_list[a] = b
    return workers_list


for k, v in OrderedDict(sorted(workers().items())).items():
    print("{0}: {1}".format(k, v))
