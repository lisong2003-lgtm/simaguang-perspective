@echo off
rem prepare_input 跨平台 CLI 入口（Windows；macOS/Linux 用 scripts/prepare_input.sh）。
setlocal
set "PY_SCRIPT=%~dp0prepare_input.py"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%PY_SCRIPT%" %*
  exit /b %errorlevel%
)
where python >nul 2>nul
if %errorlevel%==0 (
  python "%PY_SCRIPT%" %*
  exit /b %errorlevel%
)
echo [prepare_input] 未找到 Python 3（py/python）；请安装 Python 并加入 PATH 1>&2
exit /b 127
