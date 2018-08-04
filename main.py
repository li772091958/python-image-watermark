#-*- coding:utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import glob, math

# 将数字转为指定长度的编号，0补齐
def convertToNo(num, length = 4):
    num += 1 * math.pow(10, length + 1)
    return str(int(num))[2:]

# 设置所使用的字体
font = ImageFont.truetype('/System/Library/Fonts/Symbol.ttf', 100)
# 文字颜色
color = (255, 255, 255)
# 累加编号（水印内容）
index = 1

print('图片名\t编号')
for infile in glob.glob('images/*.jpg'):
    # 打开图片
    img = Image.open(infile)
    # 获取图片高度和宽度
    (width, height) = img.size
    # 水印位置（底部中间）
    position = (width / 2, height - 100)
    # 水印内容
    text = convertToNo(index)

    # 画图
    draw = ImageDraw.Draw(img)
    # 添加水印
    draw.text(position, text, color, font)
    # 保存图片(输出目录：./out)
    img.save("out/" + infile)
    print("out/" + infile + "\t" + text)

    index += 1

