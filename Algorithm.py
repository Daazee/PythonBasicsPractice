def reFormatDate(dates):
    for date in dates:
        dateDetails=date.split()
        dayPosition=dateDetails[0]
        monthName = dateDetails[1]
        year=dateDetails[2]
        if(len(dayPosition)==4):
            day = dayPosition[0:2]
        else:
             day = "0"+dayPosition[0:1]
        month="00"
        if(monthName=="Jan"):
            month="01"
        elif(monthName=="Feb"):
            month="02"
        elif(monthName=="Mar"):
            month="03"
        elif(monthName=="Apr"):
            month="04"
        elif(monthName=="May"):
            month="05"
        elif(monthName=="Jun"):
            month="06"
        elif(monthName=="Jul"):
            month="07"
        elif(monthName=="Aug"):
            month="09"
        elif(monthName=="Oct"):
            month="10"
        elif(monthName=="Nov"):
            month="11"
        elif(monthName=="Dec"):
            month="12"

        result=year + "-" + month + "-" + day
        print(result)




dates = ['20th Oct 2052', '3rd Nov 1999']
reFormatDate(dates)