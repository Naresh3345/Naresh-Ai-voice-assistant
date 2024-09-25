import datetime

def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    return Time

def get_date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    date = day + "/" + month + "/" + year
    return date

def Wishing():
    h = datetime.datetime.now().hour
    if h >= 0 and h < 12:
        wish = "Good Morning"
    elif h >= 12 and h < 15:
        wish = "Good Afternoon"
    elif h >= 15 and h < 19:
        wish = "Good Evening"
    else:
        wish = "Good Night"
    return wish

if __name__ == "__main__":
    print("The Time is: ", get_time())
    print("The Date is: ", get_date())
    print(Wishing())
