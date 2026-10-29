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
('mAh、Wh、W\n是三件不同的事。','完整 3C 選購指南在\nSmartPicksTW 網站')],
'usb_c_cable':[
("USB-C 線材\n都一樣嗎？","外形相同，能力可能不同"),
("01 / 資料傳輸","部分 USB-C 線材\n只支援較低傳輸速度"),
("02 / 充電功率","線材、充電器與設備\n都要符合支援條件"),
("03 / 顯示器","影像輸出更需要\n設備與線材一起支援"),
("買線材別只看接頭！","詳細指南 → SmartPicksTW")
],
'hdmi_refresh':[
("4K HDMI\n不一定都是 60Hz！","解析度和更新率要分開看"),
("01 / 螢幕能力","先看螢幕支援的\n解析度與更新率"),
("02 / 來源設備","筆電與轉接器也要\n支援相同輸出模式"),
("03 / 傳輸線材","傳輸線規格也可能\n限制訊號頻寬"),
("規格要整套一起看。","更多實用知識 SmartPicksTW")
],
'pd_charger':[
("100W 充電器\n不代表每孔都 100W！","多孔分享功率要留意"),
("01 / 單孔輸出","先看各個連接埠的\n額定最高功率"),
("02 / 同時充電","多孔使用時可能\n需要共用總輸出"),
("03 / 協定相容","裝置的充電協定\n也會影響實際功率"),
("看完整規格表，\n不只看最大瓦數！","SmartPicksTW 選購知識")
],
'ssd_enclosure':[
("外接 SSD\n為何沒有標示那麼快？","傳輸速度取決於整條路徑"),
("01 / SSD 本體","先確認 SSD 的\n介面與標示速度"),
("02 / 外接盒","USB 外接盒規格\n可能限制最高速度"),
("03 / 電腦接口","主機連接埠與線材\n也會形成速度瓶頸"),
("速度看整套，\n不是只看 SSD！","SmartPicksTW 3C 知識")
],
'wifi_bands':[
("Wi-Fi 2.4G\n跟 5G 怎麼選？","頻段不是網路方案名稱"),
("01 / 覆蓋範圍","2.4GHz 一般穿透性\n較有利但容易擁擠"),
("02 / 資料速率","5GHz 在相近條件下\n通常更有速度優勢"),
("03 / 連線實況","路由器、距離及干擾\n都會影響實際表現"),
("先選穩定連線，\n再追求理論速度。","SmartPicksTW 原創資訊")
],
'monitor_refresh':[
("144Hz 螢幕\n不代表遊戲一定 144FPS！","螢幕更新率與遊戲幀率不同"),
("01 / 更新率 Hz","表示顯示器每秒\n可更新畫面的次數"),
("02 / 遊戲 FPS","表示電腦每秒\n產出的畫面幀數"),
("03 / 連接能力","訊號線與顯示輸出\n也可能限制更新率"),
("檢查 FPS、Hz、\n輸出介面三件事。","SmartPicksTW 3C 知識")
],
'usb_storage':[
("USB 隨身碟\n容量跟速度是兩回事！","買前看清楚用途"),
("01 / 容量","儲存空間大小\n不等於讀寫速度"),
("02 / 標示速度","讀取與寫入數字\n可能有很大差異"),
("03 / 實際測試","檔案大小和主機介面\n都會影響使用體驗"),
("別只看容量價格！","SmartPicksTW 選購筆記")
],
'wireless_charge':[
("磁吸功能\n不等於無線充電！","兩種功能可能分開設計"),
("01 / 磁吸定位","磁鐵可以用來\n協助定位或固定"),
("02 / 充電規格","手機與充電器都須\n具備相容無線充電能力"),
("03 / 散熱條件","充電效率與溫升\n受到環境和擺放影響"),
("磁吸和充電能力，\n請分別核對。","SmartPicksTW 原創指南")
],
'usb_power':[
("標榜 5A 的線材\n能替你快充嗎？","電流標示不等於實際充電速度"),
("01 / 供電來源","充電器輸出功率\n與協定要相容"),
("02 / 線材能力","線材額定規格與\n辨識方式要符合需求"),
("03 / 設備限制","手機或筆電自己決定\n可接受的充電模式"),
("快充是整組協作，\n不是只換一條線。","SmartPicksTW 3C 選購")
],
'usb_c_hub':[
("USB-C Hub\\n接了卻沒畫面？","買前先看三個相容重點"),
("01 / 先看設備","確認主機 USB-C 埠\\n是否支援影像輸出"),
("02 / 看埠速","確認 Hub 介面規格\\n與連接裝置需求"),
("03 / PD 供電","看支援輸入與\\n實際充電需求"),
("別只看 Hub 外型！","選購指南在 SmartPicksTW")
],
'sneaker_fit':[
("網購運動鞋\\n只看鞋碼會踩雷？","先查三件事再下單"),
("01 / 腳長","對照品牌尺寸表\\n別只靠習慣鞋號"),
("02 / 鞋楦","D、2E 等楦型標示\\n需核對實際版型"),
("03 / 退換貨","確認賣場與品牌的\\n試穿及退貨規則"),
("鞋碼、楦型、用途\\n三項一起看","SmartPicksTW 精選鞋款")
]
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
    d.text((69,253),'SmartPicksTW 原創選購小教室',font=f(25,True),fill='#FF9978')
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
    pending=[(name,slides) for name,slides in TOPICS.items() if not (OUT/(name+'.mp4')).exists()]
    if not pending: print('All original Reels completed; no re-upload of old topics.')
    for name,slides in pending[:2]:render(name,slides)
