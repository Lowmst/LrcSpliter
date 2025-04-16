import os
import re
print('准备运行')
os.system('pause')
pattern = '(?<=\\S)\\s\\s(?=\\S)'
lrcfilelist = os.listdir('file')
for i, item in enumerate(lrcfilelist):
    lrcfilelist[i] = 'file/' + lrcfilelist[i]
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