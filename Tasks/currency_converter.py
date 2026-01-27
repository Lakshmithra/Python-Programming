import requests
url = "https://api.exchangerate-api.com/v4/latest/USD"
data = requests.get(url)
if data.status_code != 200:
    print("Error ! Data couldn't be retrieved !")   
else:
    datadict = data.json()
    currencylist = list(datadict["rates"].keys())
    print("\nAvailable currencies : \n",currencylist)  
    while True:
          fromcurrency = input("\nEnter the currency you have : ").upper()
          if fromcurrency not in datadict["rates"]:
                print("Invalid ! Enter a valid currency !")
          else:
                break
    while True:
            tocurrency = input("\nEnter the currency you want to convert it to : ").upper()
            if tocurrency not in datadict["rates"]:
                  print("Invalid ! Enter a valid currency !")
            else:
                  break            
    amount = int(input("\nEnter the amount : "))
    
    fromrate = datadict["rates"][fromcurrency]
    torate = datadict["rates"][tocurrency]
    
    converted_amount = amount * (torate / fromrate)
    converted_amount = round(converted_amount , 2)
    
    print("\nConverted amount from {} to {} : {}".format(fromcurrency , tocurrency , converted_amount))
