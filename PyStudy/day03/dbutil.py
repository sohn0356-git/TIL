
def insert(**kwargs):
    id = kwargs['id']
    pwd = kwargs['pwd']
    name = kwargs['name']
    age = kwargs['age']
    print('%s %s %s %d inserted ......' % (id,pwd,name,age))


def select():
    data = []
    data.append((['id01','pwd01','name01',22]))
    data.append((['id02', 'pwd02', 'name02',23]))
    data.append((['id03', 'pwd03', 'name03',15]))
    data.append((['id04', 'pwd04', 'name04',20]))
    data.append((['id05', 'pwd05', 'name05',33]))
    return data

def select(**kwargs):
    data = []
    id = kwargs.get('id')
    if id:
        data.append((['id01', 'pwd01', 'name01', 10]))
    else:
        data.append((['id01', 'pwd01', 'name01', 22]))
        data.append((['id02', 'pwd02', 'name02', 23]))
        data.append((['id03', 'pwd03', 'name03', 15]))
        data.append((['id04', 'pwd04', 'name04', 20]))
        data.append((['id05', 'pwd05', 'name05', 33]))

    return data

