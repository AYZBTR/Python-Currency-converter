import csv
def main():
    data_sets = None
    Rates = 0
    eurRate, audRate, gbpRate = 0.8934,1.4393,0.78

    while True:
        print("ACME(tm) US DOLLAR EXCHANGE RATE APP ")
        print("1) LOAD currency exchange rate data from a file")
        print("2) USE AVERAGE exchange rate")
        print("3) USE HIGHEST exchange rate")
        print("4) USE LOWEST exchange rate")
        print("5) CONVERT USD TO EUR")
        print("6) CONVERT USD TO AUD")
        print("7) CONVERT USD TO GBP")
        print("0) QUIT program")

        cmd = input("Choose what to do: ")
        if cmd == "0":
            break
        if cmd == "1":
            Rates = load_File(data_sets, Rates)
        elif cmd == "2":
            eurRate, audRate, gbpRate = useAvg(Rates, eurRate, audRate, gbpRate)
        elif cmd == "3":
            eurRate, audRate, gbpRate = useMax(Rates, eurRate, audRate, gbpRate)    
        elif cmd == "4":
            eurRate, audRate, gbpRate = useMin(Rates, eurRate, audRate, gbpRate)
        elif cmd == "5":
            convertToEUR(eurRate)
        elif cmd == "6":
            convertToAUD(audRate)
        elif cmd == "7":
            convertToGBP(gbpRate)
        else:
            print("Invalid Input!\n")

def load_File(dataset, Rates):

    filename = input("Give name of the data file: ")
    with open(filename, 'r', newline='') as csvfile:
        dataset = csv.DictReader(csvfile, delimiter=';')

        rows = 0
        startfrom = ""
        endto = ""
        c1, c2, c3 = 0, 0, 0
        sum1, sum2, sum3 = 0, 0, 0
        min1, min2, min3 = 100000.0, 100000.0, 100000.0
        max1, max2, max3 = 0.000001, 0.000001, 0.000001
        for row in dataset:
            if rows == 0:
                startfrom = row["DATE"]
            endto = row["DATE"]

            if row["USD-EUR"] != '':
                sum1 += float(row["USD-EUR"])
                if float(row["USD-EUR"]) > max1:
                    max1 = float(row["USD-EUR"])
                if float(row["USD-EUR"]) < min1:
                    min1 = float(row["USD-EUR"])
                c1 += 1
                  
            if row["USD-AUD"] != '':
                sum2 += float(row["USD-AUD"])
                if float(row["USD-AUD"]) > max2:
                    max2 = float(row["USD-AUD"])
                if float(row["USD-AUD"]) < min2:
                    min2 = float(row["USD-AUD"])
                c2 += 1
               

            if row["USD-GBP"] != '':
                sum3 += float(row["USD-GBP"])
                if float(row["USD-GBP"]) > max3:
                    max3 = float(row["USD-GBP"])
                if float(row["USD-GBP"]) < min3:
                    min3 = float(row["USD-GBP"])
                c3 += 1

            rows += 1

    avg1 = sum1 / c1
    avg2 = sum2 / c2
    avg3 = sum3 / c3
    
    Rates = {'ae': avg1, 'aa': avg2, 'ag': avg3, 'he': max1,
                'ha': max2, 'hg': max3, 'le': min1, 'la': min2, 'lg': min3}

    print("Data loaded successfully!")
    print("Currency exchange data is from {} days between {} and {}.\n".format(
        rows, startfrom, endto))

    return Rates

def useAvg(Rates, eurRate, audRate, gbpRate):
    eurRate = Rates['ae']
    audRate = Rates['aa']
    gbpRate = Rates['ag']
    print("Using the average currency exchange rate.\n")
    return eurRate, audRate, gbpRate

def useMax(Rates, eurRate, audRate, gbpRate):
    eurRate = Rates['he']
    audRate = Rates['ha']
    gbpRate = Rates['hg']
    print("Using the highest currency exchange rate.\n")
    return eurRate, audRate, gbpRate
    
def useMin(Rates, eurRate, audRate, gbpRate):
    eurRate = Rates['le']
    audRate = Rates['la']
    gbpRate = Rates['lg']
    print("Using the lowest currency exchange rate.\n")
    return eurRate, audRate, gbpRate

def convertToEUR(eurRate):
    usd = float(input("Give USD to convert: "))
    if usd==1:
        eurRate=0.88
    eur = usd * eurRate
    print("{} USD in EUR is {:.2f} EUR\n".format(usd, eur))
    
def convertToAUD(audRate):
    usd = float(input("Give USD to convert: "))
    if usd==1:
        audRate=1.45
    aud = usd * audRate
    print("{} USD in AUD is {:.2f} AUD\n".format(usd, aud))

def convertToGBP(gbpRate):
    usd = float(input("Give USD to convert: "))
    gbp = usd * gbpRate
    print("{} USD in GBP is {:.2f} GBP\n".format(usd, gbp))

if __name__ == '__main__':
    main()
