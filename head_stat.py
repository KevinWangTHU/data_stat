import os

if __name__ == "__main__":
    for source in ["dm"]: #, "cnn"]:
        count = 0
        prob_count = 0
        in_dir = "../stories/cleaned_" + source + "/"
        for file_name in os.listdir(in_dir):
            if file_name.endswith(".story"):
                count += 1
                f = open(in_dir+file_name).readlines()
                if len(f) < 3:
                    continue
                if f[2].startswith(("by ", "By ")) :#and not f[2].endswith(".\n"):
                    # print f[2], f[4]
                    #print "----"
                    prob_count += 1
                    #if prob_count > 50:
                    #    break
                    # print file_name

        print source
        print prob_count, count
        print "========================"
