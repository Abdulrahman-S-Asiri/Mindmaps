import os
from pyecharts import options as opts
from pyecharts.charts import Tree

biology_map = {
    "1. الخلية\nThe Cell": {
        "بنية الخلية\nCell Structure": {
            "العضيات\nOrganelles": ["النواة - مركز التحكم (Nucleus)", "الميتوكوندريا - مصنع الطاقة (Mitochondria)", "الريبوسوم - مصنع البروتين (Ribosome)", "الشبكة الإندوبلازمية (Endoplasmic Reticulum)", "جهاز غولجي (Golgi Apparatus)"],
            "أنواع الخلايا\nCell Types": ["بدائية النواة: البكتيريا (Prokaryotic)", "حقيقية النواة: حيوانية ونباتية (Eukaryotic)", "خلايا جذعية (Stem Cells)"]
        },
        "الانقسام الخلوي\nCell Division": ["الانقسام المتساوي - النمو (Mitosis)", "الانقسام المنصف - التكاثر (Meiosis)", "دورة الخلية ونقاط التفتيش (Cell Cycle Checkpoints)", "السرطان = انقسام خارج السيطرة"]
    },
    "2. الحمض النووي والوراثة\nDNA & Genetics": {
        "DNA\nالحمض النووي": {
            "البنية\nStructure": ["اللولب المزدوج - واتسون وكريك 1953 (Double Helix)", "أزواج القواعد: A-T و G-C (Base Pairs)", "3 مليارات زوج قاعدي (3 Billion Base Pairs)", "الجينوم البشري: 20,000-25,000 جين"],
            "العمليات\nProcesses": ["النسخ (DNA Replication)", "النسخ إلى RNA (Transcription)", "الترجمة إلى بروتين (Translation)", "المبدأ المركزي: DNA → RNA → Protein"]
        },
        "الوراثة\nGenetics": {
            "مندل\nMendel": ["قوانين الوراثة (Laws of Inheritance)", "السائد والمتنحي (Dominant & Recessive)", "الفصل المستقل (Independent Assortment)"],
            "الوراثة الحديثة\nModern Genetics": ["الطفرات (Mutations)", "الأمراض الوراثية (Genetic Disorders)", "الهندسة الوراثية (Genetic Engineering)", "كريسبر - مقص الجينات (CRISPR-Cas9)"]
        }
    },
    "3. التطور والتنوع\nEvolution & Biodiversity": {
        "نظرية التطور\nEvolution Theory": {
            "داروين\nDarwin": ["أصل الأنواع 1859 (Origin of Species)", "الانتقاء الطبيعي (Natural Selection)", "البقاء للأصلح (Survival of the Fittest)", "الأصل المشترك (Common Ancestry)"],
            "آليات التطور\nMechanisms": ["الطفرات العشوائية (Random Mutations)", "الانحراف الجيني (Genetic Drift)", "تدفق الجينات (Gene Flow)", "الانتقاء الجنسي (Sexual Selection)"]
        },
        "التنوع الحيوي\nBiodiversity": ["8.7 مليون نوع على الأرض (تقدير)", "الانقراض الجماعي السادس (6th Mass Extinction)", "فقدان 70% من الحياة البرية منذ 1970", "أهمية التنوع للنظم البيئية"]
    },
    "4. جسم الإنسان\nHuman Body": {
        "الأجهزة الحيوية\nVital Systems": {
            "القلب والأوعية\nCardiovascular": ["القلب يضخ 7,500 لتر يومياً", "100,000 كم أوعية دموية", "النوبات القلبية - القاتل الأول عالمياً"],
            "الجهاز العصبي\nNervous System": ["الدماغ: 86 مليار خلية عصبية", "السرعة: 432 كم/ساعة", "الجهاز السمبثاوي والباراسمبثاوي"],
            "المناعة\nImmune System": ["المناعة الفطرية (Innate Immunity)", "المناعة التكيفية (Adaptive Immunity)", "الأجسام المضادة (Antibodies)", "اللقاحات - كيف تعمل (Vaccines)"]
        },
        "الميكروبيوم\nMicrobiome": ["39 تريليون ميكروب في جسمك", "أكثر من عدد خلاياك البشرية!", "تأثير على المزاج والمناعة والوزن", "محور الأمعاء-الدماغ (Gut-Brain Axis)"]
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#66bb6a", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#66bb6a", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#388e3c", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#388e3c"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1b5e20", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#81c784"}, "symbolSize": 12, "itemStyle": {"color": "#1b5e20"}},
        {"label": {"fontSize": 13, "color": "#c8e6c9", "fontWeight": "bold", "backgroundColor": "#0d3311", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#0d3311"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#a5d6a7", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#43a047"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("علم الأحياء\nBiology", biology_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3800px", theme="dark", bg_color="#051a05", page_title="Biology", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="علم الأحياء", subtitle="From DNA to Ecosystems — The Science of Life", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#66bb6a", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#a5d6a7", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "biology_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Biology Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "biology_mindmap.html")
