class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # -------------------------------------------

    def set_width(self, new_width):
        self.width = new_width

    # -------------------------------------------

    def set_height(self, new_height):
        self.height = new_height

    # -------------------------------------------

    def get_area(self):
        return self.width * self.height

    # -------------------------------------------

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    # -------------------------------------------

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # -------------------------------------------

    def get_picture(self):
        if self.width >= 50 or self.height >= 50:
            return 'Too big for picture.'

        picture = ('*' * self.width + '\n') * self.height
        return picture

    # -------------------------------------------

    def get_amount_inside(self, other):
        return self.get_area() // other.get_area()

    # -------------------------------------------

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


# ===============================================


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    # -------------------------------------------

    def set_side(self, new_side):
        self.width = new_side
        self.height = new_side

    # -------------------------------------------

    def set_width(self, new_width):
        self.set_side(new_width)

    # -------------------------------------------

    def set_height(self, new_height):
        self.set_side(new_height)

    # -------------------------------------------

    def __repr__(self):
        return f'Square(side={self.width})'


# ===============================================
