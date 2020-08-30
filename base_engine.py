f = open("base.txt", "r", encoding="utf8")

data = f.read().split("#")[1:]
data = [i.split("\n")[:-1] for i in data]
d = {}
for i in data:
    d[i[0]] = [j.split(":") for j in i[1:]]


def get_base(theme=None):
    if theme is None:
        return [j for i in d.values() for j in i]
    else:
        return [i for i in d.values()][theme]


def get_themes():
    return d.keys()
