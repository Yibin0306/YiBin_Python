# 定义员工信息
worker_dict = {
    "楚伊斌":{
        "部门":"科技部",
        "工资":7000,
        "级别":2
    },"徐嘉乐":{
        "部门":"市场部",
        "工资":5000,
        "级别":1
    },"王高科":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    }
}
print(f"全体员工当心信息如下:\n{worker_dict}")
# 全体员工级别为1的员工完成升职+1加薪+1000操作
for key in worker_dict:
    if worker_dict[key]["级别"] == 1:
        worker_dict[key]["级别"] += 1
        worker_dict[key]["工资"] += 1000
print(f"全体员工级别为1的员工完成升职加薪操作，操作后:\n{worker_dict}")