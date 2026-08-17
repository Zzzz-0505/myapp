# myapp —— 你的第一个部署练习项目
import os
from datetime import datetime

from fastapi import FastAPI

# 练习坑 1 在这里：main.py 用到了 python-dotenv，
# 但 requirements.txt 里没有列这一项，装完依赖后启动会报 ModuleNotFoundError。
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="我的部署练习项目")


@app.get("/")
def home():
    """首页：显示问候语和服务器名字"""
    server_name = os.getenv("SERVER_NAME", "myapp")
    return {"message": "部署成功！", "server": server_name}


@app.get("/now")
def now():
    """时间接口：显示服务器当前时间"""
    return {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


@app.get("/broken")
def broken():
    """练习坑 2 在这里：故意用错变量名，访问这个接口一定会报 500。"""
    lucky_number = 7
    return {"lucky_number": lucky_number}
