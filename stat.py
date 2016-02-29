import os


if __name__ == "__main__":

    for source in ["dm", "cnn"]:
        avg_para = 0
        avg_sen = 0
        avg_len = 0
        avg_sen_s = 0
        avg_len_s = 0

        in_dir = "../stories/stories_" + source + "/"
        count = 0
        for file_name in os.listdir(in_dir):
            if file_name.endswith(".story"):
                count += 1
                f = open(in_dir + file_name).readlines()
                for i in range(len(f)):
                    para = f[i].split(" ")
                    if para == ["@highlight\n"]:
                        break
                    if para == ['\n']:
                        continue
                    avg_para += 1
                    avg_len += len(para)
                    # print para
                    # print len(para)

                    para = f[i].split(".")
                    avg_sen += len(para) - 1
                    # print para
                    # print len(para) - 1

        avg_para /= count
        avg_len /= count
        avg_sen /= count

        in_dir = "../stories/highlights_" + source + "/"
        count = 0
        for file_name in os.listdir(in_dir):
            if file_name.endswith(".highlight"):
                count += 1
                f = open(in_dir+file_name).readlines()
                for i in range(len(f)):
                    sen = f[i].split(" ")
                    avg_sen_s += 1
                    avg_len_s += len(sen)

        avg_len_s /= count
        avg_sen_s /= count

        fo = open("../stories/"+source+"_stat.txt", "w")
        fo.write("avg_len = " + str(avg_len) + "\n")
        fo.write("avg_sen = " + str(avg_sen) + "\n")
        fo.write("avg_para = " + str(avg_para) + "\n")
        fo.write("avg_len_s = " + str(avg_len_s) + "\n")
        fo.write("avg_sen_s = " + str(avg_sen_s) + "\n")




