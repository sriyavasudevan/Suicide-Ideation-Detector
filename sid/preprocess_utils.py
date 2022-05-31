import pandas as pd

import re
from emot.emo_unicode import UNICODE_EMOJI, EMOTICONS_EMO
import string

import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

def convert_csv_to_df():
    """

    :return:
    """
    filename = "Suicide_Detection.csv"
    df = pd.read_csv(filename)
    print(df.info)
    df.drop(columns=df.columns[0], axis=1, inplace=True)
    print(df.head(10))
    return df


def convert_lowercase(df):
    """

    :param df:
    :return:
    """
    df['lower_text'] = df['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    return df


def convert_emojis(text):
    """

    :param text:
    :return:
    """
    rem_punc_text = text.translate(str.maketrans('', '', string.punctuation))
    text_split = list(rem_punc_text)
    for i, item in enumerate(text_split):
        if item in UNICODE_EMOJI.keys():
            text_split[i] = " " + UNICODE_EMOJI[item].replace(",", "").replace(":", "").replace("_", " ") + " "

    conv_text = "".join(text_split).strip()
    return conv_text


def remove_noise(text_tokens, stop_words):
    """

    :param text_tokens:
    :param stop_words:
    :return:
    """
    cleaned_tokens = []

    for word in text_tokens:
        token = word.text
        pos = word.pos_
        token = re.sub("_", " ", token)
        token = word.lemma_
        if len(token) > 0 and token not in string.punctuation and token not in stop_words:
            cleaned_tokens.append(token)

    return cleaned_tokens


def get_all_words(cleaned_tokens_list):
    """

    :param cleaned_tokens_list:
    :return:
    """
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):
    """

    :param cleaned_tokens_list:
    :return:
    """
    for text_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in text_tokens)


def using_spacy():
    """
    want to try to use spacy to tokenize
    :return:
    """
