import random as rand
from datetime import date
from array import array

l = 10
years = [rand.randint(date.today().year - 5, date.today().year) for y in range(l)]
months = [rand.randint(1, 12) for m in range(l)]
days = []
for i in range(l):
    if months[i] in [1, 3, 5, 7, 8, 10, 12]:
        days.append(rand.randint(1, 31))
    elif months[i] in [4, 6, 9, 11]:
        days.append(rand.randint(1, 30))
    elif months[i] == 2 and years[i] % 4 == 0:
        days.append(rand.randint(1, 29))
    else:
        days.append(rand.randint(1, 28))

dates = [date(years[i], months[i], days[i]) for i in range(l)]

datearray = array('i', [])
for dt in dates:
    datearray.append(dt.toordinal())

for i in range(l - 1):
    print(f"Разница между {dates[i]} и {dates[i + 1]}: {abs(datearray[i + 1] - datearray[i])} дней")