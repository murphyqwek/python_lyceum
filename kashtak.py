from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import *

texts = [
    "Плазмохимический реактор",
    "Он очень круто!!!",
    "Это мой научный проект",
]

def create_img(name, text):
    name = "uju/" + name + '.jpg'
    im = Image.new('RGB', (1366, 768), color="#000000")
    draw_text = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", 32, encoding='UTF-8')
    draw_text.text(
        (683, 100),
        text,
        fill= "#FFFFFF",
        font= font
    )
    im.save(name)

def create_video():
    direct = 'uju/'
    files= os.listdir(direct)
    imag = list(filter(lambda x: x.endswith('.jpg'), files))
    clips = [ImageClip('uju/'+ m).set_duration(2) for m  in imag]

    final = concatenate_videoclips(clips, method='compose')
    final.write_videofile('movie.mp4',fps=24)

for i in range(len(texts)):
    create_img(str(i), texts[i])

create_video()