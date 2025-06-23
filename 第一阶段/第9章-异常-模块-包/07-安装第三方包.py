"""
在Python程序的生态中，有许多非常多的第三方包（非Python官方），可以极大的帮助我们提高开发效率，如：
·科学计算中常用的：numpy包
·数据分析中常用的：pandas包
·大数据计算中常用的：pyspark、apache-flink包
·图形可视化常用的：matplotlib、pyecharts
·人工智能常用的：tensorflow
等

使用python内置的pip程序安装第三方包
pip install 包的名称
我们可以通过如下命令，让其连接国内的网站进行包的安装：
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

pycharm安装软件包
"""

import numpy as np
print(np.random.seed(42))