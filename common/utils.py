from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random


class imagecode():
    def get_number(self):
        random_number = random.randint(1000, 9999)
        return str(random_number)
    
    def draw_verify(self):
        code = self.get_number()
        width, height = 80, 40
        im = Image.new('RGB', (width, height), (255, 255, 255))
        font = ImageFont.truetype("arial.ttf", 24) # 字體
        draw = ImageDraw.Draw(im)
        for i in range(0, 4):
            draw.text((random.randint(3, 9)+15*i,random.randint(3, 9)), text=code[i], font=font, fill=(0, 0, 0))

        return im, code
    
    def get_image_code(self):
        ima, code = self.draw_verify()
        buf = BytesIO()
        ima.save(buf, 'jpeg')
        return buf.getvalue(), code
