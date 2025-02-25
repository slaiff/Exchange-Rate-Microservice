# Exchange-Rate-Microservice
## Description
This micro-service reports back a currency's exchange rate in terms of United States Dollars. The service allows for a calling program to send a desired currency, such as MXN (Mexican Peso), in which case the service will respond back with the exchange rate of 1 USD to X MXN Pesos. 
### Additional Important Information / Instructions
- The microservice communicates back to a calling program via .txt files. The name of the used textfile may be modified within the microservice.
- The microservice awaits a keyword within said textfile, by default, this keyword is "go" (can be changed). This keyword **must** exist on the first line of the used text file, on it's own. 
- Upon receival of keyword, the main program begins and reads the next line of the file, line[1] for the 3-Char keyname for the currency, ie. MXN, GBR, etc.
- Upon completion, the same textfile will be truncated/overwritten. The first line will contain "done" to indicate to the ***calling*** program that the microservice is done.
- The ***calling*** program can expect the rate of USD to X Requested Currency to be populated on the second line (line[1]) of the file. 
## Requires
- Use of text file communication.
- Python 'Time' Library, or similar for other languages. 
## Requests to the Exchange-Rate-Microservice
  1. User should run the microservice, it will **wait** for a keyword on line 0 of the text file. This keyword should be written to file by the main/calling program.
## Receiving data from the Exchange-Rate-Microservice 
  3. The ***calling*** program should wait for a completion keyword (default = "done"), upon receival of this, it may extract the exchange rate from file for use.
## Example Call for ***Requesting*** (in Python)

  ![image](https://github.com/user-attachments/assets/14093f38-abe2-4542-8194-9cfde794ce11)

## Example call for ***Receiving*** data (in Python)

  ![image](https://github.com/user-attachments/assets/464677c0-468e-4da4-bfb9-70f775dfdf04)

## UML Sequence Diagram

  
