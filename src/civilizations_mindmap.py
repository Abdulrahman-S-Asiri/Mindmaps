import os
from pyecharts import options as opts
from pyecharts.charts import Tree

civilizations_map = {
    "1. الحضارة الإسلامية\nIslamic Civilization": {
        "العصر الذهبي (750-1258)\nGolden Age": {
            "بيت الحكمة\nHouse of Wisdom": ["بغداد - عاصمة العلم العالمي", "ترجمة التراث اليوناني والفارسي والهندي", "أكبر مكتبة في العالم آنذاك", "مركز بحثي متعدد التخصصات"],
            "عباقرة العلوم\nScientific Geniuses": {
                "الرياضيات\nMathematics": ["الخوارزمي - أبو الجبر (Al-Khwarizmi - Algebra)", "اختراع الصفر والنظام العشري", "عمر الخيام - حل المعادلات التكعيبية"],
                "الطب\nMedicine": ["ابن سينا - القانون في الطب (Avicenna)", "الرازي - أبو الطب السريري (Al-Razi)", "الزهراوي - أبو الجراحة الحديثة (Al-Zahrawi)", "ابن النفيس - اكتشاف الدورة الدموية الصغرى"],
                "البصريات والفيزياء\nOptics & Physics": ["ابن الهيثم - أبو البصريات (Ibn al-Haytham)", "كتاب المناظر - أسس المنهج العلمي التجريبي", "شرح الكاميرا المظلمة (Camera Obscura)"],
                "الكيمياء\nChemistry": ["جابر بن حيان - أبو الكيمياء (Jabir ibn Hayyan)", "اكتشاف حمض الهيدروكلوريك والنتريك", "التقطير والتبلور والتسامي"],
                "الفلك\nAstronomy": ["البيروني - حساب محيط الأرض", "الإدريسي - خريطة العالم الأدق", "المراصد الفلكية في سمرقند"]
            }
        },
        "العمارة والفنون\nArchitecture & Arts": ["الأندلس وقصر الحمراء (Alhambra)", "مسجد قرطبة الكبير", "الخط العربي كفن راقٍ", "الزخرفة الهندسية والأرابيسك (Arabesque)", "قبة الصخرة في القدس"],
        "النظم والمؤسسات\nSystems & Institutions": ["الوقف الإسلامي (Waqf - أول مؤسسة خيرية دائمة)", "البيمارستان (أول مستشفى حديث)", "نظام الحسبة (رقابة السوق والجودة)", "المدارس النظامية (أول جامعات منظمة)"]
    },
    "2. الحضارة اليونانية\nGreek Civilization": {
        "الفلاسفة الكبار\nGreat Philosophers": {
            "سقراط (469-399 ق.م)\nSocrates": ["المنهج السقراطي - الأسئلة التوليدية", "اعرف نفسك (Know Thyself)", "محاكمته وإعدامه بالسم"],
            "أفلاطون (428-348 ق.م)\nPlato": ["نظرية المُثل (Theory of Forms)", "أسطورة الكهف (Allegory of the Cave)", "الجمهورية (The Republic)", "أكاديمية أثينا (Plato's Academy)"],
            "أرسطو (384-322 ق.م)\nAristotle": ["أبو المنطق الصوري (Formal Logic)", "الأخلاق النيقوماخية (Nicomachean Ethics)", "السياسة والدستور", "معلم الإسكندر الأكبر"]
        },
        "العلوم اليونانية\nGreek Sciences": {
            "الرياضيات\nMaths": ["إقليدس - أصول الهندسة (Euclid - Elements)", "فيثاغورس - النظرية الشهيرة (Pythagorean Theorem)", "أرخميدس - الطفو والروافع (Archimedes)"],
            "الطب\nMedicine": ["أبقراط - أبو الطب (Hippocrates)", "القسم الطبي (Hippocratic Oath)", "جالينوس - التشريح (Galen)"]
        },
        "الديمقراطية الأثينية\nAthenian Democracy": ["أول نظام ديمقراطي مباشر (508 ق.م)", "كليسثنيس - أبو الديمقراطية", "مجلس الـ 500 (Boule)", "حق التصويت للمواطنين الذكور فقط", "استبعاد النساء والعبيد والأجانب"]
    },
    "3. الحضارة الصينية\nChinese Civilization": {
        "الاختراعات العظمى\nGreat Inventions": {
            "الأربعة الكبرى\nFour Great": ["الورق - تساي لون 105م (Cai Lun)", "البوصلة - عهد هان (Han Dynasty)", "البارود - عهد تانغ (Tang Dynasty)", "الطباعة - بي شنغ (Bi Sheng)"],
            "اختراعات أخرى\nOther Inventions": ["الحرير (Silk)", "الخزف والبورسلين (Porcelain)", "العملات الورقية (Paper Money)", "الساعة المائية (Water Clock)"]
        },
        "الفلسفات الصينية\nChinese Philosophies": {
            "كونفوشيوس\nConfucius": ["الأخلاق والنظام الاجتماعي", "بر الوالدين واحترام الكبير", "التعليم كطريق للفضيلة"],
            "لاو تزو - الطاوية\nLao Tzu - Taoism": ["الطاو - الطريق (The Way)", "التوازن: يين ويانغ (Yin & Yang)", "البساطة والتناغم مع الطبيعة"],
            "صن تزو\nSun Tzu": ["فن الحرب (The Art of War)", "أعظم انتصار بلا قتال", "الإستراتيجية الحربية والنفسية"]
        },
        "الإنجازات الكبرى\nMajor Achievements": ["سور الصين العظيم (6,259 كم)", "طريق الحرير - أول شبكة تجارة عالمية", "جيش التيراكوتا (8,000 جندي طيني)", "قناة الإمبراطور الكبرى (Grand Canal)"]
    },
    "4. حضارة مصر القديمة\nAncient Egypt": {
        "الأهرامات والعمارة\nPyramids & Architecture": {
            "هرم الجيزة الأكبر\nGreat Pyramid": ["بناه الملك خوفو (2560 ق.م)", "2.3 مليون كتلة حجرية", "دقة هندسية مذهلة - خطأ 0.05%", "أطول مبنى لمدة 3800 سنة"],
            "معابد ومقابر\nTemples & Tombs": ["وادي الملوك (Valley of the Kings)", "معبد الكرنك (Karnak Temple)", "أبو سمبل (Abu Simbel)"]
        },
        "العلوم المصرية\nEgyptian Sciences": ["التحنيط - حفظ الجثث آلاف السنين (Mummification)", "الهيروغليفية - أقدم نظام كتابة (Hieroglyphics)", "حجر رشيد (Rosetta Stone - 196 ق.م)", "التقويم الشمسي 365 يوم (Solar Calendar)", "الجراحة المبكرة - بردية إدوين سميث (Edwin Smith Papyrus)"],
        "الحكم والمجتمع\nGovernance": ["الفرعون كإله حي (God-King)", "نظام البيروقراطية (أول نظام إداري)", "الكتبة والكهنة كنخبة مثقفة"]
    },
    "5. الحضارة الرومانية\nRoman Civilization": {
        "الهندسة والقانون\nEngineering & Law": {
            "الإنجازات الهندسية\nEngineering Feats": ["الطرق الرومانية - 400,000 كم (Roman Roads)", "القنوات المائية (Aqueducts)", "الكولوسيوم - 50,000 متفرج (Colosseum)", "نظام الصرف الصحي (Sewage System)"],
            "القانون الروماني\nRoman Law": ["أساس كل القانون الغربي الحديث", "مبدأ البراءة حتى إثبات الإدانة", "حق الملكية والعقود", "القانون المدني (Civil Law)"]
        },
        "من الجمهورية إلى الإمبراطورية\nRepublic to Empire": {
            "الجمهورية\nRepublic": ["مجلس الشيوخ (Senate)", "القناصل والتريبيون (Consuls & Tribunes)", "الحروب البونيقية ضد قرطاج (Punic Wars)"],
            "الإمبراطورية\nEmpire": ["يوليوس قيصر - نهاية الجمهورية (Julius Caesar)", "أغسطس - أول إمبراطور (Augustus)", "Pax Romana - 200 سنة سلام", "سقوط روما الغربية 476م"],
            "أسباب السقوط\nReasons for Fall": ["الانحلال الأخلاقي والترف", "الغزوات البربرية (Barbarian Invasions)", "التضخم وانهيار العملة", "الانقسام بين شرق وغرب"]
        }
    },
    "📚 المراجع\nReferences": ["Ibn Khaldun - Al-Muqaddimah (1377)", "Will Durant - Story of Civilization", "Arnold Toynbee - A Study of History", "Edward Gibbon - Decline and Fall of the Roman Empire (1776)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#8d6e63", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#8d6e63", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#bcaaa4", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#bcaaa4"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#5d4037", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#a1887f"}, "symbolSize": 12, "itemStyle": {"color": "#5d4037"}},
        {"label": {"fontSize": 13, "color": "#d7ccc8", "fontWeight": "bold", "backgroundColor": "#3e2723", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#3e2723"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#bcaaa4", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#795548"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("تاريخ الحضارات\nHistory of Civilizations", civilizations_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4500px", theme="dark", bg_color="#1a1210", page_title="Civilizations", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="تاريخ الحضارات العظمى", subtitle="The Great Civilizations That Shaped Humanity", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#bcaaa4", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#8d6e63", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "civilizations_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Civilizations Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "civilizations_mindmap.html")
