from utils.postag import token_postag
from utils.db import get_db_data

def GetInfo(text):

    # text = text.lower()
    tmp_text_array = text.split(" ")
    info = ''
    allinfo = ''

    # identify the nouns
    tokens_array = []
    for token in tmp_text_array:
        token_postag(token, tokens_array)

    #Query the DB for the nounces anc collect info
    for token in tokens_array:
        info = get_db_data(tokens_array)
        if info:
            allinfo += info
            print(info, allinfo)
    # info = "Beautiful city"

    return allinfo