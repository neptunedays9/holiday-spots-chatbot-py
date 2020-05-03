from utils.postag import token_postag

def GetInfo(text):
    # print(text)
    text = text.lower()
    tmp_text_array = text.split(" ")

    # identify the nouns
    tokens_array = []
    for token in tmp_text_array:
        token_postag(token, tokens_array)

    #Query the DB for the nounces anc collect info
    info = "Beautiful city"

    return info