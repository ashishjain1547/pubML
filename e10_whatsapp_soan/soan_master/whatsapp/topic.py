import pandas   as pd
import numpy    as np

from pattern.nl     import parse, split, singularize, predicative, lemma

from sklearn.decomposition              import NMF, LatentDirichletAllocation
from sklearn.feature_extraction.text    import TfidfVectorizer, CountVectorizer

def print_top_words(model, feature_names, n_top_words):
    """ Prints the top words representing the topics created
    by "model". 
    
    Parameters:
    -----------
    model : sklearn model
        Model that is used for the analysis, either NMF or LDA
    feature_names : str
        Used to extract the messages
    n_top_words : int
        Number of words to be shown
    """
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()
    
def prepare_text_nl(row):
    """ Prepares dutch text by doing the following:
    * Lemmatize a word
    * Singularize a word
    * Predicative a word
    
    Parameters:
    -----------
    row : pandas dataframe
        A row of a pandas dataframe
        
    Returns:
    --------
    new_message : pandas dataframe
        A row of a pandas dataframe 
    
    """
    try:
        message = split(parse(row.Message_Only_Text))
    except:
        print(row.Message_Only_Text)
        
    new_message = ''

    for sentence in message:
        for word, tag in sentence.tagged:
            if (tag == 'MD') | ('VB' in tag):
                new_message += lemma(word) + ' '
            elif tag == 'NNS':
                new_message += singularize(word) + ' '
            elif 'JJ' in tag:
                new_message += predicative(word) + ' '
            else:
                new_message += word + ' '
    
    return new_message
    
def topics(df, model = "lda", stopwords = None):
    """ Either executes LDA or NMF on a dutch document.
    This is a simple implementation and only used for
    "fun" purposes. It is not so much to find the very
    best topics, but topics that are good enough. 
    
    
    Parameters:
    -----------
    df : pandas dataframe
        Pandas dataframe that contains the raw messages
    mode : str, default "lda"
        Which model to use for topic modelling. 
        Either "lda" or "nmf" works for now
    stopwords : str, default None
        If you want to remove stopwords, provide a local 
        link to the text file (that includes a list of words)
        including the extension. 
    
    """
    # Prepare stopwords
    if stopwords:
        with open(stopwords) as stopwords_list:
            stopwords_list = stopwords_list.readlines()
            stopwords_list = [word[:-1] for word in stopwords_list]
    else:
        stopwords_list = []
        
    # Create Topics
    for user in df.User.unique():
        print("#" * len(user) + "########")
        print("### " + user + " ###")
        print("#" * len(user) + "########\n")

        data_samples = df[df.User == user].Message_Prepared
        data_samples = data_samples.tolist()
        
        if model == "lda":
            # Extracting Features
            tf_vectorizer = CountVectorizer(max_df=0.95, min_df=2,stop_words=stopwords_list)
            tf = tf_vectorizer.fit_transform(data_samples)

            # Fitting LDA
            topic_model = LatentDirichletAllocation(n_components=5, max_iter=5,
                                            learning_method='online',
                                            learning_offset=50.,
                                            random_state=0)
            topic_model.fit(tf)
            feature_names = tf_vectorizer.get_feature_names()
        else:
            # MNF uses tfidf
            tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, stop_words=stopwords_list)
            tfidf = tfidf_vectorizer.fit_transform(data_samples)
            feature_names = tfidf_vectorizer.get_feature_names()

            # Run NMF
            n_compo = 5
            for i in range(5, 0, -1):
                try:
                    topic_model = NMF(n_components=i, random_state=1, alpha=.1, l1_ratio=.5, init='nndsvd')
                    topic_model.fit(tfidf)
                    break
                except:
                    pass
        
        print("\nTopics in {} model:".format(model))
        print_top_words(topic_model, feature_names, 7)