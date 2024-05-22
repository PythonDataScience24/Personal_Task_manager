Unittest
Important -> the test file inside the source folder is just temporary and was mainly to create rdm test data
the final tests are inside the tests folder.

For this task we created the taskValidator_test:

We tested each method of the taskValidator class the wrong outputs from this class could be if the method doesnt work correctly (not correctly used library functions, false logic in coding). In the case of the deadline it could be that the formats are not correctly recognized, in priority we have to ensure that only invalid strings are catched and set to 0 while valid Strings need to be typechanged. Our tests therefore focus on entering such inputs into the methods and aticipate the expected outcome and comparing the two.

Of course these methods are rather simple but they are essential for the other methods to function.
