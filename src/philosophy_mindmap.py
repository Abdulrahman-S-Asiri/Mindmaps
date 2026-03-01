import os
from pyecharts import options as opts
from pyecharts.charts import Tree

philosophy_map = {
    "1. فروع الفلسفة\nBranches of Philosophy": {
        "الميتافيزيقا\nMetaphysics": {
            "طبيعة الوجود\nNature of Being": ["الوجودية - سارتر (Existentialism)", "العدمية - نيتشه (Nihilism)", "المثالية - هيغل (Idealism)", "المادية - ماركس (Materialism)"],
            "أسئلة كبرى\nBig Questions": ["لماذا يوجد شيء بدل لا شيء؟", "هل الوعي مادي أم غير مادي؟", "هل الكون مصمم أم عشوائي؟", "هل الإرادة الحرة حقيقية؟ (Free Will)"]
        },
        "الإبستمولوجيا\nEpistemology": {
            "مصادر المعرفة\nSources of Knowledge": ["العقلانية - ديكارت (Rationalism)", "التجريبية - جون لوك (Empiricism)", "النقدية - كانط (Critical Philosophy)", "الذرائعية - جون ديوي (Pragmatism)"],
            "مشاكل المعرفة\nProblems": ["مشكلة الاستقراء - هيوم (Problem of Induction)", "الشك المنهجي - ديكارت (Methodical Doubt)", "معضلة غيتير (Gettier Problem)"]
        },
        "الأخلاق\nEthics": {
            "المدارس الأخلاقية\nEthical Schools": ["النفعية - جيريمي بنثام ومِل (Utilitarianism)", "الأخلاق الواجبية - كانط (Deontology)", "أخلاق الفضيلة - أرسطو (Virtue Ethics)", "العقد الاجتماعي - روسو وهوبز (Social Contract)"],
            "معضلات أخلاقية\nMoral Dilemmas": ["معضلة العربة (Trolley Problem)", "هل الأخلاق نسبية أم مطلقة؟", "أخلاقيات الذكاء الاصطناعي"]
        },
        "فلسفة العقل\nPhilosophy of Mind": ["ثنائية ديكارت: عقل وجسد (Mind-Body Dualism)", "الطبيعانية: العقل = الدماغ (Physicalism)", "مشكلة الوعي الصعبة (Hard Problem of Consciousness)", "الغرفة الصينية - سيرل (Chinese Room - Searle)"]
    },
    "2. الفلاسفة عبر التاريخ\nPhilosophers Through History": {
        "الفلسفة اليونانية\nAncient Greek": {
            "ما قبل سقراط\nPre-Socratic": ["طاليس - الماء أصل كل شيء (Thales)", "هرقليطس - كل شيء يتغير (Heraclitus)", "بارمنيدس - الوجود ثابت (Parmenides)", "ديموقريطس - الذرة (Democritus)"],
            "الثلاثة الكبار\nThe Big Three": ["سقراط - أعرف أنني لا أعرف", "أفلاطون - عالم المثل والكهف", "أرسطو - المنطق والفحص التجريبي"]
        },
        "الفلسفة الإسلامية\nIslamic Philosophy": ["الكندي - فيلسوف العرب الأول", "الفارابي - المدينة الفاضلة (Al-Farabi)", "ابن سينا - الوجود والماهية (Avicenna)", "ابن رشد - التوفيق بين الفلسفة والدين (Averroes)", "الغزالي - تهافت الفلاسفة (Al-Ghazali)"],
        "الفلسفة الحديثة\nModern Philosophy": {
            "عصر التنوير\nEnlightenment": ["ديكارت - أنا أفكر إذن أنا موجود (Cogito)", "كانط - نقد العقل المحض (Critique of Pure Reason)", "هيوم - الشك التجريبي (Empirical Skepticism)"],
            "القرن 19-20\nModern Era": ["نيتشه - موت الإله وإرادة القوة (Will to Power)", "هايدغر - الوجود والزمان (Being and Time)", "سارتر - الوجود يسبق الماهية (Existence Precedes Essence)", "فتغنشتاين - حدود اللغة (Limits of Language)", "ألبير كامو - العبثية (Absurdism - The Myth of Sisyphus)"]
        }
    },
    "3. فلسفة العلم والتكنولوجيا\nPhilosophy of Science & Tech": {
        "فلسفة العلم\nPhil. of Science": ["كارل بوبر - قابلية التكذيب (Falsifiability)", "توماس كون - الثورات العلمية (Paradigm Shifts)", "بول فايرابند - ضد المنهج (Against Method)", "مشكلة الترسيم (Demarcation Problem)"],
        "فلسفة التكنولوجيا\nPhil. of Technology": ["هل التكنولوجيا محايدة؟ (Is Tech Neutral?)", "التفرد التكنولوجي (Technological Singularity)", "أخلاقيات الذكاء الاصطناعي (AI Ethics)", "هايدغر والتقنية (The Question Concerning Technology)"]
    },
    "4. التفكير النقدي\nCritical Thinking": {
        "أدوات التفكير\nThinking Tools": ["شفرة أوكام (Occam's Razor)", "شفرة هانلون (Hanlon's Razor)", "الشك المنهجي (Systematic Doubt)", "الفولاذمان (Steelman) مقابل رجل القش (Strawman)"],
        "المغالطات المنطقية\nLogical Fallacies": ["الشخصنة (Ad Hominem)", "الاحتكام للسلطة (Appeal to Authority)", "المنحدر الزلق (Slippery Slope)", "ثنائية زائفة (False Dichotomy)", "الاحتكام للمشاعر (Appeal to Emotion)", "ما بعده إذن بسببه (Post Hoc)"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#b0bec5", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#b0bec5", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#546e7a", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#546e7a"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#37474f", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#78909c"}, "symbolSize": 12, "itemStyle": {"color": "#37474f"}},
        {"label": {"fontSize": 13, "color": "#cfd8dc", "fontWeight": "bold", "backgroundColor": "#263238", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#263238"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#90a4ae", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#607d8b"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الفلسفة العميقة\nDeep Philosophy", philosophy_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4000px", theme="dark", bg_color="#101418", page_title="Deep Philosophy", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الفلسفة العميقة", subtitle="From Socrates to Sartre — The Ultimate Philosophical Journey", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#b0bec5", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#78909c", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "philosophy_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Philosophy Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "philosophy_mindmap.html")
