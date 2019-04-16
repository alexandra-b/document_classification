from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def obtain_summary(file_name):
    stopWords = set(stopwords.words("english"))
    text = open(file_name, 'r', encoding="utf-8", errors='ignore')
    str_list = []
    str_text = ''
    words = []
    for line in text:
        words_inter = word_tokenize(line)
        filtered_sentence = [w for w in words_inter if not w in stopWords]
        words.extend(filtered_sentence)
        str_text += line[:-1]
    freqTable = dict()
    # print('Text is ', str_text)
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if len(word) == 1:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    sentences = sent_tokenize(str_text)
    # print(sentences)
    # print(freqTable)
    sentenceValue = dict()
    for sentence in sentences:
        for wordValue in freqTable:
            # print(wordValue, freqTable[wordValue])
            if wordValue in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freqTable[wordValue]
                else:
                    sentenceValue[sentence] = freqTable[wordValue]
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from original text
    try:
        average = int(sumValues / len(sentenceValue))
    except ZeroDivisionError:
        return ''
    summary = ''
    for sentence in sentences:
            if sentence in sentenceValue and sentenceValue[sentence] > (1.5 * average):
                summary +=  " " + sentence
    return summary
