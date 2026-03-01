import os
from pyecharts import options as opts
from pyecharts.charts import Tree

modern_history_map = {
    "1. الحرب العالمية الأولى (1914-1918)\nWorld War I": {
        "الأسباب\nCauses": ["اغتيال فرانز فرديناند (Archduke Assassination)", "التحالفات المتشابكة (Alliance System)", "سباق التسلح (Arms Race)", "القومية المتطرفة (Extreme Nationalism)"],
        "الأحداث\nKey Events": ["خنادق الجبهة الغربية (Trench Warfare)", "معركة السوم - 1 مليون ضحية (Battle of Somme)", "دخول أمريكا 1917 (US Entry)", "الثورة الروسية 1917 (Russian Revolution)"],
        "النتائج\nConsequences": ["معاهدة فرساي 1919 (Treaty of Versailles)", "سقوط 4 إمبراطوريات (Ottoman, Austro-Hungarian, Russian, German)", "20 مليون قتيل", "بذور الحرب العالمية الثانية"]
    },
    "2. الحرب العالمية الثانية (1939-1945)\nWorld War II": {
        "الأسباب\nCauses": ["صعود هتلر والنازية (Rise of Hitler)", "فشل معاهدة فرساي (Versailles Failure)", "الكساد العظيم 1929 (Great Depression)", "سياسة الاسترضاء (Appeasement Policy)"],
        "المحطات الكبرى\nMajor Events": {
            "المحور\nAxis": ["الحرب الخاطفة - Blitzkrieg", "اجتياح فرنسا 1940 (Fall of France)", "الهولوكوست - 6 ملايين يهودي (Holocaust)", "هجوم بيرل هاربر 1941 (Pearl Harbor)"],
            "الحلفاء\nAllies": ["معركة ستالينغراد - نقطة التحول (Stalingrad)", "إنزال نورماندي D-Day 1944", "القنبلتان الذريتان: هيروشيما وناغازاكي (Atomic Bombs)", "استسلام ألمانيا واليابان 1945"]
        },
        "النتائج\nConsequences": ["70-85 مليون قتيل (أكبر حرب في التاريخ)", "تأسيس الأمم المتحدة 1945 (United Nations)", "بداية الحرب الباردة (Cold War)", "تأسيس إسرائيل 1948"]
    },
    "3. الحرب الباردة (1947-1991)\nThe Cold War": {
        "المواجهة\nConfrontation": ["حائط برلين 1961-1989 (Berlin Wall)", "أزمة الصواريخ الكوبية 1962 (Cuban Missile Crisis)", "سباق الفضاء: سبوتنيك vs أبولو (Space Race)", "حرب فيتنام 1955-1975 (Vietnam War)"],
        "الأيديولوجيا\nIdeology": ["الرأسمالية الغربية vs الشيوعية السوفيتية", "حلف الناتو NATO vs حلف وارسو", "نظرية الدومينو (Domino Theory)", "الردع النووي MAD (Mutually Assured Destruction)"],
        "النهاية\nThe End": ["بيريسترويكا - غورباتشوف (Perestroika)", "سقوط جدار برلين 1989", "تفكك الاتحاد السوفيتي 1991", "أمريكا القطب الأوحد (Unipolar Moment)"]
    },
    "4. العالم المعاصر (2000-اليوم)\nThe Modern World": {
        "11 سبتمبر وما بعده\n9/11 & Aftermath": ["هجمات 11 سبتمبر 2001", "الحرب على الإرهاب (War on Terror)", "غزو أفغانستان 2001 والعراق 2003", "صعود داعش (ISIS 2014)"],
        "الأزمات الاقتصادية\nEconomic Crises": ["أزمة 2008 المالية العالمية", "أزمة الديون الأوروبية 2010", "جائحة كوفيد-19 وأثرها الاقتصادي 2020", "التضخم العالمي 2022-2023"],
        "تحولات جيوسياسية\nGeopolitical Shifts": ["صعود الصين كقوة عظمى", "الحرب الروسية الأوكرانية 2022", "BRICS مقابل G7", "التنافس التكنولوجي الأمريكي-الصيني"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#d32f2f", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#d32f2f", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#c62828", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#c62828"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#8e0000", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#ef5350"}, "symbolSize": 12, "itemStyle": {"color": "#8e0000"}},
        {"label": {"fontSize": 13, "color": "#ffcdd2", "fontWeight": "bold", "backgroundColor": "#5d0000", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#5d0000"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#ef9a9a", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#e53935"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("التاريخ الحديث\nModern History", modern_history_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#1a0505", page_title="Modern History", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="التاريخ الحديث", subtitle="From World Wars to the Modern World Order", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#ef5350", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#ef9a9a", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "modern_history_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Modern History Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "modern_history_mindmap.html")
