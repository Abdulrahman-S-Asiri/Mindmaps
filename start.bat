@echo off
color 0A
echo ===================================================
echo       Mindmaps Encyclopedia Generator
echo       19 Interactive Knowledge Maps
echo ===================================================
echo.

echo [1/19] Generating Absolute Truth Mindmap...
python src\truth_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [2/19] Generating AI Ecosystem Mindmap...
python src\ai_ecosystem_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [3/19] Generating AI Learning Truth Mindmap...
python src\learn_ai_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [4/19] Generating Modern Realities Mindmap...
python src\modern_realities_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [5/19] Generating Psychology Mindmap...
python src\psychology_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [6/19] Generating Economy Mindmap...
python src\economy_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [7/19] Generating Civilizations Mindmap...
python src\civilizations_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [8/19] Generating Health Mindmap...
python src\health_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [9/19] Generating Learning Philosophy Mindmap...
python src\learning_philosophy_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [10/19] Generating Cybersecurity Mindmap...
python src\cybersecurity_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [11/19] Generating Entrepreneurship Mindmap...
python src\entrepreneurship_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [12/19] Generating Space Mindmap...
python src\space_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [13/19] Generating Quantum Physics Mindmap...
python src\quantum_physics_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [14/19] Generating Philosophy Mindmap...
python src\philosophy_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [15/19] Generating Programming Mindmap...
python src\programming_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [16/19] Generating Modern History Mindmap...
python src\modern_history_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [17/19] Generating Sociology Mindmap...
python src\sociology_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [18/19] Generating Geopolitics Mindmap...
python src\geopolitics_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo [19/19] Generating Biology Mindmap...
python src\biology_mindmap.py
if %ERRORLEVEL% neq 0 (echo Error! & exit /b %ERRORLEVEL%)

echo.
echo ===================================================
echo   All 19 Mindmaps Generated Successfully!
echo ===================================================
echo.
echo Opening Web Portal...
start "" "public\index.html"
