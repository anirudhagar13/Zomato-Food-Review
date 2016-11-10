import os

if __name__ == "__main__":
    dirname1 = "Reviews/"
    dirname2 = "Ratings/"

    rest_details = dict()
    for fname in os.listdir(dirname1):
        for root, dirs, files in os.walk(dirname2):
            for filename in files:
                if fname[:-12] in filename[:-12]:
                    ls = list()
                    rest_details[fname[:-12]] = dict()
                    f1 = open((dirname1+fname),'r')
                    f2 = open((dirname2+filename),'r')
                    lines = f2.readlines()
                    lines2 = f1.read()
                    lines2 = lines2.split('-')
                    lines2.pop(0)
                    s1 = len(lines)
                    s2 = len(lines2)
                    s = 0
                    if s1 < s2:
                        s = s1
                        lines2 = lines2[:s]
                    elif s2 > s1:
                        s = s2
                        lines = lines[:s]
                    for i in range(s):
                        review = lines2[i].strip()
                        rating = lines[i].rstrip()
                        ls.append((rating,review))
                    rest_details[fname[:-12]] = ls
                    '''
                    for line,i in zip(f.read().split('-'),lines):
                        rest_details[fname[:-12]].append([i[:-1],line.strip().split('\n')])
                        #print i[:-1],line.strip().split('\n')
                    '''
                    #print "*******************

    print rest_details['BelgYum']
