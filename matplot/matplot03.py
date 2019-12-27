import matplotlib.pyplot as plt
import numpy as np

# xy轴的范围、描述、刻度标识重定义
# 
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

plt.show()

