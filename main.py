#imports 
import requests #provides library functions to request data from API's
import time     #provides functions like sleep()

#globals
apiKey   = "https://api.exchangeratesapi.io/v1/latest?access_key=df37d056ef6f5582fa076874030e0943"
fileName = "middleMan.txt"

#Fetches rate desired by user
def fetchRate(desiredRate):
    #attempt request to API and validate it was successful
    fetch = requests.get(apiKey) 
    if fetch.status_code != 200: #200 indicates a successful get
        print(f"Request to API failed, status code {fetch.status_code}")
    else: #success
        #store the json data
        data = fetch.json()
        #Get USD's Current Rate (if it exists)
        currUSD = "USD"
        if currUSD in data["rates"]:
            currUSD = data["rates"][currUSD]
            print(f"Current EURO to USD is : {currUSD} USD") #check 
            #See if user's desired rate exists within API
            if desiredRate in data["rates"]:
                    #write to file - FIXME
                    rate = data["rates"][desiredRate]
                    rate /= currUSD
                    rate = round(rate, 2)
                    #print(f"1 USD is {rate} {desiredRate}")
                    #Reopen the file, and write
                    outfile = open(fileName, "w")   #open file for writing
                    outfile.write("done\n")
                    outfile.write(str(rate))
                    print(f"The exchange rate for 1 USD to {desiredRate} is {rate} and has been written to file\n")
                    outfile.close()
                    
            else:
                    print("Your rate couldnt be found, sorry.")
        else:
            print("Could not locate USD...something is defintiely wrong")

#Opens file, checks for listening key on loop, once found-
#-snags desiredCurrency and uses in fetchRate()
def openFile():
    #Variables
    key = ""   #init an empty key
   
    #loops until the file contains the key
    while key != "go":
        time.sleep(1) #sleep 1 sec per loop
        elementsInFile = []  #define a list - must be done each loop to preserve logic
        with open(fileName, 'r') as file:   #opens file & ensures closing in all-cases
            for line in file:
                aCleanedLine = line.strip()             #each line is stripped of whitespace, \n, etc, stored into var
                elementsInFile.append(aCleanedLine)     #append var item into the list
        #after loop, see if "go" is ready
        if elementsInFile and elementsInFile[0] == "go":            #check elementsInFile exists/is populated, then see if index 0 is "go"
            if len(elementsInFile) > 1 and elementsInFile[1]:       #If so, check the list has more than 1 element, & that [1] is not empty/un-init
                key = elementsInFile[0]
                desiredRate = elementsInFile[1].upper()
                #call fetchRate()
                fetchRate(desiredRate)
              
            
#define main program
def main():
    openFile()
 

#call main / all other needs funcs
main()