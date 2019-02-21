# Pillow常见用法
from PIL import Image

im = Image.open('cat.jpg')
w, h = im.size
print('宽：%s,高：%s' % (w, h))

im.thumbnail((w // 2, h // 2))
print('宽：%s,高：%s' % (w, h))
im.save('cat_narrow.jpg', 'jpeg')
