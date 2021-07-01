#!/bin/bash
pip3 install -r "conf/requirements.txt"  -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com
pyarmor obfuscate py/qzqxdata_main.py
nohup python3 -u dist/qzqxdata_main.py > log/print.log 2>&1 &
#nohup python3 -u py/qzqxdata_main.py > log/print.log 2>&1 &
rm -rf py