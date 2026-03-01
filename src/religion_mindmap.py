import os
from pyecharts import options as opts
from pyecharts.charts import Tree

religion_map = {
    "1. الإسلام\nIslam": {
        "أركان الإسلام الخمسة\nFive Pillars": ["الشهادتان (Shahada)", "الصلاة - 5 يومياً (Salah)", "الزكاة - 2.5% (Zakat)", "صوم رمضان (Sawm)", "الحج (Hajj)"],
        "أركان الإيمان الستة\nSix Articles of Faith": ["الإيمان بالله", "الملائكة", "الكتب السماوية", "الرسل", "اليوم الآخر", "القضاء والقدر"],
        "مصادر التشريع\nSources of Law": ["القرآن الكريم - 114 سورة", "السنة النبوية - الأحاديث", "الإجماع (Ijma)", "القياس (Qiyas)"],
        "المذاهب الفقهية\nJurisprudence Schools": ["الحنفي - أبو حنيفة (Hanafi)", "المالكي - مالك بن أنس (Maliki)", "الشافعي - الإمام الشافعي (Shafi'i)", "الحنبلي - أحمد بن حنبل (Hanbali)"]
    },
    "2. المسيحية\nChristianity": {
        "الأساسيات\nBasics": ["الكتاب المقدس: العهد القديم والجديد", "الوصايا العشر (Ten Commandments)", "الثالوث: الآب والابن والروح القدس (Trinity)"],
        "الطوائف الرئيسية\nMajor Denominations": ["الكاثوليكية - 1.3 مليار (Catholicism)", "البروتستانتية - 900 مليون (Protestantism)", "الأرثوذكسية - 220 مليون (Eastern Orthodox)"]
    },
    "3. اليهودية\nJudaism": ["التوراة (Torah - أسفار موسى الخمسة)", "التلمود (Talmud)", "السبت (Shabbat)", "الكنيس (Synagogue)"],
    "4. الديانات الشرقية\nEastern Religions": {
        "البوذية\nBuddhism": ["سيدهارتا غوتاما (Siddhartha Gautama)", "الحقائق النبيلة الأربع (Four Noble Truths)", "الطريق الثماني النبيل (Eightfold Path)", "النيرفانا (Nirvana)"],
        "الهندوسية\nHinduism": ["أقدم ديانة حية (4000+ سنة)", "الفيدا (Vedas)", "الكارما وإعادة الميلاد (Karma & Reincarnation)", "1 مليار معتنق"]
    },
    "5. مقارنة الأديان\nComparative Religion": ["التوحيد vs التعدد (Monotheism vs Polytheism)", "مفهوم الآخرة في الأديان", "الأخلاق المشتركة بين الأديان", "الحوار بين الأديان (Interfaith Dialogue)"],
    "📚 المراجع\nReferences": ["القرآن الكريم", "صحيح البخاري ومسلم", "Karen Armstrong - A History of God (1993)", "Huston Smith - The World's Religions (1958)", "Reza Aslan - No god but God (2005)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#d4af37", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#d4af37", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#c9a84c", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#c9a84c"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#8b6914", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#d4af37"}, "symbolSize": 12, "itemStyle": {"color": "#8b6914"}},
        {"label": {"fontSize": 13, "color": "#f5e6b8", "fontWeight": "bold", "backgroundColor": "#5c4510", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#5c4510"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#d4af37", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#b8941f"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الأديان والعقائد\nReligions & Beliefs", religion_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#1a1400", page_title="Religions", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الأديان والعقائد", subtitle="Understanding the World's Major Faiths", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#d4af37", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#c9a84c", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "religion_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Religion Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "religion_mindmap.html")
