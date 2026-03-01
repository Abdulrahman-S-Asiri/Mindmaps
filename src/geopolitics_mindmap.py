import os
from pyecharts import options as opts
from pyecharts.charts import Tree

geopolitics_map = {
    "1. القوى العظمى\nGreat Powers": {
        "الولايات المتحدة\nUSA": {
            "أركان القوة\nPillars": ["أقوى جيش: 800+ قاعدة عسكرية حول العالم", "هيمنة الدولار (Dollar Hegemony)", "التفوق التكنولوجي (Tech Supremacy)", "القوة الناعمة: هوليوود وسيلكون فالي"],
            "التحديات\nChallenges": ["الانقسام الداخلي (Internal Polarization)", "الدين الوطني: 34+ تريليون دولار", "تراجع النفوذ العالمي (Declining Global Influence)"]
        },
        "الصين\nChina": {
            "الصعود\nThe Rise": ["ثاني أكبر اقتصاد عالمياً (GDP $18T+)", "مبادرة الحزام والطريق (Belt & Road Initiative)", "التفوق في التصنيع (World's Factory)", "التقدم في الذكاء الاصطناعي والتكنولوجيا"],
            "التحديات\nChallenges": ["أزمة العقارات (Real Estate Crisis)", "شيخوخة السكان (Aging Population)", "التوترات مع تايوان (Taiwan Tensions)"]
        },
        "روسيا\nRussia": ["أكبر ترسانة نووية في العالم", "موارد الطاقة: نفط وغاز طبيعي", "الحرب في أوكرانيا 2022+", "التحالف مع الصين"],
        "قوى صاعدة\nRising Powers": ["الهند - أكبر سكان وأسرع نمو", "البرازيل - عملاق أمريكا اللاتينية", "تركيا - بين الشرق والغرب", "السعودية - تحول رؤية 2030"]
    },
    "2. التحالفات والصراعات\nAlliances & Conflicts": {
        "التحالفات\nAlliances": ["NATO - حلف الناتو (31 دولة)", "BRICS+ - البريكس (البديل للغرب)", "SCO - منظمة شنغهاي", "AUKUS - أمريكا، بريطانيا، أستراليا", "G7 vs G20"],
        "الصراعات الجيوسياسية\nGeopolitical Conflicts": {
            "نقاط ساخنة\nHotspots": ["تايوان - بؤرة التوتر الأولى", "بحر الصين الجنوبي (South China Sea)", "أوكرانيا وتوسع الناتو", "فلسطين والشرق الأوسط", "شبه الجزيرة الكورية (North Korea)"]
        }
    },
    "3. أدوات الجيوسياسة\nGeopolitical Tools": {
        "القوة الصلبة\nHard Power": ["الجيش والتسلح (Military)", "العقوبات الاقتصادية (Sanctions)", "الحروب بالوكالة (Proxy Wars)"],
        "القوة الناعمة\nSoft Power": ["الإعلام والدعاية (Media & Propaganda)", "الثقافة والسينما والرياضة", "المساعدات والتنمية الدولية", "الدبلوماسية (Diplomacy)"],
        "الحرب الاقتصادية\nEconomic Warfare": ["حرب العملات (Currency Wars)", "حرب الرقائق الأمريكية-الصينية (Chip War)", "سلاح الطاقة (Energy as Weapon)", "تسليح الدولار (Weaponizing the Dollar)"]
    },
    "4. مستقبل النظام العالمي\nFuture World Order": {
        "سيناريوهات\nScenarios": ["عالم متعدد الأقطاب (Multipolar World)", "فخ ثيوسيديدس - حرب بين الصاعد والمهيمن", "حكومة عالمية (World Government - Unlikely)", "فوضى وتشرذم (Fragmentation)"],
        "تحديات عالمية\nGlobal Challenges": ["تغير المناخ (Climate Change)", "الذكاء الاصطناعي كسلاح (AI as Weapon)", "الأوبئة المستقبلية (Future Pandemics)", "أزمة المياه والغذاء (Water & Food Crisis)"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#455a64", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#455a64", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#37474f", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#37474f"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#263238", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#78909c"}, "symbolSize": 12, "itemStyle": {"color": "#263238"}},
        {"label": {"fontSize": 13, "color": "#b0bec5", "fontWeight": "bold", "backgroundColor": "#1c2830", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#1c2830"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#90a4ae", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#607d8b"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الجيوسياسة\nGeopolitics", geopolitics_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#0d1518", page_title="Geopolitics", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الجيوسياسة العالمية", subtitle="Power, Alliances & The Future World Order", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#b0bec5", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#78909c", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "geopolitics_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Geopolitics Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "geopolitics_mindmap.html")
