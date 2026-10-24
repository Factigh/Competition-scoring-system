
def control_input(text,lower):
    error=True
    while error:
        try:
            input1=int(input(text))
            while input1<lower:
                input1=int(input(text))
        except ValueError:
            print("Invalid entry.")
        else:
            error=False
    return input1

def createlist(row,column):
    newlist=[]
    for i in range(row):
        newlist.append([0]*column)
    return newlist

def controlcoach(coach,coachscore,choosenlist,contestant_num,coach_point_list):
    error=True
    while error:
        try:
            contestant=int(input(f"Which number of contestant {coach}.coach give the score {coachscore}? "))
            while contestant==coach or contestant<1 or contestant>contestant_num or contestant in choosenlist:
                contestant=int(input(f"Which number of contestant {coach}.coach give the score {coachscore}? "))
        except ValueError:
            print("Invalid Entry.")
        else:
            error=False
    
    coach_point_list[contestant-1][coach]+=coachscore
    return contestant,coach_point_list

def controlaudience(score,audience_choosenlist,contestant_num):
    error=True
    while error:
        try:
            contestant=int(input(f"Which number of contestant audience give the score {score}? "))
            while contestant<1 or contestant>contestant_num or contestant in audience_choosenlist:
                contestant=int(input(f"Which number of contestant audience give the score {score}? "))
        except ValueError:
            print("Invalid Entry.")
        else:
            error=False
    return contestant

def sortlist(listt,index,boolean):
    return sorted(listt, key=lambda x: x[index], reverse=boolean)

def table(listt,text,contestant_num):
    print(text)
    print("----  -------------  -----------  --------------  -----------")
    for i in range(contestant_num):
        print(f"{listt[i][0]:2d} {listt[i][1]:10d} {listt[i][2]:13d} {listt[i][3]:14d} {listt[i][4]:14d}")

def mini_table(listt,text,contestant_num):
    print(text)
    print("---- ------------- -----")
    for i in range(contestant_num):
        print(f"{listt[i][0]:2d} {listt[i][1]:9d} {listt[i][2]:10d}")

def table_champ(listt,text,contestant_num,weeks_num):
    print(text)
    print("Contestant No",end="  ")
    for i in range(1,weeks_num+1):
        print(f"Week-{i}",end="  ")
    print("Week Championships")
    print("-------------",end="  ")
    for i in range(weeks_num):
        print("------",end="  ")
    print("------------------")
    for i in range(contestant_num):
        print(f"{listt[i][0]}",end="          ")
        for j in range(1,weeks_num+1):
             print(f"{listt[i][j]:8d}",end="")
        print(f"{listt[i][weeks_num+1]:13d}")

def table_coach(listt,text,contestant_num):
    print(text)
    print("Contestant No",end="  ")
    for i in range(1,contestant_num+1):
        print(f"Coach-{i}",end="  ")
    print()
    print("-------------",end="  ")
    for i in range(contestant_num):
        print("-------",end="  ")
    print()
    for i in range(contestant_num):
        print(f"{listt[i][0]:7d}",end="   ")
        for j in range(1,contestant_num+1):
            if j==i+1:
                print("        -",end="")
            else:
                print(f"{listt[i][j]:9d}",end="")
        print()

def week_score(contestant_num,coach_point_list):
    list_week=createlist(contestant_num,5)
    for coach in range(1,contestant_num+1):
        choosenlist=[]
        for coachscore in range(1,4):
            contestant,coach_point_list=controlcoach(coach,coachscore,choosenlist,contestant_num,coach_point_list)
            choosenlist.append(contestant)
            list_week[contestant-1][2]+=coachscore
            list_week[contestant-1][4]+=coachscore
    audience_choosenlist=[]

    for score in range(1,4):
        contestant=controlaudience(score,audience_choosenlist,contestant_num)
        audience_score=score*(contestant_num-1)
        list_week[contestant-1][3]+=audience_score
        list_week[contestant-1][4]+=audience_score
        audience_choosenlist.append(contestant)

    for i in range(contestant_num):
        list_week[i][1]=i+1
        list_week[i][0]=i+1

    return list_week,coach_point_list

def weeksorted(contestant_num,weekresults):
    sorted_list_week=sortlist(weekresults,2,True)
    sorted_list_week=sortlist(sorted_list_week,4,True)

    for i in range(contestant_num):
        sorted_list_week[i][0]=i+1

    return sorted_list_week

def overall(list_total,contestant_num,weekresults):
    
    for i in range(contestant_num):
        list_total[i][1]=weekresults[i][1]
        list_total[i][2]+=weekresults[i][2]
        list_total[i][3]+=weekresults[i][3]
        list_total[i][4]+=weekresults[i][4]

    sorted_listtotal=sortlist(list_total,2,True)
    sorted_listtotal=sortlist(sorted_listtotal,4,True)

    for i in range(contestant_num):
        sorted_listtotal[i][0]=i+1
    return sorted_listtotal
    
def trioscore(contestant_num,list_total,index):
    triolist=createlist(contestant_num,3)
    for i in range(contestant_num):
        triolist[i][2]=list_total[i][index]
        triolist[i][1]=i+1
    triolist=sortlist(triolist,2,True)
    for i in range(contestant_num):
        triolist[i][0]=i+1

    return triolist

def maximum(champlist,weeks_num,contestant_num):
    for week in range(1,weeks_num+1):
        max_value=max(champlist, key=lambda x: x[week])[week]
        
        for i in range(contestant_num):
            if champlist[i][week]==max_value:
                champlist[i][weeks_num+1]+=1

    return champlist

def champs(champlist,contestant_num,weekresults,week):
    for i in range(contestant_num):
        champlist[i][0]=i+1
    
    for i in range(contestant_num):
        champlist[i][week]=weekresults[i][4]

    return champlist

def get_coach_point(contestant_num,coach_point_list):
    for i in range(contestant_num):
        coach_point_list[i][0]=i+1
        
def main():
    question="y"
    while question=="y" or question=="Y":
        contestant_num=control_input("Enter contestant number ",5)
        weeks_num=control_input("Enter number of weeks ",3)
        list_total=createlist(contestant_num,5)
        champlist=createlist(contestant_num,weeks_num+2)
        coach_point_list=createlist(contestant_num,contestant_num+1)

        for week in range(1,weeks_num+1):
            weekresults,coach_point_list=week_score(contestant_num,coach_point_list)
            scorelist=weeksorted(contestant_num,weekresults)
            text=f"Scoring results for week-{week}:\nRank  Contestant No  Coach Score  Audience Score  Total Score"
            table(scorelist,text,contestant_num)
            overallist=overall(list_total,contestant_num,weekresults)
            text1=f"Overall standings at the end of week-{week}:\nRank  Contestant No  Coach Score  Audience Score  Total Score"
            table(overallist,text1,contestant_num)
            champlist=champs(champlist,contestant_num,weekresults,week)

        champlist=maximum(champlist,weeks_num,contestant_num)
        coachlist=trioscore(contestant_num,list_total,2)
        textcoach="Overall standings based on the coaches' scores only:\nRank Contestant No Score"
        mini_table(coachlist,textcoach,contestant_num)
        audiencelist=trioscore(contestant_num,list_total,3)
        textaudience="Overall standings based on the audience scores only:\nRank Contestant No Score"
        mini_table(audiencelist,textaudience,contestant_num)
        textchamps="Total scores for each week and the number of week championships of the contestants:"
        table_champ(champlist,textchamps,contestant_num,weeks_num)
        get_coach_point(contestant_num,coach_point_list)
        textcoachtotal="Total scores received by the contestants from the coaches:"
        table_coach(coach_point_list,textcoachtotal,contestant_num)
        question=input("Would you like to organize a new competition? (y/Y/n/N) ")
        while question!="y" and question!="Y" and question!="n" and question!="N":
            question=input("Invalid entry. Would you like to organize a new competition? (y/Y/n/N) ")

main()