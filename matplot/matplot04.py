import matplotlib.pyplot as plt
import numpy as np

# 四个轴的位置设定
# xy轴交汇位置设定
x = np.linspace(-1,1,50)
y1 = 2*x+1
y2 = x**2

plt.figure() 
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.xlim((-1,2)) #x取值范围
plt.ylim((-2,3)) #y取值范围
plt.xlabel('I am x') #描述
plt.ylabel('I am y') #描述
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks) # 更换xy轴刻度标识
plt.yticks([-2,-1.8,-1,1.22,3,],['read bad','bad','noral','good','really good'])

# 四周四个轴的操作
ax = plt.gca()
# 将右边和上面的轴颜色设置为空，就可以实现隐藏功能
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置xy轴指哪个轴,并命名
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 设置x放置在y轴的位置，y轴的0处 还有axes方法不指定具体值指百分比
ax.spines['bottom'].set_position(('data',0))
# 设置y放置在x轴位置，x轴的0处 data指数据 0代表值
ax.spines['left'].set_position(('data',0))
plt.show()

