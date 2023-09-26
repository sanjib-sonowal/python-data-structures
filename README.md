# Python Data Structures
This repo consists of several programs related to data structures in Python.
# Sample Programs
## Recursion
Recursion is a key idea in data structures and computer science. It describes the method that a function uses to invoke itself during the course of its own execution. Recursive functions, then, are functions that solve problems by splitting them up into smaller, easier-to-manage subproblems of the same kind and then solving those subproblems by calling themselves. Up until a base case is achieved, each recursive call tackles a smaller amount of the issue before returning a solution.

When a problem can be broken down naturally into smaller instances of the same problem, recursion is frequently utilized to solve it. Given that many data structures, like trees and linked lists, exhibit recursive features, it is particularly prevalent in data structures and algorithms.

Key elements of recursion include:

Base Case: This is a condition that defines when the recursion should stop. It's the simplest instance of the problem that can be solved directly without further recursion.

Recursive Case: This is the part of the function where it calls itself with a modified version of the problem. It's where the problem is broken down into smaller, similar subproblems.

Progress Toward Base Case: Each recursive call should make progress toward the base case, ensuring that the recursion eventually terminates.

Recursion is often used in various data structure operations and algorithms, such as:

Tree Traversal: Recursive algorithms are commonly used to traverse trees, like binary trees and binary search trees, by visiting each node in a systematic way.

Sorting Algorithms: Some sorting algorithms, such as quicksort and mergesort, are implemented using recursion to divide the array into smaller subarrays for sorting.

Search Algorithms: Recursive search algorithms, like binary search, divide the search space into smaller parts with each recursive call.

Mathematical Calculations: Recursion is used in mathematical calculations involving sequences and series, like the Fibonacci sequence or factorial calculations.

Graph Algorithms: Recursive algorithms can be used to explore and traverse graphs, especially in depth-first search (DFS).

## Array
An array is a fundamental data structure in computer science used for storing and organizing a collection of elements, each identified by an index or a key. Arrays are used to store data of the same type, such as integers, characters, or objects. They are one of the simplest and most widely used data structures due to their efficiency and ease of use.

Key characteristics of arrays include:

Homogeneity: Arrays store elements of the same data type. For example, an integer array can only store integers, and a character array can only store characters.

Fixed Size: In many programming languages, arrays have a fixed size, meaning you need to specify the number of elements it can hold when declaring it. This size doesn't change during the array's lifetime. Some languages, like Python, allow dynamic arrays that can resize themselves as needed.

Index-Based: Elements in an array are accessed using an index or position. The index typically starts at 0 for the first element and goes up to (size - 1) for an array of size "size." So, the index represents the relative position of an element within the array.

Contiguous Memory: In memory, the elements of an array are stored in contiguous (adjacent) locations. This means that the elements are stored one after the other, making it efficient to access them by their index.

Random Access: Arrays support constant-time random access, which means you can directly access any element in the array by providing its index.

Ordered Collection: Elements in an array are ordered, meaning they have a specific sequence. The order is determined by their positions in the array.

Common operations on arrays include:

Access: Retrieving the value of an element at a specific index.
Insertion: Adding a new element to the array at a particular index or at the end.
Deletion: Removing an element from the array, either by index or by value.
Search: Finding the index or position of a specific element in the array.
Update: Changing the value of an existing element at a specific index.

Arrays are used in a wide range of applications, from simple data storage to more complex data structures like stacks, queues, matrices, and dynamic arrays (lists). They are the foundation for many algorithms and data manipulation tasks in computer science and programming.

It's important to note that in some programming languages, arrays have limitations such as fixed size, which has led to the development of dynamic arrays (e.g., ArrayList in Java or List in Python) that can resize themselves as needed, providing more flexibility in data storage.
## Linked List
A linked list is a fundamental data structure in computer science used to organize and store a collection of elements, each of which is called a "node." Unlike arrays, which use contiguous memory locations to store elements, linked lists use a structure where each node contains both the data and a reference (or link) to the next node in the sequence. This arrangement allows for dynamic memory allocation, making linked lists particularly useful when the size of the data structure needs to change frequently during program execution.

Key characteristics of linked lists include:

Nodes: Each node in a linked list contains two parts: the data or element being stored, and a reference (or pointer) to the next node in the sequence. Some linked lists, such as doubly linked lists, also include a reference to the previous node.

Dynamic Size: Linked lists can grow or shrink in size during program execution because memory for each node is allocated independently. This contrasts with arrays, which often have a fixed size.

No Contiguous Memory: Unlike arrays, linked list nodes do not need to be stored in contiguous memory locations. Each node can be placed anywhere in memory, and the references connect them.

Head: The first node of the linked list is referred to as the "head." It serves as the starting point for traversing the list.

Tail: In a singly linked list, the last node (i.e., the one whose reference points to null) is often referred to as the "tail." In doubly linked lists, there may also be a "tail" that points to the last node.

Singly Linked vs. Doubly Linked: In singly linked lists, each node has a reference to the next node, while in doubly linked lists, each node has references to both the next and previous nodes. Doubly linked lists allow for more efficient traversal in both directions but use more memory.

Common operations on linked lists include:

Insertion: Adding a new node at the beginning, end, or a specific position within the list.
Deletion: Removing a node from the list, either by value or by position.
Traversal: Iterating through the list to access or modify its elements.
Searching: Finding a specific element within the list.
Concatenation: Combining two linked lists.
Reversing: Changing the order of elements in the list.

Linked lists come in various forms, including singly linked lists, doubly linked lists, and circular linked lists, each with its own advantages and use cases. Linked lists are particularly useful when elements need to be inserted or removed frequently, as these operations can be done with a time complexity of O(1) if you have a reference to the node. However, accessing elements by index is less efficient than with arrays, as it requires traversing the list from the head.
## Stack
In computer science, a stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. This means that the last element added to the stack is the first one to be removed. Think of it like a stack of books: you add books to the top of the stack and remove them from the top as well.

A stack has two primary operations:

Push: This operation is used to add an element to the top of the stack. It's equivalent to placing a new book on top of the stack of books.

Pop: This operation is used to remove and retrieve the top element from the stack. It's equivalent to taking the top book off the stack.

In addition to these core operations, stacks typically support the following operations:

Peek (or Top): This operation allows you to view the top element of the stack without removing it. It's like looking at the top book without taking it off the stack.
Stacks are used in a variety of applications and algorithms, including:

Function Call Stack: In programming languages, a stack is often used to keep track of function calls and their local variables. When a function is called, its information is pushed onto the stack, and when the function returns, it's popped off.

Expression Evaluation: Stacks can be used to evaluate arithmetic expressions, particularly those in postfix (Reverse Polish Notation) or prefix (Polish Notation) form.

Backtracking Algorithms: Stacks can help with backtracking algorithms, such as depth-first search (DFS) in graph traversal.

Parsing: Stacks are used in parsing algorithms to keep track of symbols and operators in expressions or programming languages.

Undo and Redo Operations: In applications like text editors or graphic design software, stacks can be used to implement undo and redo functionality.

Memory Management: Stacks are used in memory management, including managing call frames and handling interrupts.

Expression Conversion: Stacks are used in converting infix expressions to postfix or prefix form.

It's important to note that many programming languages provide built-in support for stacks through data structures called "stacks" or "call stacks." In these languages, you can use the push and pop operations implicitly when working with function calls and local variables. However, you can also implement a stack data structure explicitly if needed.
## Queue
In computer science, a queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. This means that the first element added to the queue is the first one to be removed. Think of it like a queue of people waiting in line: the person who arrives first is the one who gets served first.

A queue has two primary operations:

Enqueue: This operation is used to add (or "enqueue") an element to the back of the queue. It's equivalent to a person joining the back of the line.

Dequeue: This operation is used to remove (or "dequeue") the front element from the queue. It's equivalent to the person at the front of the line being served and then leaving the line.

In addition to these core operations, queues often support the following operations:

Peek (or Front): This operation allows you to view the front element of the queue without removing it. It's like checking who is at the front of the line without asking them to leave.

IsEmpty: This operation checks whether the queue is empty or not. If the queue has no elements, it returns true; otherwise, it returns false.

Size: This operation returns the number of elements currently in the queue.

Queues are used in a variety of applications and algorithms, including:

Task Scheduling: Queues are used to schedule tasks or processes for execution in an orderly manner. For example, in operating systems, processes waiting for CPU time are typically organized in a queue.

Breadth-First Search (BFS): Queues are used in graph traversal algorithms, like BFS, to explore nodes at each level of the graph before moving deeper.

Print Queue: In printers, documents to be printed are typically stored in a queue. The first document in is the first to be printed.

Job Queues: In multithreading or multiprocessing applications, job queues are used to distribute tasks or jobs among worker threads or processes.

Request Handling: Web servers often use queues to handle incoming requests from clients. Requests are added to a queue and processed in the order they were received.

Data Buffering: Queues can be used to buffer data between two processes or components that operate at different speeds, ensuring that data is processed in an orderly manner.

It's important to choose the appropriate data structure for a given problem, and queues are particularly useful when you need to manage elements in a way that respects their order of arrival. Like stacks, queues are also implemented in many programming languages, and you can use them directly when needed.
## Binary Tree
## Binary Search Tree
## AVL Tree
## Binary Heap
## Trie
## Hashing
## Sorting
## Graph
## Greedy Algorithm
## Divide and Conquer
## Dynamic Programming
