def main():
    x="happy"
    y="pimpkin"
    z="orange"
    pumpkin="sleepy"
    orange="vampire"

    orange(y,x,z)
    orange(x,z,y)
    orange(pumpkin,z,"y")
    z="green"
    orange("x","pumpkin",z)
    orange(y,z,orange)

def orange(z,y,x):
        print(y+" and "+" were "+x)
