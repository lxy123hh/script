import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties

try:
    font_path = r'C:\Windows\Fonts\simsun.ttc'
    font_prop = FontProperties(fname=font_path, size=12)
except:
    font_prop = None
years = [2016, 2018, 2020, 2022, 2024]
data_volume = [16.1, 33, 59, 103, 175]  # 单位：Zettabytes

x = np.arange(len(years))

plt.figure(figsize=(9, 7))
plt.fill_between(x, data_volume, color='lightcoral', alpha=0.6)
plt.plot(x, data_volume, color='red', marker='o')

plt.xticks(x, years)
plt.title('全球互联网数据总量增长趋势', fontproperties=font_prop, fontsize=16)
plt.ylabel('数据总量 (Zettabytes)', fontproperties=font_prop)
plt.ylim(0, 200)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for i, val in enumerate(data_volume):
    plt.text(i, val + 5, f'{val} ZB', ha='center', fontsize=11)

plt.tight_layout()
plt.savefig(r'D:\study\project\script\面积图.png', dpi=300)
plt.show()
