import codecs
import re

#:===============================:#
#: fungsinya buat deteksi apakah :#
#: encnya ROT13 atau bukan       :#
#: misal jika encnya ROT13 brati :#
#: retun ke true kalo bukan      :#
#: brati false yah               :#
#================================:#
def isROT13(val) -> bool:
    if not isinstance(val, str):return False
    if not re.fullmatch(r'[A-Za-z\s\.,!?\'"0-9]*', val):return False
    try:return codecs.encode(codecs.encode(val, 'rot_13'), 'rot_13') == val
    except Exception:return False

#:=================================:#
#: singkat saja nih fungsinya buat :#
#: dec ROT13 ke string biasa       :#
#: atau lebih disebut teks         :#
#: biasa                           :#
#:=================================:#
def decROT13(val) -> str:
    if not isinstance(val, str):raise ValueError("Maaf seperti input nya bukan string🧐");return codecs.decode(val, 'rot_13')