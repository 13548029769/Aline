import json
import pygal
import math
from itertools import groupby


def draw_line(x_date, y_date, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_date, y_date)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, int(sum(y_list) / len(y_list))])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file('image/{} .svg'.format(title))
    return line_chart


filename = 'data/btc_close_2017.json'
with open(filename, 'r') as f:
    bct_data = json.load(f)

    dates = []
    months = []
    weeks = []
    weekdays = []
    close = []
    for bct_dic in bct_data:
        dates.append(bct_dic['date'])
        months.append(int(bct_dic['month']))
        weeks.append(int(bct_dic['week']))
        weekdays.append(bct_dic['weekday'])
        close.append(int(float(bct_dic['close'])))
        # print("{0[date]} is mouth {0[month]} week {0[week]}, {0[weekday]}, the close price is {0[close]} RMB".format(bct_dic))

# print(dates[::20])
line_chart = pygal.Line(x_label_rotation=20,show_minor_xlabels=False)
line_chart.title = '收盘价（¥）'
# line_chart.x_labels= dates
N = 20
# Can't achieve on mac os
line_chart._x_labels_major = dates[::N]
# close_log = [math.log(value,10) for value in close]
close_log = [math.log10(value) for value in close]
line_chart.add('收盘价',close_log)
line_chart.render_to_file('image/收盘价格折线图（¥）.svg')

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价格月日均值', '月日均值')

idx_week = dates.index('2017-12-01')
line_chart_month = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价格月日均值', '月日均值')

idx_week = dates.index('2017-12-11')
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekday = draw_line(weekdays_int,close[1:idx_week],'收盘价星期均值（¥）','星期均值')
line_chart_weekday.x_labels = ['周一','周二','周三','周四','周五','周六','周日']
line_chart_weekday.render_to_file('image/收盘价星期均值2（¥）.svg')

with open('收盘价Dsahboard.html','w',encoding='utf8') as html_file:
    html_file.write('<html><head><title>收盘价Dsahboard</title><meta'
                    'charset="utf8"></head><body>\n')
    for svg in [
        'image/收盘价格月日均值 .svg','image/收盘价格折线图（¥）.svg',
        'image/收盘价星期均值（¥） .svg','image/收盘价星期均值2（¥）.svg'
    ]:
        html_file.write('<object type="image/svg+xml" data ="{0}" height=500></object>\n'.format(svg))
        html_file.write('</body<html>')