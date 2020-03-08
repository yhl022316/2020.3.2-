def sum01(s1,s2):
    a=list(s1)
    b=list(s2)
    pos1=0
    flag=True
    while flag and pos1<(len(s1)):
        pos2=0
        found=False
        while pos2<(len(s2)):
            if a[pos1]==b[pos2]:
                found=True
            else:
                pos2=pos2+1
        if found:
            b[s2]=None
            pos1=pos1+1
        else:
            flag=False
    return flag
print(sum01('yyyy','yyyy'))








def sum02(s1,s2):
    a1=[0]*26
    b1=[0]*26

    for i in range(len(s1)):
        pos=ord(s1[i])-ord('a')
        a1[pos]=a1[pos]+1
    for i in range(len(s2)):
        pos=ord(s2[i])-ord('a')
        b1[pos]=b1[pos]+1

    count=0
    flag=True
    while count<26 and flag:
        if a1[count]==b1[count]:
            count=count+1
        else:
            flag=False
    return flag
print(sum02('yuyuyu','huhuhu'))



def sum03(s1,s2):
    alist1=list(s1)
    alist2=list(s2)

    alist1.sort()
    alist2.sort()
    flag = True
    pos=0
    while pos<len(s1) and flag:
        if alist1[pos]==alist2[pos]:
            pos=pos+1
        else:
            flag=False
    return flag
print(sum03('hhhh','hhhh'))

