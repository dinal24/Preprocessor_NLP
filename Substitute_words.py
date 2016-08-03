__author__ = 'Januka Samaranayake'

def ConvetToUnicode(str_input):
    str_input= str_input.encode('unicode_escape')
    return str_input

if __name__ == '__main__':
    print ConvetToUnicode(":D")