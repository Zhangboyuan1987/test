def document(name):
    document_li = []
    document_f = open(name, 'r+', encoding='utf-8')
    for i in document_f:
        document_li.append(i)
    return document_li
def document_judge(name,dat):
    document_judge_li = document(name)
    #匹配是否有对应值，
    for s in document_judge_li:
        if (s.lstrip(">").startswith(dat)):
            flag = 1
            return flag
        else:
            flag = 0
    return flag
text =open('test.csv','r+',encoding='utf-8')
number = 1
for d in text:
    txt = d.split(",")
    if(document_judge('ef1-a.txt',txt[0])): #ef1为真
        count = 0
        ef1_li = document('ef1-a.txt')
        for s in ef1_li:#ef1有匹配值且执行
            if s.lstrip(">").startswith(txt[0]):
                ef1 = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                ef1.write(s)
                if count == len(ef1_li)-1:
                    break
                else:
                    ef1.write(ef1_li[count + 1].rstrip("\n"))
                ef1.close()
            count+=1
        if(document_judge('rpb1.txt',txt[1])):#ef1为真rpb1为真
            count = 0
            rpb1_li = document('rpb1.txt')
            for s in rpb1_li:#rpb1有匹配值且执行
                if s.lstrip(">").startswith(txt[1]):
                    rpb1 = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                    if count == len(rpb1_li)-1:
                        break
                    else:
                        rpb1.write(rpb1_li[count + 1].rstrip("\n"))
                        rpb1.close()
                count+=1
            if (document_judge('rpb2.txt', txt[2])):#ef1为真rpb1为真rpb2为真
                count = 0
                rpb2_li = document('rpb2.txt')
                for s in rpb2_li:  # rpb1有匹配值且执行
                    if s.lstrip(">").startswith(txt[2]):
                        rpb2 = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                        if count == len(rpb2_li) - 1:
                            break
                        else:
                            rpb2.write(rpb2_li[count + 1].rstrip("\n"))
                            rpb2.close()
                    count += 1
                if (document_judge('its.txt', txt[3])): #ef1为真rpb1为真rpb2为真its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                       #ef1为真rpb1为真rpb2为真its为假
                    pass
            else:                                       #ef1为真rpb1为真rpb2为假
                if (document_judge('its.txt', txt[3])): #ef1为真rpb1为真rpb2为假its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                       #ef1为真rpb1为真rpb2为假its为假
                    pass
        else:                                     #ef1为真rpb1为假
            if (document_judge('rpb2.txt', txt[2])):#ef1为真rpb1为假rpb2为真
                count = 0
                rpb2_li = document('rpb2.txt')
                for s in rpb2_li:  # rpb1有匹配值且执行
                    if s.lstrip(">").startswith(txt[2]):
                        rpb2 = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                        if count == len(rpb2_li) - 1:
                            break
                        else:
                            rpb2.write(rpb2_li[count + 1].rstrip("\n"))
                            rpb2.close()
                    count += 1
                if (document_judge('its.txt', txt[3])):  #ef1为真rpb1为假rpb2为真its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                        #ef1为真rpb1为假rpb2为真its为假
                    pass
            else:                                       #ef1为真rpb1为假rpb2为假
                if (document_judge('its.txt', txt[3])): #ef1为真rpb1为假rpb2为假its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('ef1-a_new_%s.txt' %number, 'a+', encoding='utf-8')
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                       #ef1为真rpb1为假rpb2为假its为假
                    pass
    else:                                      #ef1为假
        if (document_judge('rpb1.txt', txt[1])):  # ef1为假的rpb1为真
            count = 0
            rpb1_li = document('rpb1.txt')
            for s in rpb1_li:  # rpb1有匹配值且执行
                if s.lstrip(">").startswith(txt[1]):
                    rpb1 = open('rpb1_new_%s.txt' %number, 'a+', encoding='utf-8')
                    rpb1.write(s)
                    if count == len(rpb1_li) - 1:
                        break
                    else:
                        rpb1.write(rpb1_li[count + 1].rstrip("\n"))
                        rpb1.close()
                count += 1
            if (document_judge('rpb2.txt', txt[2])):  # ef1为假的rpb1为真rpb2为真
                count = 0
                rpb2_li = document('rpb2.txt')
                for s in rpb2_li:  # rpb1有匹配值且执行
                    if s.lstrip(">").startswith(txt[2]):
                        rpb2 = open('rpb1_new_%s.txt' %number, 'a+', encoding='utf-8')
                        if count == len(rpb2_li) - 1:
                            break
                        else:
                            rpb2.write(rpb2_li[count + 1].rstrip("\n"))
                            rpb2.close()
                    count += 1
                if (document_judge('its.txt', txt[3])):  # ef1为假rpb1为真rpb2为真its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('rpb1_new_%s.txt' %number, 'a+', encoding='utf-8')
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                       # ef1为假rpb1为真rpb2为真its为假
                    pass
            else:                                         # ef1为假的rpb1为真rpb2为假
                if (document_judge('its.txt', txt[3])):  # ef1为假rpb1为真rpb2为假its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('rpb1_new_%s.txt' %number, 'a+', encoding='utf-8')
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                       # ef1为假rpb1为真rpb2为假its为假
                    pass
        else:                                          # ef1为假rpb1为假
            if (document_judge('rpb2.txt', txt[2])):  # ef1为假rpb1为假rpb2为真
                count = 0
                rpb2_li = document('rpb2.txt')
                for s in rpb2_li:  # rpb1有匹配值且执行
                    if s.lstrip(">").startswith(txt[2]):
                        rpb2 = open('rpb2_new_%s.txt' %number, 'a+', encoding='utf-8')
                        rpb2.write(s)
                        if count == len(rpb2_li) - 1:
                            break
                        else:
                            rpb2.write(rpb2_li[count + 1].rstrip("\n"))
                            rpb2.close()
                    count += 1
                if (document_judge('its.txt', txt[3])):  # ef1为假rpb1为假rpb2为真its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('rpb2_new_%s.txt' %number, 'a+', encoding='utf-8')
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                         # ef1为假rpb1为假rpb2为真its为假
                    pass
            else:                                         # ef1为假rpb1为假rpb2为假
                if (document_judge('its.txt', txt[3])):  # ef1为假rpb1为假rpb2为假its为真
                    count = 0
                    its_li = document('its.txt')
                    for s in its_li:  # its有匹配值且执行
                        if s.lstrip(">").startswith(txt[3]):
                            its = open('its_new_%s.txt' %number, 'a+', encoding='utf-8')
                            its.write(s)
                            if count == len(its_li) - 1:
                                break
                            else:
                                its.write(its_li[count + 1].rstrip("\n"))
                                its.close()
                        count += 1
                else:                                       # ef1为假rpb1为假rpb2为假its为假
                    pass
    number+=1
text.close()
