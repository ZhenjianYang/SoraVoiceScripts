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

    if len(sys.argv) <= istart:
        print('%s [--cp=<codepage>] XXXX.TXT [output folder]' % sys.argv[0])
        print('  default codepage = gbk')
        return

    path = sys.argv[istart]
    dir_out = os.path.dirname(path) if len(sys.argv) <= istart + 1 else sys.argv[istart + 1]
    if len(dir_out) == 0:
        dir_out = '.'
    file_name = os.path.split(path)[-1]

    fs = open(path, mode='r', encoding=CODE_PAGE_IN)
    lines = fs.readlines()
    fs.close()

    out_name = None
    groups = [[]]
    for line in lines:
        line = line.rstrip('\n').rstrip('\r')
        if len(line) == 0 or line[0] == ';':
            continue
        if out_name == None:
            out_name = line
            continue
        if len(groups[-1]) == 8:
            groups.append([])

        if len(groups[-1]) <= 1:
            groups[-1].append(int(line))
        else:
            groups[-1].append(encode_str(line))

    if len(groups) == 0:
        print('No groups, skip.')
        return

    if len(groups[-1]) != 8:
        raise Exception('Group not complete!')
    
    off = 2 * len(groups)
    for group in groups:
        group[1] = [group[0], group[1]]
        group[0] = off
        off += 0x10
        for str in group[2:]:
            group[1].append(off)
            off += len(str)

    if not os.path.exists(dir_out):
        os.makedirs(dir_out)
    fs_out = open(os.path.join(dir_out, out_name), 'wb')
    for group in groups:
        fs_out.write(struct.pack('<H', group[0]))
    for group in groups:
        for off2 in group[1]:
            fs_out.write(struct.pack('<H', off2))
        for str in group[2:]:
            fs_out.write(str)
    fs_out.close()

if __name__ == '__main__':
    main()

