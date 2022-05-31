import pandas as pd
import nltk
from nltk import FreqDist, classify, NaiveBayesClassifier


def naivebayes(train_data, test_data):
    """

    :param train_data:
    :param test_data:
    :return:
    """
    classifier = NaiveBayesClassifier.train(train_data)
    print("Accuracy is:", classify.accuracy(classifier, test_data))
    print(classifier.show_most_informative_features(10))

    # but then what is the difference between nltk naive bayes and sklearn naive bayes - need to find out