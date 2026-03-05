"""CSV清洗工具完整测试用例（8条）- Week1周五"""
import pytest
import pandas as pd
import os
from src.csv_cleaner import clean_csv

# 自动创建/删除临时测试文件
@pytest.fixture
def temp_test_files():
    raw_path = "data/raw/temp_test.csv"
    save_path = "data/cleaned/temp_clean_test.csv"
    # 写入测试数据（4行：含空值、重复行）
    pd.DataFrame({
        "name": ["张三", "李四", None, "张三"],
        "age": [25, None, 28, 25]
    }).to_csv(raw_path, index=False, encoding="utf-8")
    yield raw_path, save_path
    # 测试结束自动清理临时文件
    if os.path.exists(raw_path):
        os.remove(raw_path)
    if os.path.exists(save_path):
        os.remove(save_path)

# 测试1：清洗后文件是否生成
def test_clean_csv_file_generated(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path)
    assert os.path.exists(save_path)

# 测试2：默认清洗（删所有空值+去重）
def test_clean_csv_data_correct(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path)
    cleaned_df = pd.read_csv(save_path)
    assert len(cleaned_df) == 1
    assert cleaned_df.iloc[0]["name"] == "张三"

# 测试3：指定单列去空（只删name列空值）
def test_clean_csv_specify_single_col(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path, drop_na_cols=["name"])
    cleaned_df = pd.read_csv(save_path)
    assert len(cleaned_df) == 2  # 删name空值(1行)+去重(1行)→剩2行

# 测试4：指定多列去空（删name+age列空值）
def test_clean_csv_specify_multi_cols(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path, drop_na_cols=["name", "age"])
    cleaned_df = pd.read_csv(save_path)
    assert len(cleaned_df) == 1

# 测试5：不传参数，默认删所有空值行
def test_clean_csv_default_drop_all(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path)
    cleaned_df = pd.read_csv(save_path)
    assert len(cleaned_df) == 1

# 测试6：空CSV文件清洗不报错
def test_clean_empty_csv(temp_test_files):
    raw_path, save_path = temp_test_files
    # 覆盖为空白CSV
    pd.DataFrame().to_csv(raw_path, index=False)
    clean_csv(raw_path, save_path)
    assert os.path.exists(save_path)  # 确保文件仍生成

# 测试7：去重后指定列无重复值
def test_clean_duplicate_only_name(temp_test_files):
    raw_path, save_path = temp_test_files
    clean_csv(raw_path, save_path, drop_na_cols=["name"])
    df = pd.read_csv(save_path)
    # 验证name列无重复
    assert len(df["name"].unique()) == len(df["name"])

# 测试8：保存目录不存在时自动创建
def test_save_dir_auto_create(temp_test_files):
    raw_path, _ = temp_test_files
    # 指定不存在的子目录
    save_path = "data/cleaned/new_dir/result.csv"
    clean_csv(raw_path, save_path, drop_na_cols=["name"])
    assert os.path.exists(save_path)
    # 清理临时目录
    import shutil
    shutil.rmtree("data/cleaned/new_dir")