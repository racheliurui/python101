# Just For fun
# http://news.sina.com.cn/s/wh/2018-03-02/doc-ifyrztfz6281140.shtml
# ['B', 'C', 'A', 'C', 'A', 'C', 'D', 'A', 'B', 'A']
# find the asnwer after 0.330770015717 second
# exit after 0.85631608963second
#

import  time
def assertQ1(answserList):

    return True

# answer of question 5 is A.C B.D C.A D.B
def assertQ2(answserList):


    if answserList[1]=="A" and answserList[4]=="C":
        return True
    if answserList[1] == "B" and answserList[4] == "D":
        return True
    if answserList[1] == "C" and answserList[4] == "A":
        return True
    if answserList[1] == "D" and answserList[4] == "B":
        return True
    return False


# which answer is different with rest three A.3 B.6 C.2 D.4
def assertQ3(answers):
    if answers[2]=="A" and answers[2]!=answers[5] and answers[2]!=answers[1] and answers[2]!=answers[3] :
        return True
    if answers[2] == "B" and answers[5]!=answers[2] and answers[5]!=answers[1] and answers[5]!=answers[3] :
        return True
    if answers[2] == "C" and answers[1]!=answers[5] and answers[1]!=answers[2] and answers[1]!=answers[3] :
        return True
    if answers[2] == "D" and answers[3]!=answers[5] and answers[3]!=answers[1] and answers[3]!=answers[2] :
        return True
    return False


# which 2 answers are the same: A.1,5 (0,4) B.2,7 (1,6) C.1, 9 (0,8) D. 6,10 (5,9)
def assertQ4(answers):

    if answers[3]=="A" and answers[0]==answers[4]:
        return True
    if answers[3] == "B" and answers[1]==answers[6]:
        return True
    if answers[3] == "C" and answers[0]==answers[8]:
        return True
    if answers[3] == "D" and answers[5]==answers[9]:
        return True
    return False


# which answer are the same with current : A 8 B 4 C 9 D 7
def assertQ5(answers):

    if answers[4]=="A" and answers[7]=="A":
        return True
    if answers[4] == "B" and answers[3]=="B":
        return True
    if answers[4] == "C" and answers[8]=="C":
        return True
    if answers[4] == "D" and answers[6]=="D":
        return True
    return False

# which 2 have same answer with q8 : A2,4(1,3) B. 1,6,(0,5) C. 3,10 (2,9) D.5,9 (4,8)
def assertQ6 (answers):

    if answers[5]=="A" and answers[7]==answers[1]==answers[3]:
        return True
    if answers[5]=="B" and answers[7]==answers[0]==answers[5]:
        return True
    if answers[5]=="C" and answers[7]==answers[2]==answers[9]:
        return True
    if answers[5]=="D" and answers[7]==answers[4]==answers[8]:
        return True
    return False

# which answser has least number of chosen among all 10 questions A. C, B. B, C. A, D. D
def assertQ7 (answers):


    minChosenCountA = answers.count("A")
    minChosenCountB = answers.count("B")
    minChosenCountC = answers.count("C")
    minChosenCountD = answers.count("D")
    minChosen = "A"
    minChosenCount=minChosenCountA
    if minChosenCountB<minChosenCount:
        minChosen="B"
        minChosenCount=minChosenCountB
    if minChosenCountC<minChosenCount:
        minChosen="C"
        minChosenCount=minChosenCountC
    if minChosenCountD<minChosenCount:
        minChosen="D"
        minChosenCount=minChosenCountD

    if answers[6]=="A" and minChosen=="C":
        return True
    if answers[6]=="B" and minChosen=="B":
        return True
    if answers[6]=="C" and minChosen=="A":
        return True
    if answers[6]=="D" and minChosen=="D":
        return True
    return False




def isNotAdjasent(a1,a2):
    dic = {"A": 1, "B": 2, "C": 3, "D": 4}
    if (dic.get(a1)-dic.get(a2))==1 or (dic.get(a2)-dic.get(a1))==1:
        return False
    return True

# which answser is not adjasent with question1 A7,B5,C2,D10
def assertQ8 (answers):
    if answers[7]=="A" and isNotAdjasent(answers[0],answers[6]):
        return True
    if answers[7]=="B" and isNotAdjasent(answers[0],answers[4]):
        return True
    if answers[7]=="C" and isNotAdjasent(answers[0],answers[1]):
        return True
    if answers[7]=="D" and isNotAdjasent(answers[0],answers[9]):
        return True
    return False

# "q1 == q6" and "x==q5" is opersite , then x is A 6,B 10,C 2,D 9
def assertQ9 (answers):
    expected= not (answers[0]==answers[5])
    if answers[8]=="A" and expected==(answers[4]==answers[5]):
        return True
    if answers[8]=="B" and expected==(answers[4]==answers[9]):
        return True
    if answers[8]=="C" and expected==(answers[4]==answers[1]):
        return True
    if answers[8]=="D" and expected==(answers[4]==answers[8]):
        return True
    return False


# max num of chosen - min num of chosen A 3,  B 2,C 4, D1
def assertQ10 (answers):
    countA = answers.count("A")
    countB = answers.count("B")
    countC = answers.count("C")
    countD = answers.count("D")
    gap=max(countA,countB,countC,countD)-min(countA,countB,countC,countD)

    if answers[9]=="A" and gap==3:
        return True
    if answers[9]=="B" and gap==2:
        return True
    if answers[9]=="C" and gap==4:
        return True
    if answers[9]=="D" and gap==1:
        return True
    return False


def assertAnswers(answers):
    return assertQ1(answers) and assertQ2(answers) and assertQ3(answers) and assertQ4(answers) and assertQ5(answers) and assertQ6(answers) and assertQ7(answers) and assertQ8(answers) and assertQ9(answers) and assertQ10(answers)

starttime=time.time()


selects = "ABCD"
currentAns=["Z","Z","Z","Z","Z","Z","Z","Z","Z","Z"]

for sel1 in selects:    # print each character from ABCD
    currentAns[0]=sel1
    for sel2 in selects:
        currentAns[1]=sel2
        for sel3 in selects:
            currentAns[2] = sel3
            for sel4 in selects:
                currentAns[3] = sel4
                for sel5 in selects:
                    currentAns[4] = sel5
                    for sel6 in selects:
                        currentAns[5] = sel6
                        for sel7 in selects:
                            currentAns[6] = sel7
                            for sel8 in selects:
                                currentAns[7] = sel8
                                for sel9 in selects:
                                    currentAns[8] = sel9
                                    for sel10 in selects:
                                        currentAns[9] = sel10
                                        if assertAnswers(currentAns):
                                          print (currentAns)
                                          findanswer= str(time.time() - starttime)
                                          print("find the asnwer after " + findanswer+" second" )


exitTime= str(time.time() - starttime)
print("exit after " + exitTime + "second")