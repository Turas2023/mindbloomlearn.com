
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont, JpegImagePlugin  # noqa: F401

ROOT=Path(__file__).parent
OUT=ROOT/"output"; OUT.mkdir(exist_ok=True)
ASSETS=ROOT/"assets"
W,H=1800,2400

C={"purple":"#5E1B9A","orange":"#F57C00","green":"#2E7D32","blue":"#1565C0","red":"#D50000","black":"#111111","white":"#FFFFFF"}

def font(size,bold=False):
    """Load a font that contains Tamil glyphs on macOS and Linux."""
    paths=[
      "/System/Library/Fonts/Supplemental/Tamil Sangam MN.ttc",
      "/System/Library/Fonts/Supplemental/Tamil MN.ttc",
      "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
      "/usr/share/fonts/truetype/noto/NotoSansTamil-Bold.ttf" if bold else
      "/usr/share/fonts/truetype/noto/NotoSansTamil-Regular.ttf",
      "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else
      "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for p in paths:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    raise RuntimeError(
        "No Tamil-capable font found. Install Noto Sans Tamil or add a "
        "Tamil font path in generate.py."
    )

F={"title":font(76,True),"head":font(52,True),"body":font(38,True),"small":font(30),
   "tbig":font(520,True),"tmed":font(130,True),"grid":font(74,True)}

def rr(d,xy,r=28,outline=None,fill=None,w=4): d.rounded_rectangle(xy,radius=r,outline=outline,fill=fill,width=w)
def center(d,box,text,f,fill):
    x1,y1,x2,y2=box; b=d.textbbox((0,0),text,font=f); tw=b[2]-b[0]; th=b[3]-b[1]
    d.text((x1+(x2-x1-tw)/2-b[0],y1+(y2-y1-th)/2-b[1]),text,font=f,fill=fill)
def center_fit(d,box,text,max_size,min_size,fill,bold=True):
    x1,y1,x2,y2=box
    for size in range(max_size,min_size-1,-2):
        f=font(size,bold); b=d.textbbox((0,0),text,font=f)
        if b[2]-b[0] <= x2-x1 and b[3]-b[1] <= y2-y1:
            center(d,box,text,f,fill); return
    center(d,box,text,font(min_size,bold),fill)
def asset(can,name,box,label=""):
    p=ASSETS/name; x1,y1,x2,y2=box; d=ImageDraw.Draw(can)
    if p.exists():
        im=Image.open(p).convert("RGBA"); im.thumbnail((x2-x1,y2-y1))
        can.alpha_composite(im,(int(x1+(x2-x1-im.width)/2),int(y1+(y2-y1-im.height)/2)))
    else:
        rr(d,box,22,"#CCC","#FFF",3); center(d,box,label or name.replace(".png",""),F["small"],"#777")
def header(d,n,title,color):
    d.text((70,45),"ColorQuest",font=F["head"],fill=C["purple"])
    d.polygon([(75,120),(330,120),(300,170),(45,170)],fill=C["purple"])
    center(d,(45,120,330,170),"Tamil Adventures",F["small"],C["white"])
    rr(d,(475,45,600,160),18,color,color); center(d,(475,45,600,160),str(n),F["title"],C["white"])
    rr(d,(630,45,1265,160),18,color,color); center(d,(630,45,1265,160),title,F["title"],C["white"])
    d.text((1340,55),"MindBloom",font=F["head"],fill=C["green"])
    d.text((1530,115),"Learn™",font=F["head"],fill=C["orange"])
    d.text((1360,175),"Helping Every Mind Bloom™",font=F["small"],fill=C["black"])
    rr(d,(1600,260,1725,420),20,color,color); center(d,(1600,260,1725,420),"Ages\n3–6",F["body"],C["white"])
def footer(d,n,color,msg):
    d.rectangle((0,H-170,W,H),fill=color)
    d.text((720,H-112),msg,font=F["body"],fill=C["white"])
    d.text((1525,H-125),f"Page {n}",font=F["title"],fill=C["white"])
def questy(can,box,label="Questy™"): asset(can,"questy.png",box,label)

def page1(it,ans=False):
    can=Image.new("RGBA",(W,H),C["white"]); d=ImageDraw.Draw(can); color=C["purple"]
    header(d,1,"COLOR & TRACE",color)
    d.text((70,430),"Color the letter.",font=F["body"],fill=C["black"])
    rr(d,(70,520,570,1030),30,color,C["white"]); center(d,(85,530,555,1010),it["letter"],F["tbig"],C["red"] if ans else C["black"])
    d.text((620,430),"Trace the letter.",font=F["body"],fill=C["black"])
    rr(d,(610,520,1725,1030),30,color,C["white"])
    for i in range(5):
        x=690+i*200; d.text((x,670),it["letter"],font=F["tmed"],fill=C["red"] if ans else "#333"); d.line((x+160,570,x+160,980),fill="#77B7FF",width=3)
    d.text((70,1180),"Write the letter.",font=F["body"],fill=C["black"])
    for i in range(5):
        x=80+i*230; rr(d,(x,1320,x+185,1690),25,color,C["white"]); d.line((x,1505,x+185,1505),fill="#7EC8FF",width=3); d.line((x,1635,x+185,1635),fill="#FF69B4",width=3)
        if ans: center(d,(x,1320,x+185,1690),it["letter"],F["tmed"],C["red"])
    d.text((1320,1160),"Vocabulary",font=F["body"],fill=C["black"]); rr(d,(1280,1240,1725,1930),30,color,C["white"])
    asset(can,it["page1_image"],(1325,1280,1680,1600),it["page1_word_latin"])
    center_fit(d,(1300,1600,1705,1720),it["page1_word_tamil"],100,48,C["purple"]); center(d,(1280,1740,1725,1830),it["page1_word_latin"],F["head"],C["black"])
    questy(can,(70,1740,450,2200)); footer(d,1,color,"Great job! Keep practicing!")
    return can.convert("RGB")

def page2(it,ans=False):
    can=Image.new("RGBA",(W,H),C["white"]); d=ImageDraw.Draw(can); color=C["green"]; header(d,2,"TRACE & WRITE",color)
    d.text((70,430),"Trace the letter.",font=F["body"],fill=C["black"])
    for row in range(2):
        y=550+row*390; rr(d,(70,y,1730,y+285),28,color,C["white"])
        for i in range(5):
            x=185+i*300; d.text((x,y+65),it["letter"],font=font(150,True),fill=C["red"] if ans else "#333"); d.line((x+210,y+35,x+210,y+250),fill="#77B7FF",width=3)
    d.text((70,1320),"Write the letter.",font=F["body"],fill=C["black"])
    for i in range(5):
        x=90+i*300; rr(d,(x,1460,x+230,2000),26,color,C["white"]); d.line((x,1710,x+230,1710),fill="#7EC8FF",width=3); d.line((x,1935,x+230,1935),fill="#FF69B4",width=3)
        if ans: center(d,(x,1460,x+230,2000),it["letter"],F["tmed"],C["red"])
    questy(can,(1425,1580,1730,2100)); footer(d,2,color,"Fantastic! Keep it up!")
    return can.convert("RGB")

def page3(it,ans=False):
    can=Image.new("RGBA",(W,H),C["white"]); d=ImageDraw.Draw(can); color=C["orange"]; header(d,3,"FIND THE LETTER",color)
    d.text((70,430),f'Circle every “{it["letter"]}”.',font=F["body"],fill=C["black"]); rr(d,(90,560,1710,1835),30,color,C["white"])
    sx,sy,gx,gy=180,640,260,185
    for r,row in enumerate(it["grid"]):
        for c,ch in enumerate(row):
            x=sx+c*gx; y=sy+r*gy; d.text((x,y),ch,font=F["grid"],fill=C["black"])
            if ans and ch==it["letter"]: d.ellipse((x-20,y-15,x+95,y+95),outline=C["red"],width=5)
    questy(can,(60,1845,430,2240)); footer(d,3,color,"You’re doing amazing!")
    return can.convert("RGB")

def page4(it,ans=False):
    can=Image.new("RGBA",(W,H),C["white"]); d=ImageDraw.Draw(can); color=C["blue"]; header(d,4,"VOCABULARY",color)
    d.text((70,430),f'Color the pictures that start with “{it["letter"]}”.',font=F["body"],fill=C["black"])
    cards=[(80,570,560,1050),(660,570,1140,1050),(1240,570,1720,1050),(80,1120,560,1600),(660,1120,1140,1600),(1240,1120,1720,1600)]
    for card,v in zip(cards,it["vocabulary"]):
        x1,y1,x2,y2=card; rr(d,card,26,color,C["white"])
        if ans:
            fill="#188038" if v["correct"] else C["red"]
            d.ellipse((x1+18,y1+18,x1+75,y1+75),fill=fill)
            if v["correct"]:
                d.line((x1+32,y1+47,x1+43,y1+59,x1+64,y1+34),fill=C["white"],width=6,joint="curve")
            else:
                d.line((x1+34,y1+34,x1+61,y1+61),fill=C["white"],width=6)
                d.line((x1+61,y1+34,x1+34,y1+61),fill=C["white"],width=6)
        asset(can,v["image"],(x1+60,y1+60,x2-60,y1+300),v["latin"])
        center_fit(d,(x1+20,y1+305,x2-20,y1+390),v["tamil"],38,24,C["purple"]); center(d,(x1+20,y1+390,x2-20,y1+455),v["latin"],F["body"],C["black"])
    questy(can,(1380,1660,1730,2200)); footer(d,4,color,"Well done! Keep learning!")
    return can.convert("RGB")

def save_item(it,ans=False):
    pages=[page1(it,ans),page2(it,ans),page3(it,ans),page4(it,ans)]
    s="_answer" if ans else ""
    for i,p in enumerate(pages,1): p.save(OUT/f"ColorQuest_Tamil_{it['id']}_{it['latin'].upper()}_Page{i}{s}.png")
    pages[0].save(OUT/f"ColorQuest_Tamil_{it['id']}_{it['latin'].upper()}{s}.pdf",save_all=True,append_images=pages[1:],resolution=300)

def main():
    for it in json.loads((ROOT/"data"/"letters.json").read_text(encoding="utf-8")):
        save_item(it,False); save_item(it,True)
    print("Generated in",OUT)
if __name__=="__main__": main()
