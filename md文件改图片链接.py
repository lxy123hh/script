import re
import os

def rewrite_image_paths(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 匹配 Markdown 图片语法中的路径
    pattern = r'(!\[.*?\])\((\.\/.*?\.assets\/)(.*?)\)'
    replaced = re.sub(pattern, r'\1(/frontend.assets/\3)', content)

    with open(md_file_path, 'w', encoding='utf-8') as f:
        f.write(replaced)

    print(f"✅ 已处理文件：{md_file_path}")


def batch_process(directory, target_ext='.md'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(target_ext):
                path = os.path.join(root, file)
                rewrite_image_paths(path)


if __name__ == "__main__":
    # 修改为你的 Markdown 根目录路径（如 'docs'）
    rewrite_image_paths(r'D:\study\project\personal_notes\docs\前端.md')
