import utils


def test_word_count():
    count = utils.word_count(['count the words'])
    assert count == {'count': 1, 'the': 1, 'words': 1}


def test_word_count_tricky():
    count = utils.word_count(['count the words'])
    count = utils.word_count(['count the words return of the word count'], count)
    assert count == {'count': 3, 'the': 3, 'words': 2, 'return': 1, 'of': 1, 'word': 1}


