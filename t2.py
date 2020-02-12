from tkinter import *
root=Tk()
root.title("Check")
root.geometry("1920x1080")
root.propagate(0)



f1=Frame(root,height=1920,width=1080,bg='red')
f1.pack()

n1=StringVar()
n2=StringVar()
def button():
    t1=n1.get()
    t2=n2.get()
    temp_value2=open("admission_number.txt","r")
    temp_value4=temp_value2.read(1)
    temp_value2.close()
    temp_value2=open("admission_number.txt","w")
    temp_value4=int(temp_value4)
    temp_value3=temp_value4
    temp_value4=temp_value4+1
    temp_value4=str(temp_value4)
    temp_value2.write(temp_value4)
    temp_value2.close()



    temp_value1=str(temp_value3)
    full_file_name=temp_value1+".txt"
    student_record=open(full_file_name,"x")
    student_record.close()
    student_record=open(full_file_name,"a")
    student_record.write("First Name: "+t1)
    student_record.write("\nSecond Name: "+t2)
    student_record.close()
    print("Admission Number is",(temp_value3))









l1=Label(f1,text="First Name",bg='white')
l1.place(x=180,y=30)

e1=Entry(f1,textvariable=n1)
e1.place(x=320,y=30)

l2=Label(f1,text="Last Name",bg='white')
l2.place(x=180,y=80)

e2=Entry(f1,textvariable=n2)
e2.place(x=320,y=80)


b1=Button(f1,text="Click",bg='green',command=button)
b1.place(x=310,y=300)












root.mainloop()