
#:========================================:#
#: singkat aja soalnya males ngetik komen :#
#: fungsinya buat deteksi enc hex         :#
#: apa bukan                              :#
#:========================================:#
def isHex(val:str)->bool:
    if isinstance(val, str) and len(val) > 0:return all(c in '0123456789abcdefABCDEF' for c in val);return False

#:=======================:#
#: buat dec heksadesimal :#
#:=======================:#
def decHex(val) -> str:
    try:novcantik = bytes.fromhex(val).decode('utf-8');return "%s"%novcantik
    except ValueError:return "False"
    except UnicodeDecodeError:return "Tidak terdeteksi UTF-8"

