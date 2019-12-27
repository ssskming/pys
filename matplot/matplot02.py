import matplotlib.pyplot as plt
import numpy as np

# 图片大小和编号 
# 图线颜色和宽度、格式
x = np.linspace(-1,1,50)
y1 = 2*x+1
y2 = x**2
plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5)) #num 图片序号 figsize 图片大小
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
plt.show()