# Income Statement Calculator

'''Designed to help calculate and store various income statement data using inputs from the user.'''

# Import Libraries
import datetime as dt


# Define Income Statement Functions

def companyname(cn):
    while True:
        try:
            cn = str(cn)
            print(cn)
            return cn
        except Exception as e:
            print("Invalid input try again!\n")
            print(e)
            cn = input("What Company you would like to analyse? ")
            continue

def period(p):
    print(p)
    return p

def sales(s):
    while True:
        try:
            s = int(s)
            print(s)
            return s
        except Exception as e:
            print("Invalid entry! Please use integers only, no commas!\n")
            print(e)
            s = input("\nWhat is the total sales or revenue for period in millions? ")
            continue


def costofsales(cogs):
    while True:
        try:
            cogs = int(cogs)
            print(cogs)
            return cogs
        except Exception as e:
            print("Invalid entry! Please use integers only, no commas!\n")
            print(e)
            cogs = input("\nWhat is the Cost of Goods Sold for period in millions? ")
            continue

def grossmargin(gm):
    try:
        print("\nGross Margin =",gm)
        return gm
    except Exception as e:
        print("An Error has occurred! Please double check you numbers and try again!\n")
        print(e)
        pass

def grossmarginpercent(gmp):
    try:
        print("\nGross Margin Percentage =",gmp)
        return gmp
    except Exception as e:
        print("An Error has occurred! Please double check you numbers and try again!\n")
        print(e)
        pass

def operatingexpenses(opx):
    while True:
        try:
            opx = int(opx)
            print(opx)
            return opx
        except Exception as e:
            print("Invalid entry! Please use integers only, no commas!\n")
            print(e)
            opx = input("\nWhat is the total Operating Expenses for period in millions? ")
            continue

def operatingincome(oi):
    while True:
        try:
            print("\nOperating Income =", oi)
            return oi
        except Exception as e:
            print("An Error has occurred! Please double check you numbers and try again!\n")
            print(e)
            pass

def operatingmargin(om):
    while True:
        try:
            print("\nOperating Income Margin =", om)
            return om
        except Exception as e:
            print("An Error has occurred! Please double check you numbers and try again!\n")
            print(e)
            pass

def otherincomeandexpenses(oix):
    while True:
        try:
            oix = int(oix)
            print(oix)
            return oix
        except Exception as e:
            print("Invalid entry! Please use integers only, no commas!\n")
            print(e)
            oix = input("\nWhat other Non Operating Income and or Expenses were accrued for period in millions? ")
            continue

def taxes(t):
    while True:
        try:
            t = int(t)
            print(t)
            return t
        except Exception as e:
            print("Invalid entry! Please use integers only, no commas!\n")
            print(e)
            t = input("\nHow much were Income Taxes for period in millions? ")
            continue

def netincome(ni):
    while True:
        try:
            print("\nNet Income =", ni)
            return ni
        except Exception as e:
            print("An Error has occurred! Please double check you numbers and try again!\n")
            print(e)
            pass

def netprofitmargin(np):
    while True:
        try:
            print("\nNet Profit Margin Percentage =", np)
            return np
        except Exception as e:
            print("An Error has occurred! Please double check you numbers and try again!\n")
            print(e)
            pass

def readinfile():
    with open("IncomeStatementCalculator.txt", "r+") as f:
        read_file = f.read()
        print(read_file)


# Collect Inputs from user
readinfile() # Begin program by reading in file.

cn = companyname(input("What Company you would like to analyse? ")).title()

p = period(input("\nWhat Period does this statement pertain to? i.e MM/DD/YYYY "))

s = sales(input("\nWhat is the total Sales or Revenue for period in millions? "))

cogs = costofsales(input("\nWhat is the Cost of Goods Sold for period in millions? "))

gm = s - cogs # Calculate Gross Margin

gmp = round(gm / s,2) # Calculate Gross Margin Percent

opx = operatingexpenses(input("\nWhat is the total Operating Expenses for period in millions? "))

oix = otherincomeandexpenses(input("\nWhat other Non Operating Income and or Expenses were accrued for period in millions? "))# Add input for other income and expenses.

oi = gm - opx # Calculate Operating Income

om = round(oi / s,2) # Calculate operating income or EBIT, Earnings Before Interest and Tax

t = taxes(input("\nHow much were Income Taxes for period in millions? "))

ni = oi + oix - t

np = round(ni / s,2) # Calculate Net Profit Margin Percentage


# Print Summary of Calculations

print("\t\tAll values are in millions! Except for the percentages!")

grossmargin(gm)

grossmarginpercent(gmp)

operatingincome(oi)

operatingmargin(om)

netincome(ni)

netprofitmargin(np)

print("\n")


# Create Income Statement list of headers
income_statement_list_headers = ["Company_Name","Period","Gross_Margin","Gross_Margin_Percent","Operating_Income","Operating_Margin_Percent","Net_Income","Net_Profit_Margin_Percentage"]
print(income_statement_list_headers)

# Create Income Statement list
income_statement_list = [cn,p,gm,gmp,oi,om,ni,np]
print(income_statement_list)


def savetofile(income_statement_list):
    try:
        with open("IncomeStatementCalculator.txt", "a") as f:
            for item in income_statement_list:
                item = str(item)
                f.write(item)
                f.write(",")
            f.write("\n")
            print("Inputs saved to file!")
    except Exception as e:
        print("Inputs not saved to file!")
        print(e)

savetofile(income_statement_list)

# Create Menu Options


# if (choice.strip() == "1"):
#
# elif (choice.strip() == "2"):
#
# elif (choice.strip() == "3"):
#
# elif (choice.strip() == "4"):
#     break # exit programm



# Run Relevant calculations
