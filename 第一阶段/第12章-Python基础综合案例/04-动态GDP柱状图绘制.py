from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

# 读取数据
f = open("D:/Resources/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding="GB2312")
data_lines = f.readlines()

# 关闭文件
f.close()

# 删除第一行数据
data_lines.pop(0)

# 将数据转换为字典存储，格式为：
# {年份：[[国家GPD]，[国家GPD]，....]，年份：[[国家GPD]，[国家GPD]，....]，....}
data_dict = {}
for line in data_lines:
     year = int(line.split(",")[0])   # 年份
     country = line.split(",")[1]     # 国家
     gdp = float(line.split(",")[2])  # gdp数据
     # 如何判断字典里面有没有指定的key？
     try:
         data_dict[year].append([country, gdp])
     except KeyError:
         data_dict[year] = []
         data_dict[year].append([country, gdp])

# 创建一个时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})

# 排序年份
sorted_year = sorted(data_dict.keys())
for year in sorted_year:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前八的国家
    yea_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gad in yea_data:
        x_data.append(country_gad[0]) # x轴添加国家
        y_data.append(country_gad[1] / 100000000) # y轴添加gdp

    # 构建柱状图对象
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴y轴
    bar.reversal_axis()

    # 设置每一年图标的的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前8GDP数据"),
    )
    # timeline对象添加bar柱状图，添加时间线
    timeline.add(bar, str(year))

# 自动播放设置
timeline.add_schema(
    play_interval=1000, # 自动播放时间，单位毫秒
    is_timeline_show=True, # 是否在自动播放时候，显示时间线
    is_auto_play=True, # 是否自动播放
    is_loop_play=False, # 是否循环自动播放
)

# 绘图
timeline.render("1960-2019年全球GDP前8国家.html")