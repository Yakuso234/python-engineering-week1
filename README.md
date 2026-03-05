# Week1 - CSV数据清洗小工具
Python工程化入门实战项目：轻量级CSV文件清洗命令行工具，支持空值删除、重复行删除，兼容中文编码与空白文件。

 📌 核心功能
- 📖 编码兼容：自动适配UTF-8/GBK编码，解决Excel导出CSV乱码问题
- 🗑️ 空值清理：支持「删除所有空值行」或「仅删除指定列空值行」
- 🔄 重复行去重：自动删除重复行，仅保留首次出现的记录
- 📁 自动建目录：保存文件时自动创建不存在的目录，无需手动操作
- 🧰 鲁棒性强：完美处理空白CSV文件，无报错终止

📂 项目目录结构  

week1/  

├── data/ # 数据存储目录（规范分类）  

│ ├── raw/ # 原始 CSV 文件（待清洗）  

│ └── cleaned/ # 清洗后的 CSV 文件（输出）  

├── src/ # 核心源代码目录  

│ └── csv_cleaner.py # 清洗工具主程序  

├── tests/ # 单元测试目录  

│ └── test_csv_cleaner.py # 8 条完整测试用例  

├── scripts/ # 20 道 Python 练习题目录  

├── README.md # 项目说明文档（当前文件）  

├── pyproject.toml # 工程化配置（格式化 / 测试）    

├──requirements.txt #记录 Python 项目所有依赖的清单文件

└── .gitignore # Git 忽略配置（不提交冗余文件）  

  剩下三个文件simple_output.csv,test.txt,text.csv都是用于20道python测试题的文件，与清洗小工具无关


 🚀 快速使用指南  
 
 1. 前置准备（激活虚拟环境）
    
打开PowerShell，进入`week1`根目录，执行以下命令激活虚拟环境（前缀出现`(.venv)`即为成功）：

输入PowerShell  

. .\.venv\Scripts\Activate.ps1  

3. 基础清洗（删除所有空值行 + 去重）
   
适用于需要清理所有含空值行的场景，命令格式：  

python src/csv_cleaner.py 原始文件路径 保存文件路径  

示例：  

python src/csv_cleaner.py data/raw/test.csv data/cleaned/result.csv  

5. 进阶清洗（仅删除指定列空值）
   
适用于只清理特定列空值的场景，添加--drop-na-cols参数（多列用英文逗号分隔）：  
 
python src/csv_cleaner.py data/raw/test.csv data/cleaned/result.csv --drop-na-cols name,age  

🧪 测试与覆盖率验证  

1. 运行所有测试用例（共 8 条）
   
先设置 Python 路径（避免模块找不到），再运行测试，预期显示8 passed：  

设置Python路径（当前PowerShell窗口有效）  

$env:PYTHONPATH = "$(Get-Location)"  

运行测试  

pytest tests/ -v  

3. 查看代码覆盖率
   
验证代码被测试覆盖的比例（本项目覆盖率≥70%，达标）：  

pytest tests/ --cov=src --cov-report=term  

💡 新手避坑提示  

所有命令必须在week1根目录下执行。  
 
文件路径请使用英文，避免中文路径导致报错。  

--drop-na-cols参数的列名分隔符必须是英文逗号，不可用中文逗号。  

虚拟环境激活后，所有操作均需在(.venv)环境下完成。  
