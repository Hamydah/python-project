# project code

# program display to user
program_abilities = ("\n1.Draw a scatter plot" +
                     "\n2.Find correlation coefficient (r),coefficient of determination and comment on it")

print("This program can :" + program_abilities)

# taking input for data from the user
print("\nPlease input data then choose what do you want to calculate")

# adding a note to user to maintain program speed and also to avoid error
print("\nNote: "+
      "\ni- Do not exceed 'n' from 20."+
      "\nii- 'n' should be an integer"+
      "\niii- Don't type an alphabet!!")

# input for no. of obervations
n = no_of_observations = int(input("\nEnter no. of observations(n):  \nn = "))

# note regarding values of x and y
print("\nNote regarding values of x and y: "+
      "\n\ni- value can be integer or float."+
      "\nii- Don't enter an alphabet.")

# take input for n values of x
x = []
print("\nEnter values of x: ")
for i in range(0,n):
    print("\nEnter value at index", i , ":")
    x_value = float(input())
    x.append(x_value)

print("\nx =",x)

# take input for n values of y
y = []
print("\nEnter values of y: ")
for i in range(0,n):
    print("\nEnter value at index", i , ":")
    y_value = float(input()) 
    y.append(y_value)

print("\ny =",y)

# storing scatter plot in a function  
def scatter_plot():         
    import matplotlib.pyplot as plt
    """plotting points as a scatter plot"""
    plt.scatter(x,y, label= "points" ,color = "red",
                marker = "*", s=150)
    """x-axis label"""
    plt.xlabel = ('x-axis')
    """y-axis label"""
    plt.ylabel = ('y-axis')
    """plot title"""
    plt.title('Scatter plot!')
    """showing legend"""
    plt.legend()    
    """function to show the point"""
    plt.show()

# formula for correlation coefficient "r"
r = ("[n(∑ xy)-(∑ x)(∑ y)] / [(n∑ (x^2)-(∑ x)^2)(n∑ (y^2)-(∑ y)^2)]")

# storing formula of correlation coefficient & coefficient of detemination in a function 
def correlation_coeffiecint():   
    """finding ∑ x"""
    sum_x = sum(x)
    """finding ∑ y"""
    sum_y = sum(y)
    """finding ∑ xy"""
    xy = list(x[i]*y[i] for i in range(len(x)))
    sum_xy = sum(xy)
    """finding ∑ (x^2)"""
    x2 = list(x[i]**2 for i in range(len(x)))
    sum_x2 = sum(x2)
    """finding ∑ (y^2)"""
    y2 = list(y[i]**2 for i in range(len(y)))
    sum_y2 = sum(y2)
    """now calculate "r"""
    calculation_r = ((n*sum_xy)-(sum_x*sum_y))/(((n*sum_x2)-(sum_x**2))*((n*sum_y2)-(sum_y**2)))
    """when user willing to find correlation coefficient (r)"""
    print("\nFormula for correlation coefficient:"+
          "\nr = ",r)
    print("\n∑ x =", sum_x)
    print("\n∑ y =", sum_y)
    print("\n∑ xy =", sum_xy)
    print("\n∑ (x^2) =", sum_x2)
    print("\n∑ (y^2) =", sum_y2)
    print("\ncorrelation coefficient 'r' =",calculation_r)    
    """calculating coefficient of determination"""
    r2 = calculation_r**2   
    print("\ncoefficient of determination 'r^2'=",r2)
    if (r2*100) == 0 :
        print("\nComment on coefficient of determination:"+
              "\n\tno relation between x and y.")
    elif (r2*100) == 1 :    
        print("\nComment on coefficient of determination:"+
              "\n\tvariation in y totally depends on x.")
    elif 1 > (r2*100) > 0 :
        print("\nComment on coefficient of determination:"+
              "\n\n\t", r2*100 , "% of the variation in y can be explained by x.")

# note regarding choosing option from the list
print("\nNote :"+
      "\nPlease choose a option given at the start of program.")

# store options in a function
def option():
    """now ask user to choose from the given options what to calculate"""
    option_1 = input("\nType '1' OR '2' for the respective option: ")
    """when user willing to draw a scatter plot"""       
    if option_1 == "1":
        scatter_plot()
        second()      # asking user after executing program one time that he wants to continue or not
    elif option_1 == "2":
        correlation_coeffiecint()
    else:
        print("\nError!!!"+
              "\nPlease read the instructions carefully")

def second(): 
    """ask user if he wants to continue or quit the program"""
    option_2 = input("\nDo you want to continue?"+
                     "\nType (y) for 'Yes' OR (n) for 'No': ")
    if option_2 == "y":
        option()
    else:
        print("\nProgram End")

# calling functions
option()
second()
