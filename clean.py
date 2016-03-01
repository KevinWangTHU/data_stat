import os

if __name__ == "__main__":
    dirs = os.listdir("../stories/")

    if "cleaned_dm" not in dirs:
        os.mkdir("../stories/cleaned_dm")
    if "cleaned_cnn" not in dirs:
        os.mkdir("../stories/cleaned_cnn")

    for source in ["dm", "cnn"]:
        in_dir = "../stories/stories_" + source + "/"
        out_dir = "../stories/cleaned_" + source + "/"
        count = 0
        for file_name in os.listdir(in_dir):
            if file_name.endswith(".story"):
                count += 1
                if count % 500 == 0:
                    print count
                f = open(in_dir + file_name).readlines()
                fo = open(out_dir + file_name, "w")
                output = []
                for i in range(len(f)):
                    if f[i] == '\n':
                        output.append(f[i])
                        continue
                    if f[i] == "@highlight\n":
                        break
                    if f[i+1] == '\n':
                        output.append(f[i])
                    else:
                        if f[i][-2] == ' ':
                            output.append(f[i][:-1])
                        else:
                            output.append(f[i][:-1]+' ')
                for i in range(len(output)):
                    fo.write(output[i])
