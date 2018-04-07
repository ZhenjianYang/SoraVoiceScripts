import os, sys
import struct

CODE_PAGE = 'gbk'
CODE_PAGE_IN = 'utf-8'

def set_code_page(code_page):
    global CODE_PAGE
    CODE_PAGE = code_page

def encode_str(str):
    bytes = bytearray()
    i = 0
    while i < len(str):
        if i + 4 < len(str) and str[i + 4] == ']' and str[i] == '[' and str[i+1] == 'x':
            bytes.append(int(str[i+2:i+4]))
            i += 5
        else:
            bytes.extend(str[i].encode(CODE_PAGE))
            i += 1
    bytes.append(0)
    return bytes

def main():
    istart = 1
    if len(sys.argv) > 1 and sys.argv[1].startswith('--cp='):
        set_code_page(sys.argv[1][5:])
        istart += 1

    if len(sys.argv) < istart + 3:
        print('%s [--cp=<codepage>] T_FISH._DT TXT dir_out' % sys.argv[0])
        print('  default codepage = gbk')
        return

    fish_out = sys.argv[istart + 2]
    txt_in = sys.argv[istart + 1]
    fish_in = sys.argv[istart]

    fs = open(txt_in, mode='r', encoding=CODE_PAGE_IN)
    lines = fs.readlines()
    fs.close()

    fs = open(fish_in, 'rb')
    buff = fs.read()
    fs.close()

    offoff, = struct.unpack('H', buff[8:8 + 2])
    off0, = struct.unpack('H', buff[offoff:offoff + 2])

    cnt = (off0 - offoff) // 2
    class Empty(): pass
    strs = []

    pre_off = off0
    name = None
    for line in lines:
        line = line.rstrip('\n').rstrip('\r')
        if len(line) == 0 or line[0] == ';':
            continue

        if name == None:
            name = line
            continue

        s = Empty()
        s.off = pre_off
        s.txt = encode_str(line)
        strs.append(s)
        pre_off += len(s.txt) + 2

    buff = buff[0:offoff]
    for s in strs:
        buff += struct.pack('H', s.off)
    for s in strs:
        while len(buff) < s.off:
            buff += b'\x00'
        buff+= s.txt
    while len(buff) < pre_off:
            buff += b'\x00'

    fs_out = open(os.path.join(fish_out, name), 'wb')
    fs_out.write(buff)
    fs_out.close()


if __name__ == '__main__':
    main()
