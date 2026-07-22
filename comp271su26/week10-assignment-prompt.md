# Week 10 assignment

The assignment will be posted as week10-assignment.md in the student facing folder, under week10.

As with previous assignments, this one too will have an ungrading reflection based on the solutions for week09.

After summarizing the week based on the transcripts available in the week's folder, ask students to perform the following tasks:

* Rewrite stackq.py so that push() and pop() will operate from the first line of the file not the last.

* Implement a double-linked list using files only. For simplicity, the data payload can be just a simple string. Without giving out too much information to students, the idea here is to have two files, head.txt. and tail.txt. The file structure can be simple, like:
````
payload
next_filename
prev_filename
```

On instantiation both files are empty and the linked list's size is 0.

Adding nodes is assumed to be always birectional (ie, both next and prev pointers exist). On size==1 the linked list should look like
```
head.txt               tail.txt
initial_payload        initial_payload
(empty line for next)  (empty line for next)
(empty line for prev)  (empty line for prev)
```

After adding another node, (size==2), the files will be:

```
head.txt             tail.txt
initial_payload      second_payload
tail.txt             (empty line for next)
(empty for prev)     head.txt
```

After adding another node (size==3), the files will be:

 29
 30 ```
 31 head.txt                  random_file_name.txt      tail.txt
 32 initial_payload           second_payload            third_payload
 33 random_file_name.txt      tail.txt                  (empty line for next)
 34 (empty for prev)          head.txt                  random_file_name.txt
 35 ```

 File names for intermediate nodes are generated randomly as a combination of 8 letter characters (upper and lower letters only). Duplicates are unlikely but to avoid them we maintain a file with node file names. New files are compared against that directory before used.

 No lists or other in-memory data structures can be used.
