import os
from pyecharts import options as opts
from pyecharts.charts import Tree

food_map = {
    "1. الأمن الغذائي العالمي\nGlobal Food Security": {
        "الأرقام\nThe Numbers": ["8 مليار إنسان يحتاجون طعاماً يومياً", "828 مليون يعانون من الجوع (2023)", "30-40% من الغذاء يُهدر عالمياً (Food Waste)", "أسعار الغذاء ارتفعت 65% بين 2019-2023"],
        "التحديات\nChallenges": ["تغير المناخ يقلل الإنتاجية", "نضوب المياه الجوفية (Groundwater Depletion)", "تزايد السكان: 10 مليار بحلول 2050", "التربة تفقد خصوبتها (Soil Degradation)"]
    },
    "2. أنظمة الزراعة\nFarming Systems": {
        "الزراعة التقليدية\nConventional": ["استخدام المبيدات والأسمدة الكيميائية", "الزراعة الأحادية (Monoculture)", "إنتاجية عالية لكن ضرر بيئي"],
        "الزراعة العضوية\nOrganic": ["بدون كيماويات صناعية", "تكلفة أعلى وإنتاجية أقل 20-25%", "أفضل للتربة والتنوع الحيوي"],
        "الزراعة المستقبلية\nFuture Farming": ["الزراعة العمودية (Vertical Farming)", "الزراعة المائية (Hydroponics)", "الزراعة الدقيقة بالـ AI (Precision Agriculture)", "الطائرات المسيّرة الزراعية (Agricultural Drones)"]
    },
    "3. الغذاء والصناعة\nFood Industry": {
        "الغذاء المصنّع\nProcessed Food": ["Ultra-Processed = أكثر من 5 مكونات صناعية", "مرتبط بالسمنة والسكري وأمراض القلب", "73% من أغذية السوبرماركت معالجة فائقة (US)"],
        "البدائل الغذائية\nFood Alternatives": ["لحوم نباتية (Beyond Meat, Impossible)", "اللحم المزروع في المختبر (Cultured Meat)", "بروتين الحشرات (Insect Protein)", "الطحالب كغذاء مستقبلي (Algae)"],
        "الكائنات المعدلة وراثياً\nGMOs": ["فوائد: مقاومة الآفات وزيادة الإنتاج", "مخاوف: التأثير طويل المدى", "الأرز الذهبي - فيتامين A (Golden Rice)", "75% من الغذاء المعالج يحتوي GMO (US)"]
    },
    "📚 المراجع\nReferences": ["FAO - The State of Food Security 2023", "Michael Pollan - The Omnivore's Dilemma (2006)", "McKinsey - Future of Food Report", "Carlo Petrini - Slow Food Nation (2007)", "David Montgomery - Dirt: The Erosion of Civilizations (2007)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#8bc34a", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#8bc34a", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#689f38", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#689f38"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#33691e", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#aed581"}, "symbolSize": 12, "itemStyle": {"color": "#33691e"}},
        {"label": {"fontSize": 13, "color": "#dcedc8", "fontWeight": "bold", "backgroundColor": "#1a3a0a", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#1a3a0a"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#aed581", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#7cb342"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الغذاء والزراعة\nFood & Agriculture", food_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#0d1a05", page_title="Food & Agriculture", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الغذاء والزراعة", subtitle="Feeding 8 Billion People — Today & Tomorrow", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#8bc34a", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#aed581", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "food_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Food Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "food_agriculture_mindmap.html")
