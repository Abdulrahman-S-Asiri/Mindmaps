import os
from pyecharts import options as opts
from pyecharts.charts import Tree

math_map = {
    "1. الحساب والجبر\nArithmetic & Algebra": {
        "الحساب\nArithmetic": ["الأعداد الطبيعية والصحيحة والنسبية", "العمليات الأربع والأسس واللوغاريتمات", "النسب والتناسب (Ratios & Proportions)"],
        "الجبر\nAlgebra": {
            "الأساسيات\nBasics": ["المتغيرات والمعادلات (Variables & Equations)", "المعادلات الخطية والتربيعية", "المتباينات (Inequalities)", "كثيرات الحدود (Polynomials)"],
            "الجبر المتقدم\nAdvanced": ["المصفوفات (Matrices)", "الأعداد المركبة (Complex Numbers)", "نظرية الزمر (Group Theory)", "الجبر الخطي (Linear Algebra)"]
        }
    },
    "2. الهندسة\nGeometry": {
        "الهندسة الإقليدية\nEuclidean": ["النقطة والخط والمستوي (Point, Line, Plane)", "المثلثات والدوائر والمضلعات", "نظرية فيثاغورس (Pythagorean Theorem)", "التطابق والتشابه (Congruence & Similarity)"],
        "الهندسة التحليلية\nAnalytic": ["المستوي الديكارتي (Cartesian Plane)", "معادلات الخطوط والمنحنيات", "المقاطع المخروطية (Conic Sections)"],
        "الهندسة اللاإقليدية\nNon-Euclidean": ["هندسة ريمان (Riemannian - كروية)", "هندسة لوباتشيفسكي (Hyperbolic)", "أساس النسبية العامة لآينشتاين"]
    },
    "3. التفاضل والتكامل\nCalculus": {
        "التفاضل\nDifferential": ["النهايات (Limits)", "المشتقات وقواعدها (Derivatives)", "تطبيقات: السرعة والتسارع", "قاعدة السلسلة (Chain Rule)"],
        "التكامل\nIntegral": ["التكامل المحدد وغير المحدد", "النظرية الأساسية للتفاضل والتكامل", "المساحات والحجوم (Areas & Volumes)", "المعادلات التفاضلية (Differential Equations)"],
        "التاريخ\nHistory": ["نيوتن ولايبنتز - اكتشاف متزامن (1680s)", "الصراع حول الأولوية (Priority Dispute)"]
    },
    "4. الإحصاء والاحتمالات\nStatistics & Probability": {
        "الإحصاء\nStatistics": ["المتوسط والوسيط والمنوال", "الانحراف المعياري (Standard Deviation)", "التوزيع الطبيعي (Normal Distribution)", "الارتباط والانحدار (Correlation & Regression)"],
        "الاحتمالات\nProbability": ["القوانين الأساسية (Basic Rules)", "نظرية بايز (Bayes' Theorem)", "التوزيعات: ثنائي، بواسون، طبيعي", "مونتي كارلو (Monte Carlo Methods)"]
    },
    "📚 المراجع\nReferences": ["Euclid - Elements (300 BC)", "Isaac Newton - Principia Mathematica (1687)", "Leonhard Euler - Introductio in Analysin Infinitorum (1748)", "Carl Friedrich Gauss - Disquisitiones Arithmeticae (1801)", "Khan Academy - Mathematics Courses", "3Blue1Brown - Essence of Linear Algebra & Calculus"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1565c0", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#1565c0", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#0d47a1", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#0d47a1"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1a237e", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#42a5f5"}, "symbolSize": 12, "itemStyle": {"color": "#1a237e"}},
        {"label": {"fontSize": 13, "color": "#bbdefb", "fontWeight": "bold", "backgroundColor": "#0d1a40", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#0d1a40"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#90caf9", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#1976d2"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الرياضيات\nMathematics", math_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#050a1a", page_title="Mathematics", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الرياضيات", subtitle="The Queen of Sciences", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#42a5f5", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#90caf9", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "math_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Mathematics Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "mathematics_mindmap.html")
