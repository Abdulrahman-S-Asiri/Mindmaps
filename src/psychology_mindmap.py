import os
from pyecharts import options as opts
from pyecharts.charts import Tree

psychology_map = {
    "1. مدارس علم النفس\nSchools of Psychology": {
        "التحليل النفسي\nPsychoanalysis": {
            "سيغموند فرويد\nSigmund Freud": {
                "بنية الشخصية\nPersonality Structure": ["الهو - الغرائز البدائية (Id - Primal Drives)", "الأنا - الوسيط الواقعي (Ego - Reality Mediator)", "الأنا العليا - الضمير الأخلاقي (Superego - Moral Conscience)"],
                "آليات الدفاع\nDefense Mechanisms": ["الكبت (Repression)", "الإسقاط (Projection)", "التبرير (Rationalization)", "النكوص (Regression)", "الإزاحة (Displacement)", "التسامي (Sublimation)"],
                "مراحل النمو النفسجنسي\nPsychosexual Stages": ["الفمية (Oral 0-1)", "الشرجية (Anal 1-3)", "القضيبية (Phallic 3-6)", "الكمون (Latency 6-12)", "التناسلية (Genital 12+)"]
            },
            "كارل يونغ\nCarl Jung": {
                "اللاوعي الجمعي\nCollective Unconscious": ["أنماط أولية مشتركة بين البشر (Shared Human Archetypes)", "الموروث النفسي عبر الأجيال (Psychic Heritage)"],
                "الأنماط الأولية\nArchetypes": ["الظل - الجانب المظلم (The Shadow)", "الأنيما/الأنيموس (Anima/Animus)", "الحكيم (The Wise Old Man)", "الذات الكاملة (The Self)", "البطل (The Hero)"],
                "أنماط الشخصية\nPersonality Types": ["الانطوائي مقابل الانبساطي (Introvert vs Extrovert)", "الحدسي مقابل الحسي (Intuitive vs Sensing)", "أساس اختبار MBTI"]
            },
            "ألفريد أدلر\nAlfred Adler": ["عقدة النقص (Inferiority Complex)", "السعي نحو التفوق (Striving for Superiority)", "ترتيب الميلاد والشخصية (Birth Order Theory)"]
        },
        "السلوكية\nBehaviorism": {
            "الاشتراط الكلاسيكي\nClassical Conditioning": ["إيفان بافلوف - تجربة الكلب (Pavlov's Dog)", "المنبه الشرطي وغير الشرطي", "الانطفاء والاسترداد التلقائي (Extinction & Spontaneous Recovery)"],
            "الاشتراط الإجرائي\nOperant Conditioning": ["بي إف سكينر - صندوق سكينر (Skinner Box)", "التعزيز الإيجابي والسلبي (Positive & Negative Reinforcement)", "العقاب وتأثيره (Punishment)", "جداول التعزيز (Schedules of Reinforcement)"],
            "التعلم بالملاحظة\nObservational Learning": ["ألبرت باندورا (Albert Bandura)", "تجربة دمية بوبو (Bobo Doll Experiment)", "الكفاءة الذاتية (Self-Efficacy)"]
        },
        "علم النفس الإنساني\nHumanistic": {
            "أبراهام ماسلو\nAbraham Maslow": ["الاحتياجات الفسيولوجية (Physiological)", "الأمان (Safety)", "الانتماء والحب (Belonging)", "التقدير (Esteem)", "تحقيق الذات (Self-Actualization)", "التسامي (Self-Transcendence)"],
            "كارل روجرز\nCarl Rogers": ["التقبل غير المشروط (Unconditional Positive Regard)", "التطابق بين الذات الحقيقية والمثالية (Congruence)", "العلاج المتمركز حول العميل (Client-Centered Therapy)"]
        },
        "علم النفس المعرفي\nCognitive Psychology": {
            "معالجة المعلومات\nInformation Processing": ["الانتباه الانتقائي (Selective Attention)", "الترميز والتخزين والاسترجاع (Encoding, Storage, Retrieval)", "نظرية المعالجة المزدوجة - كانيمان (Dual Process Theory)"],
            "التشوهات المعرفية\nCognitive Distortions": ["التفكير الكل-أو-لاشيء (All-or-Nothing Thinking)", "التكبير والتصغير (Magnification & Minimization)", "القراءة الذهنية (Mind Reading)", "التهويل (Catastrophizing)"]
        }
    },
    "2. الوعي والعقل\nConsciousness & Mind": {
        "مستويات الوعي\nLevels of Awareness": {
            "الوعي الكامل\nFull Consciousness": ["الإدراك الحسي (Sensory Awareness)", "الوعي بالذات (Self-Awareness)", "الوعي الانعكاسي (Reflective Consciousness)"],
            "ما قبل الوعي\nPreconscious": ["الذكريات القابلة للاستدعاء (Retrievable Memories)", "المعرفة السلبية (Passive Knowledge)"],
            "اللاوعي\nUnconscious": ["الرغبات المكبوتة (Repressed Desires)", "الصدمات المنسية (Forgotten Traumas)", "الدوافع الخفية (Hidden Motives)"]
        },
        "حالات الوعي المتغيرة\nAltered States": {
            "النوم والأحلام\nSleep & Dreams": ["مراحل النوم الـ 4 (4 Sleep Stages)", "حركة العين السريعة REM", "الأحلام الواضحة (Lucid Dreaming)", "نظريات تفسير الأحلام (Dream Theories)"],
            "التأمل\nMeditation": ["تأمل اليقظة (Mindfulness Meditation)", "التأمل التجاوزي (Transcendental Meditation)", "حالة التدفق (Flow State - Csikszentmihalyi)"],
            "التنويم الإيحائي\nHypnosis": ["القابلية للتنويم (Hypnotic Suggestibility)", "الاستخدامات العلاجية (Therapeutic Uses)", "أسطورة مقابل حقيقة (Myth vs Fact)"]
        },
        "الدماغ والعقل\nBrain vs Mind": {
            "البنية العصبية\nNeural Architecture": ["100 مليار خلية عصبية (100 Billion Neurons)", "التشابكات العصبية (Synapses)", "المرونة العصبية (Neuroplasticity)"],
            "الناقلات العصبية\nNeurotransmitters": ["الدوبامين - المكافأة (Dopamine - Reward)", "السيروتونين - المزاج (Serotonin - Mood)", "النورإبينفرين - اليقظة (Norepinephrine - Alertness)", "GABA - الاسترخاء (GABA - Relaxation)", "الأستيل كولين - الذاكرة (Acetylcholine - Memory)"],
            "مشكلة الوعي الصعبة\nHard Problem": ["لماذا نختبر الأشياء ذاتياً؟ (Why Subjective Experience?)", "فجوة التفسير (Explanatory Gap)", "موقف ديفيد تشالمرز (David Chalmers)"]
        }
    },
    "3. الذكاء العاطفي\nEmotional Intelligence (EQ)": {
        "نموذج دانييل غولمان\nGoleman's Model": {
            "الوعي الذاتي\nSelf-Awareness": ["التعرف على المشاعر (Recognizing Emotions)", "تقييم الذات الدقيق (Accurate Self-Assessment)", "الثقة بالنفس (Self-Confidence)"],
            "التنظيم الذاتي\nSelf-Regulation": ["ضبط الانفعالات (Impulse Control)", "المرونة والتكيف (Adaptability)", "النزاهة (Conscientiousness)"],
            "الدافعية\nMotivation": ["الدافع الداخلي (Intrinsic Drive)", "التفاؤل الواقعي (Realistic Optimism)", "الالتزام بالأهداف (Goal Commitment)"],
            "التعاطف\nEmpathy": ["قراءة مشاعر الآخرين (Reading Others)", "الاستجابة العاطفية (Emotional Responsiveness)", "التوجه الخدمي (Service Orientation)"],
            "المهارات الاجتماعية\nSocial Skills": ["القيادة (Leadership)", "إدارة النزاعات (Conflict Management)", "بناء العلاقات (Building Bonds)", "التأثير والإقناع (Influence & Persuasion)"]
        },
        "EQ مقابل IQ\nEQ vs IQ": ["IQ يتنبأ بـ 20% فقط من النجاح", "EQ أهم في القيادة والعلاقات", "EQ قابل للتطوير بعكس IQ"]
    },
    "4. الصحة النفسية\nMental Health": {
        "الاضطرابات الشائعة\nCommon Disorders": {
            "اضطرابات القلق\nAnxiety Disorders": ["القلق المعمم (GAD)", "اضطراب الهلع (Panic Disorder)", "الرهاب الاجتماعي (Social Phobia)", "الوسواس القهري (OCD)"],
            "اضطرابات المزاج\nMood Disorders": ["الاكتئاب الشديد (Major Depression)", "ثنائي القطب (Bipolar Disorder)", "الاكتئاب الموسمي (Seasonal Affective Disorder)"],
            "اضطرابات الشخصية\nPersonality Disorders": ["النرجسية (Narcissistic PD)", "الحدية (Borderline PD)", "المعادية للمجتمع (Antisocial PD)"],
            "اضطرابات الصدمة\nTrauma Disorders": ["اضطراب ما بعد الصدمة PTSD", "اضطراب الصدمة الحاد (Acute Stress)", "الصدمات المعقدة (Complex PTSD)"]
        },
        "العلاجات النفسية\nPsychotherapies": {
            "العلاج المعرفي السلوكي CBT": ["تحدي الأفكار السلبية (Challenging Negative Thoughts)", "إعادة الهيكلة المعرفية (Cognitive Restructuring)", "التعرض التدريجي (Gradual Exposure)"],
            "علاجات أخرى\nOther Therapies": ["العلاج بالتقبل والالتزام ACT", "العلاج الجدلي السلوكي DBT", "EMDR - إزالة حساسية حركة العين", "العلاج النفسي الديناميكي (Psychodynamic)"]
        },
        "وصمة المرض النفسي\nMental Health Stigma": ["المرض النفسي ليس ضعفاً (Not a Weakness)", "1 من كل 4 أشخاص يتأثر (1 in 4 People Affected)", "العلاج فعال ومتاح (Treatment Works)"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#00e676", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#00e676", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#69f0ae", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#69f0ae"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#2e7d32", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#66bb6a"}, "symbolSize": 12, "itemStyle": {"color": "#2e7d32"}},
        {"label": {"fontSize": 13, "color": "#c8e6c9", "fontWeight": "bold", "backgroundColor": "#1b5e20", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#1b5e20"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#a5d6a7", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#4caf50"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("علم النفس البشري\nHuman Psychology", psychology_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4000px", theme="dark", bg_color="#071a0a", page_title="Human Psychology", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="علم النفس البشري", subtitle="Understanding the Human Mind", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#00e676", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#a5d6a7", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "psychology_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Psychology Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "psychology_mindmap.html")
