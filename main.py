# Based on project 5, and using the formula KE = (1/2)mv2, we will now calculate the kinetic energy of a moving object based on its mass and velocity:

# Input the mass (in kilograms) and velocity (in meters per second)
massString = input("What is an object's mass in kilograms? ")
velocityString = input("What is an object's velocity in meters per second? ")

mass = int(massString)
velocity = int(velocityString)

# Compute the object’s kinetic energy using the formula:
# Kinetic energy = (1/2) * mass * (velocity squared)	(v2)
kineticEnergy =  (1/2) * mass * (velocity ** 2)

# Compute the object’s momentum using the formula:
# Momentum = mass * velocity
momentum = mass * velocity

# Print the kinetic energy and the momentum
print("The object has a kinetic energy of " + str(kineticEnergy) + " and a momentum of " + str(momentum) + ".")