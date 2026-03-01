import os
from pyecharts import options as opts
from pyecharts.charts import Tree

finance_map = {
    "1. أساسيات المالية الشخصية\nPersonal Finance Basics": {
        "الميزانية\nBudgeting": ["قاعدة 50/30/20 (Needs/Wants/Savings)", "تتبع المصاريف (Expense Tracking)", "صندوق الطوارئ: 3-6 أشهر مصاريف", "الفرق بين الأصول والالتزامات (Assets vs Liabilities)"],
        "الديون\nDebt": ["ديون جيدة vs سيئة (Good vs Bad Debt)", "طريقة كرة الثلج (Debt Snowball - Dave Ramsey)", "طريقة الانهيار (Debt Avalanche)", "الفائدة المركبة ضدك (Compound Interest Against You)"]
    },
    "2. الاستثمار\nInvesting": {
        "أنواع الاستثمار\nInvestment Types": {
            "الأسهم\nStocks": ["الأسهم الفردية (Individual Stocks)", "صناديق المؤشرات (Index Funds - S&P 500)", "صناديق ETF", "توزيعات الأرباح (Dividends)"],
            "السندات\nBonds": ["سندات حكومية (Government Bonds)", "سندات شركات (Corporate Bonds)", "العائد vs المخاطرة (Yield vs Risk)"],
            "العقارات\nReal Estate": ["الشراء للتأجير (Buy to Rent)", "صناديق الريت REITs", "التمويل العقاري (Mortgage)"]
        },
        "استراتيجيات\nStrategies": ["الشراء والاحتفاظ (Buy & Hold)", "متوسط تكلفة الدولار (Dollar-Cost Averaging)", "التنويع (Diversification)", "لا تحاول توقيت السوق (Don't Time the Market)"],
        "مفاهيم مهمة\nKey Concepts": ["الفائدة المركبة - الأعجوبة الثامنة (Compound Interest)", "قاعدة الـ 72 (Rule of 72)", "التضخم يأكل قيمة أموالك (Inflation Erosion)", "المخاطرة والعائد (Risk-Return Tradeoff)"]
    },
    "3. حركة FIRE\nFIRE Movement": ["Financial Independence, Retire Early", "معدل الادخار 50-70%", "قاعدة الـ 4% للسحب (4% Rule)", "Lean FIRE vs Fat FIRE", "المليونير المجاور (The Millionaire Next Door)"],
    "📚 المراجع\nReferences": ["Robert Kiyosaki - Rich Dad Poor Dad (1997)", "Benjamin Graham - The Intelligent Investor (1949)", "Morgan Housel - The Psychology of Money (2020)", "JL Collins - The Simple Path to Wealth (2016)", "Dave Ramsey - Total Money Makeover (2003)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#4caf50", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#4caf50", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#2e7d32", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#2e7d32"}},
        {"label": {"fontSize": 14, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#1b5e20", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#66bb6a"}, "symbolSize": 12, "itemStyle": {"color": "#1b5e20"}},
        {"label": {"fontSize": 13, "color": "#c8e6c9", "fontWeight": "bold", "backgroundColor": "#0d3311", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#0d3311"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#a5d6a7", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#43a047"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("المالية الشخصية\nPersonal Finance", finance_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="3500px", theme="dark", bg_color="#0a1a0a", page_title="Personal Finance", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="المالية الشخصية", subtitle="Master Your Money — Build Your Wealth", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#4caf50", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#a5d6a7", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "finance_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Personal Finance Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "personal_finance_mindmap.html")
