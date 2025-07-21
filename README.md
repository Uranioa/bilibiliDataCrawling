# 项目说明

## 项目简介

本项目为基于 Python 的 BiliBili 数据查询与处理工具，支持将数据写入 Excel 文件，并可通过打包为 Windows 可执行文件（exe）便于分发和使用。项目结构清晰，包含主程序、模块化代码及资源文件，适合数据采集、分析及自动化办公场景。

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
- nuitka

### 安装依赖

在命令行中执行：

```bash
pip install -r requirements.txt
```

如无 `requirements.txt`，可手动安装主要依赖：

```bash
pip install openpyxl nuitka
```

## 使用说明

### 运行源码

直接运行主程序：

```bash
python main.py
```

### 打包为 Windows 可执行文件

本项目推荐使用 Nuitka 进行打包，命令如下：

```bash
nuitka --standalone --windows-icon-from-ico=Resources/app.ico --output-filename=bilibiliDataCrawling.exe --msvc=latest main.py
```

**参数说明：**

- `--standalone`：生成独立文件夹，包含所有依赖
- `--windows-icon-from-ico=Resources/app.ico`：指定 exe 图标
- `--output-filename=bilibiliDataCrawling.exe`：指定输出文件名
- `--msvc=latest`：使用最新版本的 Visual Studio C++ 编译器

> **注意：**  
> 需提前安装 Visual Studio C++ 工具集，或根据 Nuitka 提示配置编译环境。

## 功能简介

- 数据采集与处理
- 支持将数据写入 Excel 文件，保留原有内容
- 模块化设计，便于扩展
- 可打包为 Windows 独立应用

## 常见问题

1. **打包报错缺少编译环境**  
   请确保已安装 Visual Studio C++ 工具集，并在“x64 Native Tools Command Prompt for VS”中执行打包命令。

2. **Excel 数据未保存或被覆盖**  
   请确保写入 Excel 时采用追加或覆盖指定单元格的方式，避免整体覆盖。

## 联系方式

如有问题或建议，请通过 Issue 反馈。