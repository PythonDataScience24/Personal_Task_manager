import datetime as dt

class Tasklistguardian:

    #to do but maybe its more usefull if we know which kind of input the user is able to give?
    @staticmethod
    def guardDeadline(x):
        if dt.now() > x:
            print("this is not a valid deadline")
            return 0
        else:
            return x

    @staticmethod
    def guardPriority(x):
        #guard to low and to high inputs
        if x < 0:
            return 0
        if x > 3:
            return 3
        else:
            return x
    

   
    
   
