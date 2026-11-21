from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parent
S = 2
im = Image.new('RGB', (1024*S, 1024*S), '#ffffff')
d = ImageDraw.Draw(im)
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def box(xy, fill, outline=None, width=1):
    d.rectangle(tuple(int(v*S) for v in xy), fill, outline, width*S)
def line(points, fill, width=2):
    d.line([(int(x*S),int(y*S)) for x,y in points], fill, width*S)
def poly(points, fill, outline=None):
    d.polygon([(int(x*S),int(y*S)) for x,y in points], fill, outline)
def ellipse(xy, fill):
    d.ellipse(tuple(int(v*S) for v in xy), fill)
def text(x,y,t,size=24,fill='white',anchor=None):
    d.text((x*S,y*S),t,font=ImageFont.truetype(FONT,size*S),fill=fill,anchor=anchor)
def fit(x,y,t,size,maxwidth,fill='white'):
    while d.textlength(t,font=ImageFont.truetype(FONT,size*S)) > maxwidth*S:
        size -= 1
    text(x,y,t,size,fill)
def star(x,y,r,fill):
    poly([(x+math.sin(i*math.pi/5)*r*(1 if i%2==0 else .4),y-math.cos(i*math.pi/5)*r*(1 if i%2==0 else .4)) for i in range(10)],fill)
navy='#081625'; gold='#ffd365'; red='#ff4b53'
box((0,0,1024,110),navy)
fit(512,17,'SATURDAY 21 NOVEMBER 2026',42,970) if False else None
text(512,15,'SATURDAY 21 NOVEMBER 2026',42,anchor='mt')
text(512,70,'THE WORLD IN ONE DAY',22,gold,anchor='mt')
box((0,116,509,548),'#103b68'); box((515,116,1024,548),'#671f26')
box((0,554,509,984),'#10151e'); box((515,554,1024,984),'#073f46')
# Summit: flags and three delegates seated at one table.
text(24,132,'01 / DIPLOMACY',17,gold)
for x in (27,185,343):
    box((x-2,174,x+140,263),'#8aabc2')
for i in range(13):
    box((27,176+i*6.5,165,176+(i+1)*6.5),'#e65764' if i%2==0 else '#ffffff')
box((27,176,88,221),'#173c78')
for row in range(4):
    for col in range(5): star(34+col*11,182+row*10,2.5,'white')
box((185,176,323,260),'#df2638'); star(208,197,12,gold)
for x,y in ((226,185),(234,195),(234,208),(225,219)): star(x,y,4,gold)
for i,c in enumerate(('white','#2872c9','#df3547')): box((343,176+i*28,481,204+i*28),c)
for x in (97,254,411):
    ellipse((x-16,278,x+16,310),'#dce6ef')
    poly([(x-35,344),(x-24,315),(x+24,315),(x+35,344)],navy)
    poly([(x-3,317),(x+4,317),(x+7,338),(x,343),(x-6,338)],gold)
poly([(45,345),(463,345),(487,370),(23,370)],'#79a5bd')
box((73,371,83,389),navy); box((426,371,436,389),navy)
fit(23,397,'FIRST TRILATERAL SUMMIT',30,465)
text(24,440,'TRUMP - XI - PUTIN',25)
text(24,477,'APEC SHENZHEN',22,gold)
text(24,510,'4-POINT PEACE DECLARATION',21)
# Poland: recognisable country contour and incoming cruise missile.
text(539,132,'02 / WAR IN EUROPE',17,gold)
poly([(691,202),(729,192),(763,206),(797,202),(819,226),(851,233),(846,266),(866,297),(843,319),(834,351),(799,347),(776,365),(745,351),(712,355),(690,331),(663,320),(670,288),(652,266),(670,243),(668,219)],'#ae493d', '#ffc47c')
text(757,276,'POLAND',24,anchor='mt')
line([(562,191),(684,229)],'#ff8c50',8)
line([(543,182),(651,216)],gold,3)
poly([(665,216),(745,240),(756,253),(732,254),(660,231),(642,239),(646,223),(637,208)],'#f8e6d1')
for x,y in ((590,318),(910,253)):
    poly([(x,y-23),(x-25,y+22),(x+25,y+22)],gold)
    text(x,y-18,'!',30,navy,anchor='mt')
text(757,374,'RUSSIAN MISSILES + DRONE',17,gold,anchor='mt')
fit(538,405,'MISSILES LAND IN POLAND',29,465)
text(539,448,'KYIV UNDER FIRE',27)
text(539,485,'NATO ON ALERT',25,gold)
text(539,520,'KYIV: AT LEAST 8 KILLED',18)
# Markets: chart, candles, and unmistakable downward arrow.
text(24,570,'03 / MARKETS • FRI 20 NOV',17,gold)
for y in (640,690,740,790): line([(27,y),(478,y)],'#303743',1)
for i,(top,bottom) in enumerate(((632,655),(644,672),(651,677),(675,701),(687,725),(709,750),(735,770),(756,799))):
    x=48+i*46
    line([(x,top-9),(x,bottom+10)],red,2); box((x-7,top,x+7,bottom),red)
line([(28,625),(89,639),(133,630),(179,666),(222,680),(265,712),(310,730),(354,770),(416,796)],red,6)
poly([(421,713),(451,713),(451,774),(478,774),(436,821),(394,774),(421,774)],red)
text(29,807,'S&P 500  -3.7%',34,red)
fit(24,855,'WALL STREET CRASHES',32,465)
text(24,902,'IN CORRECTION',26)
text(24,944,'NVIDIA SUBPOENAED',24,gold)
# Justice: balanced scales over the Peace Palace.
text(539,570,'04 / JUSTICE • RULING 19 NOV',16,gold)
line([(770,615),(770,720)],gold,8)
ellipse((762,603,778,619),gold)
line([(672,636),(868,636)],gold,6)
for x in (691,849):
    line([(x,637),(x-30,688),(x+30,688),(x,637)],gold,2)
    d.pieslice(((x-32)*S,674*S,(x+32)*S,708*S),0,180,fill=gold)
box((732,719,808,726),gold)
# Central clock tower, gables and arched windows.
box((661,763,886,818),'#85b1aa')
poly([(649,764),(683,743),(718,764)],'#b5d2c7')
poly([(802,764),(843,741),(895,764)],'#b5d2c7')
box((736,734,785,818),'#b5d2c7')
poly([(730,734),(760,704),(791,734)],gold)
box((748,688,771,713),'#b5d2c7'); poly([(744,688),(760,662),(776,688)],gold)
ellipse((749,739,771,761),navy)
for x in (675,699,724,750,775,803,829,855):
    box((x,785,x+11,818),navy); ellipse((x,779,x+11,791),navy)
box((641,819,905,825),gold)
text(770,834,'THE HAGUE / PEACE PALACE',15,gold,anchor='mt')
text(539,860,'GENOCIDE RULING',34)
text(539,907,'ICJ 9-6 / MYANMAR GUILTY',23)
text(539,945,'ROHINGYA',25,gold)
box((0,990,1024,1024),navy)
text(512,998,'APEC SHENZHEN - POLAND - WALL STREET - THE HAGUE',19,anchor='mt')
im.resize((1024,1024),Image.Resampling.LANCZOS).save(ROOT/'entry.png',optimize=True)
print('Created a front page with four illustrated world stories.')
