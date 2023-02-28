
# Create a class Rectangle with variables width and height
class Rectangle:
    
    width = 0
    height = 0
    
    # Intialize the class setting the width and height to the arguments given
    def __init__(self, width, height):
        self.width = width
        self.height = height        
        return
    
    
    # Set the width to the users argument
    def set_width(self, width):
        self.width = width
        return
        
        
    # Set the height to the users argument    
    def set_height(self, height):
        self.height = height
        return
    
    
    # Return the area calculation
    def get_area(self):
        return self.width* self.height
        
        
    # Return the perimeter calculation    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    
    # Return the diagonal calculation
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
     
    # Return the picture string representation 
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = "*" * self.width + "\n"    
            return picture * self.height  
        
    # Perform the inside calculation using the shape argument to perform an area calculation on itself with the area method    
    def get_amount_inside(self, shape):
        
        outside = self.width * self.height
        inside = shape.get_area()      
        return outside // inside
        
    # Return the string with the variable information    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


# Create the Square class that inherits from the Rectangle class
class Square(Rectangle):


    # Initialize the width and height variables from the argument
    def __init__(self, length):
        self.width = length
        self.height = length
        return 
    
    # Set the width and height variables to the input argument
    def set_side(self, length):
        self.width = length
        self.height = length  
        return
   
   
    # Redefine the method within the Square class to set both the width and height to the argument
    def set_width(self, width):
        self.width = self.height = width
        return
        
        
    # Redefine the method within the Square class to set both the width and height to the argument    
    def set_height(self, height):
        self.height = self.width = height
        return
    
    
    # Return the string with the variable information
    def __str__(self):
        return f"Square(side={self.height})"
    

# Test Case
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
print(sq)

# Test Response Expected
#50
#26
#Rectangle(width=10, height=3)
#**********
#**********
#**********
#
#81
#5.656854249492381
#Square(side=4)
#****
#****
#****
#****
#
#8