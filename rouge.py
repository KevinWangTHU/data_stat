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


def _score(storyName, highlightName):
    geneSen = PlaintextParser.from_file(storyName, Tokenizer(LANGUAGE)).document.sentences
    refSen = PlaintextParser.from_file(highlightName, Tokenizer(LANGUAGE)).document.sentences
    print "=============="
    for sen in refSen:
        print sen
    for gs in geneSen:
        r1 = []
        print gs
        for rs in refSen:
            r1.append(rouge_n([gs], [rs], 1))
        print r1

    # print geneSen[0]
    # print refSen[0], refSen[1]
    # try:
    #     print rouge_n([geneSen[0]], [refSen[0]], 1)
    #     print rouge_n([geneSen[0]], [refSen[0]], 2)
    #     print rouge_n([geneSen[0]], [refSen[1]], 1)
    #     print rouge_n([geneSen[0]], [refSen[1]], 2)
    # except ZeroDivisionError:
    #     pass
    raw_input()



def get_scores(source):
    story_dir = "../stories/final_" + source + "/"
    highlight_dir = "../stories/highlights_" + source + "/"
    storyFiles = os.listdir(story_dir)
    for i in range(len(storyFiles)):
        storyName = storyFiles[i]
        if not storyName.endswith(".story"):
            continue
        highlightName = storyFiles[i].strip("story")+"highlight.txt"
        print storyName
        rouge = _score(story_dir + storyName, highlight_dir + highlightName)
        # print rouge[0]
        # raw_input()
        # print rouge[1]
        # raw_input()
        # print rouge[2]
        # raw_input()


def add_period(source):
    highlight_dir = "../stories/highlights_" + source + "/"
    highlightFiles = os.listdir(highlight_dir)
    for i in range(len(highlightFiles)):
        highlightName = highlightFiles[i]
        if not highlightName.endswith(".highlight"):
            continue
        lines = open(highlight_dir + highlightName).readlines()
        outfile = open(highlight_dir + highlightName + ".txt", "w")
        for line in lines:
            outfile.write(line[:-1]+".\n")
        if i % 500 == 0:
            print i


def ap():
    add_period("cnn")
    add_period("dm")

if __name__ == "__main__":
    get_scores("cnn")
    # ap()
