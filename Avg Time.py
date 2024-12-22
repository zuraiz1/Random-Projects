for x in range(0,29,1) :
    totaltime = 0
    print(x) 
    print; "please enter time logged on and time logged off"
    timelogon=int(input("please enter time logged on"))
    timelogoff=int(input("please enter time logged off"))
    timelength= timelogoff - timelogon
    totaltime = totaltime + timelength
    avgtime = totaltime/30
    print("the average length of time per day is") 
    print(avgtime)