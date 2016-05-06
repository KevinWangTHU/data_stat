import os

if __name__ == "__main__":
    for source in ["cnn", "dailymail"]:
        if "title" not in os.listdir("./"+source+"/"):
            os.mkdir("./"+source+"/source")
        fileList = os.listdir("./"+source+"/download")
        outDir = "./" + source + "/title/"
        count = 0
        for html in fileList:
            if html.endswith(".html"):
                count += 1
                if count % 500 == 0:
                    print count
                for line in open("./"+source+"/download/"+html).readlines():
                    if line.startswith("<title>") and line.endswith("</title>\n"):
                        outf = open(outDir + html.strip(".html") + ".txt", "w")
                        outf.write(line[7:-9])
                break
