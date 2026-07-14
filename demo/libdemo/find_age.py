from datetime import *
while True:
    dobstr = input("Enter your date of birth (yyyymmdd) [enter to stop]: ")
    if dobstr == "":
        break
    try:
        dob = datetime.strptime(dobstr, "%Y%m%d")
        now = datetime.now()
        diff = now - dob     # timedelta
        years = diff.days // 365
        months = diff.days % 365 // 30
        days = diff.days - (years * 365 + months * 30)
        print(f"{years} y {months} m {days} d")
    except:
        print(f"{dobstr} is not a valid date. Give it in yyyymmdd format")

datetime.datetime.now().date()