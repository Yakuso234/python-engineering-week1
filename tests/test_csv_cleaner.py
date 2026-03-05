"""CSV清洗工具基础单元测试 - Week1周三"""

import os

import pandas as pd
import pytest

from src.csv_cleaner import clean_csv


# 自动创建+删除临时测试文件，不用手动管理
@pytest.fixture
def temp_test_files():
    raw_path = "data/raw/temp_test.csv"
    save_path = "data/cleaned/temp_clean_test.csv"

    pd.DataFrame(
        {"name": ["张三", "李四", None, "张三"], "age": [25, None, 28, 25]}
    ).to_csv(raw_path, index=False, encoding="utf-8")

    yield raw_path, save_path

    if os.path.exists(raw_path):
        os.remove(raw_path)
    if os.path.exists(save_path):
        os.remove(save_path)


# 测试1 清洗后文件可以正常生成：
def test_clean_csv_file_generated(temp_test_files):
    raw_path, save_path = temp_test_files

    clean_csv(raw_path, save_path)

    assert os.path.exists(save_path)


# 测试2 清洗后数据正确去空，去重：
def test_clean_csv_data_correct(temp_test_files):
    raw_path, save_path = temp_test_files

    clean_csv(raw_path, save_path)

    cleaned_df = pd.read_csv(save_path)

    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]["name"] == "张三"


# 新增测试3：指定单列去空（只删name列空值）
def test_clean_csv_specify_single_col(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path, drop_na_cols=["name"])
    cleaned_df = pd.read_csv(save_path)
    assert len(cleaned_df) == 2  # 原始4行，删name空值后剩3行（去重后）


# 新增测试4：指定多列去空（删name+age列空值）
def test_clean_csv_specify_multi_cols(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path, drop_na_cols=["name", "age"])
    cleaned_df = pd.read_csv(save_path)
    assert len(cleaned_df) == 1  # 只保留张三（无空值）
