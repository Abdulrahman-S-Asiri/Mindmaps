import os
from pyecharts import options as opts
from pyecharts.charts import Tree

# ─── 1. Deep & Detailed Data Structure ─────────────────────────
learn_ai_map = {
    "1. الأسس والجذور\nThe Foundations": {
        "الرياضيات\nMathematics": {
            "الجبر الخطي\nLinear Algebra": ["المصفوفات والمتجهات (Matrices & Vectors)", "القيم المتجهة (Eigenvectors & Eigenvalues)", "العمليات على المصفوفات (Matrix Operations)"],
            "التفاضل والتكامل\nCalculus": ["المشتقات والتدرج (Derivatives & Gradients)", "قاعدة السلسلة (Chain Rule)", "التحسين (Optimization math)"],
            "الاحتمالات والإحصاء\nProbability & Statistics": ["التوزيعات (Distributions)", "نظرية بايز (Bayes' Theorem)", "اختبار الفرضيات (Hypothesis Testing)"]
        },
        "البرمجة والأدوات\nProgramming & Tools": {
            "لغة بايثون\nPython": ["هياكل البيانات (Data Structures)", "البرمجة الكائنية (OOP)", "الخوارزميات (Algorithms)"],
            "المكتبات الأساسية\nCore Libraries": ["NumPy", "Pandas", "Matplotlib / Seaborn"],
            "أدوات المطورين\nDev Tools": ["Git / GitHub", "Linux CLI", "محررات الأكواد (VS Code / Cursor)"]
        }
    },
    "2. التعلم الآلي الكلاسيكي\nClassical Machine Learning": {
        "التعلم الخاضع للإشراف\nSupervised Learning": ["الانحدار الخطي واللوجستي (Linear & Logistic Regression)", "أشجار القرارات والغابات العشوائية (Decision Trees & Random Forests)", "آلة المتجهات الداعمة (SVM)"],
        "التعلم غير الخاضع للإشراف\nUnsupervised Learning": ["التجميع أو العنقَدَة (K-Means Clustering)", "تقليل الأبعاد (PCA / t-SNE)"],
        "التقييم والتحسين\nEvaluation & Tuning": ["مقاييس الأداء (Accuracy, F1-Score, RMSE)", "التحقق المتقاطع (Cross-Validation)", "ضبط المعلمات الفائقة (Hyperparameter Tuning / GridSearch)"]
    },
    "3. التعلم العميق\nDeep Learning (DL)": {
        "الشبكات العصبية الأساسية\nNeural Networks (MLP)": ["الخلايا العصبية والانتشار العكسي (Perceptrons & Backpropagation)", "دوال التنشيط (ReLU, Sigmoid, Softmax)", "دوّال الخسارة والتحسين (Loss Functions & Adam Optimizer)"],
        "الرؤية الحاسوبية\nComputer Vision (CNNs)": ["طبقات الطي (Convolutional Layers)", "تصنيف واكتشاف الكائنات (Classification & Object Detection)", "تجزئة الصور (Image Segmentation: YOLO, U-Net)"],
        "معالجة اللغات الطبيعية\nNLP": ["تضمين الكلمات (Word2Vec, GloVe)", "الشبكات المتكررة (RNNs & LSTMs)", "آلية الانتباه (Attention Mechanism)"]
    },
    "4. مسار الذكاء التوليدي والحديث\nModern Generative AI": {
        "بنية المحولات\nTransformers": ["المحولات المشفرة (Encoder-Only: BERT)", "المحولات المولّدة (Decoder-Only: GPT Series)"],
        "النماذج اللغوية الكبيرة\nLLMs": ["التدريب المسبق الهائل (Large-Scale Pre-training)", "الضبط الدقيق (Fine-Tuning: LoRA, QLoRA)", "التوليد المعزز بالاسترجاع (RAG)"],
        "توجيه ومواءمة النماذج\nPrompting & Alignment": ["تصميم هندسة الأوامر (Prompt Engineering)", "التعلم المعزز من البشر (RLHF / DPO)", "الوكلاء الذاتيون (Autonomous AI Agents)"],
        "نماذج التوليد المتعدد الوسائط\nMultimodal Models": ["نماذج الانتشار للصور (Diffusion Models: Stable Diffusion)", "توليد الفيديو والصوتيات (Text-to-Video/Audio)"]
    },
    "5. الجانب العملي وهندسة التشغيل\nPractical ML & MLOps": {
        "بناء التطبيقات الكاملة\nBuilding Applications": ["إطارات العمل (LangChain, LlamaIndex)", "تطوير واجهات برمجة التطبيقات (FastAPI)"],
        "أدوات وبيئات الصناعة\nIndustry Frameworks": ["بيئة العمل العميقة (PyTorch vs TensorFlow)", "منصة نماذج الذكاء (HuggingFace)"],
        "نشر النماذج ومراقبتها\nDeployment & Monitoring": ["الحاويات وأنظمة التنسيق (Docker & Kubernetes)", "النشر السحابي السريع (AWS, Azure, GCP)", "مراقبة الانحراف وإدارة دورة الحياة (Data Drift / Model Registry)"]
    },
    "6. الحقيقة المرة في الصناعة\nThe Hard Industry Truth": {
        "الوهم مقابل الواقع\nHype vs Reality": ["الذكاء الاصطناعي مجرد إحصاء مركب (It is Math, not Consciousness)", "الخوارزميات غبية بدون بيانات (GIGO)", "محدودية الاستدلال الحقيقي (Lack of Genuine Reasoning)"],
        "هيمنة البنية التحتية\nThe Hardware Monopoly": ["احتكار الشركات لشرائح العتاد (Nvidia GPU Monopoly)", "التكلفة الباهظة جداً للتدريب (Astronomical Training Costs)", "التأثير البيئي واستهلاك الطاقة (Massive Power Consumption)"],
        "تحديات خطيرة\nCritical Challenges": ["مشكلة الصندوق الأسود (The Black Box & Interpretability)", "التحيز المعرفي الموروث من البيانات (Data Bias & Fairness)", "التشفير والأمان (Security Vulnerabilities)"]
    }
}

# ─── 2. Rich Professional Styling by Depth ─────────────────────
def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    
    # Custom Cyberpunk/Neon Theme (Pink / Purple / Violet)
    if depth == 0:
        node["label"] = {
            "fontSize": 26, "color": "#050505", "fontWeight": "bold", 
            "backgroundColor": "#ff007f", "padding": [18, 30], "borderRadius": 15
        }
        node["symbolSize"] = 40
        node["itemStyle"] = {"color": "#ff007f", "borderColor": "#ffffff", "borderWidth": 3}

    elif depth == 1:
        node["label"] = {
            "fontSize": 18, "color": "#ffffff", "fontWeight": "bold", 
            "backgroundColor": "#8a2be2", "padding": [12, 22], "borderRadius": 10
        }
        node["symbolSize"] = 24
        node["itemStyle"] = {"color": "#8a2be2", "borderColor": "#ffd1ff", "borderWidth": 2}

    elif depth == 2:
        node["label"] = {
            "fontSize": 15, "color": "#ffffff", "fontWeight": "bold",
            "backgroundColor": "#d100d1", "padding": [8, 16], "borderRadius": 8,
            "borderWidth": 1, "borderColor": "#ff66ff"
        }
        node["symbolSize"] = 16
        node["itemStyle"] = {"color": "#d100d1"}

    elif depth == 3:
        node["label"] = {
            "fontSize": 13, "color": "#ffe6ff", "fontWeight": "bold",
            "backgroundColor": "#4b0082", "padding": [6, 12], "borderRadius": 6,
        }
        node["symbolSize"] = 10
        node["itemStyle"] = {"color": "#4b0082"}

    else:
        node["label"] = {
            "fontSize": 12, "color": "#b3b3cc",
            "backgroundColor": "transparent"
        }
        node["symbolSize"] = 6
        node["itemStyle"] = {"color": "#5e5e7a"}

    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
        
    return node

root_label = "أعماق الذكاء الاصطناعي وحقيقته\nThe Deep Reality of AI"
tree_data = [dict_to_tree(root_label, learn_ai_map)]

# ─── 3. Generate the Interactive Mindmap ───────────────────────
def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(
        width="100%", 
        height="3200px", # Extreme height for huge rich structure
        theme="dark",
        bg_color="#080012", # Very dark violent background
        page_title="AI Learning & Truth",
        renderer="svg"
    ))
    
    c.add(
        series_name="",
        data=data,
        orient="LR",
        initial_tree_depth=-1,
        symbol="emptyCircle",
        edge_shape="curve",
        edge_fork_position="50%",
        is_roam=True,
        label_opts=opts.LabelOpts(position="right")
    )
    
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title="خارطة الطريق الحقيقية لتعلم الذكاء الاصطناعي",
            subtitle="The Ultimate Deep Dive Roadmap & Truth About AI",
            pos_left="center",
            pos_top="1%",
            title_textstyle_opts=opts.TextStyleOpts(color="#ff007f", font_size=42, font_weight="bolder"),
            subtitle_textstyle_opts=opts.TextStyleOpts(color="#d896ff", font_size=22)
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "saveAsImage": {"type": "png", "name": "learning_ai_truth_mindmap", "title": "Save PNG", "pixelRatio": 4}
            }
        )
    )
    
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Enhanced AI Roadmap generated successfully: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "learning_ai_truth_mindmap.html")
