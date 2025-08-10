from urllib.parse import parse_qs
def test1():
    str1 = "pk_Id=0&secondName=%E8%BF%91%E6%9D%A5%E5%8F%AF%E5%A5%BD&userName=%E5%A4%A7%E5%B8%88%E5%82%85&phoneNumber=13688882277&warnSecondBalance=88&powers=101%2C104%2C102%2C110%2C109%2C1061%2C201%2C202%2C203%2C301%2C302%2C303%2C315%2C304%2C306%2C307%2C308%2C310%2C501%2C503%2C504%2C601%2C701&logoPhoto=&secondSysName=&transportNum=0&smsNumber=0&isSmS=1&isRelevance=1&exCompanyJson=%5B%5D&addUser=b5075cb063b941c186c6daaae08e1c2f&companyCode=c8e405c097a3463ba27ee83cadd9dce5"
    a=parse_qs(str1)
    print(a)
    dict1=dict([k,v[0] ] for k,v in a.items())
    print(dict1)