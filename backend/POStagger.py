import json
import nltk
from nltk.corpus import stopwords
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def Preprocess(t):
    '''
        Everything reduced to lower case for ease of processing
    '''
    t = t.lower()

    # Specific case to remove <'> so as to tag properly
    t = t.replace('\'','')

    return t

def Postag(t):
    '''
        Text Segmentation and Tagging
    '''
    sentences = nltk.sent_tokenize(t)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]

    # Attaching POS tags
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]

    # Flattening list of lists
    pos_tagged = [item for sublist in tagged_sentences for item in sublist]

    return pos_tagged

def Chunking(t):
    '''
        Chunking is grouping tagged words as phrases
    '''
    # Tag pattern to identify dishes
    pattern = '''FOOD : {<NN.*>+}'''

    chunk_rule = nltk.RegexpParser(pattern)
    tree = chunk_rule.parse(t)

    return tree

def Treeparse(tree):
    '''
        To parse chunk tree
    '''
    foods = []
    for subtree in tree.subtrees():
        if subtree.label() == 'FOOD':
            foods.append(' '.join([str(child[0]) for child in subtree]))

    return foods

if __name__ == '__main__':

    unprocess_data = {}
    process_data = {}
    named_entity = {}

    # Reading data back
    with open('../data/Reviews.json', 'r') as f:
         unprocess_data = json.load(f)

    for place, reviews in unprocess_data.items():
        for review, rating in reviews:
            processed = Preprocess(str(review))
            tagged = Postag(processed)
            chunked = Chunking(tagged)
            parsed = set(Treeparse(chunked))

            # parsed has all menu items mentioned in one single review
            for item in parsed:
                if len(item) >= 4:
                    if item in process_data.keys():
                        stats = process_data[item]
                        popular = stats[0]
                        senti = stats[1]

                        # Update new values of item aggr. senti and popularity
                        popular += 1
                        senti += rating
                        process_data[item] = [popular, senti]
                    else:
                        process_data[item] = [1, rating]

        # Putting menu generated via reviews against place
        place = place.encode('utf-8')
        named_entity[place] = process_data
        process_data = {} # Done to process other place reviews

    # Writing JSON data
    with open('../data/tagged_mentions.json', 'w') as f:
         json.dump(named_entity, f)