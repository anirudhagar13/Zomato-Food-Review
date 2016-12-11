import json

big_tup = ()
small_tup = ()
lst = []
rest = ''
dic = {}
dic2 = {}
with open('../data/menu.csv') as fp:
    for line in fp:
        line = line.rstrip()
        ls = line.split(',')
        if(ls[0] != ""):
            if(rest != ''):
                dic[rest_id] = (rate,lst)
                dic2[rest_id] = rest
                lst = []

            rest = ls[0].lower()
            rate = ls[1]
            rest_id = ls[4]

        menu = ls[2]
        price = ls[3]
        tup1 = (menu, price)
        lst.append(tup1)

    dic[rest_id] = (rate,lst)
    dic2[rest_id] = rest


with open('../data/restname_id.json', 'wb') as handle:
  json.dump(dic2, handle)
with open('../data/restid_menu.json', 'wb') as handle:
  json.dump(dic, handle)

