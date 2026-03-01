import os
from pyecharts import options as opts
from pyecharts.charts import Tree

media_map = {
    "1. أدوات التلاعب\nManipulation Tools": {
        "البروباغندا\nPropaganda": {
            "تقنيات كلاسيكية\nClassic Techniques": ["التكرار حتى التصديق (Repetition - Goebbels)", "العدو المشترك (Common Enemy)", "نقل السلطة (Transfer)", "عربة الفائز (Bandwagon)", "الشهادة (Testimonial)"],
            "بروباغندا حديثة\nModern Propaganda": ["الأخبار المزيفة (Fake News)", "التزييف العميق (Deepfakes)", "مزارع الترول (Troll Farms)", "الحملات المنسقة (Coordinated Campaigns)"]
        },
        "التأطير\nFraming": ["نفس الخبر بقالبين مختلفين = انطباعين مختلفين", "اختيار الكلمات (Word Choice)", "اختيار الصور (Image Selection)", "ما لا يُذكر أهم مما يُذكر (Omission)"]
    },
    "2. اقتصاد الانتباه\nAttention Economy": {
        "كيف تعمل الخوارزميات\nHow Algorithms Work": ["فقاعات المعلومات (Filter Bubbles - Eli Pariser)", "غرف الصدى (Echo Chambers)", "التغذية اللانهائية (Infinite Scroll)", "الإشعارات = محفز الدوبامين (Notifications = Dopamine)"],
        "التأثير على السياسة\nPolitical Impact": ["فضيحة Cambridge Analytica 2018", "التأثير على الانتخابات (Election Interference)", "التطرف عبر الخوارزميات (Algorithmic Radicalization)", "The Social Dilemma (2020 - Netflix)"]
    },
    "3. محو الأمية الإعلامية\nMedia Literacy": ["من يملك هذه الوسيلة؟ (Who Owns This?)", "ما هو الهدف؟ (What's The Purpose?)", "ما المصادر؟ (Check Sources)", "تحقق من التحيز (Check for Bias)", "CRAAP Test: حداثة، ملاءمة، سلطة، دقة، غرض"],
    "📚 المراجع\nReferences": ["Noam Chomsky - Manufacturing Consent (1988)", "Edward Bernays - Propaganda (1928)", "Neil Postman - Amusing Ourselves to Death (1985)", "Eli Pariser - The Filter Bubble (2011)", "Tristan Harris - The Social Dilemma (2020)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#e91e63", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#e91e63", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#c2185b", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#c2185b"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#880e4f", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#f48fb1"}, "symbolSize": 12, "itemStyle": {"color": "#880e4f"}},
        {"label": {"fontSize": 13, "color": "#f8bbd0", "fontWeight": "bold", "backgroundColor": "#560027", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#560027"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#f48fb1", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#e91e63"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الإعلام والبروباغندا\nMedia & Propaganda", media_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#1a050d", page_title="Media & Propaganda", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الإعلام والبروباغندا", subtitle="How Public Opinion is Manufactured", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#f48fb1", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#f8bbd0", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "media_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Media Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "media_propaganda_mindmap.html")
