## Dependencies
import numpy as np

## Data: yearly salary in ($1000) [2025, 2026, 2027]
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer =      [118, 118, 127]
softwareEngineer = [129, 131, 137]

employees = np.array([dataScientist,
                      productManager,
                      designer,
                      softwareEngineer])

## One-liner
employees[0,::2] = employees[0,::2] * 1.1
#this means the new employees variable will change by taking the first index' all rows,columns every other element and multiply by 1.1

## Result
print(employees)



 
print(employees.dtype)
#int 32 
employees[0,::2] = employees[0,::2] * 1.1
print (employees.dtype)
#int 32, python assumes it's integer

#this code reviews slicing, slice assignment, and broadcasting.
