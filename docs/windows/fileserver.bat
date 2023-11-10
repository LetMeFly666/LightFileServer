@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
F:
cd F:\OtherApps\Program\Git\Store\Store45_LightFileServer\LightFileServer
python server.py
