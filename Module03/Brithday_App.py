import datetime
# Creates divider for program


def header():
    print('---------------------------')
    print('   BIRTHDAY APP            ')
    print('---------------------------')
    print()
# Asks user for their birthday


def day_of_birth():
    print('Please enter the day ou were born mm/dd/yyyy')
    month = int(input("Month: "))
    day = int(input("Day: "))
    year = int(input("Year: "))
    birth = datetime.date(year, month, day)
    return birth
# Calculates the number of days from the current day until the user's birthday


def days_btwn_dates(ini_date, end_date):
    this_year = datetime.date(end_date.year, ini_date.month, ini_date.day)
    time_until = this_year - end_date
    return time_until.days
# Outputs a message to the user depending on the time from the current date to his/her birthday


def birthday_info(days):
    if days < 0:
        print('Your birthday was %i days ago.' % days)
    elif days > 0:
        print('Your birthday is in %i days from now.' % days)
    else:
        print('HAPPY BIRTHDAY')


def main():
    header()
    birthday = day_of_birth()
    now = datetime.date.today()
    days_btwn = days_btwn_dates(birthday, now)
    birthday_info(days_btwn)


main()