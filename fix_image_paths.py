#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MkDocs 圖片路徑修正腳本
將 GitBook 格式的圖片路徑轉換為 MkDocs 格式
"""

import os
import re
import glob
import sys
from pathlib import Path

def fix_image_paths_in_file(file_path):
    """修正單個檔案中的圖片路徑"""
    try:
        # 讀取檔案內容 (使用 UTF-8 編碼)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 模式1: 修正 ../.gitbook/assets/ 為 ../assets/
        # 匹配 ![任何文字](../.gitbook/assets/檔名) 或 ![任何文字](<../.gitbook/assets/檔名>)
        pattern1 = r'!\[([^\]]*)\]\(<?\.\./\.gitbook/assets/([^)>]+)>?\)'
        content = re.sub(pattern1, r'![\1](../assets/\2)', content)
        
        # 檢查是否有修改
        if content != original_content:
            # 寫回檔案 (保持 UTF-8 編碼)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
    
    except Exception as e:
        print(f"錯誤處理檔案 {file_path}: {str(e)}")
        return False

def find_and_fix_markdown_files(docs_dir):
    """尋找並修正所有 Markdown 檔案"""
    docs_path = Path(docs_dir)
    
    if not docs_path.exists():
        print(f"錯誤：目錄 {docs_dir} 不存在")
        return
    
    # 尋找所有 .md 檔案
    md_files = list(docs_path.rglob("*.md"))
    
    if not md_files:
        print("未找到任何 Markdown 檔案")
        return
    
    print(f"找到 {len(md_files)} 個 Markdown 檔案")
    
    fixed_count = 0
    
    for md_file in md_files:
        print(f"處理檔案: {md_file.relative_to(docs_path)}")
        
        if fix_image_paths_in_file(md_file):
            fixed_count += 1
            print(f"  ✓ 已修正圖片路徑")
        else:
            print(f"  - 無需修改")
    
    print(f"\n完成！共修正了 {fixed_count} 個檔案")

def main():
    # 設定 docs 目錄路徑
    script_dir = Path(__file__).parent
    docs_dir = script_dir / "docs"
    
    print("MkDocs 圖片路徑修正工具")
    print("=" * 40)
    print(f"目標目錄: {docs_dir}")
    print(f"修正模式: ../.gitbook/assets/ → ../assets/")
    print("=" * 40)
    
    # 確認是否繼續
    confirm = input("按 Enter 繼續，或輸入 'n' 取消: ").strip().lower()
    if confirm == 'n':
        print("已取消操作")
        return
    
    find_and_fix_markdown_files(docs_dir)

if __name__ == "__main__":
    main()