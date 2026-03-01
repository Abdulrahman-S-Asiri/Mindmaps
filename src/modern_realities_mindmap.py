import os
from pyecharts import options as opts
from pyecharts.charts import Tree

# ─── 1. Deep & Detailed Data Structure ─────────────────────────
modern_realities_map = {
    "1. وهم المال والاقتصاد\nThe Financial Matrix": {
        "النقود الإلزامية (Fiat Money)": {
            "المال كدين مطبوع (Money as Debt)": ["البنوك المركزية (Central Banks)", "التسهيل الكمي (Quantitative Easing)", "نظام الاحتياطي الجزئي (Fractional Reserve Banking)"],
            "التضخم (Inflation)": ["ضريبة خفية على المدخرين (Hidden Tax)", "تدمير القوة الشرائية (Eroding Purchasing Power)", "فقاعات الأصول (Asset Bubbles)"]
        },
        "القيمة والندرة (Value & Scarcity)": {
            "الندرة الحقيقية (True Scarcity)": ["الوقت (Time)", "الطاقة (Energy)", "السلع الأساسية كالذهب (Commodities & Gold)", "البيتكوين (Bitcoin Math)"],
            "الندرة المفتعلة (Artificial Scarcity)": ["الألماس (Diamonds Cartels)", "احتكار الملكية الفكرية (IP Monopolies)", "القيود الجمركية (Trade Barriers)"]
        },
        "فخ الاستهلاك (Consumerism Trap)": ["التقادم المخطط (Planned Obsolescence)", "صناعة الرغبات الوهمية (Manufactured Desires)", "ثقافة القروض والديون (Credit Culture)"]
    },
    "2. البيانات والمعلومات\nData & The Attention Economy": {
        "نفط العصر (Data as Oil)": {
            "تحليل السلوك (Behavioral Analysis)": ["التنبؤ بالخيارات (Predictive Analytics)", "الاستهداف الدقيق (Micro-Targeting)"],
            "رأسمالية المراقبة (Surveillance Capitalism)": ["المنتج هو أنت (You Are The Product)", "انتهاك الخصوصية المنظم (Systematic Privacy Erosion)"]
        },
        "حرب الانتباه (The War on Attention)": {
            "خوارزميات الإدمان (Addiction Algorithms)": ["دوبامين التمرير اللانهائي (Infinite Scroll Dopamine)", "استغلال الغضب والجدل (Rage-baiting & Polarization)"],
            "تدمير العمق (Shattering Depth)": ["تشتت التركيز المستمر (Continuous Partial Attention)", "تآكل الذاكرة العميقة (Erosion of Deep Memory)"]
        },
        "الحقيقة المصنعة (Manufactured Truth)": ["التزييف العميق (Deepfakes)", "فقاعات الفلترة (Filter Bubbles/Echo Chambers)", "توجيه وتأطير الإعلام (Media Framing)"]
    },
    "3. القوة والتحكم\nPower, Control & Hegemony": {
        "الهيمنة الناعمة (Soft Hegemony)": {
            "وهم الاختيار (Illusion of Choice)": ["ديمقراطيات الشركات (Corporatocracy)", "الاستقطاب الحزبي الوهمي (Two-Party Illusion)"],
            "صناعة الثقافة (Culture Industry)": ["تسطيح الفكر عبر الترفيه (Dumbing Down via Entertainment)", "تطبيع الشذوذ والانحراف (Normalizing Deviance)"]
        },
        "التبعية التكنولوجية (Tech Dependence)": {
            "الرقابة الرقمية (Digital Censorship)": ["الإلغاء الاجتماعي (Cancel Culture)", "حظر الحسابات (Deplatforming)"],
            "المراتب الاجتماعية (Social Credit)": ["التحكم المالي الرقمي (CBDCs)", "المراقبة البيومترية (Biometric Surveillance)"]
        },
        "تسليم الإرادة (Surrendering Will)": ["الاعتماد الكلي على الذكاء الاصطناعي (Over-reliance on AI)", "فقدان المهارات البشرية الأساسية (Loss of Core Human Skills)"]
    },
    "📚 المراجع\nReferences": ["Yuval Harari - 21 Lessons (2018)", "Shoshana Zuboff - Surveillance Capitalism (2019)", "Noam Chomsky - Manufacturing Consent (1988)", "Jaron Lanier - Ten Arguments (2018)"]
}

# ─── 2. Rich Professional Styling by Depth ─────────────────────
def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    
    # Custom Matrix/Hacker Theme (Crimson Red / Blood Orange / Deep Charcoal)
    if depth == 0:
        node["label"] = {
            "fontSize": 26, "color": "#f8f9fa", "fontWeight": "bold", 
            "backgroundColor": "#d10020", "padding": [18, 30], "borderRadius": 14
        }
        node["symbolSize"] = 40
        node["itemStyle"] = {"color": "#d10020", "borderColor": "#ffffff", "borderWidth": 3}

    elif depth == 1:
        node["label"] = {
            "fontSize": 18, "color": "#0a0a0a", "fontWeight": "bold", 
            "backgroundColor": "#ff4d4d", "padding": [12, 22], "borderRadius": 10
        }
        node["symbolSize"] = 24
        node["itemStyle"] = {"color": "#ff4d4d", "borderColor": "#ffffff", "borderWidth": 2}

    elif depth == 2:
        node["label"] = {
            "fontSize": 15, "color": "#ffffff", "fontWeight": "bold",
            "backgroundColor": "#b30000", "padding": [8, 16], "borderRadius": 8,
            "borderWidth": 1, "borderColor": "#ff6666"
        }
        node["symbolSize"] = 16
        node["itemStyle"] = {"color": "#b30000"}

    elif depth == 3:
        node["label"] = {
            "fontSize": 13, "color": "#ffcccc", "fontWeight": "bold",
            "backgroundColor": "#4d0000", "padding": [6, 12], "borderRadius": 6,
        }
        node["symbolSize"] = 10
        node["itemStyle"] = {"color": "#4d0000"}

    else:
        node["label"] = {
            "fontSize": 12, "color": "#b3b3b3",
            "backgroundColor": "transparent"
        }
        node["symbolSize"] = 6
        node["itemStyle"] = {"color": "#666666"}

    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
        
    return node

root_label = "الماتريكس وحقائق العصر\nThe Matrix & Modern Realities"
tree_data = [dict_to_tree(root_label, modern_realities_map)]

# ─── 3. Generate the Interactive Mindmap ───────────────────────
def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(
        width="100%", 
        height="2600px", 
        theme="dark",
        bg_color="#0a0305", # Very dark deep crimson/black
        page_title="Modern Realities",
        renderer="svg"
    ))
    
    c.add(
        series_name="",
        data=data,
        orient="LR",
        initial_tree_depth=-1,
        symbol="emptyCircle",
        edge_shape="curve",
        edge_fork_position="50%",
        is_roam=True,
        label_opts=opts.LabelOpts(position="right")
    )
    
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title="حقائق العصر الحديث الوهمية والمبطنة",
            subtitle="Unveiling the Illusions of Money, Data, and Hegemony",
            pos_left="center",
            pos_top="1%",
            title_textstyle_opts=opts.TextStyleOpts(color="#ff4d4d", font_size=40, font_weight="bolder"),
            subtitle_textstyle_opts=opts.TextStyleOpts(color="#ffcccc", font_size=20)
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "saveAsImage": {"type": "png", "name": "modern_realities_map", "title": "Save PNG", "pixelRatio": 4}
            }
        )
    )
    
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Modern Realities Map generated successfully: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "modern_realities_mindmap.html")
