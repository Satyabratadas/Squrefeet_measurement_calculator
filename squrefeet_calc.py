# Its a Calculator to measure the square feet area  of any type land



user = "yes"
while(user == "yes"):
    def measurement(a):
        if (a == 1):
            x = int(input("Enter the value of length in feet : "))
            y = int(input("enter the value of length in inch : "))
            m = int(input("Enter the value of bredth in feet : "))
            n = int(input("Enter the value of bredth in Inch : "))

            show = int(input("Choose \n 1:Get original value \n 2:Get approx value : "))
            if (show == 1 ):
                l = (x+(y/12))
                b = (m+(n/12))
                a = (l*b)
            else:
                l = (x+(y//12))
                b = (m+(n//12))
                a = (l*b)

            return a
        if (a == 2):
            x = int(input("Enter the value of length in feet : "))
            y = int(input("enter the value of length in inch : "))

            show = int(input("Choose \n 1:Get original value \n 2:Get approx value : "))
            if (show == 1 ):
                s = (x+(y/12))
                a = (s*s)
            else:
                s = (x+(y//12))
                a = (s*s)
           
            return a
        if (a == 3):
            x = int(input("Enter the value of base in feet : "))
            y = int(input("enter the value of base in inch : "))
            p = int(input("enter the value of height in feet : "))
            q = int(input("enter the value of height in inch : "))

            show = int(input("Choose \n 1:Get original value \n 2:Get approx value : "))
            if (show == 1 ):
                b = (x+(y/12))
                h = (p+(q/12))
                a = ((1/2)*b*h)
            else:
                b = (x+(y//12))
                h = (p+(q//12))
                a = ((1//2)*b*h)

            return a
        if (a == 4):
            x = int(input("Enter the value of diameter in feet : "))
            y = int(input("enter the value of diameter in inch : "))
            R = (x+(y/12))
            r = R/2
            show = int(input("Choose \n 1:Get original value \n 2:Get approx value : "))

            if (show == 1 ):
                a = ((22/7)*(r*r))
            else:
                a = ((22//7)*(r*r))
            
            return a
        if (a == 5):
            x = int(input("Enter the value of diameter in feet : "))
            y = int(input("enter the value of diameter in inch : "))
            R = (x+(y/12))
            r = R/2
            show = int(input("Choose \n 1:Get original value \n 2:Get approx value : "))
            if (show == 1 ):
                a = ((22/7)*(r*r))/2
            else:
                a = ((22//7)*(r*r))//2
            
            return a




    if __name__ == "__main__":
        print("Land Squrefeet Measurement")
        a = int(input("Choose \n 1:Rectangle , 2:Square , 3:Triangle , 4:Circle , 5:Semi-circle :-"))
        print("Area is ",measurement(a),"Square feet")
    user = input("enter yes to continue:  ")