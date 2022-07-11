README for models

A directory within 0x0C-python-almost_a_circle. A directory within the holbertonschool-higher_level_programming repo.

File Name Description
**init**.py An empty file to make this folder a Python module.
base.py A class called Base that sets the public instance attribute id within the instantiation. It contains the private class attribute **nb_objects and has many json methods. This includes: to_json_string, save_to_file, from_json_string, create, and load_from_file.
rectangle.py A class called Rectangle that inherits Base. It has an instantiation using the variables: width, height, x, y, and id. Each one but id are private instance attributes with their own getters and setters. These attributes can be updated at any time. There's also a **str\_\_ method, along with area, display that actually prints the instance, and to_dictionary prints the dictionary representation of Rectangle.
square.py A class called Square that inherits Rectangle. It has an instantiation using the variables: size, x, y, and id. It calls it's super in order to set these variables, using size to represent width and height. This class contains a setter and getter for size. Any of these attributes can be updated at any time. There's also a dictionary representation of Square.
