import os
lrcfilelist=os.listdir("file")
for i,item in enumerate(lrcfilelist):
    lrcfilelist[i]="file/"+lrcfilelist[i]
for lrcfile in lrcfilelist:
    finallist=list()
    with open(lrcfile,mode="r",encoding="UTF-8") as lrc:
        lrclist=lrc.readlines()
        for i,item in enumerate(lrclist):
            lrclist[i]=lrclist[i].strip()
        for lrcline in lrclist:
            lrcpart=lrcline.split("  ")
            lrctime=lrcpart[0][:10]
            if len(lrcpart)>2:
                lrctrans=lrcpart[-1]
                lrcpart=lrcpart[:-1]
                lrcpartoring="".join(lrcpart)
                lrcpart.clear()
                lrcpart=[lrcpartoring,lrctrans]
            for i,item in enumerate(lrcpart):
                lrcpart[i]=lrcpart[i].strip(lrctime)
                lrcpart[i]=lrctime+lrcpart[i] 
            finallist+=lrcpart

    with open(lrcfile,mode="w+",encoding="UTF-8") as final:
        for i in finallist:
            final.write(i)
            final.write("\n")