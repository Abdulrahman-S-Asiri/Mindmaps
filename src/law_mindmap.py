import os
from pyecharts import options as opts
from pyecharts.charts import Tree

law_map = {
    "1. أنظمة القانون\nLegal Systems": {
        "القانون المدني\nCivil Law": ["فرنسا وألمانيا وأغلب أوروبا", "مبني على تقنينات مكتوبة (Codes)", "قانون نابليون 1804 (Napoleonic Code)"],
        "القانون العام\nCommon Law": ["بريطانيا وأمريكا وأستراليا", "مبني على السوابق القضائية (Precedent)", "المحلفون (Jury System)"],
        "الشريعة الإسلامية\nIslamic Law": ["القرآن والسنة كمصدر أساسي", "الاجتهاد والفتوى", "نظام الحدود والتعزيرات"]
    },
    "2. فروع القانون\nBranches of Law": {
        "القانون الجنائي\nCriminal Law": ["الجرائم والعقوبات", "البراءة حتى ثبوت الإدانة", "الحق في محامي (Right to Counsel)"],
        "القانون المدني\nCivil Code": ["العقود والالتزامات (Contracts)", "الملكية (Property Law)", "التعويضات (Damages)"],
        "القانون الدولي\nInternational Law": ["ميثاق الأمم المتحدة 1945", "اتفاقيات جنيف (Geneva Conventions)", "المحكمة الجنائية الدولية ICC", "القانون الإنساني الدولي"]
    },
    "3. حقوق الإنسان\nHuman Rights": ["الإعلان العالمي لحقوق الإنسان 1948", "حق الحياة والحرية (Right to Life & Liberty)", "حرية التعبير (Freedom of Expression)", "حق التعليم والعمل (Right to Education & Work)"],
    "📚 المراجع\nReferences": ["الإعلان العالمي لحقوق الإنسان (UN 1948)", "Montesquieu - The Spirit of the Laws (1748)", "John Rawls - A Theory of Justice (1971)", "نظام الحكم الأساسي - المملكة العربية السعودية"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#5c6bc0", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#5c6bc0", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#3949ab", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#3949ab"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#283593", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#7986cb"}, "symbolSize": 12, "itemStyle": {"color": "#283593"}},
        {"label": {"fontSize": 13, "color": "#c5cae9", "fontWeight": "bold", "backgroundColor": "#1a237e", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#1a237e"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#9fa8da", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#3f51b5"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("القانون والحقوق\nLaw & Rights", law_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3000px", theme="dark", bg_color="#0d0f1a", page_title="Law & Rights", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="القانون والحقوق", subtitle="Justice, Rights & Rule of Law", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#7986cb", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#9fa8da", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "law_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Law Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "law_mindmap.html")
