"""
Properly add references to all mindmap scripts.
Inserts reference line BEFORE the closing brace of the top-level dict, WITH proper comma.
"""
import os

REFS = {
    "truth_mindmap.py": (
        "truth_map",
        '    "📚 المراجع\\nReferences": ["Quran & Hadith", "Plato - The Republic", "Descartes - Meditations (1641)", "Kant - Critique of Pure Reason (1781)", "Karl Popper - Conjectures and Refutations (1963)"]'
    ),
    "ai_ecosystem_mindmap.py": (
        "ai_map",
        '    "📚 المراجع\\nReferences": ["Stanford AI Index Report", "McKinsey Global AI Survey", "OpenAI Research Papers", "Google DeepMind Publications", "MIT Technology Review"]'
    ),
    "learn_ai_mindmap.py": (
        "learn_map",
        '    "📚 المراجع\\nReferences": ["Andrew Ng - Machine Learning (Coursera)", "Ian Goodfellow - Deep Learning (2016)", "fast.ai - Practical Deep Learning", "Andrej Karpathy - Neural Networks", "Yann LeCun - Deep Learning (Nature 2015)"]'
    ),
    "modern_realities_mindmap.py": (
        "realities_map",
        '    "📚 المراجع\\nReferences": ["Yuval Harari - 21 Lessons (2018)", "Shoshana Zuboff - Surveillance Capitalism (2019)", "Noam Chomsky - Manufacturing Consent (1988)", "Jaron Lanier - Ten Arguments (2018)"]'
    ),
    "psychology_mindmap.py": (
        "psychology_map",
        '    "📚 المراجع\\nReferences": ["Freud - Interpretation of Dreams (1899)", "Carl Jung - Man and His Symbols (1964)", "Daniel Goleman - Emotional Intelligence (1995)", "DSM-5 (APA 2013)"]'
    ),
    "economy_mindmap.py": (
        "economy_map",
        '    "📚 المراجع\\nReferences": ["Adam Smith - Wealth of Nations (1776)", "Keynes - General Theory (1936)", "Satoshi Nakamoto - Bitcoin Whitepaper (2008)", "Ray Dalio - Changing World Order (2021)"]'
    ),
    "civilizations_mindmap.py": (
        "civilizations_map",
        '    "📚 المراجع\\nReferences": ["Ibn Khaldun - Al-Muqaddimah (1377)", "Will Durant - Story of Civilization", "Arnold Toynbee - A Study of History", "Edward Gibbon - Decline and Fall of the Roman Empire (1776)"]'
    ),
    "health_mindmap.py": (
        "health_map",
        '    "📚 المراجع\\nReferences": ["Matthew Walker - Why We Sleep (2017)", "Peter Attia - Outlive (2023)", "Andrew Huberman - Huberman Lab Podcast", "WHO World Health Statistics"]'
    ),
    "cybersecurity_mindmap.py": (
        "cyber_map",
        '    "📚 المراجع\\nReferences": ["NIST Cybersecurity Framework", "OWASP Top 10 (2021)", "Bruce Schneier - Applied Cryptography (1996)", "Kevin Mitnick - Art of Deception (2002)"]'
    ),
    "entrepreneurship_mindmap.py": (
        "entrepreneur_map",
        '    "📚 المراجع\\nReferences": ["Eric Ries - Lean Startup (2011)", "Peter Thiel - Zero to One (2014)", "Ben Horowitz - Hard Thing About Hard Things (2014)", "CB Insights - Startup Failure Report"]'
    ),
    "space_mindmap.py": (
        "space_map",
        '    "📚 المراجع\\nReferences": ["Carl Sagan - Cosmos (1980)", "Stephen Hawking - A Brief History of Time (1988)", "NASA JPL Data", "Neil deGrasse Tyson - Astrophysics for People in a Hurry (2017)"]'
    ),
    "geopolitics_mindmap.py": (
        "geopolitics_map",
        '    "📚 المراجع\\nReferences": ["Henry Kissinger - World Order (2014)", "Brzezinski - The Grand Chessboard (1997)", "Graham Allison - Destined for War (2017)", "Peter Zeihan - End of the World (2022)"]'
    ),
    "biology_mindmap.py": (
        "biology_map",
        '    "📚 المراجع\\nReferences": ["Darwin - On the Origin of Species (1859)", "James Watson - The Double Helix (1968)", "Richard Dawkins - The Selfish Gene (1976)", "Siddhartha Mukherjee - The Gene (2016)"]'
    ),
    "sociology_mindmap.py": (
        "sociology_map",
        '    "📚 المراجع\\nReferences": ["Ibn Khaldun - Al-Muqaddimah (1377)", "Emile Durkheim - Suicide (1897)", "Max Weber - Economy and Society (1922)", "Bourdieu - Distinction (1979)"]'
    ),
    "modern_history_mindmap.py": (
        "modern_history_map",
        '    "📚 المراجع\\nReferences": ["Eric Hobsbawm - Age of Extremes (1994)", "John Keegan - The First World War (1998)", "Antony Beevor - The Second World War (2012)", "Gaddis - The Cold War (2005)"]'
    ),
}

src_dir = "src"
for filename, (var_name, ref_line) in REFS.items():
    filepath = os.path.join(src_dir, filename)
    if not os.path.exists(filepath):
        print(f"⚠️  Not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "المراجع" in content:
        print(f"✅ Already done: {filename}")
        continue
    
    # Find the last top-level entry in the dict and add a comma + new entry
    lines = content.split('\n')
    # Find closing brace of the var_name dict
    # Strategy: find line with just "}" that closes the main dict
    depth = 0
    start_found = False
    insert_at = -1
    
    for i, line in enumerate(lines):
        if f'{var_name} = {{' in line or f'{var_name}= {{' in line or f'{var_name} =' in line:
            start_found = True
            depth = 0
        if start_found:
            for ch in line:
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        insert_at = i
                        break
            if insert_at >= 0:
                break
    
    if insert_at >= 0:
        # Replace the closing "}" with ",\n    ref_line\n}"
        closing_line = lines[insert_at]
        # Find where the } is and insert before it
        indent_match = closing_line.rstrip()
        lines[insert_at] = ref_line + '\n' + closing_line
        
        # Make sure the previous line ends with a comma
        prev_idx = insert_at - 1
        while prev_idx >= 0 and lines[prev_idx].strip() == '':
            prev_idx -= 1
        if prev_idx >= 0:
            prev_line = lines[prev_idx].rstrip()
            if prev_line.endswith('}') or prev_line.endswith(']') or prev_line.endswith('"') or prev_line.endswith("'"):
                if not prev_line.endswith(','):
                    lines[prev_idx] = prev_line + ','
        
        new_content = '\n'.join(lines)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Added refs: {filename}")
    else:
        print(f"❌ Could not find dict end: {filename}")

print("\n🎉 All done!")
