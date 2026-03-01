import os
from pyecharts import options as opts
from pyecharts.charts import Tree

energy_map = {
    "1. مصادر الطاقة\nEnergy Sources": {
        "الأحفورية\nFossil Fuels": ["النفط - 31% من الطاقة العالمية (Oil)", "الغاز الطبيعي - 24% (Natural Gas)", "الفحم - 27% (Coal)", "ذروة النفط (Peak Oil Theory)"],
        "المتجددة\nRenewables": {
            "الشمسية\nSolar": ["الخلايا الكهروضوئية (Photovoltaic - PV)", "الطاقة الشمسية المركزة (CSP)", "انخفاض التكلفة 90% منذ 2010"],
            "الرياح\nWind": ["توربينات برية وبحرية (Onshore/Offshore)", "أسرع مصدر نمواً في أوروبا"],
            "أخرى\nOther": ["الطاقة المائية (Hydropower)", "الطاقة الحرارية الأرضية (Geothermal)", "الكتلة الحيوية (Biomass)"]
        },
        "النووية\nNuclear": ["الانشطار النووي (Fission)", "الاندماج النووي - طاقة المستقبل (Fusion)", "مفاعل ITER - فرنسا", "مشكلة النفايات المشعة"]
    },
    "2. تغير المناخ\nClimate Change": {
        "العلم\nThe Science": ["ثاني أكسيد الكربون CO2 = 421 ppm (2023)", "ارتفاع حرارة الأرض 1.1°C فوق مستويات ما قبل الصناعة", "IPCC - الهيئة الحكومية الدولية", "تأثير الغازات الدفيئة (Greenhouse Effect)"],
        "التأثيرات\nImpacts": ["ذوبان القمم الجليدية (Ice Melt)", "ارتفاع مستوى البحر (Sea Level Rise)", "موجات الحر والجفاف (Heatwaves)", "الأحداث المناخية المتطرفة (Extreme Events)"],
        "الحلول\nSolutions": ["اتفاقية باريس 2015 (Paris Agreement)", "صافي صفر انبعاثات بحلول 2050 (Net Zero)", "تسعير الكربون (Carbon Pricing)", "احتجاز الكربون (Carbon Capture)"]
    },
    "3. جيوسياسة الطاقة\nEnergy Geopolitics": ["أوبك+ والتحكم بأسعار النفط (OPEC+)", "حرب الطاقة الروسية-الأوروبية", "التحول الطاقوي السعودي (Vision 2030)", "سباق المعادن النادرة (Rare Earth Minerals)"],
    "📚 المراجع\nReferences": ["IPCC - Climate Change 2021/2022 Reports", "Vaclav Smil - Energy and Civilization (2017)", "Daniel Yergin - The Prize: Oil, Money & Power (1991)", "IEA World Energy Outlook (Annual)", "Bill Gates - How to Avoid a Climate Disaster (2021)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#fdd835", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#fdd835", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#f9a825", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#f9a825"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#f57f17", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#fdd835"}, "symbolSize": 12, "itemStyle": {"color": "#f57f17"}},
        {"label": {"fontSize": 13, "color": "#fff9c4", "fontWeight": "bold", "backgroundColor": "#e65100", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#e65100"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#fff176", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#fbc02d"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الطاقة والمناخ\nEnergy & Climate", energy_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#1a1400", page_title="Energy & Climate", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الطاقة والمناخ", subtitle="Energy Crisis, Climate Change & The Path Forward", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#fdd835", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#fff176", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "energy_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Energy & Climate Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "energy_climate_mindmap.html")
