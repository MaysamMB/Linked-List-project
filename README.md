**Car Brands and Models Management System**

This Python project provides a console-based system to manage car brands and their respective models.
It simulates a linked list structure where each brand can have multiple car models associated with it.

**Features**

Add and remove car brands.

Add and remove car models for a specific brand.

Display all brands with their models.

Display models of a specific brand.

Search for a brand or a specific model within a brand.

Save to and read data from a file (basic implementation).

**Structure Overview**

*Classes:*
 
- Brand

Represents a car brand.

Has links to the next and previous brand.

Holds a pointer to the head of its Model linked list.

- Model

Represents a specific car model.

Stores the model name, year, and price.

Has a pointer to the next model in the list.

- List

Acts as a double linked list container for all Brand nodes.

Provides functionality to:

Add/remove/search/display brands.

Add/remove/search/display models of a specific brand.

**Main Idea:**

Using Pointer as singly linked list with a doubly linked list.

How point Works
Each Brand node contains a point pointer, which links to a separate singly linked list of Model nodes.
This design allows each brand to maintain its own list of car models independently.

For example:

Brand("Toyota") --> point --> Model("Corolla") --> Model("Camry") --> ...
  
This structure ensures that models are organized under their respective brands and prevents mixing data between different brands.


**Utility:**

Interactive text menu for user input.

Simple save/read functionality using a .txt file.

**Requirements**

Python 3.x

**Run the App**

python CARS_DS.py

**Author**

Developed by [Maysam Baradiya]

Date: Dec 2024
