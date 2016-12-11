from Match import *
import json

def HierarchyMatch(mention, menu_item):
    if ExactMatch(mention, menu_item):
        return True
    elif SubstringMatch(mention, menu_item):
        return True
    elif PartialMatch(mention, menu_item):
        return True
    elif FuzzyMatch(mention, menu_item, 3):
        return True
    elif PercentMatch(mention, menu_item, .9):
        return True
    else:
        return False

def CompareItems(mentions, menus):
    dic = {}
    for mention, stuff in mentions.items():
        popularity = stuff[0]
        dish_rating = stuff[1]
        for menu_item in menus:
            price = str(menu_item[1])
            food = menu_item[0]
            if(HierarchyMatch(mention, food)):
            	if(dic.has_key(food)):
                	val = dic[food]
                	val[2] += popularity
                	val[1] += dish_rating
                	dic[food] = val
                else:
                	dic[food] = [price,dish_rating,popularity]
    return dic


def Convert(rest_search):
    dic = {}
    for rest,info in rest_search.items():
        rest_rating = info[0]
    	for dish, dish_info in info[1].items():
    		price = dish_info[0]
    		dish_rating = dish_info[1]
    		popularity = dish_info[2]
    		if dic.has_key(dish):
    			val = dic[dish]
    			tup = (rest,rest_rating,price,dish_rating,popularity)
    			val.append(tup)
    			dic[dish] = val
    		else:
    			val = []
    			tup = (rest,rest_rating,price,dish_rating,popularity)
    			val.append(tup)
    			dic[dish] = val
    return dic

if __name__ == '__main__':

    file = open("../data/restid_menu.json",'r')
    menu = json.load(file)

    file = open("../data/tagged_mentions.json",'r')
    tagged_mentions = json.load(file)

    rest_search = {}
    dish_mention = {}
    for rest_id, menu_items in menu.items():
        rest_mentions = tagged_mentions[rest_id]
        rest_rating = menu_items[0]
        items = menu_items[1]

        dish_mention = CompareItems(rest_mentions, items)
        rest_search[rest_id] = (rest_rating, dish_mention)

    dish_search = Convert(rest_search)

    with open('../data/rest_search.json', 'wb') as f:
    	json.dump(rest_search,f)

    with open('../data/dish_search.json', 'wb') as f:
    	json.dump(dish_search,f)
