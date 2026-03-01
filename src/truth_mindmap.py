import os
from pyecharts import options as opts
from pyecharts.charts import Tree

# ─── 1. Deep & Detailed Data Structure ─────────────────────────
absolute_truth_map = {
    "1. الجذور والأصل\nOrigin & Foundations": {
        "المنظور الفلسفي\nPhilosophical": {
            "الابستمولوجيا (نظرية المعرفة)\nEpistemology": ["التجريبية (Empiricism)", "العقلانية (Rationalism)", "الذرائعية (Pragmatism)"],
            "الميتافيزيقا (ما وراء الطبيعة)\nMetaphysics": ["الوجودية (Existentialism)", "العدمية (Nihilism)", "الحتمية (Determinism)"]
        },
        "المنظور الديني\nReligious": {
            "الوحي الإلهي\nDivine Revelation": ["الكتب السماوية", "رسالات الأنبياء", "السنن الكونية"],
            "العقيدة واليقين\nFaith & Certainty": ["التوحيد", "الغيبيات", "البعث أو الجزاء"]
        },
        "المنظور العلمي\nScientific": {
            "الفيزياء الكونية\nCosmology": ["نشأة الكون (Big Bang)", "الضبط الدقيق (Fine-Tuning)", "الأنتروبيا (Entropy)"],
            "ميكانيكا الكم\nQuantum Mechanics": ["مبدأ عدم اليقين (Uncertainty)", "المراقب والتأثير (Observer Effect)"],
            "الرياضيات والمنطق\nMath & Logic": ["التجريد المطلق", "مبرهنات عدم الاكتمال لغودل"]
        }
    },
    "2. كيف نعرفها؟\nHow to know? (Tools)": {
        "العقل والمنطق\nReason & Logic": ["الاستنتاج (Deduction)", "الاستقراء (Induction)", "البديهيات (Axioms)"],
        "الحواس والتجربة\nSenses & Experience": ["المنهج التجريبي (Empirical Method)", "الملاحظة الدقيقة (Observation)", "القابلية للتكرار (Replicability)"],
        "الحدس والبصيرة\nIntuition & Insight": ["التأمل العميق (Deep Contemplation)", "الفطرة السليمة (Innate Nature)", "الوعي الداخلي (Inner Consciousness)"],
        "النقل والتاريخ\nTransmission & History": ["التواتر (Continuous Testimony)", "التدقيق المصدري (Source Verification)", "الآثار التاريخية (Artifacts)"]
    },
    "3. عقبات وأوهام\nObstacles & Illusions": {
        "أوهام معرفية\nCognitive Biases": {
            "الانحيازات\nBiases": ["الانحياز التأكيدي (Confirmation Bias)", "تأثير دانينغ-كروجر", "تأثير الهالة (Halo Effect)"],
            "المغالطات\nFallacies": ["الرجل القش (Strawman)", "الشخصنة (Ad Hominem)", "الاحتكام للجهل"]
        },
        "أمراض الفكر المعاصر\nModern Intellectual Diseases": ["عصر ما بعد الحقيقة (Post-truth)", "النسبية الأخلاقية (Moral Relativism)", "التشكيك المطلق (Radical Skepticism)"],
        "أهواء نفسية ومجتمعية\nPsychological & Social": ["الغرور المعرفي (Intellectual Arrogance)", "الخوف من المجهول", "عقلية القطيع (Herd Mentality)"]
    },
    "4. بناء اليقين ومراحله\nStages of Certainty": {
        "المرحلة 1: التخلية\nStage 1: Unlearning": ["الاعتراف بالجهل (Admitting Ignorance)", "كسر الأصنام الفكرية (Shattering False Dogmas)", "طرح الأسئلة الصعبة (Asking Hard Questions)"],
        "المرحلة 2: التحلية\nStage 2: Learning": ["جمع البيانات بموضوعية (Objective Data Gathering)", "تعريض النفس للآراء المخالفة (Exposure to Antagonists)", "فهم السياق التاريخي (Historical Context)"],
        "المرحلة 3: الغربلة\nStage 3: Filtration": ["التحليل النقدي الصارم (Strict Critical Analysis)", "كشف التناقضات (Finding Contradictions)", "استخدام شفرة أوكام (Occam's Razor)"],
        "المرحلة 4: درجات اليقين\nStage 4: Degrees of Certainty": ["علم اليقين (بالعقل والبرهان)", "عين اليقين (بالمشاهدة والقياس)", "حق اليقين (بالمعايشة والتجربة)"]
    },
    "5. ثمار الوصول\nThe Fruits of Truth": {
        "على مستوى الفرد\nIndividual Level": ["السكينة والاطمئنان (Inner Peace)", "استقلالية التفكير (Independent Thinking)", "الشجاعة الأخلاقية (Moral Courage)"],
        "على مستوى المجتمع\nSocietal Level": ["العدالة المطلقة (Absolute Justice)", "نهضة حضارية واعية (Conscious Civilization)", "تأسيس نظم غير قابلة للفساد (Incorruptible Systems)"]
    }
}

# ─── 2. Rich Professional Styling by Depth ─────────────────────
def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    
    # Custom Truth Theme (Gold / Amber / Deep Navy)
    if depth == 0:
        node["label"] = {
            "fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", 
            "backgroundColor": "#ffd700", "padding": [16, 28], "borderRadius": 12
        }
        node["symbolSize"] = 35
        node["itemStyle"] = {"color": "#ffd700", "borderColor": "#ffffff", "borderWidth": 3}

    elif depth == 1:
        node["label"] = {
            "fontSize": 16, "color": "#111111", "fontWeight": "bold", 
            "backgroundColor": "#ffb822", "padding": [10, 20], "borderRadius": 8
        }
        node["symbolSize"] = 20
        node["itemStyle"] = {"color": "#ffb822"}

    elif depth == 2:
        node["label"] = {
            "fontSize": 14, "color": "#ffffff", "fontWeight": "bold",
            "backgroundColor": "#d17a22", "padding": [6, 14], "borderRadius": 6,
            "borderWidth": 1, "borderColor": "#e28743"
        }
        node["symbolSize"] = 12
        node["itemStyle"] = {"color": "#d17a22"}

    elif depth == 3:
        node["label"] = {
            "fontSize": 13, "color": "#f8f9fa",
            "backgroundColor": "#2c3e50", "padding": [4, 10], "borderRadius": 4,
        }
        node["symbolSize"] = 8
        node["itemStyle"] = {"color": "#2c3e50"}

    else:
        node["label"] = {
            "fontSize": 12, "color": "#b0b8c1",
            "backgroundColor": "transparent"
        }
        node["symbolSize"] = 6
        node["itemStyle"] = {"color": "#6c7a89"}

    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
        
    return node

root_label = "الحقيقة المطلقة\nAbsolute Truth"
tree_data = [dict_to_tree(root_label, absolute_truth_map)]

# ─── 3. Generate the Interactive Mindmap ───────────────────────
def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(
        width="100%", 
        height="2400px", 
        theme="dark",
        bg_color="#05080f", # Very dark deep navy
        page_title="Absolute Truth",
        renderer="svg"
    ))
    
    c.add(
        series_name="",
        data=data,
        orient="LR",
        initial_tree_depth=-1,
        symbol="emptyCircle",
        edge_shape="curve",
        edge_fork_position="60%",
        is_roam=True,
        label_opts=opts.LabelOpts(position="right")
    )
    
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title="رحلة البحث عن الحقيقة المطلقة",
            subtitle="The Ultimate Journey to the Absolute Truth",
            pos_left="center",
            pos_top="2%",
            title_textstyle_opts=opts.TextStyleOpts(color="#ffd700", font_size=40, font_weight="bolder"),
            subtitle_textstyle_opts=opts.TextStyleOpts(color="#bdc3c7", font_size=20)
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "saveAsImage": {"type": "png", "name": "absolute_truth_map", "title": "Save PNG", "pixelRatio": 4}
            }
        )
    )
    
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Enhanced Mindmap generated successfully: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "absolute_truth_mindmap.html")
