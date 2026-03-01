import os
from pyecharts import options as opts
from pyecharts.charts import Tree

economy_map = {
    "1. النظام المالي العالمي\nThe Global Financial System": {
        "البنوك المركزية\nCentral Banks": {
            "الاحتياطي الفيدرالي\nThe Federal Reserve": ["تأسس عام 1913", "التحكم بأسعار الفائدة (Federal Funds Rate)", "التسهيل الكمي QE (طباعة النقود)", "الهيمنة على الدولار العالمي"],
            "بنوك مركزية أخرى\nOther Central Banks": ["البنك المركزي الأوروبي ECB", "بنك إنجلترا (Bank of England)", "بنك اليابان (Bank of Japan)", "بنك الشعب الصيني (PBOC)"],
            "أدوات السيطرة\nControl Tools": ["أسعار الفائدة (Interest Rates)", "عمليات السوق المفتوحة (Open Market Operations)", "نسبة الاحتياطي الإلزامي (Reserve Requirements)"]
        },
        "نظام بريتون وودز\nBretton Woods System": {
            "العصر الذهبي (1944-1971)\nGold Era": ["ربط الدولار بالذهب: 35$ للأونصة", "الدولار = عملة الاحتياط العالمية", "استقرار نسبي في أسعار الصرف"],
            "صدمة نيكسون 1971\nNixon Shock": ["فك ارتباط الدولار بالذهب", "ولادة النقود الإلزامية (Fiat Money)", "التضخم المتسارع في السبعينات"],
            "نظام البترودولار\nPetrodollar System": ["اتفاق السعودية-أمريكا 1974", "بيع النفط بالدولار حصرياً", "تمويل الدين الأمريكي عبر سندات الخزانة"]
        },
        "المؤسسات الدولية\nGlobal Institutions": ["صندوق النقد الدولي IMF - إقراض الدول المتعثرة", "البنك الدولي - تمويل مشاريع التنمية", "منظمة التجارة العالمية WTO", "بنك التسويات الدولي BIS - بنك البنوك المركزية"]
    },
    "2. النظريات الاقتصادية\nEconomic Theories": {
        "الاقتصاد الكلاسيكي\nClassical Economics": {
            "آدم سميث (1776)\nAdam Smith": ["ثروة الأمم (Wealth of Nations)", "اليد الخفية (Invisible Hand)", "تقسيم العمل (Division of Labor)", "المصلحة الذاتية تخدم المجتمع"],
            "ديفيد ريكاردو\nDavid Ricardo": ["الميزة النسبية (Comparative Advantage)", "نظرية القيمة بالعمل (Labor Theory of Value)", "قانون تناقص الغلة (Diminishing Returns)"]
        },
        "الكينزية\nKeynesian Economics": ["جون ماينارد كينز (1936)", "تدخل الدولة لمكافحة الركود", "الإنفاق الحكومي بالعجز (Deficit Spending)", "مضاعف الإنفاق (Spending Multiplier)", "فخ السيولة (Liquidity Trap)"],
        "المدرسة النمساوية\nAustrian School": ["فريدريش هايك - الطريق إلى العبودية (Road to Serfdom)", "لودفيغ فون ميزس - الفعل البشري (Human Action)", "الحرية الاقتصادية المطلقة (Laissez-faire)", "دورات الأعمال النمساوية (Austrian Business Cycle Theory)"],
        "الاقتصاد السلوكي\nBehavioral Economics": {
            "دانيال كانيمان\nDaniel Kahneman": ["نظرية الاحتمالات (Prospect Theory)", "النظام 1 والنظام 2 (System 1 & System 2)", "كره الخسارة (Loss Aversion)", "تأثير التأطير (Framing Effect)"],
            "ريتشارد ثالر\nRichard Thaler": ["نظرية الوكزة (Nudge Theory)", "المحاسبة الذهنية (Mental Accounting)", "التحيز للوضع الراهن (Status Quo Bias)"]
        }
    },
    "3. الذهب والعملات الرقمية\nGold & Crypto": {
        "الذهب\nGold": {
            "تاريخ الذهب\nHistory": ["5000 سنة كمخزن للقيمة", "معيار الذهب في القرن 19", "احتياطي البنوك المركزية - 35,000 طن عالمياً"],
            "لماذا الذهب؟\nWhy Gold?": ["ندرة طبيعية (لا يمكن طباعته)", "لا يتآكل ولا يتلف (Incorruptible)", "التحوط ضد التضخم (Inflation Hedge)", "ملاذ آمن في الأزمات (Safe Haven)"]
        },
        "البيتكوين\nBitcoin": {
            "الأساسيات\nFundamentals": ["ساتوشي ناكاموتو - الورقة البيضاء 2008", "أول كتلة: 3 يناير 2009 (Genesis Block)", "21 مليون وحدة فقط (Fixed Supply)", "لامركزي بالكامل (Fully Decentralized)"],
            "التقنية\nTechnology": ["سلسلة الكتل (Blockchain)", "إثبات العمل (Proof of Work)", "التعدين (Mining)", "محافظ التخزين البارد (Cold Storage)"],
            "الجدل\nControversy": ["استهلاك الطاقة الهائل (Energy Consumption)", "التقلب الشديد (Extreme Volatility)", "استخدامات غير مشروعة (Illicit Use)", "هل هو ذهب رقمي أم فقاعة؟"]
        },
        "إيثريوم والعقود الذكية\nEthereum & DeFi": ["فيتاليك بوتيرين 2015 (Vitalik Buterin)", "العقود الذكية (Smart Contracts)", "التمويل اللامركزي DeFi", "الرموز غير القابلة للاستبدال NFTs", "إثبات الحصة (Proof of Stake)"]
    },
    "4. فخاخ اقتصادية وفقاعات\nEconomic Traps & Bubbles": {
        "فقاعات تاريخية\nHistorical Bubbles": {
            "هوس التوليب 1637\nTulip Mania": ["هولندا - أول فقاعة مسجلة", "بصيلة واحدة = ثمن 10 منازل", "الانهيار الكامل في أسابيع"],
            "فقاعة بحر الجنوب 1720\nSouth Sea Bubble": ["إنجلترا - خسر فيها نيوتن ثروته", "المضاربة الجنونية (Mania)", "انهيار الثقة العامة"],
            "فقاعة دوت كوم 2000\nDot-com Bubble": ["شركات إنترنت بلا أرباح", "NASDAQ فقد 78% من قيمته", "الدرس: الإيرادات أهم من الوعود"],
            "أزمة 2008\nSubprime Crisis": ["الرهون العقارية عالية المخاطر (Subprime Mortgages)", "المشتقات المالية المعقدة (CDOs, CDS)", "سقوط Lehman Brothers", "الإنقاذ الحكومي - 700 مليار دولار (TARP)"]
        },
        "أدوات التحكم الخفية\nHidden Control Tools": ["التضخم كضريبة خفية (Inflation as Hidden Tax)", "فخ الديون الاستهلاكية (Consumer Debt Trap)", "درجة الائتمان كأداة تحكم (Credit Score Control)", "النظام الضريبي المعقد (Complex Tax System)"]
    },
    "📚 المراجع\nReferences": ["Adam Smith - Wealth of Nations (1776)", "Keynes - General Theory (1936)", "Satoshi Nakamoto - Bitcoin Whitepaper (2008)", "Ray Dalio - Changing World Order (2021)"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#ffc107", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#ffc107", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#ffca28", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#ffca28"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#f57f17", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#ffb300"}, "symbolSize": 12, "itemStyle": {"color": "#f57f17"}},
        {"label": {"fontSize": 13, "color": "#fff8e1", "fontWeight": "bold", "backgroundColor": "#e65100", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#e65100"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#ffe082", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#ff8f00"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الاقتصاد الحقيقي\nThe Real Economy", economy_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4000px", theme="dark", bg_color="#1a1000", page_title="Real Economy", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الاقتصاد الحقيقي", subtitle="From Gold Standard to Crypto Revolution", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#ffc107", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#ffe082", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "economy_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Economy Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "economy_mindmap.html")
