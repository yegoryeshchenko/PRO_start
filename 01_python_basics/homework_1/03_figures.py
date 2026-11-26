def draw_rectangle():
    height = int(input("Enter height of the figure:"))
    length = int(input("Enter length of the figure:"))

    for i in range(0, height):
        print("*" * length)
        i += 1


def draw_triangle():
    height = int(input("Enter height of the figure:"))

    for i in range(1, height + 1):
        print("*" * i)
        i += 1


def draw_reverted_triangle():
    height = int(input("Enter height of the figure:"))

    for i in range(height, 0, -1):
        print("*" * i)


draw_rectangle()
draw_triangle()
draw_reverted_triangle()