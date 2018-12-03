## 1. Python Foudations

1. Basic Usage

   ```python
   '''
   swap data
   '''
   a = 1
   b = 2
   a, b = b, a
   --------------
   a = a + b
   b = a - b
   a = a - b
   --------------
   a = a ^ b
   b = b ^ a
   a = a ^ b
   ```

2.  How to read data of 5G by 4G RAM:

   1. by genenrator

   2. by split method in linux

3. read, readline, readlines

   1. read for all file contents

   2. readline: read the next line by generator

   3. readlines: read all file contents as an iterator for us to iterate

4. shallow copy and deepcopy

   shallow copy: methods of slice, factory function, copy in copy module

   deepcopy: deepcopy in copy module

5. difference between _ _ init _ _ and __ _new _  _:

   1. init begins after the object created, and initiate the object

   2. new create a object before the object created, and return that to init

6. mess up a sorted a list

   ```python
   import random
   random.shuffle(alist)
   ```

7. os.path and sys.path

   os.path for manipulation of files in system route

   sys.path for manipulation of environ params

8. strong language and dynamic

   1. different types of data not allowed to be added

   2. without a claim of data type , only defined by the value first passed

9. python2  and python3

   1. python3 support unicode

   2. python2 uses ASCII  str, unicode, 

   3. python3 adopt the abs path to import 

   4. some others

10. to improve the performance of python

    1. use multi cpu

    2. use IO repeat use

    3. use built-in functions

    4. use non-global varibles

11. some linux and git

    1. netstat -anp | grep service_name

12. In ubuntu how to set a programm start when system starts:

    1. modify the contents in /etc/rc0.d ~/etc/rc6.d and /etc/rcS.d

       begins with S means start; K means no start

13. difference between find and grep:

    1. grep for lines that matched and find is for the file matched 

14. ">" means create or modified  and ">>" means append

15. hard connection and soft connection 

16. how to unzip

    1. tar -xvfz ***.tar.gz

17. difference between dict and json:

    1. dict is a data stucture

    2. json is a format of data display.

    3. for dict , the key must be hashable, and for json, key must be string

18. sorted a dict by value:

```python
d = {'a': 24, 'b':2, 'c':23}
sorted(d.items(), key=lambda x: x[1], reverse=True)
```

19. detect effiency for python function :

    1. ```python
       import cProfile
       cProfile.run()
       ```

20. 






