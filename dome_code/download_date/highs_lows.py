import csv
import matplotlib as mlp

mlp.use('TkAgg')
import matplotlib.pyplot as plt
from datetime import datetime

def read_file(filename,dates, highs,lows):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing data')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)


def draw_chart(dates, highs,lows):
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='green', alpha=0.1)


filename1 = "data/sitka_weather_2014.csv"
filename = "data/death_valley_2014.csv"
dates, highs, lows, dates1, highs1, lows1 = [], [], [], [], [], []
read_file(filename1, dates1, highs1,lows1)
read_file(filename,dates, highs,lows)


fig = plt.figure(dpi=128, figsize=(10, 6))
draw_chart(dates, highs,lows)
draw_chart(dates1, highs1,lows1)

# setting chart format
plt.title("Day high and low temperatures - 2014\nDeath Vallage, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=10)


plt.show()
