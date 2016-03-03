import os

if __name__ == "__main__":
    in_dir = "../stories/cleaned_cnn/"
    out_dir = "../stories/final_cnn/"
    for fileName in os.listdir(in_dir):
        print fileName
        if fileName.endswith(".story"):
            os.system("diff -u " + in_dir+fileName + " " + out_dir+fileName)
        raw_input()
