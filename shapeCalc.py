def chooseShapeToCalculate():
    if question == "1":
        square(aorp)
    elif question == "2":
        rectangle(aorp)
    elif question == "3":
        circle(aorp)
    elif question == "4":
        cone(aorv)
    elif question == "5":
        triangle(aorp)
    elif question == "6":
        cube(aorv)
    elif question == "7":
        cuboid(aorv)
    elif question == "8":
        cylinder(aorv)
    elif question == "9":
        sphere(aorv)
    elif question == "10":
        squarePyramid(aorv)  
    else: 
        print("Sorry. This shape doesn't exist")

    calc = str(input("Type y to continue, and other keys to quit."))
    return calc 

def spacing():
    print("\n")

def tryagain():
    print("please type again")

def inputQ(length,shape):
    size_question = float(input("Please enter the {} {} {} {}".format( length,"of the",shape,": ")))
    return size_question

def checkForPerimeter(aorp):
    aorp = str(input("area or perimeter? :"))
    while aorp != "area" and aorp != "perimeter":
        tryagain()
        aorp = str(input("area or perimeter? :"))
        return aorp
    return aorp

def checkForVolume(aorv):
    aorv = str(input("area or volume? :"))
    while aorv != "area" and aorv != "volume":
        tryagain()
        aorv = str(input("area or volume? :"))
        return aorv
    return aorv

def square(aorp):
    aorp = checkForPerimeter(aorp)
    length = inputQ("length","square")
    if aorp == "area":
        s_area = length * length
        print("The area of the square is ",s_area)
    elif aorp == "perimeter":
        s_perimeter = 4 * length  
        print("The perimeter of the square is ",s_perimeter)

def cone(aorv):
    aorv = checkForVolume(aorv)
    rad_length = inputQ("radius","cone")   
    if aorv == "area":
        sla_length = inputQ("slant","cone")
        spacing()
        sa_cone = 3.142*rad_length*2 + 3.142*rad_length*sla_length
        print("The surface area of the cone is ",sa_cone)
    elif aorv == "volume":
        height = inputQ("height","cone")
        spacing()
        v_cone = (1/3)*3.142*rad_length**2*height
        print("The volume of the cone is ",v_cone)

def rectangle(aorp):
    aorp = checkForPerimeter(aorp)
    rec_length = inputQ("length","rectangle")
    rec_width = inputQ("width","rectangle")
    if aorp == "area":
        area_rec = rec_length * rec_width
        print("The area of the rectangle is ",area_rec)

    elif aorp == "perimeter":
        perimeter_rec = 2 * (rec_length + rec_width)
        print("The perimeter of the rectangle is ",perimeter_rec)
 
def circle(aorp):
    aorp = checkForPerimeter(aorp)
    circ_length = inputQ("radius","circle")
    if aorp == "area":
        area_circ = 3.142 * circ_length * circ_length
        print("The area of the circle is ",area_circ)
    elif aorp == "perimeter":
        perimeter_circ = 2 * 3.142 * circ_length
        print("The perimeter of the circle is ",perimeter_circ)

def triangle(aorp):
    aorp = checkForPerimeter(aorp)
    tri_length = inputQ("length","triangle")
    if aorp == "area":
        area_tri = 0.5 * tri_length ** 2
        print("The area of the triangle is ",area_tri)

    elif aorp == "perimeter":
        perimeter_tri = 3 * tri_length
        print("The perimeter of the triangle is ",perimeter_tri)

def cube(aorv):
    aorv = checkForVolume(aorv)
    cub_length = inputQ("length","cube")
    if aorv == "area":
        cub_area = 6 * cub_length ** 2
        print("The area of the  is cube",cub_area)

    elif aorv == "volume":
        vol_cub = cub_length ** 3
        print("The volume of the cube is ",vol_cub)

def cuboid(aorv):
    aorv = checkForVolume(aorv)
    cubo_length = inputQ("length","cuboid")                             
    cubo_width = inputQ("width","cuboid")
    cubo_height = inputQ("height","cuboid")

    if aorv == "area":
        cubo_area = 2 * (cubo_length * cubo_width + cubo_length * cubo_height + cubo_height * cubo_width)
        print("The area of the cuboid is ",cubo_area)

    elif aorv == "volume":
        cubo_vol = cubo_length * cubo_width * cubo_height 
        print("The volume of the circle is ",cubo_vol)

def cylinder(aorv):
    aorv = checkForVolume(aorv)
    rad_length = inputQ("radius","cylinder")
    spacing()
    cy_h = inputQ("height","cylinder")
    spacing()
                
    if aorv == "area":
        sa_cy = 2 * 3.142 * rad_length ** 2 + 2 * 3.142 * rad_length * rad_h
        print("The surface area of the cylinder is ",sa_cy)

    elif aorv == "volume":
        v_cone = (1/3)*3.142*rad_length**2*height
        print("The volume of the cone is ",v_cone)

def sphere(aorv):
    aorv = checkForVolume(aorv)
    rad_length = inputQ("radius","sphere")
    spacing()
                
    if aorv == "area":
        sa_sp = 4 * 3.142 * rad_length ** 2
        print("The surface area of the cone is ",sa_sp)

    elif aorv == "volume":
        v_sp = (4/3) * 3.142 * rad_length ** 3
        print("The volume of the cone is ",v_sp)

def squarePyramid(aorv):
    aorv = checkForVolume(aorv)
    base_length = inputQ("base_length","square pyramid")
    if aorv == "area":
        slant_length = inputQ("slant","square pyramid")
        spacing()
        sa_sqp = (base_length ** 2) + (2 * base_length * slant_length)
        print("The surface area of the cone is ",sa_sqp)

    elif aorv == "volume":
        height_length = inputQ("height","square pyramid")
        spacing()
        v_sqp = (base_length ** 2) * (height_length  / 3)
        print("The volume of the cone is ",v_sqp)

#main
print("="*25," Welcome to the shape calculator","="*25)

calc,aorp,aorv = "y","0","0"

while calc == "y":
    question = str(input("""Please enter the number associated with the shape you want to calculate*
    1.) square
    2.) rectangle 
    3.) circle
    4.) cone
    5.) triangle
    6.) cube
    7.) cuboid
    8.) cylinder 
    9.) sphere
    10.) square pyramid 
        
Enter a shape number: """))

    calc = chooseShapeToCalculate()
    
else:
    print("thanks for using.")

