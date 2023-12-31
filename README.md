# AirBnB clone - The console
 <img src="img/hbnb_screenshot.png" alt="cover" />

## Description of the Project

Greetings and welcome to our AirBnB Clone project! This marks the inception of our journey towards crafting a comprehensive web application inspired by the esteemed Airbnb platform. Within this project, we've crafted a robust Command Line Interface (CLI) to adeptly handle AirBnB objects.

### Command Line Interface (CLI) - Bridging Vision and Execution

Our Command Line Interface (CLI) serves as the nucleus of interaction with the AirBnB Clone project. It's a dynamic tool that facilitates the seamless communication between developers and the application's core functionalities. At its heart, the CLI empowers developers to effortlessly manage and manipulate AirBnB objects through a series of intuitive commands.

### Streamlining Object Management and Interaction

The CLI isn't just a mere gateway to the application; it's a powerful mechanism that empowers developers to perform a wide array of operations on AirBnB objects:

1. **Creating Objects**: With a single command, developers can instantiate new instances of various AirBnB objects. This initial step lays the foundation for populating our application with data.

2. **Retrieving Objects**: Our CLI is equipped with the capability to retrieve specific objects based on user-defined criteria. This functionality is pivotal for developing advanced search and data retrieval features.

3. **Object Manipulation**: Beyond retrieval, developers can use the CLI to perform an array of operations on objects. From counting and computing statistics to applying updates, the CLI is a versatile toolkit for data manipulation.

4. **Attribute Updation**: The CLI seamlessly facilitates the updating of object attributes. This dynamic feature ensures that our application's data remains current and accurate.

5. **Efficient Object Management**: In situations where objects are no longer needed, the CLI simplifies the process of object destruction, ensuring efficient data management.

## Description of the Command Interpreter

### How to Start the Command Interpreter

The Command Interpreter for the AirBnB project can be initiated using both interactive and non-interactive modes.

#### Non-Interactive Mode

Non-interactive mode enables you to run the interpreter with predefined commands provided via standard input. To start the interpreter in non-interactive mode:

1. Open your terminal.
2. Navigate to the root directory of the project.
3. Use the `echo` command to pipe commands into the `console.py` script:
```
$ echo "help" | ./console.py
```
4. The interpreter will execute the provided command(s) and display the results.

**Examples:**
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Console Commands

The AirBnb Interpreter provides several commands for managing instances of classes. These commands allow you to create, show, update, delete, and list instances in a convenient and efficient way.

