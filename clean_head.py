import os

def match(paras):
    # Then we have 4 kinds of timestamp
    # return delta

    ### Long
    if len(paras) > 6:
        if paras[6].startswith("UPDATED"):
            return 10
    if len(paras) > 7:
        if paras[7].startswith("UPDATED"):
            return 11

    if paras[0].startswith("PUBLISHED"):
        ### P | U
        if "UPDATED" in paras[0]:
            return 2
        ### Short
        elif "UPDATED" in paras[2]:
            return 4

    ### UPDATED
    if paras[0].startswith(("Last updated", "UPDATED")):
        return 2

    return 0

def op(paras):
    # return filtered paras

    if len(paras) < 3:
        return paras

    beginPoint = 0
    if paras[0].startswith(("by ", "By ")):
        beginPoint = 2
    if paras[2].startswith(("by ", "By ")) and not paras[2].endswith(".\n"):
        beginPoint = 4

    delta = match(paras[beginPoint:])
    return paras[beginPoint+delta:]


def clean_dm():
    count = 0
    in_dir = "../stories/cleaned_dm/"
    out_dir = "../stories/final_dm/"
    for file_name in os.listdir(in_dir):
        if file_name.endswith(".story"):
            count += 1

            if count % 500 == 0:
                print count

            f = open(in_dir+file_name).readlines()
            try:
                output = op(f)
            except IndexError as e:
                print file_name
                exit()
            fo = open(out_dir+file_name, "w")
            for i in range(len(output)):
                fo.write(output[i])

def clean_cnn():
    count = 0
    in_dir = "../stories/cleaned_cnn/"
    out_dir = "../stories/final_cnn/"
    for file_name in os.listdir(in_dir):
        if file_name.endswith(".story"):
            count += 1
            if count % 500 == 0:
                print count
            f = open(in_dir+file_name).readlines()
            fo = open(out_dir+file_name, "w")
            if "(CNN) -- " in f[0]:
                fo.write(f[0].split("(CNN) -- ")[1])
            else:
                fo.write(f[0])
            for i in range(1, len(f)):
                fo.write(f[i])

if __name__ == "__main__":
    clean_cnn()
