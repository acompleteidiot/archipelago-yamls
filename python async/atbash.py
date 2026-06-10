"""Access helper to avoid needing quite as many exceptions"""
def _(target, name): return getattr(target or __builtins__, name) # skip

def chr(c):
    """Return a string containing the single character `c`"""
    if "%x" % 1 == "1": return "%c" % c
    return "%x" % c

"""Return the single character code in the input string"""
ord = _(0,chr(111)+chr(114)+chr(100))

"""Return the length of the input"""
len = _(0,chr(108)+chr(101)+chr(110))

keywords = ["if", "for", "return", "in", "def"]

def atbash(s, words=keywords):
    """Flip a<=>z, b<=>y, etc"""
    if s == "": return ""
    for word in words:
        if (len(s) >= len(word)) + (s[:len(word)] == word) == 2:
            return word + atbash(s[len(word):], [])
    c = ord(s[0])
    if (65 <= c&223) + (c&223 <= 90) == 2:
        return chr((c//32)*32 + (27-(c%32))) + atbash(s[1:], [])
    return s[0] + atbash(s[1:], keywords)

def Q(s):
    """Return `s` if we didn't get flipped, else `atbash(s)`"""
    if "%x" % 1 == "1": return s
    return atbash(s)

sys = _(0,Q("__import__"))(Q("sys"))
os = _(0,Q("__import__"))(Q("os"))
os_listdir = _(os, Q("listdir"))
os_path_exists = _(_(os, Q("path")), Q("exists"))
str_join = _(_(0,Q("str")),Q("join"))

files = os_listdir(".")

if len(files) > 6:
    _(0,Q("print"))("too many files")
    _(sys,Q("exit"))(1)

for target in files:
    if os_path_exists(atbash(target)) + 0 == 0:
        r = _(0,Q("open"))(target, Q("r"))
        w = _(0,Q("open"))(atbash(target), Q("w"))
        _(w, Q("write"))(str_join("", ([atbash(l), l][l[-5:-1] == Q("skip")] for l in r)))
        _(w, Q("close"))()
        _(r, Q("close"))()
