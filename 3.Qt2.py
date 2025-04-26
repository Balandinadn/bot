class Rectangle:
    def __init__(self, height=1, width=1):
        self.__height = height
        self.__width = width
        self.__square = self.__calculate_square()
        self.__perimeter = self.__calculate_perimeter()

    def __calculate_square(self):
        return self.__height * self.__width

    def __calculate_perimeter(self):
        return 2 * (self.__height + self.__width)

    def get_high(self):
        return self.__height

    def set_high(self, height):
        self.__height = height
        self.__square = self.__calculate_square()
        self.__perimeter = self.__calculate_perimeter()

    def get_length(self):
        return self.__width

    def set_length(self, width):
        self.__width = width
        self.__square = self.__calculate_square()
        self.__perimeter = self.__calculate_perimeter()

    def get_square(self):
        return self.__square

    def get_perimeter(self):
        return self.__perimeter
