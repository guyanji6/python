import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # for index,column in enumerate(header_row):
    #     print(index,column)
    # print(header_row)
    highs = []
    dates = []
    lows = []
    for row in reader:
        try:
            low = int(row[3])
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
        except ValueError:
            print(current_date,'mising data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # print(highs)
plt.plot(dates, highs,c='red',alpha=0.6)
plt.plot(dates, lows,c='blue',alpha=0.6)
plt.title('daliy high and low temperate',fontsize=24)
plt.fill_between(dates,highs,lows,alpha=0.2)
plt.ylabel('temperate')
plt.show()
