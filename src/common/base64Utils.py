import base64
import re

#:===================================:#
#: Deteksi apakah sumbernya base64   :#
#: atau tidak kalo sumbernya base64  :#
#: misal nya di enc brapa kali       :#
#: ini bisa berguna biar ngedetek    :#
#: base64 yang di enc brapa kali     :#
#:===================================:#
def isBase64(s:str)->bool:
    if not isinstance(s, str) or len(s) % 4 != 0: return False
    if not re.fullmatch(r'^[A-Za-z0-9+/]+={0,2}$', s):return False
    try:return base64.b64encode(base64.b64decode(s)).decode('utf-8').rstrip('=') == s.rstrip('=')
    except Exception:return False

#:===================================:#
#: Berfungsi buat buka enc base64    :#
#: kalo ada yang error brati base64  :#
#: Terenkripsi dengan layer enc lain :#
#: Semacam ROT13                     :# 
#:===================================:#
def decBase64(n:str)->str|None:
    try:novDec = base64.b64decode(n, validate=True);return novDec.decode('utf-8')
    except Exception:return None
