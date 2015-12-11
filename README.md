# Work Breakdown Manager
####  Craig Tingey

Class library for managing tasks for a project. Run the tests file.

```
python tests.py
python version: Python 2.7.6
```

Note: Dr. Clyde gave me permission to read from a json file instead of a xml file.


### Patterns
We learned a lot of patterns in this class and my programming skills have improved a lot from learning them. Though I sometimes mix up the patterns, I think the concepts have stayed with me and I'm more capable of writing good code than I was before this class. I'm going to try to figure out which patterns I used in this project and describe them here.

I'm using Python so some of the patterns might be applied in a different way than they would be with C# or Java.

#### Visitor
I may not have done the visitor pattern exactly according to the book but I did something similar. My TaskComponent acts like the interface for the other tasks (parallel, sequential, leaf) and each element has functions with the same name except they do different things depending on what the element is. For example the function, get_remaining_hours when called on a parent task it has to do some calculations with it's subtasks but the Leaf task just returns the attribute remaining_hours.


#### Strategy
The FileLoader acts as the interface and creates a project from a json file. It could easily be extended to create a project from xml or whatever else without changing much code.
