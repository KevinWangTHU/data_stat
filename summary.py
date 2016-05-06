# -*- coding: utf-8 -*-

import os
# from __future__ import absolute_import
# from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
# from sumy.summarizers.edmundson import EdmundsonSummarizer as Summarizer
from sumy.summarizers.text_rank import TextRankSummarizer as Summarizer
# from sumy.summarizers.lex_rank import LexRankSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.evaluation.rouge import rouge_n, rouge_l_sentence_level


LANGUAGE = "english"
SENTENCES_COUNT = 4
SPLIT = 20

def evaluate(geneSen, refSen):
    # Rouge 1, 2, L
    return rouge_n(geneSen, refSen, 1), rouge_n(geneSen, refSen, 2), rouge_l_sentence_level(geneSen, refSen)


def _summ_score(storyName, highlightName):
    parser = PlaintextParser.from_file(storyName, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    geneSen = summarizer(parser.document, SENTENCES_COUNT)
    refSen = PlaintextParser.from_file(highlightName, Tokenizer(LANGUAGE)).document.sentences


    #print geneSen
    #print "=========="
    #print refSen
    try:
        return evaluate(geneSen, refSen)
    except Exception as e:
        print storyName
        print e
        raise e

def _firstK_score(storyName, highlightName):
    parser = PlaintextParser.from_file(storyName, Tokenizer(LANGUAGE))

    geneSen = parser.document.sentences[:SENTENCES_COUNT]
    refSen = PlaintextParser.from_file(highlightName, Tokenizer(LANGUAGE)).document.sentences

    # print geneSen
    # print "=========="
    # print refSen
    # print evaluate(geneSen, refSen)
    try:
        return evaluate(geneSen, refSen)
    except Exception as e:
        print storyName
        print e
        raise e


def summarizer_score(method="summ"):
    print method
    for source in ["cnn", "dm"]:
        r1 = 0
        r2 = 0
        rl = 0
        count = 0
        story_dir = "../stories/final_" + source + "/"
        highlight_dir = "../stories/highlights_" + source + "/"
        storyFiles = os.listdir(story_dir)
        print len(storyFiles)/SPLIT
        for i in range(len(storyFiles)/SPLIT):
            # if i % 50 == 0:
            #     print i
            storyName = storyFiles[i]
            if not storyName.endswith(".story"):
                continue
            highlightName = storyFiles[i].strip("story") + "highlight.txt"
            # print storyName, highlightName
            try:
                if method == "summ":
                    rouge = _summ_score(story_dir + storyName, highlight_dir + highlightName)
                else:
                    rouge = _firstK_score(story_dir + storyName, highlight_dir + highlightName)
            except KeyboardInterrupt:
                raise
            except:
                continue
            r1 += rouge[0]
            r2 += rouge[1]
            rl += rouge[2]
            count += 1

        print "Source = " + str(source)
        print "Count = " + str(count)
        print "Rouge-1 = " + str(r1/(count+0.0))
        print "Rouge-2 = " + str(r2/(count+0.0))
        print "Rouge-L = " + str(rl/(count+0.0))


if __name__ == "__main__":
    summarizer_score()
