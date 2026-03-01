import os
from pyecharts import options as opts
from pyecharts.charts import Tree

cybersecurity_map = {
    "1. أساسيات الأمن السيبراني\nCybersecurity Fundamentals": {
        "ثلاثية CIA\nCIA Triad": {
            "السرية\nConfidentiality": ["التشفير (Encryption)", "التحكم بالوصول (Access Control)", "تصنيف البيانات (Data Classification)"],
            "النزاهة\nIntegrity": ["التجزئة (Hashing - SHA-256)", "التوقيعات الرقمية (Digital Signatures)", "سلاسل الكتل (Blockchain)"],
            "التوفر\nAvailability": ["النسخ الاحتياطي (Backup)", "التكرار (Redundancy)", "خطط استمرارية العمل (Business Continuity)"]
        },
        "التشفير بالتفصيل\nCryptography Deep Dive": {
            "التشفير المتماثل\nSymmetric": ["AES-256 - المعيار الذهبي", "ChaCha20 - سريع على الأجهزة المحمولة", "مفتاح واحد للتشفير وفك التشفير"],
            "التشفير غير المتماثل\nAsymmetric": ["RSA - 2048/4096 بت", "ECC - أقصر وأسرع (Elliptic Curve)", "مفتاح عام + مفتاح خاص", "أساس HTTPS وSSL/TLS"],
            "التجزئة\nHashing": ["SHA-256 - غير قابل للعكس (One-way)", "bcrypt - لتخزين كلمات المرور", "Argon2 - الأحدث والأأمن", "HMAC - التحقق من سلامة الرسائل"]
        },
        "نموذج الطبقات السبع\nDefense in Depth": ["الأمن الفيزيائي (Physical Security)", "أمن الشبكة (Network Security)", "أمن المضيف (Host Security)", "أمن التطبيقات (Application Security)", "أمن البيانات (Data Security)", "سياسات وإجراءات (Policies)", "التوعية البشرية (Human Awareness)"]
    },
    "2. أنواع الهجمات\nAttack Types": {
        "الهندسة الاجتماعية\nSocial Engineering": {
            "التصيد\nPhishing": ["التصيد العام (Mass Phishing)", "التصيد الموجه (Spear Phishing)", "تصيد الحيتان (Whaling - استهداف المدراء)", "التصيد الصوتي (Vishing)", "التصيد بالرسائل (Smishing)"],
            "تقنيات أخرى\nOther Techniques": ["انتحال الهوية (Pretexting)", "الطعم USB (Baiting)", "التتبع الخلفي (Tailgating)", "Quid Pro Quo - خدمة مقابل معلومة"]
        },
        "هجمات الشبكات\nNetwork Attacks": {
            "حجب الخدمة\nDDoS": ["حجب الخدمة الموزع (Distributed Denial of Service)", "هجمات Botnet (شبكة أجهزة مصابة)", "Amplification Attacks", "أكبر هجوم: 3.47 Tbps على Azure 2022"],
            "اعتراض الاتصالات\nInterception": ["هجوم الرجل في الوسط (Man-in-the-Middle)", "تسميم ARP (ARP Spoofing)", "تسميم DNS (DNS Poisoning)", "التنصت على WiFi المفتوح"]
        },
        "هجمات التطبيقات\nApplication Attacks": ["حقن SQL (SQL Injection)", "البرمجة عبر المواقع XSS", "تزوير الطلبات CSRF", "تجاوز المصادقة (Authentication Bypass)", "OWASP Top 10 - أخطر 10 ثغرات"],
        "البرمجيات الخبيثة\nMalware": {
            "الأنواع\nTypes": ["فيروسات الفدية (Ransomware - WannaCry, LockBit)", "أحصنة طروادة (Trojans)", "برامج التجسس (Spyware - Pegasus)", "الجذور الخفية (Rootkits)", "الديدان (Worms)", "Keyloggers - تسجيل لوحة المفاتيح"],
            "هجمات شهيرة\nFamous Attacks": ["WannaCry 2017 - 200,000 جهاز في 150 دولة", "SolarWinds 2020 - اختراق حكومي أمريكي", "Colonial Pipeline 2021 - شلل في الوقود", "Log4Shell 2021 - ثغرة في كل مكان"]
        }
    },
    "3. الدفاع والحماية\nDefense & Protection": {
        "أمن الشبكات\nNetwork Security": ["الجدران النارية (Firewalls - Hardware & Software)", "كشف التسلل IDS / منع التسلل IPS", "تقسيم الشبكة (Network Segmentation)", "VPN - النفق المشفر", "Zero Trust Architecture - لا تثق بأحد"],
        "أمن الهوية\nIdentity Security": {
            "المصادقة\nAuthentication": ["كلمات المرور القوية (16+ حرف)", "المصادقة الثنائية 2FA (TOTP, SMS)", "مفاتيح المرور FIDO2 / Passkeys", "المصادقة البيومترية (Biometric)"],
            "إدارة الوصول\nAccess Management": ["مبدأ الصلاحية الأقل (Least Privilege)", "الوصول المبني على الأدوار (RBAC)", "إدارة الهوية المركزية (IAM)"]
        },
        "الاستجابة للحوادث\nIncident Response": ["1. التحضير والتخطيط (Preparation)", "2. الكشف والتحليل (Detection & Analysis)", "3. الاحتواء (Containment)", "4. الاستئصال (Eradication)", "5. التعافي (Recovery)", "6. الدروس المستفادة (Lessons Learned)"],
        "الأمن الهجومي\nOffensive Security": ["اختبار الاختراق (Penetration Testing)", "صيد الثغرات (Bug Bounty)", "الفريق الأحمر مقابل الأزرق (Red Team vs Blue Team)", "أدوات: Kali Linux, Metasploit, Burp Suite"]
    },
    "4. الخصوصية الرقمية\nDigital Privacy": {
        "أدوات الحماية\nPrivacy Tools": {
            "التصفح الآمن\nSecure Browsing": ["متصفح Tor - تصفح مجهول", "Brave Browser - حظر التتبع", "إضافة uBlock Origin", "محركات بحث خاصة: DuckDuckGo, Startpage"],
            "الاتصال المشفر\nEncrypted Communication": ["Signal - الأكثر أماناً (E2E Encryption)", "ProtonMail - بريد مشفر", "Matrix/Element - دردشة لامركزية"]
        },
        "تهديدات الخصوصية\nPrivacy Threats": ["ملفات تعريف الارتباط (Tracking Cookies)", "بصمة المتصفح (Browser Fingerprinting)", "تسريبات البيانات الضخمة (Data Breaches)", "الرقابة الحكومية (Government Surveillance)", "جمع البيانات من التطبيقات المجانية"]
    },
    "📚 المراجع\nReferences": ["NIST Cybersecurity Framework", "OWASP Top 10 (2021)", "Bruce Schneier - Applied Cryptography (1996)", "Kevin Mitnick - Art of Deception (2002)", "MITRE ATT&CK Framework"]
}

def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    colors = [
        {"label": {"fontSize": 24, "color": "#00ff41", "fontWeight": "bold", "backgroundColor": "#0a0a0a", "padding": [16, 28], "borderRadius": 12, "borderWidth": 2, "borderColor": "#00ff41"}, "symbolSize": 35, "itemStyle": {"color": "#00ff41", "borderColor": "#fff", "borderWidth": 3}},
        {"label": {"fontSize": 16, "color": "#00e676", "fontWeight": "bold", "backgroundColor": "#1a1a1a", "padding": [10, 20], "borderRadius": 8, "borderWidth": 1, "borderColor": "#00e676"}, "symbolSize": 20, "itemStyle": {"color": "#00e676"}},
        {"label": {"fontSize": 14, "color": "#76ff03", "fontWeight": "bold", "backgroundColor": "#2a2a2a", "padding": [6, 14], "borderRadius": 6, "borderWidth": 1, "borderColor": "#33691e"}, "symbolSize": 12, "itemStyle": {"color": "#33691e"}},
        {"label": {"fontSize": 13, "color": "#b9f6ca", "fontWeight": "bold", "backgroundColor": "#1b1b1b", "padding": [4, 10], "borderRadius": 4}, "symbolSize": 8, "itemStyle": {"color": "#1b5e20"}},
    ]
    style = colors[min(depth, 3)] if depth <= 3 else {"label": {"fontSize": 12, "color": "#69f0ae", "backgroundColor": "transparent"}, "symbolSize": 6, "itemStyle": {"color": "#2e7d32"}}
    node.update(style)
    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
    return node

tree_data = [dict_to_tree("الأمن السيبراني\nCybersecurity", cybersecurity_map)]

def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(width="100%", height="4200px", theme="dark", bg_color="#000000", page_title="Cybersecurity", renderer="svg"))
    c.add(series_name="", data=data, orient="LR", initial_tree_depth=-1, symbol="emptyCircle", edge_shape="curve", edge_fork_position="50%", is_roam=True, label_opts=opts.LabelOpts(position="right"))
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="الأمن السيبراني", subtitle="Hack the Planet — Or Defend It", pos_left="center", pos_top="1%", title_textstyle_opts=opts.TextStyleOpts(color="#00ff41", font_size=40, font_weight="bolder"), subtitle_textstyle_opts=opts.TextStyleOpts(color="#69f0ae", font_size=20)),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(is_show=True, feature={"saveAsImage": {"type": "png", "name": "cybersecurity_map", "title": "Save PNG", "pixelRatio": 4}})
    )
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Cybersecurity Map generated: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "cybersecurity_mindmap.html")
