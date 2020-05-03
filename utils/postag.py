import nltk
# nltk.download()


# nltk.download('all')
def token_postag(token, array):
    # print(token)
    text_array = []
    tokens = nltk.word_tokenize(token)
    for tuple in nltk.pos_tag(tokens):
        print(tuple[0] + ':' + tuple[1])
        # if tuple[1] == "NN" or tuple[1] == "JJ":
        array.append(tuple[0])
    return
