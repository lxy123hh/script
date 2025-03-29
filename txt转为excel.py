import pandas as pd
txt_file_path = r"D:\study\复试\拟录取.txt"
df = pd.read_csv(txt_file_path, sep="\t")
df["考生编号"] = df["考生编号"].astype(str)
excel_file_path = r"D:\study\复试\拟录取.xlsx"
df.to_excel(excel_file_path, index=False)
print(f"txt文件已保存至：{excel_file_path}")