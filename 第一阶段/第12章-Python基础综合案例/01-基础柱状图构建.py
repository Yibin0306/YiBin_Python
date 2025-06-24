# 导包：导入Map功能构建地图对象
from pyecharts.charts import Bar
from pyecharts.options import *

# 构建柱状图对象
bar = Bar()

# 添加x轴数据
bar.add_xaxis(["中国","美国","英国"])

# 添加y轴数据
bar.add_yaxis("GDP",[30,20,10],label_opts=LabelOpts(position="right")) # 设置数值标签在右侧

# 反转x轴和y轴
bar.reversal_axis()

# 绘图
bar.render()