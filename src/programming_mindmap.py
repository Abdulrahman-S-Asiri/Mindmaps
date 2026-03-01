import os
from pyecharts import options as opts
from pyecharts.charts import Tree

programming_map = {
    "1. أساسيات البرمجة\nProgramming Fundamentals": {
        "المفاهيم الجوهرية\nCore Concepts": {
            "أنواع البيانات\nData Types": ["أعداد صحيحة (Integer)", "أعداد عشرية (Float)", "نصوص (String)", "منطقية (Boolean)", "قوائم ومصفوفات (Arrays/Lists)", "قواميس (Dictionaries/Hash Maps)"],
            "التحكم بالتدفق\nControl Flow": ["الشروط if/else/elif", "الحلقات for / while", "التكرار مع break / continue", "معالجة الأخطاء try/except"],
            "الدوال\nFunctions": ["التعريف والاستدعاء (Define & Call)", "المعاملات والقيم المُرجعة (Parameters & Return)", "النطاق (Scope - Local vs Global)", "الدوال المجهولة Lambda"],
            "البرمجة الكائنية\nOOP": ["الأصناف والكائنات (Classes & Objects)", "الوراثة (Inheritance)", "التغليف (Encapsulation)", "تعدد الأشكال (Polymorphism)", "التجريد (Abstraction)"]
        },
        "هياكل البيانات\nData Structures": {
            "الأساسية\nBasic": ["المصفوفة (Array)", "القائمة المتصلة (Linked List)", "المكدس (Stack - LIFO)", "الطابور (Queue - FIFO)"],
            "المتقدمة\nAdvanced": ["الشجرة الثنائية (Binary Tree)", "الكومة (Heap)", "جدول التجزئة (Hash Table)", "الرسم البياني (Graph)"]
        },
        "الخوارزميات\nAlgorithms": ["البحث الثنائي (Binary Search - O(log n))", "الترتيب السريع (Quick Sort - O(n log n))", "الترتيب بالدمج (Merge Sort)", "البرمجة الديناميكية (Dynamic Programming)", "الخوارزميات الجشعة (Greedy Algorithms)", "Big O Notation - تحليل التعقيد"]
    },
    "2. اللغات الرئيسية\nMajor Languages": {
        "Python\nبايثون": ["الأسهل للمبتدئين (Beginner Friendly)", "AI / Data Science / Automation", "Django / Flask / FastAPI", "المكتبات: NumPy, Pandas, TensorFlow"],
        "JavaScript\nجافاسكربت": ["لغة الويب الأولى (The Language of the Web)", "الواجهة الأمامية: React, Vue, Angular", "الواجهة الخلفية: Node.js, Express", "Full Stack Development"],
        "بقية اللغات\nOther Languages": {
            "C / C++": ["أساس أنظمة التشغيل والألعاب", "الأداء الأعلى (Closest to Hardware)", "Arduino / Embedded Systems"],
            "Java": ["المؤسسات والتطبيقات الكبيرة (Enterprise)", "تطبيقات أندرويد (Android - Kotlin)", "Write Once Run Anywhere (JVM)"],
            "Go / Rust": ["Go - خوادم جوجل (Concurrency)", "Rust - أمان الذاكرة بدون GC (Memory Safety)", "لغات المستقبل (Future Languages)"]
        }
    },
    "3. تطوير الويب\nWeb Development": {
        "الواجهة الأمامية\nFrontend": {
            "الأساسيات\nBasics": ["HTML - الهيكل (Structure)", "CSS - التنسيق (Styling)", "JavaScript - التفاعل (Interactivity)"],
            "الأطر الحديثة\nModern Frameworks": ["React - Meta (الأشهر عالمياً)", "Next.js - React مع SSR", "Vue.js - سهل التعلم", "Svelte - أسرع أداء"],
            "أدوات التصميم\nDesign Tools": ["Figma - التصميم التعاوني", "Tailwind CSS - تنسيق سريع", "Responsive Design - تصميم متجاوب"]
        },
        "الواجهة الخلفية\nBackend": {
            "الأساسيات\nBasics": ["APIs - واجهات برمجة التطبيقات (REST / GraphQL)", "قواعد البيانات SQL (PostgreSQL, MySQL)", "قواعد NoSQL (MongoDB, Redis)", "المصادقة والتفويض (Auth - JWT, OAuth)"],
            "البنية التحتية\nInfrastructure": ["Docker - الحاويات (Containers)", "Kubernetes - التنسيق (Orchestration)", "CI/CD - النشر المستمر", "AWS / Azure / GCP"]
        }
    },
    "4. المسارات المتخصصة\nSpecialized Paths": {
        "الذكاء الاصطناعي\nAI & ML": ["تعلم الآلة (Machine Learning)", "التعلم العميق (Deep Learning)", "معالجة اللغات NLP", "الرؤية الحاسوبية (Computer Vision)"],
        "تطوير الجوال\nMobile Dev": ["Swift / SwiftUI - iOS", "Kotlin / Jetpack Compose - Android", "Flutter - تطبيقات الهجين (Cross-Platform)", "React Native"],
        "هندسة البيانات\nData Engineering": ["ETL Pipelines", "Apache Spark / Kafka", "Data Warehousing (Snowflake)", "dbt - تحويل البيانات"],
        "DevOps / SRE": ["البنية كرمز (Infrastructure as Code - Terraform)", "المراقبة (Monitoring - Prometheus, Grafana)", "الأمان في DevOps (DevSecOps)", "SLA / SLO / SLI"]
    }
    "📚 المراجع\nReferences": ["CLRS - Introduction to Algorithms (2009)", "Clean Code - Robert C. Martin (2008)", "The Pragmatic Programmer - Hunt & Thomas (1999)", "MDN Web Docs - Mozilla", "freeCodeCamp / The Odin Project"],
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#00bcd4", "padding": [16, 28], "borderRadius": 12}, "symbolSize": 35, "itemStyle": {"color": "#00bcd4", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#fff", "fontWeight": "bold", "backgroundColor": "#0097a7", "padding": [10, 20], "borderRadius": 8}, "symbolSize": 20, "itemStyle": {"color": "#0097a7"}},
        {"label": {"fontSize": 14, "color": "#ffffff", "fontWeight": "bold", "backgroundColor": "#00695c", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#4dd0e1"}, "symbolSize": 12, "itemStyle": {"color": "#00695c"}},
        {"label": {"fontSize": 13, "color": "#b2dfdb", "fontWeight": "bold", "backgroundColor": "#004d40", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#004d40"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#80cbc4", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#009688"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("البرمجة من الصفر\nProgramming from Zero", programming_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4000px", theme="dark", bg_color="#001a1a", page_title="Programming", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="البرمجة من الصفر", subtitle="The Complete Programming Roadmap", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#00bcd4", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#4dd0e1", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "programming_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Programming Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "programming_mindmap.html")
