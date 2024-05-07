# Ваш коллега занимается обработкой естественного языка. Однако алгоритм в текущей реализации работает медленно. 
# Вооружившись новыми знаниями о параллельных вычислениях, любезно согласились ему помочь.
# Вам необходимо реализовать функцию clear_data, которая может параллельно обработать тексты в датасете.

import re
from string import punctuation
from joblib import Parallel, delayed
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def clear_text(text, lemmatizer, patterns, stop_words):
    """Clear and preprocess text data.

    Parameters
    ----------
    text : str
        Input text to be cleaned and preprocessed.
    
    lemmatizer : WordNetLemmatizer
        Instance of WordNetLemmatizer for lemmatization.
    
    patterns : list
        List of regular expression patterns to remove from text.
    
    stop_words : list
        List of stop words to be removed from text.

    Returns
    -------
    str
        Cleaned and preprocessed text.
    """
    text = str(text)
    for pattern in patterns:
        text = pattern.sub('', text)
    
    transform_text = text.translate(str.maketrans("", "", punctuation))
    transform_text = re.sub(" +", " ", transform_text)

    text_tokens = word_tokenize(transform_text)

    lemma_text = [
        lemmatizer.lemmatize(word.lower()) for word in text_tokens
    ]
    cleaned_text = " ".join(
        [str(word) for word in lemma_text if word not in stop_words]
        )
    return cleaned_text

def clear_data(source_path: str, target_path: str, n_jobs: int):
    """Baseline process df

    Parameters
    ----------
    source_path : str
        Path to load dataframe from

    target_path : str
        Path to save dataframe to
    
    n_jobs : int 
        Count of jobs to process
    """

    data = pd.read_parquet(source_path)
    data = data.copy().dropna().reset_index(drop=True)

    lemmatizer = WordNetLemmatizer()
    regex_patterns = [re.compile(r"https?://[^,\s]+,?"), re.compile(r"@[^,\s]+,?")]
    stop_words = stopwords.words("english")
    
    cleaned_text_list = Parallel(n_jobs=n_jobs,backend='multiprocessing')(delayed
                            (clear_text)(text, lemmatizer, regex_patterns, stop_words)
                            for text in data['text'])

    data["cleaned_text"] = cleaned_text_list

    data.to_parquet(target_path)

# if __name__ == '__main__':
#     data_path = './multiprocessing/test_data.parquet'
#     result_path = './multiprocessing/test_result.parquet'
#     clear_data(data_path, result_path, 4)
#     print(pd.read_parquet(result_path))
