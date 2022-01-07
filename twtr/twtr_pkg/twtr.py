def text_processor(df):
    import pandas as pd
    df = df[['tweet_id', 'text']]

    import nltk
    nltk.download('stopwords')

    import string
    from nltk.corpus import stopwords
    stopwords.words('english')

    def text_processing(text):
        nopunc = [char for char in text if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        nopuncnum = ''.join([i for i in text if not i.isdigit()])
        return ' '. join([word for word in nopuncnum.split() if word.lower() not in stopwords.words('english')])
    
    df['text'] = df['text'].apply(text_processing)
    return df
