import datetime
import matplotlib.pyplot as plt


def count_bdate(bdate_list):
    ages = []
    curr_date = datetime.date.today()
    for i in bdate_list:
        tempd = i.split(sep='.')
        if int(curr_date.month) > int(tempd[1]):
            ages.append(int(curr_date.year) - int(tempd[2]))
        elif int(curr_date.month) == int(tempd[1]):
            if int(curr_date.day) > int(tempd[2]):
                ages.append(int(curr_date.year) - int(tempd[2]))
            else:
                ages.append(int(curr_date.year) - int(tempd[2]) - 1)
        elif int(curr_date.month) < int(tempd[1]):
            ages.append(int(curr_date.year) - int(tempd[2]) - 1)

    return ages


def makegist(ages_list):
    plt.hist(ages_list)
    plt.show()
