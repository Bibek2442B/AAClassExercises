import numpy as np

personsNames=np.array(['Paulo','Ana','Maria','Luis','Marco','Patricia','Magda', 'Jorge', 'Martins', 'Castro'])
personHeight=np.array(np.random.randint(50,101,10))
personWeight=np.array(np.random.randint(150,201,10))
data=np.array([personHeight,personWeight])

print(personsNames)
print(data)

##Exercise 10b
bmi=data[0,:]/(data[1,:]/100)**2

print(bmi)

# Exercise 10c
# determine the category of BMI

def cat(i):
    if i < 18.5:
        return 'Low'
    elif i > 25:
        return 'High'
    else:
        return 'Ideal'

print(personsNames)
print(data)

print(np.round(bmi,1))

print(list(map(cat, bmi)))

# organize the print by categories

print('Low', personsNames[bmi < 18.5])
print('High', personsNames[bmi > 25])
print('Ideal', personsNames[(bmi >= 18.5) & (bmi <= 25)])

# Exercise 10d
ascending_bmi=bmi.argsort()
print(ascending_bmi)

print(personsNames[ascending_bmi])
print(data[0,ascending_bmi])
print(data[1,ascending_bmi])

print(np.round(bmi[ascending_bmi],1))

for i in ascending_bmi:
    print(personsNames[i])
    print(data[0,i])
    print(data[1,i])
    print(np.round(bmi[i],1))


#or
for i in ascending_bmi:
    print(f'{personsNames[i]}')
    print(f'Weight: {data[0,i]}Kg, Height: {data[1,i]}cms, BMI: {np.round(bmi[i],1)}')
    print()

# Exercise 10e

sd=data.std(axis=1)
print(sd)

print(f'Standard Deviation of weights = {round(sd[0],1)}')
print(f'Standard Deviation of weights = {round(sd[1],1)}')

#Exercise 10f

weights_mean = data.mean(axis=1)[0]

print(weights_mean)
print(data[0,:].mean())

print(data[0,:])

print(data[0,:]>data[0,:].mean())
print('Persons with Overweight: ', personsNames[data[0,:]>data[0,:].mean()])