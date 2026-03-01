import os
from pyecharts import options as opts
from pyecharts.charts import Tree

lang_map = {
    "1. علم اللسانيات\nLinguistics": {
        "فروع اللسانيات\nBranches": ["الصوتيات (Phonetics)", "الصرف (Morphology)", "النحو (Syntax)", "الدلالة (Semantics)", "التداولية (Pragmatics)"],
        "عائلات اللغات\nLanguage Families": ["الهندو-أوروبية: إنجليزي، عربي لا (Indo-European)", "السامية: العربية والعبرية (Semitic)", "الصينية-التبتية (Sino-Tibetan)", "7,000+ لغة حية في العالم", "لغة تموت كل أسبوعين"]
    },
    "2. تعلم اللغات\nLanguage Learning": {
        "طرق فعالة\nEffective Methods": ["الانغماس الكامل (Immersion)", "التكرار المتباعد (Spaced Repetition - Anki)", "الإدخال المفهوم - كراشن (Comprehensible Input - Krashen)", "التحدث من اليوم الأول (Speak from Day 1)"],
        "أخطاء شائعة\nCommon Mistakes": ["التركيز على القواعد فقط (Grammar Obsession)", "الخوف من الأخطاء (Fear of Mistakes)", "عدم الاستماع الكافي (Not Enough Listening)", "ترجمة كلمة بكلمة (Word-by-Word Translation)"],
        "مستويات CEFR\nCEFR Levels": ["A1/A2 - مبتدئ (Beginner)", "B1/B2 - متوسط (Intermediate)", "C1/C2 - متقدم (Advanced)"]
    },
    "3. فن البلاغة والإقناع\nRhetoric & Persuasion": {
        "أرسطو: 3 أدوات\nAristotle's Appeals": ["Ethos - مصداقية المتحدث", "Pathos - العاطفة والمشاعر", "Logos - المنطق والحجج"],
        "البلاغة العربية\nArabic Rhetoric": ["البيان: التشبيه والاستعارة والكناية", "المعاني: التقديم والتأخير والحذف", "البديع: الجناس والطباق والسجع"]
    },
    "4. اللغة العربية\nArabic Language": ["لغة القرآن الكريم", "أكثر من 12 مليون كلمة (الأغنى في العالم)", "28 حرفاً + نظام الإعراب", "جذور ثلاثية (Root System)", "لغة 420+ مليون ناطق"],
    "📚 المراجع\nReferences": ["Noam Chomsky - Syntactic Structures (1957)", "Stephen Krashen - The Input Hypothesis (1985)", "Steven Pinker - The Language Instinct (1994)", "سيبويه - الكتاب (8th Century)", "Gabriel Wyner - Fluent Forever (2014)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#00897b", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#00897b", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#00695c", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#00695c"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#004d40", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#4db6ac"}, "symbolSize": 12, "itemStyle": {"color": "#004d40"}},
        {"label": {"fontSize": 13, "color": "#b2dfdb", "fontWeight": "bold", "backgroundColor": "#002a22", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#002a22"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#80cbc4", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#009688"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("اللغات والتواصل\nLanguages & Communication", lang_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#001a14", page_title="Languages", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="اللغات والتواصل", subtitle="The Power of Language", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#4db6ac", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#80cbc4", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "languages_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Languages Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "languages_mindmap.html")
