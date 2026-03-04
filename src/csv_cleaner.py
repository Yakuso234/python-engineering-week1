"""CSV数据清洗工具最小可运行版本 - Week1周三核心产出"""

import argparse
import os

import pandas as pd


def clean_csv(raw_path: str, save_path: str):
    # 1. 先读入csv文件
    try:
        df = pd.read_csv(raw_path, encoding="utf-8")
    except Exception:
        df = pd.read_csv(raw_path, encoding="gbk")
    # 2. 去空值
    df = df.dropna()
    # 3. 去重复行
    df = df.drop_duplicates(keep="first")
    # 4. 重置索引
    df = df.reset_index(drop=True)
    # 5. 导出清洗之后的csv文件
    os.makedirs(os.path.dirname(save_path), exist_ok=True)  # 确保目录存在
    df.to_csv(save_path, index=False, encoding="utf-8-sig")  # 保存为csv

    # 6. 打印清洗结果
    raw_total = len(pd.read_csv(raw_path))
    print(f"清洗已经完成！原始数据{raw_total},清洗后{len(df)}")

    # 主程序入口：


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="极简csv清洗工具：去空值+去重复行+重置索引"
    )
    parser.add_argument("raw_path", help="原始csv文件路径,例如：data/raw/test.csv")
    parser.add_argument(
        "save_path", help="清洗后csv保存路径，例如：data/cleaned/clean_test.csv"
    )
    args = parser.parse_args()
    clean_csv(args.raw_path, args.save_path)
