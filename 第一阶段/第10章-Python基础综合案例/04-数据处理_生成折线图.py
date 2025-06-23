import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 处理数据
f_us = open("D:/Download/可视化案例数据/折线图数据/美国.txt","r",encoding="utf-8")
f_jp = open("D:/Download/可视化案例数据/折线图数据/日本.txt","r",encoding="utf-8")
f_in = open("D:/Download/可视化案例数据/折线图数据/印度.txt","r",encoding="utf-8")
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()

# 去掉不合json规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(","")
jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
in_data = in_data.replace("jsonp_1629350745930_63180(","")

# 去掉不合json规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# json转Python
us_dict = json.loads(us_data)
jp_data = json.loads(jp_data)
in_data = json.loads(in_data)

# 获得trend key
us_trend_data = us_dict['data'][0]["trend"]
jp_trend_data = jp_data['data'][0]["trend"]
in_trend_data = in_data['data'][0]["trend"]

# 获得日期数据，用于x轴，取2020年
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获得日期数据，用于y轴，取2020年
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图标
line = Line()
# 添加x轴数据
line.add_xaxis(us_x_data) # x轴是公用的只用一个数据即可
# 添加y轴数据
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LegendOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LegendOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LegendOpts(is_show=False))
# 设置全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图",pos_left="center",pos_bottom="1%")
)

# 调用render方法生成图像
line.render()
# 关闭文件
f_us.close()
f_jp.close()
f_in.close()