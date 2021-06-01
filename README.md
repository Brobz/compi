# NucaScript

A strongly-typed, string manipulation and file I/O centered language that uses python and PLY to compile down to a C++ virtual machine, generating an executable output of the program without the need for an intermediate object code file.

Developed in about 10 weeks as the final project of the Compiler Design class at ITESM.

## Dependencies

python 3.7.4 (+)

g++11 (+)

## **Basic Program Structure:**

    /*/ This is a comment! Comments are always multiline /*/

    program NUCA; /*/ Sets the program name, which is as the default path for the out after compilation /*/

    /*/ After the program name, the user may declare variables, methods and classes in any order he wishes to /*/

    i, j, k, arr[50] : int;   /*/ Declaration of four int variables, the latter being an array with size 50 /*/
    matrix[3][3][3] : float;  /*/ Declaration of a 3x3x3 matrix of floating point values /*/

    void say_hello(name : string) /*/ Declaration of a global void method that takes in a string argument /*/
    VARS{} /*/ Local variables can be defined for each method in the same manner that they are globally, inside the VARS{} section. This method has no global variables /*/
    {
      println("Hello,", name);
      /*/ If the last statement of a method's body is not a return statement, it automatically assumes a 'return;', which works in this case since the method is of void type /*/
    }

    class Class{ /*/ A class definition has two parts: attributes and methods, and it cannot contain other objects as attributes (no compound objects) /*/
      ATTR{
        n : int; /*/ All class attributes are public! /*/
      }

      int get_n()
      VARS{}
      {
        return this.n;      /*/ All class attributes must be accessed via the 'this.' operator /*/
      }

      void set_n(n : int)
      VARS{}
      {
        this.n = n;         /*/ That allows this kind of stuff /*/
      }

    }

    obj : object; /*/ Here we declare an object type variable, which can be instantiated to any class type /*/

    /*/ After all of the declarations, comes the main method, where the program will start its execution /*/
    main(){
      obj = new Class(); /*/ obj will now be a fresh instance of Class /*/
      print(">> Enter an integer\n-- ");
      read(i); /*/ Stores user input (from the console) into i /*/
      obj.set_n(i); /*/ Call to an object method /*/
      println(obj.get_n()); /*/ To confirm it works! /*/

      /*/ There are many more cool things one can do with NucaScript! Check out the full documentation document on the official git repository to learn more! /*/
    }
