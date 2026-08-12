
import re
import string

from sklearn.base import BaseEstimator, TransformerMixin

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


# Download required NLTK resources
# These lines are included to recreate the file exactly as it was defined
# in previous %%writefile cells that were deleted.
# In a production environment, NLTK data should ideally be pre-downloaded
# during environment setup rather than within the module itself.
nltk.download("stopwords", quiet=True)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


# Create stopwords set
stop_words = set(
    stopwords.words("english")
)

# Create stemmer
stemmer = PorterStemmer()


# ============================================================
# TEXT PREPROCESSING FUNCTION
# ============================================================

def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(
        r"http\S+|www\S+|https\S+",
        "",
        text
    )

    # Remove HTML tags
    text = re.sub(
        r"<.*?>",
        "",
        text
    )

    # Remove punctuation
    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    # Tokenization
    words = word_tokenize(text)

    # Remove stopwords
    words = [
        word
        for word in words
        if word not in stop_words
    ]

    # Stemming
    words = [
        stemmer.stem(word)
        for word in words
    ]

    return " ".join(words)


# ============================================================
# SKLEARN TEXT PREPROCESSOR
# ============================================================

class TextPreprocessor(
    BaseEstimator,
    TransformerMixin
):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        return [
            preprocess_text(str(text))
            for text in X
        ]
