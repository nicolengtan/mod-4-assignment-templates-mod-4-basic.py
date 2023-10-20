'''Module 2: Individual Programming Assignment 1

Useful Business Calculations

This assignment covers your basic proficiency with Python.
'''

def savings(gross_pay, tax_rate, expenses):
    '''Savings.
    2 points.

    This function calculates the money remaining
        for an employee after taxes and expenses.
    
    To get the take-home pay of an employee, we will
        follow the following process:
        1. Apply the tax rate to the gross pay of the employee; round down
        2. Subtract the expenses from the after-tax pay of the employee

    Parameters
    ----------
    gross_pay: int
        the gross pay of an employee for a certain time period, expressed in centavos
    tax_rate: float
        the tax rate for a certain time period, expressed as a number between 0 and 1 (e.g., 0.12)
    expenses: int
        the expenses of an employee for a certain time period, expressed in centavos

    Returns
    -------
    int
        the number of centavos remaining from an employee's pay after taxes and expenses
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
  
-------

import math

def savings(gross_pay, tax_rate, expenses):
  if 0 <= tax_rate <= 1:
    deduction = math.floor(gross_pay * tax_rate)
    tax_paid = gross_pay - deduction
    remaining_savings = tax_paid - expenses
    return remaining_savings

gross_pay = int(input("Enter employee's Gross Pay in centavos:"))
tax_rate = float(input("Enter Tax Rate:))
expense = int(input("Enter emoloyee's Expenses amount in centavos:"))
savings_amount = savings(gross_pay, tax_rate, expenses)
print(f"Remaining Savings: {savings_amount} centavos")

-------

def material_waste(total_material, material_units, num_jobs, job_consumption):
    '''Material Waste.
    2 points.

    This function calculates how much material input will be wasted
        after running a certain number of jobs that consume
        a set amount of material.

    To get the waste of a set of jobs:
        1. Multiply the number of jobs by the material consumption per job.
        2. Subtract the total material consumed from the total material available.

    The users of this function also want you to format the output as a string, annotated with the
        units in which the material is expressed. Do not add a space between the number and the unit.

    Parameters
    ----------
    total_material: int
        the total material available
    material_units: str
        the units used to express a quantity of the material (e.g., "kg", "L", etc.)
    num_jobs: int
        the number of jobs to run
    job_consumption: int
        the amount of material consumed per job

    Returns
    -------
    str
        the amount of remaining material expressed with its unit (e.g., "10kg").
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

-------

def material_waste(total_material, material_units, num_jobs, job_consumption):
    total_consumption = num_jobs * job_consumption
    material_wasted = total_material - total_consumption
    result = f"{material_wasted} {material_units}
    return result

total_material = int(input("Enter Total Material available:"))
material_units = str(input("Enter Quantity Unit of the Material:"))
num_jobs = int(input("Enter the Number of Jobs:"))
job_consumption = int(input("Enter the Amount of Material Consumed per Job:"))
waste_result = material_waste(total_material, material_units, num_jobs, job_consumption)
print(f"Material wasted after {num_jobs} jobs: {waste_result}")

-------

def interest(principal, rate, periods):
    '''Interest.
    3 points.

    This function calculates the final value of an investment after
        gaining simple interest over a number of periods.

    To calculate simple interest, simply multiply the principal to the quantity (rate * time). 
        Add this amount to the principal to get the final value.

    Round down the final amount.

    Parameters
    ----------
    principal: int
        the principal (i.e., starting) amount invested, expressed in centavos
    rate: float
        the interest rate per period, expressed as a decimal representation of a percentage (e.g., 3% is 0.03)
    periods: int
        the number of periods invested

    Returns
    -------
    int
        the final value of the investment
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

-------

def interest(principal, rate, periods):
    final_value = int(principal * (1 + rate * periods))
    return final_value

prinicipal = int(input("Enter Prinicipal Amount in centavos:"))
rate = float(input("Enter the Interest Rate per period in decimals:"))
periods = int(input("Enter the number of Periods invested:"))
final_amount = interest(principal, rate, periods)
print(f"The final value of the investment is {final_amount} centavos")

-------

def body_mass_index(weight, height):
    '''Body Mass Index.
    3 points.

    This function calculates the body mass index (BMI) of a person
        given their weight and height.

    The formula for BMI is: kg / (m ^ 2)
        (i.e., kilograms over meters squared)

    Unfortunately, the users of this function use the imperial system.
        You will need to first convert their arguments to the metric system.
    
    Parameters
    ----------
    weight: float
        the weight of the person, in pounds
    height: list
        the height of the person, expressed as a list of two integers.
        the first integer is the foot component of their height.
        the second integer is the inches component of their height.
        for example, 5'10" would be passed as [5, 10].

    Returns
    -------
    float
        the BMI of the person.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
-------

def body_mass_index(weight, height):
    # 1 pound = 0.453592 kg
    weight_kg = weight * 0.453592
    # 1 foot = 12 inches; 1 inch = 0.0254 m
    height = feet, inches
    height_m = (feet * 12 + inches) * 0.0254
    # bmi = weight / height
    bmi = weight_kg / (height_m ** 2)
    return bmi

weight = float(input("Enter Weight in pounds:"))
feet = int(input("Enter Height in Feet component:"))
inches = int(input("Enter Height in Inch component:"))
height = [feet, inches]
bmi = body_mass_index(weight, height)
print(f"The BMI of the person is {bmi}")

-------
