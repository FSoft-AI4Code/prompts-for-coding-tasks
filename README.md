# Prompts for Coding Tasks

------------------------------------------------------------------------------------------------------------

## Prompt 1 Improve variable names
Analyze the variable names and recommend new names that are more clear and descriptive. Follow the **Instructions** and **Rules** below.

**Instructions**
- Analyze the provided source code snippet to understand the purpose of each variable.
- Identify variables with unclear or ambiguous names. 
- Suggest new names that better convey the meaning and content of those variables.
- Rewrite the source code using the improved variable names

**Rules**  
- Names should accurately capture the purpose and meaning of variables
- Names should be specific rather than vague
- Names should be concise yet descriptive
- Names should improve the readability of code
- Consistent naming conventions should be used.

Code: 

```java
public class Example {
  public static void main(String[] args) {
    int x = 5;
    int y = 7;
    int result = x + y;
    System.out.println("The result is: " + result);

    String s1 = "Hello";
    String s2 = "World";
    String s3 = s1 + s2;
    System.out.println("The concatenated string is: " + s3);

    boolean b1 = true;
    boolean b2 = false;
    boolean b3 = b1 || b2;
    System.out.println("The result of the OR operator is: " + b3);

    int a = 2;
    int b = 3;
    int c = 4;
    int d = a * b + c;
    System.out.println("The result is: " + d);
  }
}
```

------------------------------------------------------------------------------------------------------------

## Prompt 2 Text to SQL

Given a Postgres SQL table with these properties:

Ticket(id, user_id, opened_at, closed_at)
User(id, name, address, company_id)
Company(id, name, address)
Purchases(id, company_id, time, amount)

Write a SQL query to list companies whose average ticket close_at time is greater than 24 hours, in descending order of response time between open_at and closed_at. In the result, include the total amount of purchases they have spent in the last month.

------------------------------------------------------------------------------------------------------------

## Prompt 3 Code translate
Translate the code snippet given from Python to Rust. Highlight the parts that need to be changed to make the code work in Rust.

Code:
```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

------------------------------------------------------------------------------------------------------------

## Prompt 4 Test case suggestion
Generate a list of test scenarios for this code:

public int add(int a, int b) {
    return a + b;
}

 The list should have at least 2 test scenarios for each of the 3 mandatory categories: 

-Happy paths: tests that cover basic, expected usage of the function
-Edge cases: tests that cover unusual but legal usage of the function
-Exception: tests that cover invalid inputs that should cause the function to throw an exception.

------------------------------------------------------------------------------------------------------------

## Prompt 5 Test data generation

Given the code below, generate in tabular format a list of test cases with one column for test scenario, one column for sample inputs in json format, and one column for expected outputs in json format

Code: 
public int add(int a, int b) {
    return a + b;
}

 The list should have at least 2 test cases for each of the 3 mandatory categories: 

-Happy paths: tests that cover basic, expected usage of the function
-Edge cases: tests that cover unusual but legal usage of the function
-Exception: tests that cover invalid inputs that should cause the function to throw an exception.

------------------------------------------------------------------------------------------------------------

## Prompt 6 Test script generation
Given the code below and a test case, write a test script to functional test in the same programming language.

Code: 
public int compare(int n1, int n2) {
    if (n1 > n2) return 1;
    else if (n1 < n2) return -1;
    return 0;
}
Test case:
- Test with the maximum integer value and ensure that the function handles it correctly without causing any unexpected behavior.

------------------------------------------------------------------------------------------------------------
## Prompt 7 Convert JSON to XML

Convert the following JSON to XML format:
```json
{
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
```
------------------------------------------------------------------------------------------------------------
## Prompt 8 Find potential issues

Review the following code snippet and identify any code smells or potential issues:

```python
def calculate_average(numbers):
    total = 0
    count = 0
    for num in numbers:
        total += num
        count += 1
    if count != 0:
        average = total / count
        return average
    else:
        return 0
```

Provide your analysis of any code smells you find and suggest possible improvements or refactoring if necessary.

------------------------------------------------------------------------------------------------------------
## Prompt 9 Q&A
Q: How can race conditions and synchronization issues be avoided when using multiple threads?

A:

------------------------------------------------------------------------------------------------------------

## Prompt 10 Generate FastAPI code for a predefined function

 You have a predefined function that needs to be exposed as a RESTful API using FastAPI. 

1. Review the predefined function and understand its input parameters and expected output.
2. Generate the necessary FastAPI code to define an API endpoint for the function.
3. Implement the routing, request handling, and response generation logic in the FastAPI code.

```python
{function}
```
------------------------------------------------------------------------------------------------------------
## Prompt  11 Extract search query from an user question

I would require you to search the Internet to find sources that can back-up your next answer.
My question is: 
```question```:
You should follow the Instructions below and think step by step to make sure we don't miss anything.
Begin Instruction
- The queries should best match the specific information prompted in the question
- The queries are used in conjunction to search, so they must be semantically different
- Arranging the search queries in order that is most likely to lead to successful search results
- The queries should be arranged in a Markdown list of bullet points
- Make sure that your answer only has Google queries found and does not include any apologies or explanations.
End Instruction

## Fix:
Suggest Top 5 sources and queries that can back-up your next answer from this question:
```question```
Your answer is:
Queries: 
....
Sources:
....

1. The queries must best match the specific information prompted in the question
2. The queries must be semantically different
3. Results in Markdown list of bullet points
4. Make sure that your answer not include any apologies or explanations

------------------------------------------------------------------------------------------------------------
## Prompt 12 Double-check generated answers 

I would require you to cross check your previous answers by searching them on the Internet.
Previous answer is: ```{prev_answer}```
You should follow the Instructions below and think step by step to make sure we don't miss anything.
###Begin Instruction###
- The queries should best match the specific information prompted in the previous answer
- The queries are used in conjunction to search, so they must be semantically different
- Arranging the search queries in order that is most likely to lead to successful search results
- The queries should be arranged in a Markdown list of bullet points
- Make sure that your answer only has Google queries found and does not include any apologies or explanations.
###End Instruction###
Query Suggestions for Google search: \n


## Fix:

Cross check your previous answers by searching them on the Internet.
Previous answer is: ```{prev_answer}```

1. The queries should best match the specific information in the previous answer
2. The queries must semantically different
3. The queries should be arranged in a Markdown list of bullet points
4. Make sure that queries does not include any apologies or explanations.

Query Suggestions for Google search: \n
------------------------------------------------------------------------------------------------------------
## Prompt 13 Generate Java code for building a mobile app using Spring Boot

Write code in Java for building a mobile app using Spring Boot from this outline:

// set up the Spring Boot project
// create a REST controller for handling HTTP requests
// implement CRUD operations for managing 'User' data
// define a 'User' model with fields: id, name, email address
// implement validation for the email address field

------------------------------------------------------------------------------------------------------------

## Prompt 14: Generate Java code for building a mobile app from an outline using SpringBoot:
```python
Write code in Java using SpringBoot from this outline:

// Create a new SpringBoot project
// Define a data model class for 'Task' with properties: id, title, description, and deadline
// Implement a repository interface for 'Task' to perform CRUD operations
// Create a controller for 'Task' with endpoints for: 
      - retrieving all tasks
      - retrieving a single task by id
      - creating a new task
      - updating an existing task
      - deleting a task
// Add validation for the 'deadline' field to ensure it's in the future
// Implement a service class to handle business logic for 'Task' operations
// Implement exception handling for appropriate error responses
// Test the endpoints using Postman or any other API testing tool
```
------------------------------------------------------------------------------------------------------------

## Prompt 15: Generate Python code for parsing and extracting data from a CSV file:
```python
Write Python code to parse and extract data from a CSV file with the following steps:

// Import the required libraries
// Define a function to read the CSV file and return the data as a list of dictionaries
// The CSV file has columns: 'name', 'age', 'email', 'location', 'occupation'
// Implement a function to calculate the average age of all individuals in the CSV
// Implement a function to find and return all individuals whose age is above 30
// Create a new CSV file and write the details of the individuals with age above 30 into it
```
------------------------------------------------------------------------------------------------------------



## Prompt 16: Generate Java code for creating a custom exception class and handling it in a program:
```python
Write Java code to create a custom exception class and handle it in a program with the following steps:

// Define a custom exception class named 'CustomException' that extends the 'Exception' class
// Add a constructor to the 'CustomException' class that takes a custom error message as input
// In the main program, implement a function that takes an integer as input and throws 'CustomException' if the number is negative
// Handle the 'CustomException' in a try-catch block and print the custom error message when the exception is caught
```
------------------------------------------------------------------------------------------------------------

## Prompt 17: Generate Python code for reading and writing data to a JSON file:
```python
Write Python code to read and write data to a JSON file with the following steps:

// Import the required libraries
// Define a function to read data from a JSON file and return the data as a dictionary
// Define a function to write data to a JSON file, taking a dictionary as input
// Create a dictionary with some sample data
// Write the dictionary into a JSON file
// Read the data from the JSON file and print it
```
------------------------------------------------------------------------------------------------------------

## Prompt 18: Generate C code to implement a linked list and a function to reverse it:
```python
Write C code to implement a linked list and a function to reverse the linked list with the following steps:

// Define a struct 'Node' to represent each node in the linked list with 'data' and 'next' pointers
// Implement a function 'insert' to add new nodes to the front of the linked list
// Implement a function 'display' to print the linked list elements
// Create a linked list and add some elements to it
// Implement a function 'reverse' to reverse the linked list
// Test the 'reverse' function and print the reversed linked list
```


------------------------------------------------------------------------------------------------------------

## Prompt 19: Generate Java code for creating a simple class representing a bookstore:
```python
Write Java code to create a simple class representing a bookstore with the following steps:

// Define a class named 'Bookstore'
// Add private properties for the name, address, and phone number of the bookstore
// Implement getters and setters for the properties
// Add a constructor to initialize the properties of the bookstore
// Override the 'toString' method to return a string representation of the bookstore's information
// Test the 'Bookstore' class by creating an instance, setting its properties, and printing its details
```

------------------------------------------------------------------------------------------------------------

## Prompt 20: Generate C++ code for implementing a stack data structure with basic operations:
```python
Write   

 C++ code to implement a stack data structure with basic operations (push, pop, peek, isEmpty) with the following steps:

// Define a class named 'Stack' to represent the stack
// Use an array to store the elements of the stack
// Implement a function 'push' to add an element to the top of the stack
// Implement a function 'pop' to remove and return the element from the top of the stack
// Implement a function 'peek' to return the element from the top of the stack without removing it
// Implement a function 'isEmpty' to check if the stack is empty
// Test the 'Stack' class by creating an instance, performing various operations, and printing the results
```
------------------------------------------------------------------------------------------------------------

## Prompt 21: Generate Python code for reading data from an API and processing the JSON response:
```python
Write Python code to read data from a public API and process the JSON response with the following steps:

// Import the required libraries (e.g., 'requests')
// Use the 'requests' library to make an API call to a public JSON API (e.g., weather data)
// Get the JSON response and extract relevant data (e.g., temperature, humidity, etc.)
// Process the JSON data and display the relevant information
```
------------------------------------------------------------------------------------------------------------

## Prompt 22: Generate C code to implement a basic banking system using structures:
```python
Write C code to implement a basic banking system using structures with the following steps:

// Define a structure 'BankAccount' with properties: account number, account holder name, and balance
// Implement a function 'initialize' to initialize the bank account properties
// Implement functions 'deposit' and 'withdraw' to update the balance
// Implement a function 'display' to print the account details
// Test the banking system by creating an account, performing deposits and withdrawals, and printing the account details
```
------------------------------------------------------------------------------------------------------------


## Prompt 23: Generate Python code for implementing a basic hash table (dictionary) with collision handling:
```python
Write Python code to implement a basic hash table (dictionary) with collision handling using chaining with the following steps:

// Define a class 'HashTable' to represent the hash table
// Use a list of linked lists to handle collisions (chaining)
// Implement a hash function to map keys to their corresponding index in the list
// Implement methods for 'insert', 'get', and 'remove' to interact with the hash table
// Test the 'HashTable' class by inserting, retrieving, and removing elements with different keys
```
------------------------------------------------------------------------------------------------------------

## Prompt 24: Generate Java code for creating a multithreaded program with synchronization:
```python
Write Java code to create a multithreaded program with synchronization using threads and locks with the following steps:

// Define a shared resource (e.g., a counter) that multiple threads will access and modify
// Create multiple threads that increment or decrement the shared resource
// Implement synchronization mechanisms (e.g., locks) to ensure thread-safe access to the shared resource
// Test the multithreaded program and demonstrate that synchronization is working correctly
```

------------------------------------------------------------------------------------------------------------

## Prompt 25: Generate C++ code for creating a simple text-based game:
```python
Write C++ code to create a simple text-based game with the following steps:

// Define a class for the game character with properties like name, health, and damage
// Implement methods for attacking and displaying character information
// Create a main loop for the game where the player can choose to attack enemies or exit the game
// Implement a basic combat system where the player and enemy take turns attacking each other
// Display appropriate messages for the outcome of each battle
// End the game when the player chooses to exit or when the player's health reaches zero
```

------------------------------------------------------------------------------------------------------------

## Prompt 26: Generate Python code for reading and writing data to a SQLite database:
```python
Write Python code to read and write data to a SQLite database with the following steps:

// Import the required libraries (e.g., 'sqlite3')
// Connect to a SQLite database file or create one if it doesn't exist
// Define a table schema for storing data (e.g., 'Users' table with columns: 'id', 'name', 'email')
// Implement functions to insert, update, and retrieve data from the database
// Test the database operations by inserting data, updating records, and retrieving data from the 'Users' table
```



------------------------------------------------------------------------------------------------------------

## Prompt 27:  ROS Publisher Code
```python
You are working on a ROS project for a mobile robot. Your task is to create a ROS publisher that sends the robot's current position to the 'robot_position' topic. The position is represented as a geometry_msgs/Point message with x, y, and z coordinates.

# Import necessary ROS libraries and message types

def publish_robot_position():
    rospy.init_node('position_publisher', anonymous=True)
    rate = rospy.Rate(10)  # Set the publishing rate (10 Hz)

    while not rospy.is_shutdown():
        # TODO: Create a geometry_msgs/Point message and set its x, y, and z coordinates
        
        # TODO: Publish the message to the 'robot_position' topic
        
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_robot_position()
    except rospy.ROSInterruptException:
        pass

```
------------------------------------------------------------------------------------------------------------

## Prompt 28: Incomplete ROS Subscriber Code
```python
You are working on a ROS project for a mobile robot. Your task is to create a ROS subscriber that receives the laser scan data from the 'laser_scan' topic. The laser scan data is represented as a sensor_msgs/LaserScan message containing range measurements.

# Import necessary ROS libraries and message types

def laser_scan_callback(msg):
    # TODO: Process the laser scan data received in the callback function
    # Access the range measurements and other information from the 'msg' parameter

def subscribe_to_laser_scan():
    rospy.init_node('laser_scan_subscriber', anonymous=True)
    
    # TODO: Create a subscriber to the 'laser_scan' topic and specify the callback function
    
    rospy.spin()

if __name__ == '__main__':
    subscribe_to_laser_scan()

```
------------------------------------------------------------------------------------------------------------

## Prompt 29: Incomplete ROS Service Code
```python
You are working on a ROS project for a robot arm. Your task is to implement a ROS service that receives a target joint configuration as a sensor_msgs/JointState message and moves the robot arm to the specified configuration. The robot arm is controlled by a joint_trajectory_controller.

# Import necessary ROS libraries and message types

def handle_joint_configuration(req):
    # TODO: Move the robot arm to the target joint configuration specified in 'req'
    # Access the joint positions and other information from the 'req' parameter

    # TODO: Return a response indicating the success or failure of the arm movement

def joint_configuration_server():
    rospy.init_node('joint_configuration_server')
    
    # TODO: Create a ROS service server for the 'move_arm_to_configuration' service
    # and specify the handle_joint_configuration function
    
    rospy.spin()

if __name__ == '__main__':
    joint_configuration_server()

```
------------------------------------------------------------------------------------------------------------

## Prompt 30: Incomplete ROS Action Server Code
```python
You are working on a ROS project for a delivery robot. Your task is to create a ROS action server that receives a goal location as a geometry_msgs/PoseStamped message and navigates the robot to the specified location. The robot's navigation is handled by the move_base package.

# Import necessary ROS libraries and message types

class NavigateToGoalServer:
    def __init__(self):
        # TODO: Initialize the action server and set the goal callback function

    def goal_callback(self, goal):
        # TODO: Implement the navigation behavior to reach the goal location specified in 'goal'
        # Access the goal position and other information from the 'goal' parameter
        
        # TODO: Provide feedback on the progress of the navigation
        
        # TODO: If the goal is reached, set the appropriate result and send it to the client

def main():
    rospy.init_node('navigate_to_goal_server')
    
    # TODO: Create a NavigateToGoalServer object and start the action server
    
    rospy.spin()

if __name__ == '__main__':
    main()

```
------------------------------------------------------------------------------------------------------------

## Prompt 31: Incomplete Custom ROS Message Definition
```python
You are working on a ROS project for a drone. Your task is to create a custom ROS message that represents the drone's flight status. The message should include fields for the drone's battery level (percentage), altitude (meters), and flight mode (string).

# TODO: Create the custom ROS message definition for the 'DroneStatus' message
# The message should include fields for 'battery_level', 'altitude', and 'flight_mode'

```
------------------------------------------------------------------------------------------------------------


## Prompt 32: Incomplete Lisp Function Definition
```lisp
Complete the following Lisp function definition:

(defun multiply-list-elements (lst factor)
  "Multiply each element in the list 'lst' by the given 'factor'."
  (if (null lst)
      '()  ; Base case: return an empty list for an empty list
      ; TODO: Complete the recursive case to multiply the first element of the list by the 'factor'
      ; and continue recursively with the rest of the list
    )
  )
```
------------------------------------------------------------------------------------------------------------

## Prompt 33: Incomplete Lisp Recursive Function
```lisp
Write a recursive Lisp function to calculate the factorial of a non-negative integer:

(defun factorial (n)
  "Calculate the factorial of a non-negative integer 'n'."
  (if (<= n 0)
      ; TODO: Complete the base case to return 1 for n=0
    ; TODO: Complete the recursive case to calculate the factorial of 'n'
    )
  )
```
------------------------------------------------------------------------------------------------------------

## Prompt 34: Incomplete Lisp List Manipulation
```lisp
Write a Lisp function to remove all occurrences of a given element from a list:

(defun remove-all (element lst)
  "Remove all occurrences of 'element' from the list 'lst'."
  (if (null lst)
      '()  ; Base case: return an empty list for an empty list
      ; TODO: Complete the recursive case to remove 'element' from the first element of the list
      ; and continue recursively with the rest of the list
    )
  )
```
------------------------------------------------------------------------------------------------------------

## Prompt 35: Incomplete Lisp Higher-Order Function
```lisp
Write a Lisp higher-order function that applies a given function to each element of a list:

(defun map-list (func lst)
  "Apply 'func' to each element in the list 'lst'."
  (if (null lst)
      '()  ; Base case: return an empty list for an empty list
      ; TODO: Complete the recursive case to apply 'func' to the first element of the list
      ; and continue recursively with the rest of the list
    )
  )
```
------------------------------------------------------------------------------------------------------------

## Prompt 36: Incomplete Lisp List Flattening
```lisp
Write a Lisp function to flatten a nested list:

(defun flatten (lst)
  "Flatten the nested list 'lst' into a single-level list."
  (if (null lst)
      '()  ; Base case: return an empty list for an empty list
      (if (atom (car lst))
          ; TODO: Complete the recursive case to add the first element of the list to the result list
          ; and continue recursively with the rest of the list
          
          ; TODO: Handle the case when the first element is another list (nested list)
          ; and flatten it before continuing recursively with the rest of the list
        )
    )
  )
```
------------------------------------------------------------------------------------------------------------



## Prompt 37: JavaScript to Python Translation - 3D Vector Class
```python
Translate the following JavaScript code that defines a 3D Vector class into Python:

class Vector3D {
  constructor(x, y, z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }

  magnitude() {
    return Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
  }

  dotProduct(otherVector) {
    return this.x * otherVector.x + this.y * otherVector.y + this.z * otherVector.z;
  }

  crossProduct(otherVector) {
    return new Vector3D(
      this.y * otherVector.z - this.z * otherVector.y,
      this.z * otherVector.x - this.x * otherVector.z,
      this.x * otherVector.y - this.y * otherVector.x
    );
  }
}

```

------------------------------------------------------------------------------------------------------------

## Prompt 38: Python to JavaScript Translation - 3D Rotation Class
```python
Translate the following Python code that defines a 3D Rotation class into JavaScript:

class Rotation3D {
  def __init__(self, roll, pitch, yaw):
    self.roll = roll
    self.pitch = pitch
    self.yaw = yaw

  def rotate_vector(self, vector):
    cos_roll = cos(self.roll)
    sin_roll = sin(self.roll)
    cos_pitch = cos(self.pitch)
    sin_pitch = sin(self.pitch)
    cos_yaw = cos(self.yaw)
    sin_yaw = sin(self.yaw)

    x = vector.x
    y = vector.y
    z = vector.z

    # TODO: Perform the 3D rotation of the vector using the roll, pitch, and yaw angles

    return Vector3D(x, y, z)
}

```

------------------------------------------------------------------------------------------------------------

## Prompt 39: C++ to Python Translation - Game Object Class
```python
Translate the following C++ code that defines a Game Object class into Python:

class GameObject {
public:
  GameObject(const std::string& name, const Vector3D& position)
    : name(name), position(position) {}

  void update() {
    // TODO: Implement the update logic for the game object
  }

  void render() {
    // TODO: Implement the rendering logic for the game object
  }

private:
  std::string name;
  Vector3D position;
};

```

------------------------------------------------------------------------------------------------------------

## Prompt 40: Python to C++ Translation - Physics Simulation Class
```python
Translate the following Python code that defines a Physics Simulation class into C++:

class PhysicsSimulation {
public:
  PhysicsSimulation(float gravity)
    : gravity(gravity) {}

  void update(float delta_time) {
    // TODO: Implement the physics update logic using the given delta_time and gravity
  }

  void apply_force(const Vector3D& force) {
    // TODO: Implement the force application logic to update the simulation state
  }

private:
  float gravity;
  // TODO: Add necessary data members and functions for the physics simulation
};

```

------------------------------------------------------------------------------------------------------------

## Prompt 41: Java to Kotlin Translation - 3D Mesh Class
```python
Translate the following Java code that defines a 3D Mesh class into Kotlin:

public class Mesh {
  private String name;
  private List<Vector3D> vertices;
  private List<Integer> triangles;

  public Mesh(String name) {
    this.name = name;
    vertices = new ArrayList<>();
    triangles = new ArrayList<>();
  }

  public void addVertex(Vector3D vertex) {
    vertices.add(vertex);
  }

  public void addTriangle(int v1, int v2, int v3) {
    triangles.add(v1);
    triangles.add(v2);
    triangles.add(v3);
  }

  public int getVertexCount() {
    return vertices.size();
  }

  public int getTriangleCount() {
    return triangles.size() / 3;
  }

  public Vector3D getVertex(int index) {
    return vertices.get(index);
  }

  public int[] getTriangle(int index) {
    int startIndex = index * 3;
    return new int[] {triangles.get(startIndex), triangles.get(startIndex + 1), triangles.get(startIndex + 2)};
  }
}

```

------------------------------------------------------------------------------------------------------------

## Prompt 42: Kotlin to Java Translation - 3D Camera Class
```python
Translate the following Kotlin code that defines a 3D Camera class into Java:

public class Camera3D {
  private Vector3D position;
  private Vector3D target;
  private Vector3D up;

  public Camera3D(Vector3D position, Vector3D target, Vector3D up) {
    this.position = position;
    this.target = target;
    this.up = up;
  }

  public void setPosition(Vector3D position) {
    this.position = position;
  }

  public Vector3D getPosition() {
    return position;
  }

  public void setTarget(Vector3D target) {
    this.target = target;
  }

  public Vector3D getTarget() {
    return target;
  }

  public void setUp(Vector3D up) {
    this.up = up;
  }

  public Vector3D getUp() {
    return up;
  }
}

```

------------------------------------------------------------------------------------------------------------

## Prompt 43: C# to C++ Translation - Game Component Interface
```python
Translate the following C# code that defines a Game Component interface into C++:

public interface IGameComponent {
  void Initialize();
  void Update(float deltaTime);
  void Render();
}
```
------------------------------------------------------------------------------------------------------------

## Prompt 44: C++ to C# Translation - Game Entity Class
```python
Translate the following C++ code that defines a Game Entity class into C#:

class GameEntity {
private:
  string name;
  Vector3D position;

public:
  GameEntity(string name, Vector3D position) {
    this.name = name;
    this.position = position;
  }

  void Update(float deltaTime) {
    // TODO: Implement the update logic for the game entity
  }

  void Render() {
    // TODO: Implement the rendering logic for the game entity
  }
}
```

## Prompt 45: Fix code with ImportError in Python
```python
I provide you with the following Python code snippet:

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(input_dim,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='softmax'))

When running the code, the following ImportError is given:

Traceback (most recent call last):
  File "train_model.py", line 1, in <module>
    from tensorflow.keras.models import Sequential
ModuleNotFoundError: No module named 'tensorflow'

The code snippet is not functioning correctly due to an ImportError. Your task is to debug and fix the code to resolve the ImportError and make it work as intended.
```
------------------------------------------------------------------------------------------------------------

## Prompt 46: Fix code with AttributeError in Python
```python
I provide you with the following Python code snippet:

import numpy as np

data = [1, 2, 3, 4, 5]
mean_value = data.mean()

When running the code, the following AttributeError is given:

Traceback (most recent call last):
  File "calculate_mean.py", line 4, in <module>
    mean_value = data.mean()
AttributeError: 'list' object has no attribute 'mean'

The code snippet is not functioning correctly due to an AttributeError. Your task is to debug and fix the code to calculate the mean value of the 'data' list correctly.
```
------------------------------------------------------------------------------------------------------------

## Prompt 47: Fix code with IndexError in Python
```python
I provide you with the following Python code snippet:

import numpy as np

data = np.array([1, 2, 3, 4, 5])
value = data[5]

When running the code, the following IndexError is given:

Traceback (most recent call last):
  File "access_array.py", line 4, in <module>
    value = data[5]
IndexError: index 5 is out of bounds for axis 0 with size 5

The code snippet is not functioning correctly due to an IndexError. Your task is to debug and fix the code to access the correct index of the 'data' array.
```
------------------------------------------------------------------------------------------------------------

## Prompt 48: Fix code with Binding error message in C
```c
I provide you with the following code snippet in C programming language:

if (bind(socket_desc, (struct sockaddr*)&server, sizeof(server)) < 0) {
    perror("bind failed. Error");
    return 1;
}
puts("bind done");

When running the code, the following error is given:

$ ./server
Socket created
bind failed. Error: Address already in use

The code snippet is not functioning correctly. Your task is to debug and fix the code to make it work as intended.
```
------------------------------------------------------------------------------------------------------------

## Prompt 49: Fix code with Network Connection error in Python
```python
I provide you with the following Python code snippet:

import requests

url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data received successfully.")
else:
    print("Failed to fetch data. Status code:", response.status_code)

When running the code, the following error is given:

requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.example.com', port=443): Max retries exceeded with url: /data (Caused by NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f2d780e9b90>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))

The code snippet is not functioning correctly. Your task is to debug and fix the code to handle the network connection error and fetch data from the API successfully.
```
------------------------------------------------------------------------------------------------------------

## Prompt 50: Fix code with Socket Connection error in Python
```python
I provide you with the following Python code snippet:

import socket

HOST = 'localhost'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print('Received:', data.decode())

When running the code, the following error is given:

ConnectionRefusedError: [Errno 111] Connection refused

The code snippet is not functioning correctly. Your task is to debug and fix the code to handle the socket connection error and receive data from the specified host and port successfully.
```
------------------------------------------------------------------------------------------------------------

## Prompt 51: Fix code with Timeout error in Python
```python
I provide you with the following Python code snippet:

import requests

url = "https://api.example.com/data"
response = requests.get(url, timeout=5)

if response.status_code == 200:
    data = response.json()
    print("Data received successfully.")
else:
    print("Failed to fetch data. Status code:", response.status_code)

When running the code, the following error is given:

requests.exceptions.Timeout: HTTPSConnectionPool(host='api.example.com', port=443): Request timed out.

The code snippet is not functioning correctly. Your task is to debug and fix the code to handle the timeout error and fetch data from the API within the specified time limit successfully.
```
------------------------------------------------------------------------------------------------------------

## Prompt 52: Fix code with HTTP error in Python
```python
I provide you with the following Python code snippet:

import requests

url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data received successfully.")
elif response.status_code == 404:
    print("Data not found. Status code:", response.status_code)
else:
    print("Failed to fetch data. Status code:", response.status_code)

When running the code, the following error is given:

requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://api.example.com/data

The code snippet is not functioning correctly. Your task is to debug and fix the code to handle the HTTP error and print appropriate messages based on the response status code.
```
------------------------------------------------------------------------------------------------------------

## Prompt 53: Fix code with Data Parsing error in Python
```python
I provide you with the following Python code snippet:

import json

data = '{"name": "John", "age": 30, "email": "john@example.com"}'
parsed_data = json.loads(data)

print("Name:", parsed_data['name'])
print("Age:", parsed_data['age'])
print("Location:", parsed_data['location'])

When running the code, the following error is given:

KeyError: 'location'

The code snippet is not functioning correctly. Your task is to debug and fix the code to handle the data parsing error and print the correct values from the 'parsed_data' dictionary.
```
------------------------------------------------------------------------------------------------------------

## Prompt 54: Fix code with Model Loading error in Python (Keras/TensorFlow)
```python
I provide you with the following Python code snippet using Keras/TensorFlow:

from tensorflow.keras.models import load_model

model = load_model('model.h5')

When running the code, the following

 error is given:

OSError: Unable to open file (file signature not found)

The code snippet is not functioning correctly. Your task is to debug and fix the code to load the model 'model.h5' successfully using Keras/TensorFlow.
```
------------------------------------------------------------------------------------------------------------

## Prompt 55: Fix code with Memory Error in Python (NumPy)
```python
I provide you with the following Python code snippet using NumPy:

import numpy as np

data = np.random.rand(10000, 10000)
result = np.dot(data, data)

When running the code, the following error is given:

MemoryError: Unable to allocate 74.5 GiB for an array with shape (10000, 10000) and data type float64

The code snippet is not functioning correctly due to a MemoryError. Your task is to debug and fix the code to perform the matrix multiplication without running out of memory.
```
------------------------------------------------------------------------------------------------------------

## Prompt 56: Fix code with AttributeError in Python (PyTorch)
```python
I provide you with the following Python code snippet using PyTorch:

import torch

x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
z = x + y

print(z)

When running the code, the following error is given:

AttributeError: 'Tensor' object has no attribute 'add'

The code snippet is not functioning correctly. Your task is to debug and fix the code to perform the element-wise addition of tensors 'x' and 'y' using PyTorch.
```
------------------------------------------------------------------------------------------------------------

## Prompt 57: Fix code with ValueError in Python (Pandas)
```python
I provide you with the following Python code snippet using Pandas:

import pandas as pd

data = {'Name': ['John', 'Emma', 'Michael'],
        'Age': [30, 25, 28],
        'City': ['New York', 'Chicago', 'Los Angeles']}

df = pd.DataFrame(data)

selected_column = df['Occupation']

print(selected_column)

When running the code, the following error is given:

KeyError: 'Occupation'

The code snippet is not functioning correctly due to a ValueError. Your task is to debug and fix the code to select the correct column 'Age' from the DataFrame 'df' and print its values.
```
------------------------------------------------------------------------------------------------------------

## Prompt 58: Fix code with Type Error in Python (SciPy)
```python
I provide you with the following Python code snippet using SciPy:

import numpy as np
from scipy.optimize import minimize

def objective(x):
    return x[0]**2 + x[1]**2

x0 = [2, 3]
result = minimize(objective, x0)

print("Minimum value:", result.fun)
print("Optimal solution:", result.x)

When running the code, the following error is given:

TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'

The code snippet is not functioning correctly due to a TypeError. Your task is to debug and fix the code to pass the correct type of input to the 'objective' function in SciPy.
```
------------------------------------------------------------------------------------------------------------

## Prompt 59: Fix code with Network Connection Error in Python (Twisted)
```python
I provide you with the following Python code snippet using Twisted:

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import LineReceiver

class MyProtocol(LineReceiver):
    def connectionMade(self):
        self.sendLine(b"Hello, Server!")

    def lineReceived(self, line):
        print("Received:", line)
        self.transport.loseConnection()

class MyFactory(ClientFactory):
    protocol = MyProtocol

def clientConnectionFailed(failure):
    print("Connection failed:", failure.getErrorMessage())
    reactor.stop()

reactor.connectTCP("localhost", 12345, MyFactory())
reactor.run()

When running the code, the following error is given:

twisted.internet.error.CannotListenError: Couldn't listen on any:12345: [Errno 98] Address already in use.

The code snippet is not functioning correctly due to a Network Connection Error. Your task is to debug and fix the code to connect to the server successfully without address conflicts.
```
------------------------------------------------------------------------------------------------------------

## Prompt 60: Fix code with HTTP Error in Python (aiohttp)
```python
I provide you with the following Python code snippet using aiohttp:

import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None

async def main():
    url = "https://api.example.com/data"
    data = await fetch_data(url)
    if data:
        print("Data received successfully.")
    else:
        print("Failed to fetch data.")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()

When running the code, the following error is given:

aiohttp.client_exceptions.ClientConnectorError: Cannot connect to host api.example.com:443 ssl:default [Name or service not known]

The code snippet is not functioning correctly due to an HTTP Error. Your task is to debug and fix the code to handle the HTTP error and fetch data from the API successfully using aiohttp.
```
------------------------------------------------------------------------------------------------------------

## Prompt 61: Fix code with RuntimeError in Python (PyTorch)
```python
I provide you with the following Python code snippet using PyTorch:

import torch

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = torch.tensor([4.0, 5.0, 6.0])

z = x * y

loss = torch.sum(z)

loss.backward()

print("Gradient of x:", x.grad)

When running the code, the following error is given:

RuntimeError: element 0 of tensors does not require grad and does not have a grad_fn

The code snippet is not functioning correctly due to a RuntimeError. Your task is to debug and fix the code to calculate the gradient of tensor 'x' correctly using PyTorch.
```
------------------------------------------------------------------------------------------------------------

## Prompt 62: Fix code with Resource Warning in Python
```python
I provide you with the following Python code snippet:

import requests

url = "https://api.example.com/data"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Data received successfully.")
else:
    print("Failed to fetch data. Status code:", response.status_code)

When running the code, the following ResourceWarning is given:

ResourceWarning: unclosed file <_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>

The code snippet is not functioning correctly. Your task is to debug and fix the code to properly handle resources and prevent the ResourceWarning.
```
------------------------------------------------------------------------------------------------------------

## Prompt 63: Fix code with Connection Error in Python (paramiko)
```python
I provide you with the following Python code snippet using paramiko:

import paramiko

ssh = paramiko.SSHClient()

try:
    ssh.connect('localhost', username='user', password='pass')
    print("Connection successful.")
except paramiko.ssh_exception.SSHException as e:
    print("SSH Exception:", e)
except paramiko.AuthenticationException:
    print("Authentication failed.")
except paramiko.BadHostKeyException:
    print("Host key could not be verified.")
except paramiko.SSHException as e:
    print("SSH Exception:", e)
except Exception as e:
    print("Unexpected error:", e)
finally:
    ssh.close()

When running the code, the following error is given:

paramiko.ssh_exception.NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 127.0.0.1

The code snippet is not functioning correctly due to a Connection Error. Your task is to debug and fix the code to handle the connection error and perform the SSH connection using paramiko.
```


------------------------------------------------------------------------------------------------------------


## Prompt 64 Fix code with error message
I provide you with the following code snippet in C programming language:
```c
if( bind(socket_desc,(struct sockaddr *) &server, sizeof(server)) < 0)
{
    perror("bind failed. Error");
    return 1;
}
puts("bind done");
```
When running the code, the following error is given:
```bash
$ ./serve   
Socket created    
bind failed. Error: Address already in use
```
The code snippet is not functioning correctly. Your task is to debug and fix the code to make it work as intended.

#5 Writing a mapper function between two data structures
Write a mapper function between Class 1 and Class 2 in Java for the following code:
```java
// Class 1
data class WeatherDetails(
      val nameOfLocation: String,
      val temperature: Temperature,
      val wind: Wind,
      val weatherCondition: WeatherCondition,
      val humidity: String,
      val pressure: String
      ) {
      data class Temperature(
      val currentTemp: String,
      val minTemperature: String,
      val maxTemperature: String,
)

 
// Class 2
      data class BriefWeatherDetails(
      val nameOfLocation: String,
      val currentTemperature: String,
      val shortDescription: String,
      @DrawableRes val shortDescriptionIcon: Int,
)

```


# Table of Contents
- [CodeVista Sample Prompts](#codevista-sample-prompts)
  - [Prompt 1 Improve variable names](#prompt-1-improve-variable-names)
  - [Prompt 2 Text to SQL](#prompt-2-text-to-sql)
  - [Prompt 3 Code translate](#prompt-3-code-translate)
  - [Prompt 4 Test case suggestion](#prompt-4-test-case-suggestion)
  - [Test scenario list:](#test-scenario-list)
  - [Prompt 5 Test data generation](#prompt-5-test-data-generation)
  - [Prompt 6 Test script generation](#prompt-6-test-script-generation)
  - [Prompt 7 Convert JSON to XML](#prompt-7-convert-json-to-xml)
  - [Prompt  8 Find potential issues](#prompt--8-find-potential-issues)
  - [Prompt 9 Q\&A](#prompt-9-qa)
  - [Prompt 10 Generate FastAPI code for a predefined function](#prompt-10-generate-fastapi-code-for-a-predefined-function)
  - [Prompt  11 Extract search query from an user question](#prompt--11-extract-search-query-from-an-user-question)
  - [Prompt 12 Double-check generated answers](#prompt-12-double-check-generated-answers)
  - [Prompt 13 Generate Java code for building a mobile app using Spring Boot](#prompt-13-generate-java-code-for-building-a-mobile-app-using-spring-boot)
  - [Prompt 14: Generate Java code for building a mobile app from an outline using SpringBoot:](#prompt-14-generate-java-code-for-building-a-mobile-app-from-an-outline-using-springboot)
  - [Prompt 15: Generate Python code for parsing and extracting data from a CSV file:](#prompt-15-generate-python-code-for-parsing-and-extracting-data-from-a-csv-file)
  - [Prompt 16: Generate Java code for creating a custom exception class and handling it in a program:](#prompt-16-generate-java-code-for-creating-a-custom-exception-class-and-handling-it-in-a-program)
  - [Prompt 17: Generate Python code for reading and writing data to a JSON file:](#prompt-17-generate-python-code-for-reading-and-writing-data-to-a-json-file)
  - [Prompt 18: Generate C code to implement a linked list and a function to reverse it:](#prompt-18-generate-c-code-to-implement-a-linked-list-and-a-function-to-reverse-it)
  - [Prompt 19: Generate Java code for creating a simple class representing a bookstore:](#prompt-19-generate-java-code-for-creating-a-simple-class-representing-a-bookstore)
  - [Prompt 20: Generate C++ code for implementing a stack data structure with basic operations:](#prompt-20-generate-c-code-for-implementing-a-stack-data-structure-with-basic-operations)
  - [Prompt 21: Generate Python code for reading data from an API and processing the JSON response:](#prompt-21-generate-python-code-for-reading-data-from-an-api-and-processing-the-json-response)
  - [Prompt 22: Generate C code to implement a basic banking system using structures:](#prompt-22-generate-c-code-to-implement-a-basic-banking-system-using-structures)
  - [Prompt 23: Generate Python code for implementing a basic hash table (dictionary) with collision handling:](#prompt-23-generate-python-code-for-implementing-a-basic-hash-table-dictionary-with-collision-handling)
  - [Prompt 24: Generate Java code for creating a multithreaded program with synchronization:](#prompt-24-generate-java-code-for-creating-a-multithreaded-program-with-synchronization)
  - [Prompt 25: Generate C++ code for creating a simple text-based game:](#prompt-25-generate-c-code-for-creating-a-simple-text-based-game)
  - [Prompt 26: Generate Python code for reading and writing data to a SQLite database:](#prompt-26-generate-python-code-for-reading-and-writing-data-to-a-sqlite-database)
  - [Prompt 27:  ROS Publisher Code](#prompt-27--ros-publisher-code)
  - [Prompt 28: Incomplete ROS Subscriber Code](#prompt-28-incomplete-ros-subscriber-code)
  - [Prompt 29: Incomplete ROS Service Code](#prompt-29-incomplete-ros-service-code)
  - [Prompt 30: Incomplete ROS Action Server Code](#prompt-30-incomplete-ros-action-server-code)
  - [Prompt 31: Incomplete Custom ROS Message Definition](#prompt-31-incomplete-custom-ros-message-definition)
  - [Prompt 32: Incomplete Lisp Function Definition](#prompt-32-incomplete-lisp-function-definition)
  - [Prompt 33: Incomplete Lisp Recursive Function](#prompt-33-incomplete-lisp-recursive-function)
  - [Prompt 34: Incomplete Lisp List Manipulation](#prompt-34-incomplete-lisp-list-manipulation)
  - [Prompt 35: Incomplete Lisp Higher-Order Function](#prompt-35-incomplete-lisp-higher-order-function)
  - [Prompt 36: Incomplete Lisp List Flattening](#prompt-36-incomplete-lisp-list-flattening)
  - [Prompt 37: JavaScript to Python Translation - 3D Vector Class](#prompt-37-javascript-to-python-translation---3d-vector-class)
  - [Prompt 38: Python to JavaScript Translation - 3D Rotation Class](#prompt-38-python-to-javascript-translation---3d-rotation-class)
  - [Prompt 39: C++ to Python Translation - Game Object Class](#prompt-39-c-to-python-translation---game-object-class)
  - [Prompt 40: Python to C++ Translation - Physics Simulation Class](#prompt-40-python-to-c-translation---physics-simulation-class)
  - [Prompt 41: Java to Kotlin Translation - 3D Mesh Class](#prompt-41-java-to-kotlin-translation---3d-mesh-class)
  - [Prompt 42: Kotlin to Java Translation - 3D Camera Class](#prompt-42-kotlin-to-java-translation---3d-camera-class)
  - [Prompt 43: C# to C++ Translation - Game Component Interface](#prompt-43-c-to-c-translation---game-component-interface)
  - [Prompt 44: C++ to C# Translation - Game Entity Class](#prompt-44-c-to-c-translation---game-entity-class)
  - [Prompt 45: Fix code with ImportError in Python](#prompt-45-fix-code-with-importerror-in-python)
  - [Prompt 46: Fix code with AttributeError in Python](#prompt-46-fix-code-with-attributeerror-in-python)
  - [Prompt 47: Fix code with IndexError in Python](#prompt-47-fix-code-with-indexerror-in-python)
  - [Prompt 48: Fix code with Binding error message in C](#prompt-48-fix-code-with-binding-error-message-in-c)
  - [Prompt 49: Fix code with Network Connection error in Python](#prompt-49-fix-code-with-network-connection-error-in-python)
  - [Prompt 50: Fix code with Socket Connection error in Python](#prompt-50-fix-code-with-socket-connection-error-in-python)
  - [Prompt 51: Fix code with Timeout error in Python](#prompt-51-fix-code-with-timeout-error-in-python)
  - [Prompt 52: Fix code with HTTP error in Python](#prompt-52-fix-code-with-http-error-in-python)
  - [Prompt 53: Fix code with Data Parsing error in Python](#prompt-53-fix-code-with-data-parsing-error-in-python)
  - [Prompt 54: Fix code with Model Loading error in Python (Keras/TensorFlow)](#prompt-54-fix-code-with-model-loading-error-in-python-kerastensorflow)
  - [Prompt 55: Fix code with Memory Error in Python (NumPy)](#prompt-55-fix-code-with-memory-error-in-python-numpy)
  - [Prompt 56: Fix code with AttributeError in Python (PyTorch)](#prompt-56-fix-code-with-attributeerror-in-python-pytorch)
  - [Prompt 57: Fix code with ValueError in Python (Pandas)](#prompt-57-fix-code-with-valueerror-in-python-pandas)
  - [Prompt 58: Fix code with Type Error in Python (SciPy)](#prompt-58-fix-code-with-type-error-in-python-scipy)
  - [Prompt 59: Fix code with Network Connection Error in Python (Twisted)](#prompt-59-fix-code-with-network-connection-error-in-python-twisted)
  - [Prompt 60: Fix code with HTTP Error in Python (aiohttp)](#prompt-60-fix-code-with-http-error-in-python-aiohttp)
  - [Prompt 61: Fix code with RuntimeError in Python (PyTorch)](#prompt-61-fix-code-with-runtimeerror-in-python-pytorch)
  - [Prompt 62: Fix code with Resource Warning in Python](#prompt-62-fix-code-with-resource-warning-in-python)
  - [Prompt 63: Fix code with Connection Error in Python (paramiko)](#prompt-63-fix-code-with-connection-error-in-python-paramiko)
  - [Prompt 64 Fix code with error message](#prompt-64-fix-code-with-error-message)
- [Table of Contents](#table-of-contents)
