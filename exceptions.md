Exceptions:
Exceptions should either be handled by giving Error Message or by handling it in a task specific way. We decided to handle exception by handling them immediately. As all of our try-except block are mainly here to catch errors in inputs (Missing file, wrong format, invalid input/wrong typed input). So our exception Handling is either to create a valid input or to just execute the method because the try method is actually checks for not valid inputs and the thrown exception is actually a valid input.

taskValidator:

validatePriority:
The try-except method aims to make ensure the input is valid:
try block : in the try block we test if the input is a string that can be converted if it cant be converted it gets set to the default value
except block: the try block should call the Value or Type Error this could suggest that the input is actually already an integer. So we handle it by simply returning x
in both cases the integer value gets scaled up or back into a valid value

validateDeadline:
Similarly this method tries multiple diffrent formats for the datetimeobject the try blocks go over diffrent formats the except blocks leading into the next format that has to be tested if None of the allowed formats match we return none and print an error message. In the last try block we also ensure that the deadline is actually in the futur. (if the format is valid)

manager:

set_inprogress:
we used try and except to ensure we dont get an error if the json file is somehow unable to be opend or corrupted.
try-block : trys to load json file
except-block : when an error apears an empty data frame gets intitialized to not cause error with the further function while also printing an error message