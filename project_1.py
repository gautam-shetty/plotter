from tkinter import*
import tkinter.messagebox
def result(ex):
	try:
		if ex<0:
			data="The given equation is STRAIGHT LINE!"
		elif ex==0:
			data="The given equation is CIRCLE!"
		elif (ex>0)&(ex<1):
			data="The given equation is HYPERBOLA!"
		elif ex==1:
			data="The given equation is PARABOLA!"
		else:
			data="The given equation is ELLIPSE!"
		return data
	except Exception as f:
		error="Uable to solve the Equation!"
		return error
def body():
	try:
		A=int(eval(e1.get()))
		B=int(eval(e2.get()))
		C=int(eval(e3.get()))
		D=int(eval(e4.get()))
		E=int(eval(e5.get()))
		F=int(eval(e6.get()))
		X=[[A,B/2,D/2],[B/2,C,E/2],[D/2,E/2,F]]
		dete_X=det(X)
		if dete_X<0:
			n=1
		elif dete_X==0:
			n=2
		else:
			n=-1
		ex=ecc(A,B,C,D,E,F,n)
		#print("Eccentricity = ",ex)
		Disp=result(ex)
	except Exception as e:
		Disp="Input all entries!"
	tkinter.messagebox.showinfo('Result',Disp)
def det(X):
	P=X[0][0]*((X[1][1]*X[2][2])-(X[1][2]*X[2][1]))
	Q=X[0][1]*((X[1][0]*X[2][2])-(X[1][2]*X[2][0]))
	R=X[0][2]*((X[1][0]*X[2][1])-(X[1][1]*X[2][0]))
	return P-Q+R
def ecc(A,B,C,D,E,F,n):
	num=2*((((A-C)**2)+(B**2)))**0.5
	den=n*(A+C)+(((A-C)**2)+(B**2))**0.5
	e=(num/den)**0.5
	return e
master=Tk()
master.title("Application - Gautam Shetty")
master.resizable(width=False,height=False)
try:
	Label(master,text=" EQUATION: Ax^2+Bxy+Cy^2+Dx+Ey+F=0 ").grid(row=0,column=0,columnspan=2,sticky=W+E)
	Label(master,text="A :").grid(row=1,column=0,sticky=E)
	e1=Entry(master)
	e1.grid(row=1,column=1)
	Label(master,text="B :").grid(row=2,column=0,sticky=E)
	e2=Entry(master)
	e2.grid(row=2,column=1)
	Label(master,text="C :").grid(row=3,column=0,sticky=E)
	e3=Entry(master)
	e3.grid(row=3,column=1)
	Label(master,text="D :").grid(row=4,column=0,sticky=E)
	e4=Entry(master)
	e4.grid(row=4,column=1)
	Label(master,text="E :").grid(row=5,column=0,sticky=E)
	e5=Entry(master)
	e5.grid(row=5,column=1)
	Label(master,text="F :").grid(row=6,column=0,sticky=E)
	e6=Entry(master)
	e6.grid(row=6,column=1)
	Button(master, text='Show',command=body, fg='white', bg='green').grid(row=7,column=0,columnspan=2,sticky=W+E)
	Button(master, text='Quit',command=quit, fg='white', bg='red').grid(row=8,column=0,columnspan=2,sticky=W+E)
	master.mainloop()
except Exception as e:
	print(e)