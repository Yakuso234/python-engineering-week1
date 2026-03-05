"""CSV数据清洗工具 - Week1周五最终版（支持空文件处理）"""
import argparse
import os
import pandas as pd
from pandas.errors import EmptyDataError

def clean_csv(raw_path: str, save_path: str, drop_na_cols: list[str] = None):
    # 1. 读取CSV文件（处理空文件+编码问题）
    try:
        df = pd.read_csv(raw_path, encoding="utf-8")
    except EmptyDataError:
        # 空文件直接返回空DataFrame
        df = pd.DataFrame()
    except Exception:
        # 编码错误换GBK读取
        df = pd.read_csv(raw_path, encoding="gbk")
    
    # 2. 计算原始行数（核心修复：加异常捕获，避免空文件报错）
    try:
        raw_df = pd.read_csv(raw_path, encoding="utf-8")
        raw_total = len(raw_df)
    except (EmptyDataError, Exception):
        # 空文件/编码错误都算0行
        raw_total = 0
    
    # 3. 去空值
    if drop_na_cols:
        df = df.dropna(subset=drop_na_cols)
    else:
        df = df.dropna()
    
    # 4. 去重复行
    df = df.drop_duplicates(keep="first")
    
    # 5. 重置索引
    df = df.reset_index(drop=True)
    
    # 6. 导出文件
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False, encoding="utf-8-sig")

    # 7. 打印结果
    print(f" 清洗完成！原始数据{raw_total}行 → 清洗后{len(df)}行")

# 主程序入口
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="极简csv清洗工具：去空值+去重复行+重置索引（支持空文件）"
    )
    parser.add_argument("raw_path", help="原始csv文件路径,例如：data/raw/test.csv")
    parser.add_argument(
        "save_path", help="清洗后csv保存路径，例如：data/cleaned/clean_test.csv"
    )
    parser.add_argument(
        "--drop-na-cols", 
        type=str, 
        default=None,
        help="指定去空值的列，多列用英文逗号分隔，例如：name,age"
    )

    args = parser.parse_args()
    drop_na_cols = args.drop_na_cols.split(",") if args.drop_na_cols else None
    clean_csv(args.raw_path, args.save_path, drop_na_cols)