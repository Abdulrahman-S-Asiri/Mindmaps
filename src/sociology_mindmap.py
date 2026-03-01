import os
from pyecharts import options as opts
from pyecharts.charts import Tree

sociology_map = {
    "1. أسس علم الاجتماع\nFoundations": {
        "الآباء المؤسسون\nFounders": {
            "إميل دوركهايم\nDurkheim": ["التضامن الآلي والعضوي", "دراسة الانتحار 1897", "الحقائق الاجتماعية"],
            "ماكس فيبر\nWeber": ["البيروقراطية", "أخلاق العمل البروتستانتية", "السلطة: تقليدية، كاريزمية، قانونية"],
            "كارل ماركس\nMarx": ["الصراع الطبقي (Class Struggle)", "الاغتراب (Alienation)", "رأس المال (Das Kapital)"],
            "ابن خلدون\nIbn Khaldun": ["المقدمة 1377", "العصبية (Asabiyyah)", "دورة الحضارات", "أول عالم اجتماع حقيقي"]
        }
    },
    "2. النظريات\nTheories": {
        "الوظيفية\nFunctionalism": ["المجتمع كجسم متكامل", "تالكوت بارسونز", "روبرت ميرتون - الوظائف الكامنة"],
        "نظرية الصراع\nConflict": ["ماركس: صراع الطبقات", "بورديو: رأس المال الثقافي", "غرامشي: الهيمنة الثقافية"],
        "التفاعلية الرمزية\nSymbolic Interactionism": ["جورج هربرت ميد", "غوفمان - المسرح الاجتماعي", "نظرية الوصم (Labeling)"],
        "النظرية النقدية\nCritical Theory": ["مدرسة فرانكفورت", "هابرماس", "نقد صناعة الثقافة"]
    },
    "3. قضايا معاصرة\nContemporary Issues": {
        "اللامساواة\nInequality": {"الطبقية\nClass": ["1% يملكون 50% من الثروة", "الحراك الاجتماعي يتراجع"], "العرق والجنس\nRace & Gender": ["العنصرية المؤسسية", "فجوة الأجور", "التقاطعية - Crenshaw"]},
        "العولمة\nGlobalization": ["ثقافة عالمية vs تنوع محلي", "الشركات متعددة الجنسيات", "الهجرة والشتات"],
        "وسائل التواصل\nSocial Media": ["فقاعات المعلومات", "الاستقطاب المجتمعي", "العزلة الرقمية"]
    },
    "4. المؤسسات\nInstitutions": {
        "الأسرة\nFamily": ["النووية vs الممتدة", "تأثير الطلاق", "أدوار الجنسين المتغيرة"],
        "التعليم\nEducation": ["التعليم كتحرر أو سيطرة", "المنهج الخفي (Hidden Curriculum)", "إعادة إنتاج الطبقية"],
        "الدين\nReligion": ["دوركهايم: لاصق اجتماعي", "ماركس: أفيون الشعوب", "فيبر: محرك للتغيير"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#ffab91", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#ffab91", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#e64a19", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#e64a19"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#bf360c", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#ff8a65"}, "symbolSize": 12, "itemStyle": {"color": "#bf360c"}},
        {"label": {"fontSize": 13, "color": "#ffccbc", "fontWeight": "bold", "backgroundColor": "#8d2000", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#8d2000"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#ffab91", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#ff5722"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("علم الاجتماع\nSociology", sociology_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#1a0800", page_title="Sociology", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="علم الاجتماع", subtitle="From Ibn Khaldun to Bourdieu", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#ffab91", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#ff8a65", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "sociology_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Sociology Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "sociology_mindmap.html")
