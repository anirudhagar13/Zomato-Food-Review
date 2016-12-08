import pickle, json

def bubble(reviews, rest_search, rest_name):
    '''
    Visualize  Restaurant Avg Price, Rating & Review length
    '''
    visual = {}
    for restid, stuff in rest_search.items():
        name = rest_name[restid]
        rating = stuff[0]
        details = stuff[1]
        all_reviews = reviews[restid]
        no_reviews = len(all_reviews)-1


        #Set params to zero in each loop
        tot_price = 0
        tot_rate = 0

        print name
        #Getting Avg price and popularity
        for info in details.values():
            print info
            #tot_price += int(str(info[0]))
            #tot_rate += info[1]

        #Calculating total words in all reviews
        for review in all_reviews:
            tot_length += len(review[1].split())

        #print name, rating, tot_price, tot_rate/no_reviews





if __name__ == '__main__':

    file = open("data/Reviews.pkl",'r')
    reviews = pickle.load(file)

    file = open("data/rest_search.json",'r')
    rest_search = json.load(file)

    file = open("data/restname_id.pickle",'r')
    rest_name = pickle.load(file)

    bubble(reviews, rest_search, rest_name)

'''
    with open('visualization/bubble.json', 'wb') as f:
        json.dump(visual,f)
'''