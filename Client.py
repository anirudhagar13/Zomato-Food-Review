from Match import *
import pickle
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
    for mention, stuff in mentions:
        popularity = stuff[0]
        dish_rating = stuff[1]
        for menu_item in menus:
            price = menu_item[1]
            if(HierarchyMatch(mention, menu_item[0])):
                if(dic.has_key(menu_item[0])):
                    val = dic[menu_item]
                    val[2] += popularity
                    val[1] += dish_rating
                    dic[menu_item] = val
                else:
                    val = []
                    val.append(price,dish_rating,popularity)
                    dic[menu_item] = val

    return dic


if __name__ == '__main__':

    file = open("data/restid_menu.pickle",'r')
    menu = pickle.load(file)

    file = open("data/tagged_mentions.pickle",'r')
    tagged_mentions = pickle.load(file)

    rest_search = {}
    for rest_id, menu_items in menu:
        rest_mentions = tagged_mentions[rest_id]
        rest_rating = menu_items[0]
        items = menu_item[1]
        dish_mention = CompareItems(rest_mentions, items)
        rest_search[rest_id] = (rest_rating, dish_mention)

    print rest_search
