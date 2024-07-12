## DESCRIPTION

A collection of design patterns in Python

# Singleton design pattern
  A singleton design pattern ensures that a class has only one instance and provides
  a global reference point to its implementation
 
 There can be only one!
            —Connor MacLeod
   
 - A Singleton design pattern that can be used to create a new instance of an object.
   The instance created is immutable and can not be changed after creation .

- The main criticism of the singleton pattern is that it is just a pretty way to get a global 
  state, which is one of the things you want to avoid when writing programs. One of the 
  reasons why you want to avoid global state is that code in one part of your project may 
  alter the global state and cause unexpected results in a completely unrelated piece of 
  code

- places where global state may be used are in caching, load balancing, and route mapping.
  In all these cases, information flows in one direction

