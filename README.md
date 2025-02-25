# Exchange-Rate-Microservice
## Description
This micro-service reports back a currency's exchange rate in terms of United States Dollars. The service allows for a calling program to send a desired currency, such as MXN (Mexican Peso), in which case the service will respond back with the exchange rate of 1 USD to X MXN Pesos. 
### Additional Important Information
The microservice communicates back to a calling program via .txt files. The name of the used textfile may be modified within the program.
The microservice awaits a keyword within said textfile, by default, this keyword is "go" (can be changed). This keyword **must** exist on the first line of the used text file, on it's own. 
Upon receival of keyword, the main program begins and reads the next line of the file, line[1] for the 3-Char keyname for the currency, ie. MXN, GBR, etc. 
## Requires
None?
## Requests to the Exchange-Rate-Microservice (ERM)
  1. User should run the microservice, it will **wait** for a keyword on line 0 of the text file. 
