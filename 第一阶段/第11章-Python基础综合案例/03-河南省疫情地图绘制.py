import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取数据文件
f = open("D:/Resources/可视化案例数据/地图数据/疫情.txt","r",encoding="utf-8")
data = f.read()

# 关闭文件
f.close()

# 将字符串json转换为python文件
data_dict = json.loads(data)

# 从字典取出河南省份的数据
cities_data_list = data_dict["areaTree"][0]["children"][3]["children"]

# 组装每个省份和确诊人数为元组，并将各个省的数据都封装到列表中
data_list = []
for cities_data in cities_data_list:
    cities_name = cities_data["name"] # 市名称
    cities_name = cities_name + '市'
    cities_confirm = cities_data["total"]["confirm"] # 市人数
    data_list.append((cities_name, cities_confirm))
print(data_list)

# 构建地图
map = Map()
map.add("河南省确诊人数", data_list,'河南')

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="河南疫情图"),
    visualmap_opts=VisualMapOpts(
        is_show=True, # 是否显示
        is_piecewise=True, # 是否分段
        pieces=[
            {"min": "1", "max": "99", "label": "1~99人", "color": "#CCFFFF"},
            {"min": "100", "max": "999", "label": "100~999人", "color": "#FFFF99"},
            {"min": "1000", "max": "4999", "label": "1000~4999人", "color": "#FF9966"},
            {"min": "5000", "max": "9999", "label": "5000~9999人", "color": "#FF6666"},
            {"min": "10000", "max": "99999", "label": "10000~99999人", "color": "#CC3333"},
            {"min": "100000","label": "100000+", "color": "#990033"},
        ]
    )
)

# 绘图
map.render("河南疫情地图.html")