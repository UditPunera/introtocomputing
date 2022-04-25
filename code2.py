#Q2
Gross_Income=float(input('Gross Income='))
N=int(input('number of dependents='))
t = Gross_Income - 10000 - (N*3000)
if t>0:
  print('Taxable Income',t)
  tax= t*0.2
  print("income tax=",tax)

else:
    print("zero tax")
