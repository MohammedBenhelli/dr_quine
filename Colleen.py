#yes
def func():
    pass
c = "#yes\ndef func():\n\tpass\nc = %r\nif __name == '__main__':\n\t#super\n\tprint(c)\n"

if __name__ == '__main__':
    #super
    print(c % c)
