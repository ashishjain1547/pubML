# The method get_number_of_words() accepts a DataFrame that has been preprocessed by the script "preprocess_data_script".
# It has a hard-coded DataFrame column name 'Message_Clean' in use.

def get_number_of_words(df):
    rtnVal = {}
    for user in df.User.unique():
        nr_words = len([x for sublist in df[df.User==user].Message_Clean.values for x in sublist.split(' ')])
        rtnVal[user] = nr_words
    return rtnVal