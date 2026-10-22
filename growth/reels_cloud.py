#!/usr/bin/env python3
"""Original, product-photo-free educational Facebook Reels for SmartPicksTW."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, wave, struct, subprocess, shutil
ROOT=Path(__file__).resolve().parent.parent
OUT=ROOT/'reels'
OUT.mkdir(exist_ok=True)
W,H,FPS=720,1280,25
FONT='/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
BOLD='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'
TOPICS={
'usb_c_hub':[
('USB-C Hub\n插得進去，\n不等於有畫面！','先別急著下單｜20 秒看懂'),
('01 / 先看電腦','USB-C 埠是否支援\n影像輸出（DP Alt Mode）？'),
('02 / 再看螢幕','HDMI 的解析度與\n更新率要一起確認'),
('03 / 最後看供電','標示 100W PD，\n不代表筆電一定拿到 100W'),
('先學會看規格，\n再挑適合的配件。','更多選購指南在\nSmartPicksTW 網站')],
'phone_stand':[
('磁吸支架\n為何有時吸不牢？','選購前先懂 3 件事'),
('01 / 先看手機','磁吸環／手機殼\n是否真的相容？'),
('02 / 再看表面','真空吸附要看平整度\n與表面材質'),
('03 / 注意固定方式','臨時拍攝與長時間固定，\n不是同一種需求'),
('不只看吸力，\n更要看使用條件！','完整選購指南在\nSmartPicksTW 網站')],
'power_bank':[
('20,000mAh\n不代表手機\n一定能充 5 次！','行動電源標示怎麼看？'),
('01 / mAh','代表電荷容量，\n不等於可充手機次數'),
('02 / Wh','代表能量，計算時\n需要知道標示電壓'),
('03 / W','功率與快充能力有關，\n還要看協定和線材'),
('mAh、Wh、W\n是三件不同的事。','完整 3C 選購指南在\nSmartPicksTW 網站')]
}
def f(size,b=False):return ImageFont.truetype(BOLD if b else FONT,size)
def scene(topic,index,title,sub,path):
    im=Image.new('RGB',(W,H));px=im.load()
    for y in range(H):
        a=y/H;col=(int(9+8*a),int(19+14*a),int(38+18*a))
        for x in range(W): px[x,y]=col
    d=ImageDraw.Draw(im)
    d.rounded_rectangle((37,40,683,1240),radius=36,outline='#304762',width=3)
    d.arc((455,175,1000,705),90,290,fill='#1c3d54',width=35)
    d.rounded_rectangle((67,82,651,176),radius=22,fill='#17334C')
    d.text((94,107),'S  SmartPicksTW',font=f(29,True),fill='white')
    d.text((69,253),'原創 3C 選購小教室',font=f(25,True),fill='#FF9978')
    sz=60 if max(map(len,title.split('\n')))<=12 else 47
    y=350
    for line in title.split('\n'):
        d.text((68,y),line,font=f(sz,True),fill='white');y+=sz+24
    d.rounded_rectangle((68,748,652,923),radius=23,fill='#1C3453')
    y=789
    for line in sub.split('\n'):
        d.text((92,y),line,font=f(28),fill='#CCDCEE');y+=49
    d.rounded_rectangle((68,993,240,1000),radius=3,fill='#FF835E')
    d.text((68,1043),'原創選購知識 · 非商品實測',font=f(22),fill='#90A8C3')
    d.text((68,1122),'smartpicks-tw / guides.html',font=f(24,True),fill='white')
    d.text((566,1122),f'{index+1:02d}/05',font=f(25,True),fill='#FF9275')
    for n in range(5):d.rounded_rectangle((68+n*116,1211,159+n*116,1219),radius=4,fill='#FA7654' if n<=index else '#2E435D')
    im.save(path,optimize=True)
def audio(path):
    sr=16000;duration=20; chords=[(220,277.18,329.63),(196,246.94,293.66),(174.61,220,261.63),(196,246.94,293.66)]
    with wave.open(str(path),'wb') as w:
        w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr)
        for i in range(sr*duration):
            t=i/sr;env=min(1,t,20-t,(t%5)/1.2,(5-t%5)/1.2)
            val=sum(math.sin(2*math.pi*x*t) for x in chords[int(t//5)%4])/3
            w.writeframesraw(struct.pack('<h',int(32767*.075*env*val)))
def render(slug,slides):
    ffmpeg=shutil.which('ffmpeg')
    if not ffmpeg:raise Exception('ffmpeg missing')
    work=ROOT/'growth'/('tmp_'+slug);work.mkdir(exist_ok=True)
    segments=[]
    for i,(title,sub) in enumerate(slides):
        png=work/f'{i}.png';scene(slug,i,title,sub,png)
        mp4=work/f'{i}.mp4'
        subprocess.run([ffmpeg,'-loglevel','error','-y','-loop','1','-i',str(png),'-vf',f"zoompan=z='min(zoom+0.00025,1.045)':d=100:s=720x1280:fps=25,format=yuv420p",'-frames:v','100','-c:v','libx264','-preset','ultrafast','-crf','26','-an',str(mp4)],check=True)
        segments.append(mp4)
    playlist=work/'list.txt'
    playlist.write_text(''.join("file '"+str(p)+"'\n" for p in segments))
    joined=work/'joined.mp4';wav=work/'ambient.wav'
    subprocess.run([ffmpeg,'-loglevel','error','-y','-f','concat','-safe','0','-i',str(playlist),'-c','copy',str(joined)],check=True)
    audio(wav)
    target=OUT/(slug+'.mp4')
    subprocess.run([ffmpeg,'-loglevel','error','-y','-i',str(joined),'-i',str(wav),'-c:v','copy','-c:a','aac','-b:a','96k','-movflags','+faststart','-shortest',str(target)],check=True)
    print('Generated',target,target.stat().st_size)
if __name__=='__main__':
    for name,slides in TOPICS.items():render(name,slides)
