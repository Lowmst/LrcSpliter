import os
import re
def readfile(pos,end):
    relist=[]
    filelist=os.listdir(pos)
    for i,item in enumerate(filelist):
        if filelist[i].endswith(end) == True:
            relist.append(filelist[i])
    return relist
    # print(relist)
lrcfilelist=readfile("file",".lrc")
print("准备运行")
os.system("pause")
pattern=r'(?<=\S)\s\s(?=\S)'
# readfile()
for i,item in enumerate(lrcfilelist):
    lrcfilelist[i]="file/"+lrcfilelist[i]
for lrcfile in lrcfilelist:
    finallist=list()
    with open(lrcfile,mode="r",encoding="UTF-8") as lrc:
        lrclist=lrc.readlines()
        for i,item in enumerate(lrclist):
            lrclist[i]=lrclist[i].strip()
        for lrcline in lrclist:
            lrcpart=re.split(pattern,lrcline)
            lrctime=lrcpart[0][:10]
            for i,item in enumerate(lrcpart):
                lrcpart[i]=lrcpart[i].strip(lrctime)
                lrcpart[i]=lrctime+lrcpart[i] 
            finallist+=lrcpart
        print(finallist)
    with open(lrcfile,mode="w+",encoding="UTF-8") as final:
        for i in finallist:
            final.write(i)
            final.write("\n")
print("完成")
os.system("pause")