# 项目说明

## 项目简介

本项目为基于 Python 的 BiliBili 数据查询与处理工具，支持将数据写入 Excel 文件，并可通过打包为 Windows
可执行文件（exe）便于分发和使用。项目结构清晰，包含主程序、模块化代码及资源文件，适合数据采集、分析及自动化办公场景。

## 目录结构

```
.
├── main.py                  # 主程序入口
├── module/                  # 功能模块目录
│   └── ...                  # 具体模块文件
├── Resources/
│   └── app.ico              # 应用程序图标
├── README.md                # 项目说明文档
```

## 环境依赖

- Python 3.7 及以上
- pip
- openpyxl
- pyinstaller

### 安装依赖

在命令行中执行：

```bash
pip install -r requirements.txt
```

如无 `requirements.txt`，可手动安装主要依赖：

```bash
pip install openpyxl pyinstaller
```

## 使用说明

### 运行源码

直接运行主程序：

```bash
python main.py
```

### 打包为 Windows 可执行文件

本项目推荐使用 PyInstaller 进行打包，命令如下：

```bash
pyinstaller --icon=Resources/app.ico --contents-director libs --name bilibiliDataCrawling main.py
```

**参数说明：**

- `--icon=Resources/app.ico`：指定 exe 图标
- `--contents-director libs`：指定生成的依赖文件夹名称
- `--name bilibiliDataCrawling`：指定输出文件名

## 功能简介

- 数据采集与处理
- 支持将数据写入 Excel 文件，保留原有内容
- 模块化设计，便于扩展
- 可打包为 Windows 独立应用

## 联系方式

如有问题或建议，请通过 Issue 反馈。