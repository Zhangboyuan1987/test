import time
flag = 0
w =open('test.csv','r+',encoding='utf-8')
for d in w:
    dat = d.split(",")
    print(dat[0],dat[1],dat[2],dat[3])


    li = []
    f =open('ef1-a.txt','r+',encoding='utf-8')
    for i in f:
            li.append(i)
    # print(li)

    count = 0
    for s in li:
        # print(s,type(s))
        if s.lstrip(">").startswith(dat[0]):
            f = open('ef1-a_1.txt', 'a+', encoding='utf-8')
            f.write(s)
            flag = 1
            # print(5)
            # time.sleep(2)
            if count == len(li)-1:
                break
            else:
                f.write(li[count + 1].rstrip("\n"))
                f.write("\n")
            f.close()
        count+=1
    f.close()

    if flag==1:
        count = 0
        li = []
        f =open('rpb1.txt','r+',encoding='utf-8')
        for i in f:
            li.append(i)
        for s in li:
             # print(s,type(s))
            if s.lstrip(">").startswith(dat[1]):
                f_nei = open('ef1-a_1.txt', 'a+', encoding='utf-8')
                if count == len(li)-1:
                    break
                else:
                    f_nei.write(li[count + 1])
                    f_nei.write("\n")
                f_nei.close()
            count+=1
        f.close()
        flag=0

     # ifflag1
     #    count = 0
     #    f = open('rpb2.txt','r+',encoding='utf-8')
     #    for i in f:
     #        li.append(i)
     #    for s in li:
     #        print(s,type(s))
     #        if s.lstrip(">").startswith(dat[2]):
     #            f = open('ef1-a_1.txt', 'a+', encoding='utf-8')
     #            if count == len(li)-1:
     #                pass
     #            else:
     #                f.write(li[count + 1].rstrip("\n"))
     #            f.close()
     #        count+=1
     #    f.close()

    # count = 0
    # f=open('its.txt','r+',encoding='utf-8')
    # for i in f:
    #     li.append(i)
    # for s in li:
    #     print(s,type(s))
    #     if s.lstrip(">").startswith(dat[3]):
    #         f = open('ef1-a_1.txt', 'a+', encoding='utf-8')
    #         if count == len(li)-1:
    #             pass
    #         else:
    #             f.write(li[count + 1])
    #         f.close()
    #     count+=1
    # f.close()
# w.close()
