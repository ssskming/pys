import sys
import os
import _io
from collections import namedtuple
from PIL import Image

class Nude(object):
    
    def __init__(self,path_or_image):
        # 如果path_or_image为Image类型的实例，直接赋值
        if isinstance(path_or_image,Image.Image):
            self.image = path_or_image
        else isinstance(path_or_image,str):
            self.image = Image.open(path_or_image)

        # 获得图片所有颜色的通道
        bands = self.image.getbands()
        #判断是否为单通道田图片也就是灰度图，是则旬灰度图转换为rgb图
        if len(bands) == 1:
            # 新建相同大小的RGB图像
            new_img = Image.new("RGB",self.image.size)
            # 拷贝灰度图self..image到RGB图new_img.paste(PIL自动进行颜色通道转换)
            new_img.paste(self.image)
            f = self.image.filename
            # 替换 self.image
            self.image = new_img
            sefl.image.filename = f
        
        # 存储对应图像所有像素的全部Skin对象
        self.skin_map = []
        # 检测到的皮肤区域，元素的索引即为皮肤区域号，元素都是包含一些skin对象的列表
        self.detected_regions = []
        # 元素都是包含一些int对象的列表
        # 这些元素中的区域号代表的区域都是待倒立工的区域
        self.merge_regions = []
        # 整合后的皮肤区域，元素的索引 即为皮肤区域号，元素都是包含一些skin对象的列表
        self.skin_regions = []
        # 最近合并 的两个皮肤区域的区域号，初始化为 -1
        self.last_from,self.last_to = -1,-1
        # 色情图像判断结果
        self.result = None
        # 处理行到的信息
        self.message = None
        # 图像宽高 
        self.width,self.height = self.image.size
        # 图像总像素
        self.total_pixels = self.width * self.height
    Skin = namedtuple("skin","id skin region x y")
