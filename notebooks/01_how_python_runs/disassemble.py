import dis

def add(a, b):
    return a.x + b[0]

dis.dis(add, show_caches=True)
