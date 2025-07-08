import hashlib

def GetSHA256(inS):
    m = hashlib.sha256()
    if isinstance(inS, str):
        m.update(inS.encode())
    elif isinstance(inS, bytes):
        m.update(inS)
    else:
        raise Exception("Unexpected type")
    return m.digest()

def GetSHA256String(inS):
    m = hashlib.sha256()
    if isinstance(inS, str):
        m.update(inS.encode())
    elif isinstance(inS, bytes):
        m.update(inS)
    else:
        raise Exception("Unexpected type")
    return m.hexdigest()

def GetSHA256FromFile(path):
    with open(path, "br") as f:
        return GetSHA256(f.read())

def GetSHA256StringFromFile(path):
    with open(path, "br") as f:
        return GetSHA256String(f.read())