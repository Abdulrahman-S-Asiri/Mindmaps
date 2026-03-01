import os
from pyecharts import options as opts
from pyecharts.charts import Tree

art_map = {
    "1. تاريخ الفن\nArt History": {
        "العصور القديمة\nAncient": ["فن الكهوف - لاسكو 17,000 سنة (Lascaux)", "الفن المصري - جدارية المقابر", "الفن اليوناني - النحت الواقعي"],
        "عصر النهضة\nRenaissance": ["ليوناردو دافنشي - الموناليزا (Mona Lisa 1503)", "ميكيلانجيلو - سقف سيستين (Sistine Chapel)", "رافاييل - مدرسة أثينا (School of Athens)"],
        "الحركات الحديثة\nModern Movements": ["الانطباعية - مونيه (Impressionism - Monet)", "التكعيبية - بيكاسو (Cubism - Picasso)", "السريالية - سلفادور دالي (Surrealism - Dalí)", "التعبيرية التجريدية - بولوك (Abstract - Pollock)", "فن البوب - آندي وارهول (Pop Art - Warhol)"]
    },
    "2. نظرية الألوان\nColor Theory": {
        "عجلة الألوان\nColor Wheel": ["ألوان أساسية: أحمر، أزرق، أصفر (Primary)", "ألوان ثانوية: برتقالي، أخضر، بنفسجي (Secondary)", "ألوان متممة: متقابلة في العجلة (Complementary)"],
        "سيكولوجية الألوان\nColor Psychology": ["أحمر: طاقة، عاطفة، خطر", "أزرق: ثقة، هدوء، احترافية", "أخضر: طبيعة، نمو، صحة", "أسود: قوة، أناقة، غموض", "ذهبي: فخامة، ثروة، نجاح"]
    },
    "3. الإبداع\nCreativity": {
        "كيف يعمل الإبداع\nHow Creativity Works": ["التفكير التباعدي (Divergent Thinking - Guilford)", "ربط أفكار غير مرتبطة (Connecting Unrelated Ideas)", "الحضانة اللاواعية (Incubation Period)", "لحظة الإلهام (Aha Moment)"],
        "تقنيات الإبداع\nCreativity Techniques": ["العصف الذهني (Brainstorming - Osborn)", "الخرائط الذهنية (Mind Mapping - Buzan)", "التفكير العكسي (Reverse Thinking)", "SCAMPER - 7 أسئلة إبداعية", "التقييد الإبداعي (Creative Constraints)"]
    },
    "4. الموسيقى\nMusic": {
        "نظرية الموسيقى\nMusic Theory": ["السلم الموسيقي (Scales - Major/Minor)", "الإيقاع (Rhythm)", "التناغم (Harmony)", "الكوردات (Chords)"],
        "تأثير الموسيقى\nMusic's Impact": ["تأثير موزارت (Mozart Effect)", "الموسيقى تفرز الدوبامين", "علاج بالموسيقى (Music Therapy)", "الترددات: 432Hz vs 440Hz (Tuning Debate)"]
    },
    "📚 المراجع\nReferences": ["Ernst Gombrich - The Story of Art (1950)", "Austin Kleon - Steal Like an Artist (2012)", "Mihaly Csikszentmihalyi - Creativity (1996)", "Betty Edwards - Drawing on the Right Side of the Brain (1979)", "Oliver Sacks - Musicophilia (2007)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#ab47bc", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#ab47bc", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#8e24aa", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#8e24aa"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#6a1b9a", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#ce93d8"}, "symbolSize": 12, "itemStyle": {"color": "#6a1b9a"}},
        {"label": {"fontSize": 13, "color": "#e1bee7", "fontWeight": "bold", "backgroundColor": "#4a148c", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#4a148c"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#ce93d8", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#9c27b0"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الفن والإبداع\nArt & Creativity", art_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#140a1a", page_title="Art & Creativity", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الفن والإبداع", subtitle="From Cave Paintings to Digital Art", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#ce93d8", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#e1bee7", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "art_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Art & Creativity Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "art_creativity_mindmap.html")
