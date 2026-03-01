import os
from pyecharts import options as opts
from pyecharts.charts import Tree

space_map = {
    "1. النظام الشمسي\nThe Solar System": {
        "الشمس\nThe Sun": {
            "حقائق أساسية\nKey Facts": ["نجم من النوع G2V (Yellow Dwarf)", "عمرها 4.6 مليار سنة - منتصف العمر", "قطرها 1.4 مليون كم (109x الأرض)", "99.86% من كتلة النظام الشمسي"],
            "الفيزياء الشمسية\nSolar Physics": ["الاندماج النووي: هيدروجين → هيليوم", "درجة حرارة اللب: 15 مليون °C", "الرياح الشمسية (Solar Wind)", "البقع الشمسية ودورة الـ 11 سنة (Sunspot Cycle)", "الانبعاثات الكتلية الإكليلية (CME)"]
        },
        "الكواكب الصخرية\nTerrestrial Planets": {
            "عطارد\nMercury": ["أقرب كوكب للشمس", "لا غلاف جوي", "درجات حرارة: -180 إلى +430°C"],
            "الزهرة\nVenus": ["توأم الأرض في الحجم", "أشد كوكب حرارة: 465°C", "ضغط جوي 90 ضعف الأرض", "تأثير الاحتباس الحراري الجامح (Runaway Greenhouse)"],
            "الأرض\nEarth": ["الكوكب الأزرق - 71% ماء", "الغلاف المغناطيسي يحمي من الإشعاع", "الكوكب الوحيد بحياة مؤكدة"],
            "المريخ\nMars": ["الكوكب الأحمر - أكسيد الحديد", "أكبر بركان: أوليمبوس مونس (22 كم)", "أدلة على مياه سابقة (Ancient Water)", "هدف الاستعمار البشري"]
        },
        "الكواكب الغازية\nGas & Ice Giants": {
            "المشتري\nJupiter": ["أكبر كوكب (318x كتلة الأرض)", "بقعة حمراء عملاقة = عاصفة 400 سنة", "79+ قمراً (Europa - محيط تحت الجليد)"],
            "زحل\nSaturn": ["الحلقات: جليد وصخور (Ice & Rocks)", "كثافته أقل من الماء (يطفو نظرياً)", "قمر تايتان - بحيرات ميثان (Titan)"],
            "أورانوس ونبتون\nUranus & Neptune": ["عمالقة جليدية (Ice Giants)", "أورانوس يدور على جانبه (97.8° ميل)", "نبتون - أسرع رياح: 2,100 كم/ساعة"]
        }
    },
    "2. النجوم ودورة حياتها\nStars & Their Life Cycle": {
        "ولادة النجوم\nStar Birth": {
            "السُدم\nNebulae": ["سحب غاز وغبار عملاقة (Gas & Dust Clouds)", "الانهيار الجاذبي (Gravitational Collapse)", "النجوم الأولية (Protostars)", "سديم الجبار (Orion Nebula) - أشهر حضانة نجمية"],
            "تصنيف النجوم\nStar Classification": ["O B A F G K M (Oh Be A Fine Girl Kiss Me)", "O - الأكثر حرارة (30,000°K+)", "M - الأبرد (2,500°K)", "الشمس = G2 (5,778°K)"]
        },
        "حياة النجوم\nStar Life": ["تسلسل رئيسي (Main Sequence) - أطول مرحلة", "عملاقة حمراء (Red Giant) - النجوم المتوسطة", "فوق عملاقة (Supergiant) - النجوم الضخمة", "مخطط هرتزبرونغ-راسل (H-R Diagram)"],
        "موت النجوم\nStar Death": {
            "نجوم صغيرة-متوسطة\nSmall-Medium Stars": ["عملاقة حمراء → سديم كوكبي → قزم أبيض", "الأقزام البيضاء = حجم الأرض بكتلة الشمس", "التبريد التدريجي عبر مليارات السنين"],
            "نجوم ضخمة\nMassive Stars": ["سوبرنوفا - أعنف انفجار كوني (Supernova)", "تصنع العناصر الثقيلة: ذهب، يورانيوم، حديد", "نجم نيوتروني: كثافة مليار طن/سم³", "النجوم النابضة (Pulsars) - نجوم نيوترونية دوارة"],
            "الثقوب السوداء\nBlack Holes": ["تتكون من نجوم > 25 كتلة شمسية", "أفق الحدث (Event Horizon) - لا شيء يهرب", "التفرد (Singularity) - كثافة لا نهائية", "أول صورة حقيقية: M87* (2019 - تلسكوب EHT)", "ثقوب سوداء فائقة في مراكز المجرات"]
        }
    },
    "3. الكون الأعظم\nThe Greater Universe": {
        "البنية الكونية\nCosmic Structure": {
            "المجرات\nGalaxies": ["درب التبانة: 200-400 مليار نجم (Milky Way)", "أنواع: حلزونية، إهليجية، غير منتظمة", "مجرة أندروميدا - أقرب مجرة كبيرة (2.5 مليون سنة ضوئية)", "اصطدام درب التبانة وأندروميدا بعد 4.5 مليار سنة"],
            "البنية الكبرى\nLarge-Scale Structure": ["العناقيد المجرية (Galaxy Clusters)", "العناقيد الفائقة (Superclusters - Laniakea)", "الخيوط الكونية (Cosmic Filaments)", "الفراغات الكونية الهائلة (Voids)"]
        },
        "نشأة الكون\nOrigin of Universe": {
            "الانفجار العظيم\nBig Bang": ["13.8 مليار سنة (بدقة ±0.02 مليار)", "ليس انفجاراً بل تمدد للفضاء نفسه", "أول 3 دقائق: تكوين الهيدروجين والهيليوم", "380,000 سنة: أول ضوء (CMB Radiation)"],
            "التضخم الكوني\nCosmic Inflation": ["آلان غوث 1980 (Alan Guth)", "توسع أسرع من الضوء في أجزاء من الثانية", "يفسر تجانس الكون (Flatness Problem)", "يفسر غياب الاحتكارات المغناطيسية"]
        },
        "ألغاز كبرى\nGreat Mysteries": {
            "المادة المظلمة\nDark Matter (27%)": ["لا تُشع ولا تمتص الضوء", "تؤثر بالجاذبية فقط", "فيرا روبين - اكتشاف دوران المجرات (1970s)", "لا نعرف ماهيتها حتى الآن (WIMPs? Axions?)"],
            "الطاقة المظلمة\nDark Energy (68%)": ["تسارع تمدد الكون (Accelerating Expansion)", "اكتشاف 1998 (جائزة نوبل 2011)", "الثابت الكوني لآينشتاين (Cosmological Constant)", "مصير الكون: التمزق الكبير؟ (Big Rip?)"],
            "أسئلة مفتوحة\nOpen Questions": ["مفارقة فيرمي - أين الجميع؟ (Fermi Paradox)", "الأكوان المتعددة (Multiverse Theory)", "قبل الانفجار العظيم - ماذا كان؟", "هل الكون محاكاة؟ (Simulation Hypothesis)"]
        }
    },
    "4. استكشاف الفضاء\nSpace Exploration": {
        "محطات تاريخية\nHistorical Milestones": ["سبوتنيك 1 - أول قمر صناعي (1957 - USSR)", "يوري غاغارين - أول إنسان في الفضاء (1961)", "أبولو 11 - أول هبوط على القمر (1969)", "محطة الفضاء الدولية ISS (1998-حالياً)", "مسبار فويجر 1 - أبعد جسم بشري (23+ مليار كم)"],
        "القطاع الخاص\nPrivate Sector": {
            "SpaceX\nسبيس إكس": ["إيلون ماسك - أسسها 2002", "Falcon 9 - أول صاروخ قابل لإعادة الاستخدام", "Starship - أكبر صاروخ في التاريخ", "Starlink - إنترنت فضائي (5,000+ قمر)", "هدف: استعمار المريخ بحلول 2030s"],
            "منافسون\nCompetitors": ["Blue Origin - جيف بيزوس (New Shepard, New Glenn)", "Virgin Galactic - سياحة فضائية", "Rocket Lab - صواريخ صغيرة (Electron)"]
        },
        "مستقبل الاستكشاف\nFuture Exploration": {
            "القمر\nMoon": ["برنامج أرتيميس - عودة البشر للقمر (Artemis)", "قاعدة قمرية دائمة (Lunar Gateway)", "تعدين الهيليوم-3 (Helium-3 Mining)"],
            "المريخ\nMars": ["رحلة 7 أشهر (7-month Journey)", "تحديات: إشعاع، جاذبية منخفضة، عزلة", "Terraform - تحويل المريخ لكوكب صالح للحياة"],
            "ما وراء المريخ\nBeyond Mars": ["أقمار المشتري: يوروبا (محيط تحت الجليد)", "تيتان قمر زحل (بحيرات ميثان)", "مسبار بين نجمي: Breakthrough Starshot", "تلسكوب جيمس ويب JWST - النظر لبدايات الكون"]
        }
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1a237e", "padding": [16, 28], "borderRadius": 12, "borderWidth": 2, "borderColor": "#536dfe"}, "symbolSize": 35, "itemStyle": {"color": "#536dfe", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#283593", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#3f51b5"}},
        {"label": {"fontSize": 14, "color": "#c5cae9", "fontWeight": "bold", "backgroundColor": "#1a237e", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#7986cb"}, "symbolSize": 12, "itemStyle": {"color": "#1a237e"}},
        {"label": {"fontSize": 13, "color": "#9fa8da", "fontWeight": "bold", "backgroundColor": "#0d1042", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#0d1042"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#7986cb", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#3f51b5"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("علوم الكون والفضاء\nSpace & Cosmos", space_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4500px", theme="dark", bg_color="#020520", page_title="Space & Cosmos", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="علوم الكون والفضاء", subtitle="From Our Solar System to the Edge of the Observable Universe", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#536dfe", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#7986cb", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "space_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Space Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "space_mindmap.html")
