import pickle, json

with open('data/Reviews.json') as data_file:
    data = json.load(data_file)

with open('data/dish_search.json') as data_file:
    data2 = json.load(data_file)

def rating_vs_numrev(option):

    graph_data = dict()
    graph_data[1.0], graph_data[1.5], graph_data[2.0], graph_data[2.5], graph_data[3.0], graph_data[3.5],graph_data[4.0], graph_data[4.5], graph_data[5.0] = 0,0,0,0,0,0,0,0,0
    #review[0] - text review of a menu item
    #review[1] - rating of that menu item
    for values in data.values():
        for review in values:
            graph_data[review[1]] += 1

    total_num_of_reviews = sum(graph_data.values())
    if option == 1:
        with open('rating_vs_numrev.json') as outfile:
            json.dump(graph_data, outfile)
    elif option == 2:
        return graph_data

def rating_vs_avgrevlen():

    graph_data = dict()
    graph_data[1.0], graph_data[1.5], graph_data[2.0], graph_data[2.5], graph_data[3.0], graph_data[3.5],graph_data[4.0], graph_data[4.5], graph_data[5.0] = 0,0,0,0,0,0,0,0,0

    for values in data.values():
        for review in values:
            graph_data[review[1]] += len(review[0].split())

    numrev = rating_vs_numrev(2)

    for key in graph_data.keys():
        print str(key) + " : " + str(graph_data[key]) + " : " + str(numrev[key])
        graph_data[key] = graph_data[key] / numrev[key]
    '''
    with open('rating_vs_avgrevlen.json') as outfile:
        json.dump(graph_data, outfile)
    '''

def price_vs_popl():
    '''
        graph_data[price] = total popl
        - number of reviews(popl) of menu items of a particular price.
    '''
    graph_data = dict()
    for values in data2.values():
        key = int(values[0][2])
        if key not in graph_data.keys():
            graph_data[key] = values[0][4]
        else:
            graph_data[key] += values[0][4]

    print graph_data
    return graph_data

def price_vs_rating():
    '''
    '''
    graph_data = dict()
    for values in data2.values():
        key = int(values[0][2])
        if key not in graph_data.keys():
            graph_data[key] = round(values[0][3]/values[0][4],2)
        else:
            graph_data[key] += round(values[0][3]/values[0][4],2)

    print graph_data[140]

if __name__ == "__main__":

    #rating_vs_numrev(1)
    #rating_vs_avgrevlen()
    #price_vs_popl()
    price_vs_rating()
