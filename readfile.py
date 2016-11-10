import os,pickle

if __name__ == "__main__":
    dirname1 = "Reviews/"
    dirname2 = "Ratings/"
    with open('data/restname_id.pickle', 'rb') as f:
        mapping = pickle.load(f)
    mapping = {int(k):v for k,v in mapping.items()}
    rest_details = dict()
    for fname in os.listdir(dirname1):
        dictid = 0
        for root, dirs, files in os.walk(dirname2):
            for filename in files:
                if fname[:-12] in filename[:-12]:
                    flg = True
                    for res_id, name in mapping.iteritems():
                        if flg == True and name == fname[:-12].lower():
                            flg = False
                            dictid = res_id
                    ls = list()
                    rest_details[dictid] = dict()
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
                    rest_details[dictid] = ls
                    #rest_details[fname[:-12]] = ls
                    '''
                    for line,i in zip(f.read().split('-'),lines):
                        rest_details[fname[:-12]].append([i[:-1],line.strip().split('\n')])
                        #print i[:-1],line.strip().split('\n')
                    '''
                    #print "*******************

    print rest_details[58818]
