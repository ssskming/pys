import matplotlib.pyplot as plt
import numpy as np

# ticks能见度
# 给刻度加个背景板并设置相关的属性
x = np.linspace(-3,3,50)
y = 0.1*x

plt.figure() 
plt.plot(x,y,linewidth=1.0)
plt.ylim(-2,2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# 字体、背景颜色、前景颜色、透明度
for label in ax.get_xticklabels()+ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='red',edgecolor='None',alpha=0.5))

plt.show()

# 第9集
