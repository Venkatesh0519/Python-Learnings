#Usage of default arguments *args and **kwargs in python

def student(name,age,*marks):
    print(type(marks))
    print("name:",name)
    print("age:",age)
    #print("marks: ",marks)
    for x in marks:
        print(x)
student('Venky',22,90,80,70,60)
#In the above program i used three parameters name,age,and marks.
#If you simply gives marks and print its gives "student() takes 3 positional arguments but 6 were given"
#So inorder to over come it we use '*' notation this means you can provide multiple arguments.
#If you use single '*' the values are given in the form of 'Tuples'

#--------------------------------------------------------------------------------------------------------------#
#In the above program i just gave only marks so in the below program i am going to give subjects to those marks
#So to do this **kwargs comes into picture
def student(name,age,**marks):
    print("name:",name)
    print("age:",age)
    print("marks:",marks)
    for i,j in marks.items():
        print(i,':',j)
student('Venky',22,Maths=90,English=80,Physics=70,Chemistry=60)
#**kwargs is similar to dictionaries where as it contains key and value pairs as arguments
#In the above program i is key and j is value.
#whenever if we use the double '**' the values are given in the form of dictionaries in output



