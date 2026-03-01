import os
from pyecharts import options as opts
from pyecharts.charts import Tree

conspiracy_map = {
    "1. ما هي نظرية المؤامرة؟\nWhat is a Conspiracy Theory?": {
        "التعريف\nDefinition": ["تفسير أحداث بمخطط سري لجهات خفية", "الفرق بين مؤامرة حقيقية ونظرية مؤامرة", "بعض المؤامرات كانت حقيقية (MKUltra, COINTELPRO)"],
        "لماذا نصدقها\nWhy We Believe": ["التحيز التأكيدي (Confirmation Bias)", "البحث عن أنماط (Pattern Seeking)", "الحاجة لتفسيرات بسيطة لأحداث معقدة", "انعدام الثقة بالمؤسسات (Institutional Distrust)", "تأثير دانينغ-كروجر (Dunning-Kruger Effect)"]
    },
    "2. أشهر النظريات وتحليلها\nFamous Theories Analyzed": {
        "هبوط القمر (1969)\nMoon Landing": {
            "الادعاء\nClaim": ["تم تصويره في استوديو", "العلم يرفرف بلا هواء", "لم يعودوا مجدداً"],
            "التحليل العلمي\nScientific Analysis": ["✅ عاكسات ليزر موجودة على القمر حتى اليوم", "✅ 400,000 شخص عملوا في المشروع", "✅ العلم ثابت بسبب القضيب المعدني", "✅ 6 بعثات أبولو هبطت (1969-1972)"]
        },
        "الأرض المسطحة\nFlat Earth": {
            "الدليل ضدها\nEvidence Against": ["✅ صور ناسا وعشرات الوكالات الفضائية", "✅ رحلات الطيران ومساراتها (Flight Paths)", "✅ الجاذبية وسلوك الماء (Gravity)", "✅ محطة الفضاء الدولية - بث مباشر"]
        },
        "الحكومة العالمية\nNew World Order": {
            "الادعاء\nClaim": ["نخبة سرية تتحكم بالعالم", "مجموعة بيلدربيرغ والماسونية", "إلغاء السيادة الوطنية"],
            "التحليل\nAnalysis": ["⚠️ تجمعات النخبة حقيقية (Davos, Bilderberg)", "⚠️ لكن العالم فوضوي وليس خاضعاً لخطة واحدة", "⚠️ الحكومات تتصارع أكثر مما تتعاون"]
        }
    },
    "3. مؤامرات حقيقية\nReal Conspiracies": ["MKUltra - تجارب CIA للتحكم بالعقل (1950s-70s)", "COINTELPRO - FBI ضد ناشطي الحقوق المدنية", "فضيحة ووترغيت (Watergate 1972)", "إيران-كونترا (Iran-Contra Affair 1986)", "تجارب توسكيجي - تجربة مرض الزهري على السود (1932-72)"],
    "4. التفكير النقدي\nCritical Thinking": ["اسأل: ما الدليل؟ (What's the Evidence?)", "شفرة أوكام: أبسط تفسير غالباً الصحيح", "تحقق من المصادر الأصلية (Primary Sources)", "العبء يقع على المدّعي (Burden of Proof)", "الارتباط ≠ السببية (Correlation ≠ Causation)"],
    "📚 المراجع\nReferences": ["Michael Shermer - Why People Believe Weird Things (1997)", "Rob Brotherton - Suspicious Minds (2015)", "Jan-Willem van Prooijen - Psychology of Conspiracy Theories (2018)", "Karl Popper - The Open Society and Its Enemies (1945)", "CIA FOIA Archive - declassified MKUltra documents"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#37474f", "padding": [16, 28], "borderRadius": 12, "borderWidth": 2, "borderColor": "#ff5252"}, "symbolSize": 35, "itemStyle": {"color": "#ff5252", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#263238", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#455a64"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1c2b33", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#546e7a"}, "symbolSize": 12, "itemStyle": {"color": "#37474f"}},
        {"label": {"fontSize": 13, "color": "#b0bec5", "fontWeight": "bold", "backgroundColor": "#111d24", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#263238"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#78909c", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#546e7a"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("نظريات المؤامرة: تحليل علمي\nConspiracy Theories: Scientific Analysis", conspiracy_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3800px", theme="dark", bg_color="#0a0f14", page_title="Conspiracy Analysis", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="نظريات المؤامرة: تحليل علمي", subtitle="Separating Fact from Fiction", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#ff5252", font_size=36, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#78909c", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "conspiracy_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Conspiracy Analysis Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "conspiracy_analysis_mindmap.html")
