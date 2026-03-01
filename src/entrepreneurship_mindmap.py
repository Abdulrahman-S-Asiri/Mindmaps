import os
from pyecharts import options as opts
from pyecharts.charts import Tree

entrepreneurship_map = {
    "1. من الفكرة إلى المنتج\nIdea to Product": {
        "إيجاد الفكرة\nFinding The Idea": {
            "مصادر الأفكار\nIdea Sources": ["مشكلة تعاني منها شخصياً (Scratch Your Own Itch)", "فجوة في السوق (Market Gap)", "تحسين منتج موجود (Better Mousetrap)", "اتجاهات تكنولوجية ناشئة (Emerging Tech Trends)"],
            "تقييم الفكرة\nIdea Evaluation": ["هل تحل مشكلة حقيقية؟ (Real Problem?)", "هل الناس مستعدون للدفع؟ (Willingness to Pay?)", "حجم السوق المتاح TAM/SAM/SOM", "الميزة التنافسية (Competitive Moat)"]
        },
        "MVP والتحقق\nMVP & Validation": {
            "المنتج الأولي\nMinimum Viable Product": ["أبسط نسخة ممكنة تحل المشكلة", "حلقة Build-Measure-Learn (Eric Ries)", "الإطلاق السريع > الكمال (Ship Fast > Perfect)", "قياس المقاييس الصحيحة (Actionable Metrics)"],
            "التحقق من السوق\nMarket Validation": ["مقابلات العملاء (Customer Interviews)", "صفحة هبوط + قائمة انتظار (Landing Page Test)", "التمويل الجماعي كتحقق (Crowdfunding as Validation)", "البيع قبل البناء (Sell Before You Build)"]
        },
        "نموذج العمل\nBusiness Model": {
            "Business Model Canvas": ["شرائح العملاء (Customer Segments)", "القيمة المقترحة (Value Proposition)", "القنوات (Channels)", "العلاقات مع العملاء (Customer Relationships)", "مصادر الإيرادات (Revenue Streams)", "الموارد الرئيسية (Key Resources)", "الأنشطة الرئيسية (Key Activities)", "الشراكات (Key Partners)", "هيكل التكاليف (Cost Structure)"],
            "نماذج إيرادات\nRevenue Models": ["اشتراك شهري SaaS (Subscription)", "فريميوم (Freemium)", "العمولة/السوق (Marketplace Commission)", "الترخيص (Licensing)", "الإعلانات (Advertising)"]
        }
    },
    "2. التمويل\nFunding": {
        "مراحل التمويل\nFunding Stages": {
            "المرحلة المبكرة\nEarly Stage": ["التمويل الذاتي - أموالك الخاصة (Bootstrapping)", "الأصدقاء والعائلة (Friends & Family)", "المستثمرون الملائكة - $25K-$500K (Angel Investors)"],
            "رأس المال المغامر\nVenture Capital": ["Pre-Seed: $100K-$500K (فكرة + فريق)", "Seed: $500K-$2M (MVP + أولى الإيرادات)", "Series A: $2M-$15M (Product-Market Fit)", "Series B: $15M-$50M (التوسع والنمو)", "Series C+: $50M+ (الهيمنة على السوق)"],
            "Exit\nالخروج": ["الاستحواذ (Acquisition)", "الطرح العام IPO", "الاندماج (Merger)", "SPAC - شركة الاستحواذ ذات الغرض الخاص"]
        },
        "مصادر بديلة\nAlternative Sources": ["التمويل الجماعي (Kickstarter, Indiegogo)", "المنح الحكومية (Government Grants)", "الحاضنات (Incubators)", "المسرعات - Y Combinator, Techstars", "إيرادات العملاء (Revenue-Based - الأفضل)"]
    },
    "3. التسويق والنمو\nMarketing & Growth": {
        "التسويق الرقمي\nDigital Marketing": {
            "SEO\nتحسين محركات البحث": ["الكلمات المفتاحية (Keyword Research)", "المحتوى عالي الجودة (Quality Content)", "الروابط الخلفية (Backlinks)", "Core Web Vitals - السرعة والأداء"],
            "إعلانات مدفوعة\nPaid Ads": ["Google Ads - نية الشراء (Purchase Intent)", "Meta Ads - الاستهداف الديموغرافي", "تكلفة الاستحواذ CAC", "عائد الإنفاق ROAS"]
        },
        "استراتيجيات النمو\nGrowth Strategies": {
            "اختراق النمو\nGrowth Hacking": ["Hotmail - أضفها في التوقيع (1996)", "Dropbox - خزن مجاني = إحالات", "Airbnb - اختراق Craigslist", "التسويق الفيروسي (Viral Loops)"],
            "PLG\nProduct-Led Growth": ["المنتج يبيع نفسه (Self-Serve Onboarding)", "فريميوم → مدفوع (Free to Paid)", "أمثلة: Slack, Notion, Zoom, Figma"],
            "بناء المجتمع\nCommunity Building": ["المحتوى التعليمي (Educational Content)", "وسائل التواصل (Social Media)", "البودكاست والنشرات البريدية (Newsletter)"]
        }
    },
    "4. الفريق والثقافة\nTeam & Culture": {
        "بناء الفريق\nTeam Building": ["المؤسس التقني + المؤسس التجاري (Technical + Business)", "أول 10 موظفين يصنعون الثقافة", "التوظيف البطيء والفصل السريع (Hire Slow, Fire Fast)", "التنوع في المهارات والخلفيات"],
        "ثقافة الشركة\nCompany Culture": ["الشفافية الجذرية (Radical Transparency)", "الاستقلالية + المسؤولية (Autonomy + Accountability)", "التعلم المستمر (Continuous Learning)", "التجريب وتقبل الفشل (Experimentation)"]
    },
    "5. الفشل والنجاح\nFailure & Success": {
        "لماذا تفشل الشركات الناشئة\nWhy Startups Fail": {
            "إحصائيات CB Insights\nCB Insights Data": ["42% - لا يوجد طلب في السوق (No Market Need)", "29% - نفاد التمويل (Ran Out of Cash)", "23% - فريق غير مناسب (Not the Right Team)", "19% - المنافسة (Got Outcompeted)", "18% - مشاكل التسعير (Pricing Issues)", "17% - منتج ضعيف (Poor Product)"]
        },
        "عقلية رائد الأعمال\nEntrepreneur Mindset": ["المرونة والتكيف - Pivot عند الضرورة", "التعلم من الفشل (Fail Forward)", "التنفيذ > الفكرة (Execution > Idea)", "الصبر الاستراتيجي (10 سنوات لنجاح ليلة واحدة)", "التفكير بالمبادئ الأولى (First Principles - Elon Musk)"],
        "دروس من العظماء\nLessons from Greats": {
            "ستيف جوبز\nSteve Jobs": ["طُرد من Apple ثم عاد وصنع iPhone", "التصميم = كيف يعمل الشيء (Design is How It Works)", "Stay Hungry, Stay Foolish"],
            "إيلون ماسك\nElon Musk": ["فشل 3 صواريخ SpaceX قبل النجاح", "التفكير من المبادئ الأولى", "هدف: جعل البشرية متعددة الكواكب"],
            "جيف بيزوس\nJeff Bezos": ["Day 1 Mentality - كل يوم هو اليوم الأول", "الهوس بالعميل (Customer Obsession)", "التفكير طويل المدى (Long-Term Thinking)"]
        }
    }
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#ff6d00", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#ff6d00", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#0a0a0a", "fontWeight": "bold", "backgroundColor": "#ffab40", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#ffab40"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#e65100", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#ff9100"}, "symbolSize": 12, "itemStyle": {"color": "#e65100"}},
        {"label": {"fontSize": 13, "color": "#ffe0b2", "fontWeight": "bold", "backgroundColor": "#bf360c", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#bf360c"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#ffcc80", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#ff9800"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("ريادة الأعمال\nEntrepreneurship", entrepreneurship_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4200px", theme="dark", bg_color="#1a0d00", page_title="Entrepreneurship", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="ريادة الأعمال", subtitle="From Zero to IPO — The Startup Journey", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#ff6d00", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#ffcc80", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "entrepreneurship_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Entrepreneurship Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "entrepreneurship_mindmap.html")
