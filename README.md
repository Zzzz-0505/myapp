# myapp —— 部署练习小项目

这是一个"今日播报"小应用，用来完整练习"从 0 到手机能访问"的部署流程。
它一共有 3 个接口：

| 接口 | 地址 | 作用 |
|---|---|---|
| 首页 | `/` | 显示问候语和服务器名字 |
| 时间 | `/now` | 显示服务器当前时间 |
| 坏接口 | `/broken` | 故意写错的接口，用于练习看日志排错 |

## 故意留下的两个坑（请先知道，再动手）

**坑 1：requirements.txt 里缺少 python-dotenv**

`main.py` 里用到了 `python-dotenv`（用来读 `.env` 配置文件的库），但 `requirements.txt` 里没有列它。

- 现象：`pip install -r requirements.txt` 这步不会报错；报错发生在下一步用 `uvicorn main:app` 启动服务时，会立刻退出，日志显示 `ModuleNotFoundError: No module named 'dotenv'`。
- 修法：在 `requirements.txt` 里加一行 `python-dotenv`，然后重新执行 `pip install -r requirements.txt`。

**坑 2：`/broken` 接口用错了变量名**

`/broken` 函数里定义了 `lucky_number`，但 `return` 时写成了 `unlucky_number`（一个不存在的变量）。

- 现象：服务能正常启动，首页和时间接口都正常，但访问 `/broken` 返回 500，日志里能看到 `NameError: name 'unlucky_number' is not defined`。
- 修法：把 `return {"lucky_number": unlucky_number}` 改成 `return {"lucky_number": lucky_number}`。

## 本地快速试跑

```bash
python3 -m venv venv
source venv/bin/activate        # Windows 的 PowerShell 用 venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

然后浏览器打开 `http://127.0.0.1:8000`，能显示 JSON 就说明环境没问题。
