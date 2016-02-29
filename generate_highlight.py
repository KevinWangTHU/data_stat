import os

if __name__ == "__main__":
    dirs = os.listdir("../stories/")
    if "highlights_dm" not in dirs:
        os.mkdir("../stories/highlights_dm")
    if "highlights_cnn" not in dirs:
        os.mkdir("../stories/highlights_cnn")

    for source in ["dm", "cnn"]:
        count = 0
        in_dir = "../stories/stories_" + source + "/"
        out_dir = "../stories/highlights_" + source + "/"
        for file_name in os.listdir(in_dir):
            if file_name.endswith(".story"):
                count += 1
                if count % 100 == 0:
                    print count
                f = open(in_dir + file_name).readlines()
                fo = open(out_dir + file_name.strip("story") + "highlight", 'w')
                highlights = []
                for i in range(len(f)):
                    if f[i] == "@highlight\n":
                        highlights.append(f[i+2])
                fo.writelines(highlights)
