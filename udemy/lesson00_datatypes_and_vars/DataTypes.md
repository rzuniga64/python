 ####Scalar data types (atomic values)
 
##### Arithmetic types: Integer
 * int
 
 #####Floating points
 * float is accurate up to 15 decimal places
 * complex
 
 ##### Hexadecimal, Octal
 
 #####Composite types:
 * list: ordered sequence of values that do not have to be of the same type
 * tuple: ordered sequence of items same as list. The only difference is that tuples are immutable. We can use the 
   slicing operator [] operator to extract items but we cannot change its value.
 * String is a sequence of Unicode characters. Strings are immutable. 
 * Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }.
   Items in a set are not ordered.
 * Dictionary is an unordered collection of key-value pairs.
 
 #####First class objects
 first-class objects can be manipulated in the usual ways without special cases and exceptions.
 *  copy (=, assignment)
 *  comparison (==, <, ...)
 *  input/output (<<, >>)
 *  ==, <, +, %, 
 * exponent operator: **
 * power method: pow(2,3)
 * abs value: abs(-2)
 * round(2.8), round(1.1)
 
 #####Second class objects
 second-class objects can be manipulated only in restricted ways, may have to define operations yourself
 * Usually primitive (built-in) data types
 
 primitive array
 * does not copy elements
 * length undefined
 * ==, <, ... do not perform as expected

 Order of operations:
 * parenthesis
 * exponentiation
 * multiplication, division
 * addition, subtraction