@echo off
color 0A
echo ===================================================
echo       Mindmaps Encyclopedia Generator
echo       30 Interactive Knowledge Maps
echo ===================================================
echo.

echo [1/30] Absolute Truth...
python src\truth_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [2/30] AI Ecosystem...
python src\ai_ecosystem_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [3/30] AI Learning Truth...
python src\learn_ai_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [4/30] Modern Realities...
python src\modern_realities_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [5/30] Psychology...
python src\psychology_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [6/30] Economy...
python src\economy_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [7/30] Civilizations...
python src\civilizations_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [8/30] Health...
python src\health_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [9/30] Learning Philosophy...
python src\learning_philosophy_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [10/30] Cybersecurity...
python src\cybersecurity_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [11/30] Entrepreneurship...
python src\entrepreneurship_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [12/30] Space...
python src\space_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [13/30] Quantum Physics...
python src\quantum_physics_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [14/30] Philosophy...
python src\philosophy_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [15/30] Programming...
python src\programming_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [16/30] Modern History...
python src\modern_history_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [17/30] Sociology...
python src\sociology_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [18/30] Geopolitics...
python src\geopolitics_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [19/30] Biology...
python src\biology_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [20/30] Mathematics...
python src\mathematics_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [21/30] Religion...
python src\religion_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [22/30] Languages...
python src\languages_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [23/30] Personal Finance...
python src\personal_finance_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [24/30] Law...
python src\law_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [25/30] Media & Propaganda...
python src\media_propaganda_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [26/30] Energy & Climate...
python src\energy_climate_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [27/30] Food & Agriculture...
python src\food_agriculture_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [28/30] Conspiracy Analysis...
python src\conspiracy_analysis_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [29/30] Influence & Persuasion...
python src\influence_persuasion_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [30/30] Art & Creativity...
python src\art_creativity_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo.
echo ===================================================
echo   All 30 Mindmaps Generated Successfully!
echo ===================================================
echo.
echo Opening Web Portal...
start "" "public\index.html"
