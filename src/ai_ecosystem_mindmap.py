import os
from pyecharts import options as opts
from pyecharts.charts import Tree

# ─── 1. Deep & Detailed Data Structure ─────────────────────────
ai_ecosystem = {
    "Architecture (الهندسة المعمارية)": {
        "Foundations (الأساسيات)": ["Transformers (المحولات)", "Self-Attention (الانتباه الذاتي)", "Positional Encoding", "Rotary Embeddings (RoPE)"],
        "Tokenization (التقطيع النصي)": ["BPE (Byte Pair Encoding)", "WordPiece", "SentencePiece", "Tiktoken"],
        "Training Pipeline (مسار التدريب)": {
            "Pre-training (التدريب المسبق)": ["Self-Supervised Learning", "Next Token Prediction", "Masked Language Modeling"],
            "Fine-Tuning (الضبط الدقيق)": ["SFT (Supervised Fine-Tuning)", "Instruction Tuning", "Parameter-Efficient (PEFT)"],
            "Alignment (المواءمة)": ["RLHF (التعلم المعزز)", "DPO (التحسين المباشر)", "Constitutional AI", "KTO"]
        },
        "Optimization (التحسين والضغط)": ["Quantization (AWQ/GPTQ/GGUF)", "LoRA / QLoRA / DoRA", "MoE (Mixture of Experts)", "FlashAttention"]
    },
    "Capabilities & Modalities (القدرات والوسائط)": {
        "Text generation (توليد النصوص)": ["Creative Writing (الكتابة الإبداعية)", "Translation (الترجمة)", "Summarization (التلخيص)", "Reasoning (الاستنتاج)"],
        "Code Generation (برمجة)": ["Copilot (مساعد برمجي)", "Code Review (مراجعة الأكواد)", "Bug Fixing (حل المشاكل)"],
        "Vision & Image (الرؤية والصور)": ["Image Generation (Midjourney, DALL-E 3)", "Visual QA (GPT-4V)", "Segmentation (تجزئة الصور)"],
        "Audio & Video (صوت وفيديو)": ["Speech-to-Text (Whisper)", "Text-to-Video (Sora, Runway)", "Voice Generation (ElevenLabs)"],
    },
    "Frameworks & Tooling (أدوات التطوير)": {
        "App Development (بناء التطبيقات)": ["LangChain", "LlamaIndex", "Haystack", "Semantic Kernel"],
        "Agents (الوكلاء المستقلون)": ["AutoGen", "CrewAI", "BabyAGI", "OpenDevin"],
        "Serving & Run (التشغيل والنشر)": ["vLLM", "Ollama", "HuggingFace TGI", "TensorRT-LLM", "LM Studio"],
        "Vector Databases (قواعد المتجهات)": ["Pinecone", "Milvus", "ChromaDB", "Qdrant", "Weaviate"]
    },
    "Players & Models (الشركات والنماذج)": {
        "OpenAI (USA)": ["GPT-4o (Omni)", "GPT-4 Turbo", "Sora (Video)", "o1-preview (Reasoning)"],
        "Google (USA)": ["Gemini 1.5 Pro / Flash", "Gemma 2 (Open)", "AlphaFold (Bio)"],
        "Anthropic (USA)": ["Claude 3.5 Sonnet", "Claude 3 Opus", "Claude 3 Haiku"],
        "Meta (USA)": ["Llama 3.1 405B / 70B", "Llama 3 Vision", "Segment Anything (SAM)"],
        "DeepSeek (China)": ["DeepSeek-V3", "DeepSeek-R1 (Reasoning)", "DeepSeek-Coder"]
    },
    "Hardware (البنية التحتية والعتاد)": {
        "GPUs (وحدات التجزئة الرسومية)": ["Nvidia H100 Hopper", "Nvidia B200 Blackwell", "AMD MI300X"],
        "Custom ASIC (مسرعات مخصصة)": ["Google TPU v5", "AWS Trainium / Inferentia", "Azure Maia"],
        "Cloud Providers (الموفرون السحابيون)": ["AWS", "Microsoft Azure", "Google Cloud (GCP)", "CoreWeave"]
    },
    "📚 المراجع\nReferences": ["Stanford AI Index Report (Annual)", "McKinsey Global AI Survey", "OpenAI Research Papers", "Google DeepMind Publications", "MIT Technology Review"]
}

# ─── 2. Rich Professional Styling by Depth ─────────────────────
def dict_to_tree(name, data, depth=0):
    node = {"name": name}
    
    # Custom AI Ecosystem Theme (Cyan / Blue / White)
    if depth == 0:
        node["label"] = {
            "fontSize": 22, "color": "#0d1117", "fontWeight": "bold", 
            "backgroundColor": "#00ffcc", "padding": [15, 25], "borderRadius": 10
        }
        node["symbolSize"] = 30
        node["itemStyle"] = {"color": "#00ffcc", "borderColor": "#ffffff", "borderWidth": 2}

    elif depth == 1:
        node["label"] = {
            "fontSize": 15, "color": "#ffffff", "fontWeight": "bold", 
            "backgroundColor": "#1f6feb", "padding": [8, 16], "borderRadius": 8,
            "borderWidth": 1, "borderColor": "#388bfd"
        }
        node["symbolSize"] = 16
        node["itemStyle"] = {"color": "#1f6feb"}

    elif depth == 2:
        node["label"] = {
            "fontSize": 13, "color": "#ffffff", "fontWeight": "bold",
            "backgroundColor": "#238636", "padding": [5, 12], "borderRadius": 5,
        }
        node["symbolSize"] = 10
        node["itemStyle"] = {"color": "#238636"}

    else:
        node["label"] = {
            "fontSize": 12, "color": "#c9d1d9",
            "backgroundColor": "transparent"
        }
        node["symbolSize"] = 6
        node["itemStyle"] = {"color": "#8b949e"}

    if isinstance(data, dict):
        node["children"] = [dict_to_tree(k, v, depth + 1) for k, v in data.items()]
    elif isinstance(data, list):
        node["children"] = [dict_to_tree(item, None, depth + 1) for item in data]
        
    return node

root_label = "AI Ecosystem\n(منظومة الذكاء الاصطناعي)"
tree_data = [dict_to_tree(root_label, ai_ecosystem)]

# ─── 3. Generate the Interactive Mindmap ───────────────────────
def create_mindmap(data, filename):
    c = Tree(init_opts=opts.InitOpts(
        width="100%", 
        height="2200px", # Increased layout space
        theme="dark",
        bg_color="#0a0e14", # Deep professional dark
        page_title="AI Ecosystem",
        renderer="svg"
    ))
    
    c.add(
        series_name="",
        data=data,
        orient="LR",
        initial_tree_depth=-1,
        symbol="emptyCircle",
        edge_shape="curve",
        edge_fork_position="63%",
        is_roam=True,
        label_opts=opts.LabelOpts(position="right")
    )
    
    c.set_global_opts(
        title_opts=opts.TitleOpts(
            title="منظومة الذكاء الاصطناعي الشاملة 2026",
            subtitle="The Ultimate AI Ecosystem Blueprint",
            pos_left="center",
            pos_top="2%",
            title_textstyle_opts=opts.TextStyleOpts(color="#00ffcc", font_size=38, font_weight="bolder"),
            subtitle_textstyle_opts=opts.TextStyleOpts(color="#8b949e", font_size=18)
        ),
        tooltip_opts=opts.TooltipOpts(trigger="item", trigger_on="mousemove"),
        toolbox_opts=opts.ToolboxOpts(
            is_show=True,
            feature={
                "saveAsImage": {"type": "png", "name": "ai_ecosystem_map", "title": "Save PNG", "pixelRatio": 4}
            }
        )
    )
    
    output_path = os.path.abspath(os.path.join("public", filename))
    c.render(output_path)
    print(f"✅ Enhanced Mindmap generated successfully: {output_path}")

if __name__ == "__main__":
    create_mindmap(tree_data, "ai_mindmap_huge.html")
