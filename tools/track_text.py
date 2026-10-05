#!/usr/bin/env python3
"""Make text follow a moving object. Usage: python3 track_text.py in.mp4 x y w h "LABEL" out.ass [dx dy]
(x,y,w,h = bounding box of the object on the FIRST frame, in pixels.) Then burn with: ffmpeg -i in.mp4 -vf subtitles=out.ass ...
Uses OpenCV CSRT tracker (opencv-contrib). Review the result; re-seed the box if the tracker drifts."""
import cv2,sys
src,x,y,w,h,label,out=sys.argv[1],*map(int,sys.argv[2:6]),sys.argv[6],sys.argv[7]
dx,dy=(int(sys.argv[8]),int(sys.argv[9])) if len(sys.argv)>9 else (0,-50)
cap=cv2.VideoCapture(src); fps=cap.get(cv2.CAP_PROP_FPS); W=int(cap.get(3)); H=int(cap.get(4))
ok,f=cap.read(); tr=cv2.TrackerCSRT_create(); tr.init(f,(x,y,w,h))
def ts(t): return f"{int(t//3600)}:{int(t%3600//60):02d}:{t%60:05.2f}"
ev=[]; i=0
while ok:
    ok2,b=tr.update(f)
    if ok2:
        cx=int(b[0]+b[2]/2)+dx; cy=int(b[1])+dy
        ev.append(f"Dialogue: 0,{ts(i/fps)},{ts((i+1)/fps)},T,,0,0,0,,{{\\an5\\pos({cx},{cy})}}{label}")
    ok,f=cap.read(); i+=1
hdr=f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
Style: T,DejaVu Sans,{max(24,H//14)},&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,3,0,5,10,10,10,1
[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
open(out,'w').write(hdr+"\n".join(ev)); print(len(ev),"tracked frames ->",out)
