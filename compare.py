import os

if __name__ == "__main__":
    in_dir = "../stories/cleaned_dm/"
    out_dir = "../stories/cleaneded_dm/"
    for fileName in os.listdir(in_dir):
        print fileName
        if fileName.endswith(".story"):
            os.system("diff -u " + in_dir+fileName + " " + out_dir+fileName)
        raw_input()
