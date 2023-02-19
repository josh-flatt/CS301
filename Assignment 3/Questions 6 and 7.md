## 6. Python's List feature
I believe that Python's internal representation of a List is a Stack/array, <br>
and not of a Linked/Doubly Linked List. Some signs that I have noticed that pointed <br>
me to this conclusion are how long inserting/removing at the beginning of a long list compares <br>
to inserting/removing at the end of the list. Also, it takes one step to access an element via <br>
its index.


## 7. Stacks, Queues, and Deques

- Stack - List
    - A stack usually would benefit from being implemented over Python's <br>
    List due to often accessing the middle of the list through an index.
- Queue - Doubly Linked List
    - A queue adds to the beginning of a list, and removes from the end. <br>
    Since there is rarely indexing through a queue, it would make sense to <br>
    have a Doubly Linked List to easily add and remove from the ends.
- Deque - Doubly Linked List
    - A Deque is very similar to a Queue, but things are added and removed <br>
    from both ends. Thus, it makes sense to implement a Doubly Linked List <br> 
    for the same reason as a Queue.