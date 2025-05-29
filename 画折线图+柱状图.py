import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

#设置中文字体
try:
    font_path = r'C:\Windows\Fonts\simsun.ttc'
    font_prop = fm.FontProperties(fname=font_path, size=12)
except:
    font_prop = None

# 数据准备
years = ['2017.12', '2018.12', '2020.03', '2020.12', '2021.12', '2022.06', '2023.12', '2024.12']
population = [77200, 82900, 90400, 98900, 103200, 105800, 109200, 110800]  # 万人
penetration = [55.8, 59.6, 64.5, 70.4, 73.0, 74.4, 77.5, 78.6]  # %

x = np.arange(len(years))

# 创建画布figure和主坐标轴axes
fig, ax = plt.subplots(figsize=(9, 7))

# 网民规模柱状图
ax.bar(x, population, width=0.4, color='cornflowerblue', label='网民规模（万人）')
ax.set_ylabel('网民规模（万人）', fontproperties=font_prop)
ax.set_xticks(x)
ax.set_xticklabels(years, rotation=45, fontproperties=font_prop)
ax.set_ylim(0, 140000)
ax.tick_params(axis='y')

# 互联网普及率折线图
ax2 = ax.twinx()
ax2.plot(x, penetration, marker='o', linestyle='-', linewidth=2, color='royalblue', label='互联网普及率（%）')
ax2.set_ylabel('互联网普及率（%）', fontproperties=font_prop)
ax2.set_ylim(0, 90)
ax2.tick_params(axis='y')

# 图例 & 标题
fig.legend(loc='upper left', bbox_to_anchor=(0.1, 0.95), prop=font_prop)
plt.title('2017–2024年中国网民规模及互联网普及率', fontproperties=font_prop, fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

# 保存图像
plt.savefig('中国网民规模与互联网普及率2017-2024.png', dpi=300)
plt.show()