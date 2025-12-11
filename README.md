# Object Oriented Programming (Encapsulation)

OOP PDF:

https://drive.google.com/file/d/1Dfu8jYSOsRFwReeNXO6nA0ffTYqtH2BT/view?usp=sharing

---

## Exercise 1

**Problem:**
 
**Student Grades (Encapsulation):**  
Create a Student class where the grade is private and safe from incorrect modification.  

Requirements:   
Private attribute: 

* `__grade`
  
Public methods:

* `set_grade(val)` - Must be 0–100  
* `get_grade()`
  
Public attribute:

* `name`   

Example:

    Input:
       s = Student("Bob")
       s.set_grade(85)
       print(s.get_grade())

    Output:
       85
  
---

## Exercise 2

**Problem:**
Create a class `TemperatureSensor` that simulates reading and updating temperature values safely.

Requirements:  

Private attribute: 
* `__temperature`

Public methods:   
* `set_temperature(value)`  
    * Accepts only values between –50°C to 150°C
    * If the value is invalid, ignore it
* `get_temperature()` 
    * Returns the current temperature
* `increase(amount)`
    * Increase temperature
    * Must respect the –50 to 150 range
* `decrease(amount)`
    * Decrease temperature
    * Also must respect the range

Public attribute: 
* `location` (e.g., "Server Room")

Example:

    Input:
         sensor = TemperatureSensor("Server Room")
         sensor.set_temperature(25)
         sensor.increase(10)
         print(sensor.get_temperature())   # 35
         sensor.decrease(100)
         print(sensor.get_temperature())   # -50 (min limit)

    Output:
        35
        -50

---

