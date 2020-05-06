def makestr1(x, y, z):
    return "%d時の%sは%.1f" % (x, y, z)

def makestr2(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

def makestr3(x, y, z):
    return f"{x}時の{y}は{z}"

x = 12
y = "気温"
z = 22.4

print(makestr1(x, y, z))
print(makestr2(x, y, z))
print(makestr3(x, y, z))