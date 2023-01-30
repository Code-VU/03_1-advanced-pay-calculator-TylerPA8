def calculatePay():
    # This first line is provided for you
    hrs = input("Enter Hours:")
    try:
        hrs = float(hrs)
    except:
        print("Error, please enter numeric input")
        return
    rate = input("Enter Rate:")
    try:
        rate = float(rate)
    except:
        print("Error, please enter numeric input")
        return
    over_rate = rate*1.5
    pay = 0
    if hrs > 40:
        pay = rate*40
        pay += (hrs-40)*over_rate
    else:
        pay = rate*hrs
    print("Pay: " + str(pay))
    
    # end assignment

## if you want to test locally before you try to sync
## run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
