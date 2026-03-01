import os
from pyecharts import options as opts
from pyecharts.charts import Tree

quantum_map = {
    "1. أساسيات ميكانيكا الكم\nQuantum Mechanics Basics": {
        "ثورة الكم\nThe Quantum Revolution": {
            "أزمة الفيزياء الكلاسيكية\nClassical Physics Crisis": ["كارثة الأشعة فوق البنفسجية (Ultraviolet Catastrophe)", "التأثير الكهروضوئي (Photoelectric Effect - Einstein 1905)", "طيف الجسم الأسود (Blackbody Radiation)"],
            "الآباء المؤسسون\nFounding Fathers": ["ماكس بلانك - كم الطاقة 1900 (Max Planck)", "نيلز بور - نموذج الذرة 1913 (Niels Bohr)", "فيرنر هايزنبرغ - مبدأ عدم اليقين (Heisenberg)", "إرفين شرودنغر - المعادلة الموجية (Schrödinger)", "بول ديراك - المعادلة النسبية (Dirac)"]
        },
        "المبادئ الأساسية\nCore Principles": {
            "ازدواجية الموجة-الجسيم\nWave-Particle Duality": ["الضوء جسيم وموجة معاً (De Broglie 1924)", "تجربة الشق المزدوج (Double-Slit Experiment)", "كل مادة لها طول موجي (Matter Waves)"],
            "مبدأ عدم اليقين\nUncertainty Principle": ["لا يمكن معرفة الموضع والسرعة معاً بدقة", "ΔxΔp ≥ ℏ/2 (Heisenberg 1927)", "ليس قصوراً في القياس بل طبيعة الكون"],
            "التراكب الكمي\nSuperposition": ["الجسيم في كل الحالات معاً حتى القياس", "قطة شرودنغر (Schrödinger's Cat)", "الدالة الموجية Ψ (Wave Function)"],
            "انهيار الدالة الموجية\nWave Function Collapse": ["القياس يُجبر الجسيم على حالة واحدة", "مشكلة القياس (Measurement Problem)", "هل المراقب يغير الواقع؟ (Observer Effect)"]
        }
    },
    "2. ظواهر كمية مذهلة\nMind-Blowing Phenomena": {
        "التشابك الكمي\nQuantum Entanglement": ["آينشتاين سماه: التأثير الشبحي عن بُعد (Spooky Action)", "جسيمان مرتبطان بغض النظر عن المسافة", "تجارب جون بيل 1964 (Bell's Theorem)", "جائزة نوبل 2022: Aspect, Clauser, Zeilinger"],
        "النفق الكمي\nQuantum Tunneling": ["الجسيم يخترق حاجز مستحيل كلاسيكياً", "يفسر الاندماج النووي في الشمس", "أساس عمل الترانزستور والمجهر STM"],
        "التداخل الكمي\nQuantum Interference": ["الأنماط الموجية (Interference Patterns)", "تجربة الشق المزدوج بإلكترونات فردية", "الممحاة الكمية (Quantum Eraser Experiment)"]
    },
    "3. تفسيرات ميكانيكا الكم\nInterpretations": {
        "تفسير كوبنهاغن\nCopenhagen": ["بور وهايزنبرغ - التفسير السائد", "الواقع لا يوجد قبل القياس", "الدالة الموجية أداة حسابية فقط"],
        "تفسير العوالم المتعددة\nMany-Worlds": ["هيو إيفرت 1957 (Hugh Everett)", "كل قياس يخلق أكواناً موازية", "لا انهيار للدالة الموجية"],
        "نظرية الموجة المرشدة\nPilot Wave": ["ديفيد بوم (David Bohm)", "الجسيمات حقيقية + موجة ترشدها", "حتمية لكن غير محلية"],
        "تفسير QBism": ["الكم = درجات اعتقاد شخصية", "لا واقع موضوعي مستقل", "كريس فوكس (Chris Fuchs)"]
    },
    "4. التطبيقات والمستقبل\nApplications & Future": {
        "الحوسبة الكمية\nQuantum Computing": {
            "الأساسيات\nBasics": ["الكيوبت (Qubit) مقابل البت الكلاسيكي", "التراكب: 0 و 1 معاً", "التشابك يربط الكيوبتات", "التفوق الكمي (Quantum Supremacy - Google 2019)"],
            "الشركات والأجهزة\nCompanies": ["IBM Quantum - 1,121 كيوبت (Condor)", "Google Sycamore - أول تفوق كمي", "IonQ - أيونات محاصرة", "D-Wave - التلدين الكمي (Quantum Annealing)"]
        },
        "التشفير الكمي\nQuantum Cryptography": ["توزيع المفاتيح الكمية QKD", "أي تنصت = كشف فوري", "تهديد التشفير الكلاسيكي (Post-Quantum Crypto)"],
        "تطبيقات أخرى\nOther Applications": ["أجهزة استشعار فائقة الدقة (Quantum Sensors)", "محاكاة الجزيئات لاكتشاف الأدوية", "الإنترنت الكمي (Quantum Internet)", "الساعات الذرية (Atomic Clocks)"]
    }
    "📚 المراجع\nReferences": ["Richard Feynman - QED: The Strange Theory of Light (1985)", "Brian Greene - The Elegant Universe (1999)", "Carlo Rovelli - Seven Brief Lessons on Physics (2014)", "Nobel Prize 2022 - Aspect, Clauser, Zeilinger", "Sean Carroll - Something Deeply Hidden (2019)"],
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#e040fb", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#e040fb", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#aa00ff", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#aa00ff"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#6a1b9a", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#ce93d8"}, "symbolSize": 12, "itemStyle": {"color": "#6a1b9a"}},
        {"label": {"fontSize": 13, "color": "#e1bee7", "fontWeight": "bold", "backgroundColor": "#4a148c", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#4a148c"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#ce93d8", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#7b1fa2"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الفيزياء الكمية\nQuantum Physics", quantum_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4000px", theme="dark", bg_color="#0d001a", page_title="Quantum Physics", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الفيزياء الكمية", subtitle="The Strange World of Quantum Mechanics", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#e040fb", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#ce93d8", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "quantum_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Quantum Physics Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "quantum_physics_mindmap.html")
