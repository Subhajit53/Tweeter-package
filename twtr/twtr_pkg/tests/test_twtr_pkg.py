from twtr_pkg import twtr

import pytest

def test_text_processor():
    import pandas as pd
    data = {'tweet_id' : [1234],
            'text' : ["Hey, did you know that the summer break is coming? Amazing right!! It's only 5 more days!!"]}
    sample_df = pd.DataFrame(data)

    processed = twtr.text_processor(sample_df)
    processed = processed['text']
    assert(processed == 'Hey, know summer break coming? Amazing right!! days!!')