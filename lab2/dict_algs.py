ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 12,
    }, {
        "name": "petja",
        "age": 10,
    }],
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}

emps = [ivan, darja]


def findch(list):
    flist = []
    for i in emps:
        for j in i['children']:
            if j['age'] > 18:
                flist.append(i)
                break
    return flist


print(*findch(emps))


