import requests
from bs4 import BeautifulSoup
from tabulate import tabulate



def datalogger():
    try:

        response = requests.get('http://horiba:password@192.168.110.89/cgi-bin/cgi-iox/data.xml?proc=801&DateSep=%2F&DecimalSep=.&DateFormat=ymd&FieldSep=%3CTab%3E&Resolution=low&Unit=1')

        soup=BeautifulSoup(response.text, 'xml')
        nazivi=soup.find_all('comp')
        vrijednosti=soup.find_all('mean')
        jedinice=soup.find_all('unit')
        print("Vrijednosti sa data logera 192.168.110.89 sljaciste povratne vode:")
        print ("*******************")
        output=[]
        
        for i in range(0, len(nazivi)):
            red1=[]
            red1.append(nazivi[i].text)
            red1.append(vrijednosti[i].text)
            red1.append(jedinice[i].text)
            output.append(red1)
        
        head=["Naziv", "Vrijednost", "Jedinice"]
        #output.insert(0, ["Naziv", "Vrijednost", "Jedinice"])
        print (tabulate(output, headers=head, tablefmt="grid"))
        print("\n")

    except Exception as e:
        print("Error: ", e)
        print("Nije uspjelo povezivanje sa datalogerom 192.168.110.89")
        head=["Naziv", "Vrijednost", "Jedinice"]
        print (tabulate(["-" "-" "-"], headers=head, tablefmt="grid"))
        print("\n")
        
def datalogger_2():
    try:       
        response2 = requests.get('http://horiba:password@192.168.110.90/cgi-bin/cgi-iox?proc=3')

        soup2=BeautifulSoup(response2.text, 'html.parser')
        
        tablica=soup2.find(class_='data').find_all('td', id='la')
        vrijednosti=soup2.find(class_='data').find_all('td', id='ra')

        print("Vrijednosti sa data logera 192.168.110.90 HPV/povratne vode ")
        print ("*******************")

        izlaz=[]
        for i in range (0, len(tablica), 3):
            row=[]
            row.append(tablica[i].text)
            row.append(tablica[i+1].text)
            row.append(tablica[i+2].text)
            izlaz.append(row)
        for i in range(0, len(vrijednosti), 2):
            izlaz[int(i/2)].insert(2, vrijednosti[i].text)

        head2=["Lokacija", "Naziv", "Vrijednost", "Jedinica"]
        #izlaz.insert(0, ["Lokacija", "Naziv", "Vrijednost", "Jedinica"])
        print(tabulate(izlaz, headers=head2, tablefmt="grid"))
        print("\n")
       

    except Exception as e:
        print("Error: ", e)
        print("Nije uspjelo povezivanje sa datalogerom 192.168.110.90")
        head2=["Lokacija", "Naziv", "Vrijednost", "Jedinica"]
        print (tabulate(["-" "-" "-" "-"], headers=head2, tablefmt="grid"))
        print("\n")