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

# 从字典取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]

# 组装每个省份和确诊人数为元组，并将各个省的数据都封装到列表中
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"] # 省份名称
    if province_name in '北京上海重庆天津':
        province_name = province_name + '市'
    elif province_name in '内蒙古壮族西藏回族':
        province_name = province_name + '自治区'
    elif province_name in '新疆':
        province_name = province_name + '维吾尔自治区'
    elif province_name in '广西':
        province_name = province_name + '壮族自治区'
    elif province_name in '宁夏':
        province_name = province_name + '回族自治区'
    elif province_name in '澳门香港':
        province_name = province_name + '特别行政区'
    else:
        province_name = province_name + '省'
    province_confirm = province_data["total"]["confirm"] # 省份人数
    data_list.append((province_name, province_confirm))

# 构建地图
map = Map()
map.add("各省份确诊人数", data_list,"china")

# 设置全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情图"),
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
map.render("全国疫情地图.html")