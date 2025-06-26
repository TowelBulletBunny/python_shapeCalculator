from termcolor import colored

def spacing():
    print("\n" + "-" * 60 + "\n")

def header(title):
    print(colored("=" * 60, "cyan"))
    print(colored(title.center(60), "cyan", attrs=["bold"]))
    print(colored("=" * 60, "cyan"))

def inputQ(length, shape):
    return float(input(f"→ Enter the {length} of the {shape}: "))

def calculations(shape_number):
    spacing()
    header("CALCULATION RESULT")
    
    unit = input(colored("🔧 Enter the unit (e.g., cm, m, in): ", "magenta"))
    print()

    def u(x): return f"{x} {unit}"  # normal
    def u2(x): return f"{x} {unit}²"
    def u3(x): return f"{x} {unit}³"

    if shape_number == "1":  # Square
        side = inputQ("side", "square")
        area = side ** 2
        perimeter = 4 * side
        print(colored("[Square]", "yellow"))
        print(colored(f"  Area      = side × side       = {side} × {side}       = {u2(area)}", "blue"))
        print(colored(f"  Perimeter = 4 × side          = 4 × {side}           = {u(perimeter)}", "blue"))

    elif shape_number == "2":  # Rectangle
        length = inputQ("length", "rectangle")
        width = inputQ("width", "rectangle")
        area = length * width
        perimeter = 2 * (length + width)
        print(colored("[Rectangle]", "yellow"))
        print(colored(f"  Area      = length × width    = {length} × {width}    = {u2(area)}", "blue"))
        print(colored(f"  Perimeter = 2 × (l + w)       = 2 × ({length} + {width}) = {u(perimeter)}", "blue"))

    elif shape_number == "3":  # Circle
        radius = inputQ("radius", "circle")
        area = 3.142 * radius ** 2
        circumference = 2 * 3.142 * radius
        print(colored("[Circle]", "yellow"))
        print(colored(f"  Area          = π × r²         = 3.142 × {radius}²       = {u2(area)}", "blue"))
        print(colored(f"  Circumference = 2 × π × r     = 2 × 3.142 × {radius}   = {u(circumference)}", "blue"))

    elif shape_number == "4":  # Cone
        radius = inputQ("radius", "cone")
        slant = inputQ("slant height", "cone")
        height = inputQ("height", "cone")
        surface_area = 3.142 * radius ** 2 + 3.142 * radius * slant
        volume = (1 / 3) * 3.142 * radius ** 2 * height
        print(colored("[Cone]", "yellow"))
        print(colored(f"  Surface Area = πr² + πrl     = 3.142 × {radius}² + 3.142 × {radius} × {slant} = {u2(surface_area)}", "blue"))
        print(colored(f"  Volume       = (1/3)πr²h     = 1/3 × 3.142 × {radius}² × {height} = {u3(volume)}", "blue"))

    elif shape_number == "5":  # Triangle
        side = inputQ("side length", "triangle")
        area = 0.5 * side ** 2
        perimeter = 3 * side
        print(colored("[Triangle (Approx)]", "yellow"))
        print(colored(f"  Area      ≈ 0.5 × side²     = 0.5 × {side}²       = {u2(area)}", "blue"))
        print(colored(f"  Perimeter = 3 × side        = 3 × {side}         = {u(perimeter)}", "blue"))

    elif shape_number == "6":  # Cube
        side = inputQ("side length", "cube")
        surface_area = 6 * side ** 2
        volume = side ** 3
        print(colored("[Cube]", "yellow"))
        print(colored(f"  Surface Area = 6 × side²     = 6 × {side}²         = {u2(surface_area)}", "blue"))
        print(colored(f"  Volume       = side³         = {side}³             = {u3(volume)}", "blue"))

    elif shape_number == "7":  # Cuboid
        l = inputQ("length", "cuboid")
        w = inputQ("width", "cuboid")
        h = inputQ("height", "cuboid")
        surface_area = 2 * (l*w + l*h + w*h)
        volume = l * w * h
        print(colored("[Cuboid]", "yellow"))
        print(colored(f"  Surface Area = 2(lw + lh + wh) = 2({l}×{w} + {l}×{h} + {w}×{h}) = {u2(surface_area)}", "blue"))
        print(colored(f"  Volume       = l × w × h       = {l} × {w} × {h} = {u3(volume)}", "blue"))

    elif shape_number == "8":  # Cylinder
        radius = inputQ("radius", "cylinder")
        height = inputQ("height", "cylinder")
        surface_area = 2 * 3.142 * radius ** 2 + 2 * 3.142 * radius * height
        volume = 3.142 * radius ** 2 * height
        print(colored("[Cylinder]", "yellow"))
        print(colored(f"  Surface Area = 2πr² + 2πrh    = 2×3.142×{radius}² + 2×3.142×{radius}×{height} = {u2(surface_area)}", "blue"))
        print(colored(f"  Volume       = πr²h           = 3.142 × {radius}² × {height} = {u3(volume)}", "blue"))

    elif shape_number == "9":  # Sphere
        radius = inputQ("radius", "sphere")
        surface_area = 4 * 3.142 * radius ** 2
        volume = (4 / 3) * 3.142 * radius ** 3
        print(colored("[Sphere]", "yellow"))
        print(colored(f"  Surface Area = 4πr²           = 4 × 3.142 × {radius}²       = {u2(surface_area)}", "blue"))
        print(colored(f"  Volume       = (4/3)πr³       = 4/3 × 3.142 × {radius}³     = {u3(volume)}", "blue"))

    elif shape_number == "10":  # Square Pyramid
        base = inputQ("base length", "square pyramid")
        slant = inputQ("slant height", "square pyramid")
        height = inputQ("height", "square pyramid")
        surface_area = base ** 2 + 2 * base * slant
        volume = (base ** 2 * height) / 3
        print(colored("[Square Pyramid]", "yellow"))
        print(colored(f"  Surface Area = b² + 2bl       = {base}² + 2×{base}×{slant} = {u2(surface_area)}", "blue"))
        print(colored(f"  Volume       = (b²×h)/3       = ({base}²×{height})/3       = {u3(volume)}", "blue"))

    else:
        print(colored("⚠️ Invalid shape selection.", "red"))

    print()
    print(colored("✅ Calculation complete!", "green", attrs=["bold"]))
    spacing()

# ========== Main Program ==========
header("WELCOME TO THE SHAPE CALCULATOR")

while True:
    print(colored("\nChoose a shape to calculate:", "cyan", attrs=["bold"]))
    print("  1. Square         6. Cube")
    print("  2. Rectangle      7. Cuboid")
    print("  3. Circle         8. Cylinder")
    print("  4. Cone           9. Sphere")
    print("  5. Triangle       10. Square Pyramid")

    shape_number = input(colored("✏️  Enter shape number (or type 'exit' to quit): ", "magenta")).strip()

    if shape_number.lower() == "exit":
        print(colored("\n🎉 Thank you for using the Shape Calculator. Goodbye!", "green"))
        break

    calculations(shape_number)

