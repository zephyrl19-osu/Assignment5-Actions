def firstrun():
    return "success"


def computecirclearea(radius):
    return radius * radius * 3.14159


def firstandlast(inputlist):
    return inputlist[0], inputlist[len(inputlist) - 1]


def timedates(date1, date2):
    # date input formate MMDDYYYY
    daydiff = 0
    monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if date1[2] == date2[2]:
        if date1[0] == date2[0]:
            daydiff = (date2[1] - date1[1])
    if date1[2] != date2[2]:
        daydiff = 365 * (date2[2] - date1[2])

    return daydiff
