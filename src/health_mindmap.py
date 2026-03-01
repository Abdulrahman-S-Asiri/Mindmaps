import os
from pyecharts import options as opts
from pyecharts.charts import Tree

health_map = {
    "1. التغذية الحقيقية\nReal Nutrition": {
        "المغذيات الكبرى\nMacronutrients": {
            "البروتين\nProtein": ["الأحماض الأمينية الأساسية (Essential Amino Acids)", "1.6-2.2 غ/كغ للرياضيين", "مصادر حيوانية: لحوم، بيض، حليب", "مصادر نباتية: بقوليات، مكسرات، صويا"],
            "الكربوهيدرات\nCarbohydrates": ["بسيطة: سكر الفواكه والعسل (Simple Sugars)", "معقدة: حبوب كاملة وبطاطا (Complex Carbs)", "الألياف الغذائية (Dietary Fiber)", "مؤشر السكر في الدم (Glycemic Index)"],
            "الدهون\nFats": ["أوميغا 3 - مضاد للالتهابات (Anti-inflammatory)", "أوميغا 6 - التوازن مطلوب", "الدهون المشبعة - ليست شريرة دائماً", "الدهون المتحولة - السم الحقيقي (Trans Fats = Poison)"]
        },
        "المغذيات الصغرى\nMicronutrients": {
            "الفيتامينات\nVitamins": ["فيتامين D - هرمون الشمس (80% من الناس ناقصون)", "فيتامين B12 - الأعصاب والطاقة", "فيتامين C - المناعة ومضاد الأكسدة", "فيتامين K2 - نقل الكالسيوم للعظام"],
            "المعادن\nMinerals": ["المغنيسيوم - 300+ تفاعل إنزيمي (أهم معدن مهمل)", "الزنك - المناعة والهرمونات", "الحديد - نقل الأوكسجين", "اليود - الغدة الدرقية"]
        },
        "أساطير غذائية\nNutrition Myths": ["الدهون ليست العدو - السكر هو (Fat ≠ Enemy)", "الكوليسترول الغذائي ليس المشكلة", "الحمية المنخفضة السعرات تبطئ الأيض", "المكملات ليست بديلاً عن الطعام الحقيقي", "الصيام المتقطع - للبعض وليس للكل"]
    },
    "2. النوم والراحة\nSleep & Recovery": {
        "علم النوم\nSleep Science": {
            "مراحل النوم\nSleep Stages": ["N1 - الانتقال للنوم (3-5%)", "N2 - النوم الخفيف (45-55%)", "N3 - النوم العميق - ترميم الجسم (15-20%)", "REM - ترميم العقل والذاكرة (20-25%)"],
            "الإيقاع اليومي\nCircadian Rhythm": ["الميلاتونين - هرمون النوم (Melatonin)", "الكورتيزول - هرمون الاستيقاظ (Cortisol)", "الساعة البيولوجية في النواة فوق التصالبية (SCN)", "الضوء الأزرق يثبط الميلاتونين"]
        },
        "قواعد النوم الذهبية\nGolden Sleep Rules": ["7-9 ساعات للبالغين (لا أقل ولا أكثر)", "الاستيقاظ بنفس الوقت يومياً", "غرفة مظلمة وباردة (18-20°C)", "لا كافيين بعد الساعة 2 ظهراً", "لا شاشات ساعة قبل النوم"],
        "أخطار قلة النوم\nSleep Deprivation Dangers": ["ضعف المناعة بنسبة 70%", "زيادة خطر السمنة والسكري", "تدهور الذاكرة والتركيز", "زيادة خطر أمراض القلب", "ارتباط بمرض الزهايمر"]
    },
    "3. اللياقة البدنية\nPhysical Fitness": {
        "أنواع التمارين\nExercise Types": {
            "تمارين المقاومة\nResistance Training": ["التضخم العضلي (Hypertrophy - 8-12 تكرار)", "القوة القصوى (Strength - 1-5 تكرار)", "التحمل العضلي (Endurance - 15+ تكرار)", "التحميل التدريجي (Progressive Overload)"],
            "تمارين القلب\nCardio": ["HIIT - تدريب متقطع عالي الشدة", "LISS - تدريب ثابت منخفض الشدة", "Zone 2 Training - الأهم لصحة القلب", "20-30 دقيقة يومياً كحد أدنى"],
            "المرونة والحركة\nFlexibility & Mobility": ["الإطالة الديناميكية قبل التمرين", "الإطالة الثابتة بعد التمرين", "اليوغا والبيلاتس", "تمارين التنفس (Breathing Exercises)"]
        },
        "الفوائد العلمية المثبتة\nProven Benefits": ["BDNF - بروتين نمو الدماغ (Brain Growth Factor)", "إفراز الإندورفين - مسكن طبيعي", "تقليل خطر السرطان بنسبة 30-50%", "إطالة العمر 3-7 سنوات", "تحسين جودة النوم بنسبة 65%"]
    },
    "4. صناعة الصحة\nThe Health Industry": {
        "صناعة الأدوية\nBig Pharma": {
            "المشاكل\nProblems": ["العلاج أربح من الوقاية (Treatment > Prevention)", "التسويق المباشر للمستهلك (DTC Advertising)", "التأثير على الأبحاث العلمية (Funding Bias)", "أسعار الأدوية الأمريكية - الأغلى عالمياً"],
            "الإيجابيات\nPositives": ["اللقاحات أنقذت ملايين الأرواح", "المضادات الحيوية - ثورة طبية", "أدوية السرطان المناعية (Immunotherapy)", "تقنيات تحرير الجينات (CRISPR)"]
        },
        "الطب التكاملي\nIntegrative Medicine": ["الأعشاب الطبية المثبتة علمياً (الكركم، الزنجبيل)", "الوخز بالإبر - فعال للألم المزمن", "التأمل واليوغا - مثبت علمياً للقلق", "الحمية كدواء (Food as Medicine)"],
        "الصحة الرقمية\nDigital Health": ["الأجهزة القابلة للارتداء (Apple Watch, Oura Ring)", "التطبيب عن بُعد (Telemedicine)", "AI في التشخيص - دقة 94% في سرطان الجلد", "السجلات الصحية الرقمية (EHR)"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1565c0", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#1565c0", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1e88e5", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#1e88e5"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#0d47a1", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#42a5f5"}, "symbolSize": 12, "itemStyle": {"color": "#0d47a1"}},
        {"label": {"fontSize": 13, "color": "#bbdefb", "fontWeight": "bold", "backgroundColor": "#0a2a5e", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#0a2a5e"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#90caf9", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#1976d2"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الصحة والجسد\nHealth & Body", health_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4000px", theme="dark", bg_color="#050d1a", page_title="Health & Body", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الصحة والجسد", subtitle="The Science Behind a Healthy Body & Mind", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#42a5f5", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#90caf9", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "health_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Health Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "health_mindmap.html")
