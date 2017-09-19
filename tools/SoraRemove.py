import os, sys
import codecs

MARK_BEGIN = '#STEAM_ONLY_BEGIN'
MARK_END = '#STEAM_ONLY_END'

def getSubFiles(dir, ext = '.py'):
    ret = []
    dir_list =  os.listdir(dir)
    for file in dir_list:
        path = os.path.join(dir, file)
        if os.path.splitext(file)[1] == ext and os.path.isfile(path):
            ret.append(file)
    return ret

def main():
    if len(sys.argv) <= 2:
        print('%s dir_in dir_out' % sys.argv[0])
        return

    dir_in = sys.argv[1]
    dir_out = sys.argv[2]
    if not os.path.exists(dir_out):
        os.makedirs(dir_out)

    cnt = 0
    for file in getSubFiles(dir_in, '.py'):
        print('Working with %s... ' % file, end='')
        has = False
        only = False
        f = codecs.open(os.path.join(dir_in, file), 'r', 'utf-8')
        lines = f.readlines()
        f.close()
        for i in range(len(lines)):
            if only and lines[i].startswith(MARK_END):
                only = False

            if not only:
                if lines[i].startswith(MARK_BEGIN):
                    has = True
                    only = True
            else:
                lines[i] = '#' + lines[i]
            
        if has:
            codecs.open(os.path.join(dir_out, file), 'w', 'utf-8').writelines(lines)
            print('Done')
            cnt += 1
        else:
            print('Skip')
    print('Done with %d files.' % cnt)

if __name__ == '__main__':
    main()
