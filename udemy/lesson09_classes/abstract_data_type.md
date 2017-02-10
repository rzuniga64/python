 ####Abstract data type
 * has attributes and behaviors
 
##### Class/Object
 * Class is a definition of an Abstract Data Type in a programming language
 * Object is an instance of a class
 
 ##### Constructor
* Instantiation means we want to create an instance of the class
* A constructor is a particular type of method
* def __init__(self,...)
* self refers to the current object
* In Python you have to reference a field using 'self'

###### ToString Method
* Allows viewing of the current state of the object
* def __str__(self):
    return self.first + ' ' + self.middle + ' ' + self.last
