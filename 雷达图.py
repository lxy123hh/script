import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

try:
    font_path = r'C:\Windows\Fonts\simsun.ttc'
    font_prop = FontProperties(fname=font_path, size=12)
except:
    font_prop = None

categories = ['数据源多样性', '数据格式复杂性', '语言多样性', '情感表达复杂性', '传播渠道多样性', '数据更新速度']
values = [8, 9, 7, 8, 9, 7]

# 闭合数据
values += values[:1]
categories += categories[:1]

# 计算角度，长度用闭合后的categories长度减1
angles = np.linspace(0, 2 * np.pi, len(categories)-1, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(polar=True))

ax.plot(angles, values, color='dodgerblue', linewidth=2, linestyle='solid')
ax.fill(angles, values, color='dodgerblue', alpha=0.25)

ax.set_thetagrids(np.degrees(angles[:-1]), categories[:-1], fontproperties=font_prop, fontsize=12)
ax.set_title('网络数据多样性与复杂性指标', fontproperties=font_prop, fontsize=16, y=1.1)

ax.set_rlim(0, 10)
ax.set_rticks([2, 4, 6, 8, 10])
ax.grid(True)

plt.tight_layout()
plt.savefig(r"D:\study\project\script\雷达图.png", dpi=300)
plt.show()
