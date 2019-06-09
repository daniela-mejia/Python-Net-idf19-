#This Program make a rocket

def draw_v():
    print(" \\    /")
    print("  \\  /")
    print("   \\/")

def draw_inverted_v():
    print("   /\\")
    print("  /  \\")
    print(" /    \\")

def draw_box():
    print("+------+")
    print("|      |")
    print("|      |")
    print("+------+")
    
def draw_rocket():
    draw_inverted_v()
    draw_box()
    print("|United|")
    print("|States|")
    draw_box()
    draw_inverted_v()

def main():
    #diamond
    draw_inverted_v()
    draw_v()

    print()

    #X

    draw_v()
    draw_inverted_v()

    print()
    
    #Rocket
    
    draw_rocket()



main()
