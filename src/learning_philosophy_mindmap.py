import os
from pyecharts import options as opts
from pyecharts.charts import Tree

learning_map = {
    "1. كيف يتعلم الدماغ\nHow the Brain Learns": {
        "بنية الدماغ التعليمية\nLearning Brain Structure": {
            "القشرة الأمامية\nPrefrontal Cortex": ["التخطيط والتنظيم (Planning)", "اتخاذ القرار (Decision Making)", "التحكم بالانفعالات (Impulse Control)", "الذاكرة العاملة (Working Memory)"],
            "الحُصَين\nHippocampus": ["تكوين الذكريات الجديدة (New Memory Formation)", "التعلم المكاني (Spatial Learning)", "تحويل الذاكرة القصيرة للطويلة أثناء النوم"],
            "اللوزة الدماغية\nAmygdala": ["التعلم العاطفي (Emotional Learning)", "ربط المشاعر بالذكريات", "الخوف يعزز التعلم أحياناً"]
        },
        "المرونة العصبية\nNeuroplasticity": {
            "كيف يعمل\nHow It Works": ["التكرار يقوي المسارات العصبية (Hebbian Learning)", "ما لا تستخدمه تفقده (Use It or Lose It)", "الميالين يسرع النقل العصبي (Myelination)"],
            "حقائق مذهلة\nAmazing Facts": ["الدماغ يُعيد تشكيل نفسه طوال الحياة", "سائقو التاكسي في لندن - حُصَين أكبر (London Taxi Study)", "العمر لا يمنع تكوين خلايا عصبية جديدة (Neurogenesis)"]
        },
        "أنواع الذاكرة\nMemory Types": {
            "نموذج أتكينسون وشيفرين\nAtkinson-Shiffrin Model": ["الذاكرة الحسية - ثوانٍ (Sensory Memory)", "الذاكرة القصيرة - 20-30 ثانية (Short-Term)", "الذاكرة الطويلة - غير محدودة (Long-Term)"],
            "أنواع الذاكرة الطويلة\nLong-Term Types": ["التصريحية: أحداث ومعلومات (Declarative)", "الإجرائية: مهارات حركية (Procedural)", "الدلالية: حقائق عامة (Semantic)", "العرضية: ذكريات شخصية (Episodic)"]
        }
    },
    "2. تقنيات التعلم الفعّال\nEffective Learning Techniques": {
        "الاسترجاع النشط\nActive Recall": {
            "الآلية\nMechanism": ["استرجاع المعلومات = تقوية المسار العصبي", "أقوى من إعادة القراءة بـ 3 مرات (Karpicke Study 2008)", "تأثير الاختبار (Testing Effect)"],
            "الأدوات\nTools": ["البطاقات التعليمية (Anki Flashcards)", "الأسئلة الذاتية (Self-Quizzing)", "الكتابة من الذاكرة (Blank Page Method)", "تعليم شخص آخر (Teach Someone)"]
        },
        "التكرار المتباعد\nSpaced Repetition": {
            "العلم\nScience": ["منحنى النسيان - إبنغهاوس 1885 (Forgetting Curve)", "المراجعة قبل النسيان بقليل = الأمثل", "الفواصل المتزايدة: 1 يوم → 3 → 7 → 14 → 30"],
            "الأدوات\nTools": ["خوارزمية SM-2 (SuperMemo Algorithm)", "تطبيق Anki - الأشهر عالمياً", "نظام لايتنر بالبطاقات (Leitner System)"]
        },
        "طريقة فاينمان\nFeynman Technique": ["1. اختر مفهوماً (Choose a Concept)", "2. اشرحه لطفل بكلمات بسيطة (Explain Simply)", "3. حدد الفجوات وارجع للمصدر (Find Gaps)", "4. بسّط أكثر واستخدم القياسات (Simplify & Analogize)"],
        "تقنيات أخرى مثبتة\nOther Proven Techniques": {
            "التعلم المتشابك\nInterleaving": ["خلط المواضيع أفضل من الحفظ المتسلسل", "أصعب في البداية لكن أعمق", "دراسة Rohrer & Taylor 2007"],
            "الترميز المزدوج\nDual Coding": ["الجمع بين النص والصور (Text + Visuals)", "نظرية بايفيو (Paivio's DCT)", "الخرائط الذهنية والرسوم البيانية"],
            "الربط والقصص\nElaboration": ["ربط المعلومة الجديدة بمعرفة سابقة", "إنشاء قصة أو سياق", "السؤال: لماذا؟ وكيف؟ (Elaborative Interrogation)"]
        }
    },
    "3. أوهام التعلم\nIllusions of Learning": {
        "وهم الإلمام\nFluency Illusion": {
            "الأعراض\nSymptoms": ["إعادة القراءة تعطي إحساساً زائفاً بالفهم", "تظليل النصوص - فعالية 0% تقريباً (Dunlosky 2013)", "مشاهدة المحاضرات = استهلاك سلبي"],
            "الحل\nSolution": ["اختبر نفسك فوراً بعد المذاكرة", "إذا لم تستطع شرحه = لم تفهمه", "الصعوبة المرغوبة (Desirable Difficulty)"]
        },
        "وهم المعرفة\nIllusion of Knowledge": ["تأثير دانينغ-كروجر (Dunning-Kruger Effect)", "الأقل معرفة = الأكثر ثقة", "الخبراء يعرفون حدود جهلهم"],
        "وهم التعدد\nMultitasking Myth": ["الدماغ لا يقوم بمهمتين في وقت واحد فعلياً", "التبديل بين المهام يكلف 40% كفاءة (Task Switching Cost)", "الهاتف في الغرفة يقلل IQ بـ 10 نقاط (Ward Study 2017)"]
    },
    "4. بيئة التعلم المثالية\nOptimal Learning Environment": {
        "حالة التدفق\nFlow State": {
            "شروطها\nConditions": ["التحدي = المهارة (Challenge = Skill)", "أهداف واضحة (Clear Goals)", "تغذية راجعة فورية (Immediate Feedback)", "تركيز عميق بلا مقاطعات"],
            "ميهالي تشيكسنتميهالي\nCsikszentmihalyi": ["اكتشف حالة التدفق 1975", "الوقت يختفي أثناء التدفق", "أعلى مستويات الإنتاجية والسعادة"]
        },
        "تقنية بومودورو\nPomodoro Technique": ["25 دقيقة تركيز + 5 دقائق راحة", "كل 4 بومودورو = راحة 15-30 دقيقة", "فرانشيسكو سيريلو 1987 (Francesco Cirillo)"],
        "النوم والتعلم\nSleep & Learning": ["تثبيت الذاكرة يحدث أثناء النوم العميق", "القيلولة 20-30 دقيقة تعزز الاستيعاب", "الحرمان من النوم يقلل التعلم 40%"],
        "الدافعية\nMotivation": ["الدافع الداخلي vs الخارجي (Intrinsic vs Extrinsic)", "نظرية تقرير المصير: الاستقلالية + الكفاءة + الانتماء (SDT)", "الفضول كأقوى وقود للتعلم"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#7c4dff", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#7c4dff", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#651fff", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#651fff"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#4a148c", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#b388ff"}, "symbolSize": 12, "itemStyle": {"color": "#4a148c"}},
        {"label": {"fontSize": 13, "color": "#e1bee7", "fontWeight": "bold", "backgroundColor": "#311b92", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#311b92"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#ce93d8", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#9c27b0"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("فلسفة التعلم\nThe Philosophy of Learning", learning_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4000px", theme="dark", bg_color="#0d0015", page_title="Learning Philosophy", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="فلسفة التعلم الحقيقي", subtitle="How the Brain Truly Learns — And How You're Doing It Wrong", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#b388ff", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#ce93d8", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "learning_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Learning Philosophy Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "learning_philosophy_mindmap.html")
