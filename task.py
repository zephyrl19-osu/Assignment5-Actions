def firstrun():
    return "success"


def computecirclearea(radius):
    return radius * radius * 3.14159


def firstandlast(inputlist):
    return inputlist[0], inputlist[len(inputlist) - 1]


def timebetweendates(date1, date2):
    # date input formate MMDDYYYY
    daydiff = 0
    day1 = int(date1[1])
    day2 = int(date2[1])
    month1 = int(date1[0])
    month2 = int(date2[0])
    monthdays = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    year1 = int(date1[2])
    year2 = int(date2[2])
    isleapyear = False
    if (year1 % 4) == 0:
        isleapyear = True
        if (year1 % 100) == 0:
            isleapyear = False
            if (year1 % 400) == 0:
                isleapyear = True
    if year1 == year2:
        if isleapyear:
            monthdays[1] = 29

    if year1 == year2:
        if month1 == month2:
            daydiff = day2 - day1
        if month1 != month2:
            for x in range(month1, month2):
                daydiff = daydiff + monthdays[x]
            daydiff = daydiff - (monthdays[month1] - day1)
            daydiff = daydiff - (monthdays[month2] - day2)
    if year1 != year2:
        if month1 == month2:
            daydiff = (365 * (year2 - year1)) + (day2 - day1)
        if month1 != month2:
            for x in range(month1, month2):
                daydiff = daydiff + monthdays[x]
            daydiff = daydiff - (monthdays[month1] - day1)
            daydiff = daydiff - (monthdays[month2] - day2)
            daydiff = daydiff + (365 * (year2 - year1))
    return daydiff
