if __name__ == "__main__":

    ratings = list()
    fname = "Ratings/Tim Tai Ratings.txt"

    f = open(fname,'r')
    for line in f.read().split('\n'):
        ratings.append(line.split(' ')[2][:-1])
    f.close()


    f = open(fname,'w')
    for i in ratings:
        f.write(i+"\n")
    f.close()
