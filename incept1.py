
def New_Registration():
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

	first_name=input("Enter First Name Of Student:")
	second_name=input("Enter Second Name Of Student:")
	father_name=input("Enter Father's Name:")
	mother_name=input("Enter Mohter's Name:")
	contact_number=input("Enter Contact Number:")
	address=input("Enter address:")

	temp_value1=str(temp_value3)
	full_file_name=temp_value1+".txt"
	student_record=open(full_file_name,"x")
	student_record.close()
	student_record=open(full_file_name,"a")
	student_record.write("First Name: "+first_name)
	student_record.write("\nSecond Name: "+second_name)
	student_record.write("\nFather Name: "+father_name)
	student_record.write("\nMohter Name: "+mother_name)
	student_record.write("\nContact Number: "+contact_number)
	student_record.write("\nAddress: "+address)
	student_record.close()
	print("Admission Number is",(temp_value3))
	
def Old_Registration():
	temp_value1=input("Enter The Admission Number:")
	temp_value2=temp_value1+".txt"
	temp_value3=open(temp_value2,"r")
	for i in temp_value3.readlines():
		print(i)


x=int(input("Enter your choice:"))
if(x==1):
	New_Registration()
elif(x==2):
	Old_Registration()


