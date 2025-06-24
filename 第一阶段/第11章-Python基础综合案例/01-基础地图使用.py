# 导包：导入Map功能构建地图对象
from cProfile import label

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

# 准备地图对象
map = Map()

# 准备数据
data = [
    ("北京市",99),
    ("上海市",199),
    ("湖南省",299),
    ("河南省",10),
    ("台湾省",99),
    ("四川省",499),
    ("湖北省",56)
]
print(data)
# 添加数据
map.add("测试地图", data,"china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": "1","max": "9","label":"1-9","color":"#CCFFFF"},
            {"min": "10","max": "99","label":"10-99","color":"#FF6666"},
            {"min": "100","max": "999","label":"100-999","color":"#990033"}
        ]
    )
)

# 绘图
map.render()
