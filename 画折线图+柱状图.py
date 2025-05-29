import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

#设置中文字体
try:
    font_path = 'C:\Windows\Fonts\simsun.ttc'
    font_prop = fm.FontProperties(fname=font_path, size=12)
except:
    font_prop = None

#数据准备
