import hashlib
from random import randrange

from flask import Flask, render_template

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Radar

def hash_code(s, salt='nemo'):
    md5 = hashlib.md5()
    s += salt
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()


def bar_base() -> Bar:
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [randrange(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [randrange(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
    )
    return c

def radar_base() -> Radar:
    v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
    v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
    c = (
        Radar()
            .add_schema(
            schema=[
                opts.RadarIndicatorItem(name="销售", max_=6500),
                opts.RadarIndicatorItem(name="管理", max_=16000),
                opts.RadarIndicatorItem(name="信息技术", max_=30000),
                opts.RadarIndicatorItem(name="客服", max_=38000),
                opts.RadarIndicatorItem(name="研发", max_=52000),
                opts.RadarIndicatorItem(name="市场", max_=25000),
            ]
        )
            .add("预算分配", v1)
            .add("实际开销", v2)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(title_opts=opts.TitleOpts(title="Radar-基本示例"))
    )
    return c