import math


print("\nUnary Quadratic Equations Calculator v1.1\n")
print("If you want to exit,Please press Ctrl+C.")

n=1
while n==1 :
	#Give tip.
	print("\nax²+bx+c=0")
	
	#Input "a b c" values.
	a=input("a=")
	b=input("b=")
	c=input("c=")
	
	try :
		#Check solves.
		d=float(b)**2-float(a)*float(c)*4
	
		if (d<0) :
		    print("The equation is unbale to solve.")
	
		#Calculate solves.
		else :
			x1=((-float(b))+math.sqrt(d))/(float(a)*2)
			x2=((-float(b))-math.sqrt(d))/(float(a)*2)
		
		    	#Output solves.
			print("x1=",x1)
			print("x2=",x2)

	#Error tips.
	except ValueError :
		print("You seems to have input a wrong number,Please check you number if it's wrong and reinput a correct number and try again.")
	
	except :
		print("It seems have some error,Please check you input or operations or the code if it is wrong and try again.")
