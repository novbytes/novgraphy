#:--
#: Sejam ngadepin laptop terus gak tidur tidur
#: disuruh tidur bilangnya nanti masih ada penting
#: goodnight ^_^ aji love youuu
#: orangnya digantikan aku (novi)
#: karena dia sudah trauma
#: kena doxing katanya
#: aku telah banyak ajarin dia
#: sekarang dia lagi sakit
#: gak terlihat lagi belakang ini
#: yh taulah aku berpura pura
#: bersifat seperti aji :v
#: nama kusoft idenya dari aku (novi)
#: jangan bilang kesiapa siapa yh
#: aku tetangganya aji
#: semoga yang baca ini tuhan yesus dan roh kudus memperpanjang umur kamu amin
#: aku gapernah pamer muka karena gak dibolehin aji
#:-- 

import sys
import os
from common import *
from middle import *
from middle.ui import novi

#:=======================================:#
#: males nulis komen jelasin aja sendiri :#
#:=======================================:#
def bfBase64(val:str,a:int)->str:
    if not isinstance(val, str) or not isinstance(a, int):print("%sInput tidak valid%s"%(w.m,w.r));return ""
    nov = val
    for i in range(a):
        novv = decBase64(nov)
        if novv is None:print("[%s!%s] Gagal decode pada lapisan ke-%d"%(w.m,w.r,int(i)));break;
        print("[%s+%s] Proses decode ke-%d: %s%s%s" % (w.h,w.r,i+1,w.h,novv,w.r))
        nov = novv;return nov

def bfHex(val:str,a:int)->str:
    if not isinstance(val,str) or not isinstance(a, int):print("Input tidak valid");return ""
    ututu=val
    for i in range(a):
        if not isHex(ututu):print("[%s!%s] Bukan Hex pada lapisan ke-%d"%(w.m,w.r,int(i)));break
        deko=decHex(ututu)
        if deko=="False":print("[%s!%s] Gagal decode pada lapisan ke-%d"%(w.m,w.r,int(i)));break
        print("[%s+%s] Proses decode ke-%d: %s%s%s"%(w.h,w.r,i+1,w.h,deko,w.r))
        ututu=deko;return ututu

def bfROT13(val: str, a: int) -> str:
    if not isinstance(val, str) or not isinstance(a, int):
        print("Input tidak valid")
        return ""
    mamahnov = val
    for i in range(a):
        if not isROT13(mamahnov):
            print("[%s!%s] Bukan ROT13 pada lapisan ke-%d"%(w.m,w.r,int(i)))
            break
        kuru = decROT13(mamahnov)
        if kuru is None:
            print("[%s!%s] Gagal decode pada lapisan ke-%s")
            break
        print(f"[+] Proses decode ke-{i+1}: {kuru}")
        mamahnov = kuru
    return mamahnov

def cl()->str:
    if os.name=="nt":os.system("cls");
    else: os.system("clear")

def ichaanov()->str:
    menu="""
menu - nampilin ini
help - nampilin ini
bs64 - dekode base64
hex - dekode heksadesimal
rot13 - dekode rot13
q - keluar"""
    cl();novi()
    while True:
        try:
            n=input("[%snovgraphy%s]:%s~%s# "%(w.h,w.r,w.b,w.r))
            arg=n.split()
            if n.startswith("menu") or n.startswith("help"):print(menu);
            elif n.startswith("bs64"):ab=arg[1];cd=arg[2];bfBase64(ab,cd);
            elif n.startswith("hex"):nov=arg[1];jii=arg[2];bfHex(nov,jii);
            elif n.startswith("rot13"):ha=arg[1];ho=arg[3];bfROT13(ha,ho);
            elif n.startswith("q"):sys.exit(0)
            else:print("\"%s\" tidak dimaksud\ncobalah ketik \"menu\""%n)
        except KeyboardInterrupt:print("keluar");sys.exit(0);return