import pickle, json

with open('data/Reviews.pkl') as data_file:
    data = pickle.load(data_file)

def ratingvsnumrev():

    graph_data = dict()
    graph_data[1.0], graph_data[1.5], graph_data[2.0], graph_data[2.5], graph_data[3.0], graph_data[3.5],graph_data[4.0], graph_data[4.5], graph_data[5.0] = 0,0,0,0,0,0,0,0,0
    #review[0] - text review of a menu item
    #review[1] - rating of that menu item
    for values in data.values():
        for review in values:
            graph_data[review[1]] += 1

    total_num_of_reviews = sum(graph_data.values())
    print total_num_of_reviews
    print (graph_data[4.0])
    print (graph_data[4.0]/float(total_num_of_reviews))*100



if __name__ == "__main__":

    ratingvsnumrev()
