@Echo off
title INSTALL Mmdrza.Com
Pushd "%~dp0"
pip install rich blocksmith lxml requests
:loop
python EthClearTrial.py
goto loop
