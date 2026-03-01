import os
from pyecharts import options as opts
from pyecharts.charts import Tree

influence_map = {
    "1. علم التأثير\nScience of Influence": {
        "روبرت تشالديني - 6 مبادئ\nCialdini's 6 Principles": {
            "المعاملة بالمثل\nReciprocity": ["أعطِ أولاً ثم اطلب (Give Then Ask)", "عينات مجانية = مبيعات أكثر", "الخدمة غير المطلوبة تخلق التزاماً"],
            "الالتزام والاتساق\nCommitment": ["ابدأ بطلب صغير ثم كبّر (Foot-in-the-Door)", "الناس تكره التناقض مع نفسها", "الالتزام المكتوب أقوى من الشفهي"],
            "الإثبات الاجتماعي\nSocial Proof": ["الناس تتبع الأغلبية (Following the Crowd)", "التقييمات والمراجعات (Reviews)", "آلاف يستخدمون = يجب أن يكون جيداً"],
            "الإعجاب\nLiking": ["نتأثر بمن نحبهم (We're Influenced by Those We Like)", "التشابه يخلق الألفة", "المظهر الجذاب يزيد الإقناع"],
            "السلطة\nAuthority": ["نطيع أصحاب المناصب والمسميات", "تجربة ملغرام - 65% أطاعوا أوامر مؤلمة (Milgram 1963)", "المعاطف البيضاء والألقاب"],
            "الندرة\nScarcity": ["باقي 3 فقط! (Only 3 Left!)", "عرض محدود (Limited Time Offer)", "الخوف من الفقدان FOMO"]
        }
    },
    "2. لغة الجسد\nBody Language": {
        "إشارات القوة\nPower Signals": ["وضعية القوة (Power Pose - Amy Cuddy)", "التواصل البصري 60-70% (Eye Contact)", "المصافحة القوية (Firm Handshake)"],
        "إشارات الكذب\nDeception Cues": ["لمس الأنف والفم (Touching Face)", "تجنب النظر أو التحديق المفرط", "تغيير إيقاع الكلام", "⚠️ ملاحظة: لا يمكن كشف الكذب 100% من لغة الجسد"]
    },
    "3. فن التفاوض\nNegotiation": {
        "مبادئ هارفارد\nHarvard Principles": ["افصل الناس عن المشكلة (Separate People from Problem)", "ركز على المصالح لا المواقف (Focus on Interests)", "ابتكر خيارات للمنفعة المشتركة (Invent Options)", "BATNA - البديل الأفضل للاتفاق (Best Alternative)"],
        "تكتيكات التفاوض\nTactics": ["التثبيت (Anchoring - أول رقم يحدد المجال)", "الصمت كأداة ضغط (Silence as Pressure)", "لا تقبل العرض الأول أبداً (Never Accept First Offer)"]
    },
    "4. التلاعب المظلم\nDark Manipulation": ["Gaslighting - إنكار واقع الضحية", "التلاعب العاطفي (Emotional Manipulation)", "تقنية الحب القنبلة (Love Bombing)", "كيف تحمي نفسك: اعرف التقنيات لتتعرف عليها"],
    "📚 المراجع\nReferences": ["Robert Cialdini - Influence: Science & Practice (1984)", "Dale Carnegie - How to Win Friends (1936)", "Chris Voss - Never Split the Difference (2016)", "Robert Greene - 48 Laws of Power (1998)", "Daniel Kahneman - Thinking Fast and Slow (2011)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#6d4c41", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#6d4c41", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#5d4037", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#5d4037"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#4e342e", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#a1887f"}, "symbolSize": 12, "itemStyle": {"color": "#4e342e"}},
        {"label": {"fontSize": 13, "color": "#d7ccc8", "fontWeight": "bold", "backgroundColor": "#3e2723", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#3e2723"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#bcaaa4", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#795548"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("فن التأثير والإقناع\nThe Art of Influence", influence_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3800px", theme="dark", bg_color="#150d08", page_title="Influence & Persuasion", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="فن التأثير والإقناع", subtitle="Cialdini, Carnegie & The Science of Persuasion", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#bcaaa4", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#a1887f", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "influence_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Influence Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "influence_persuasion_mindmap.html")
