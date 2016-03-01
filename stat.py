import os
from nltk import word_tokenize, sent_tokenize


if __name__ == "__main__":

    for source in ["dm", "cnn"]:
        avg_para = 0
        avg_sen = 0
        avg_len = 0
        avg_sen_s = 0
        avg_len_s = 0

        in_dir = "../stories/final_" + source + "/"
        count = 0.0
        for file_name in os.listdir(in_dir):
            if file_name.endswith(".story"):
                count += 1
                if count % 500 == 0:
                    print count
                f = open(in_dir + file_name).readlines()
                for i in range(len(f)):
                    para = f[i].decode('utf-8')
                    if para == "@highlight\n":
                        break
                    if para == "\n":
                        continue
                    avg_para += 1
                    # print para
                    # word tokenize
                    tokens = word_tokenize(para)
                    avg_len += len(tokens)
                    # print tokens
                    # print len(tokens)

                    # sentence tokenize
                    tokens = sent_tokenize(para)
                    avg_sen += len(tokens)
                    # print tokens
                    # print len(tokens)

        avg_para /= count
        avg_len /= count
        avg_sen /= count

        in_dir = "../stories/highlights_" + source + "/"
        count = 0.0
        for file_name in os.listdir(in_dir):
            if file_name.endswith(".highlight"):
                count += 1
                if count % 500 == 0:
                    print count
                f = open(in_dir+file_name).readlines()
                for i in range(len(f)):
                    sen = word_tokenize(f[i].decode('utf-8'))
                    avg_sen_s += 1
                    avg_len_s += len(sen)
                    # print sen
                    # print len(sen)

        avg_len_s /= count
        avg_sen_s /= count

        fo = open("../stories/"+source+"_stat_final.txt", "w")
        fo.write("avg_len = " + str(avg_len) + "\n")
        fo.write("avg_sen = " + str(avg_sen) + "\n")
        fo.write("avg_para = " + str(avg_para) + "\n")
        fo.write("avg_len_s = " + str(avg_len_s) + "\n")
        fo.write("avg_sen_s = " + str(avg_sen_s) + "\n")
