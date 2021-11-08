from os import replace


class Sales:

    def __init__(self, region, country, itemType, salesChannel, orderPrio, orderDate, orderId,
    shipDate, unitsSold, unitPrice, unitCost, totalRevenue, totalCost, totalProfit ) -> None:
        self._region = region
        self._country = country
        self._itemType = itemType
        self._salesChannel = salesChannel
        self._orderPrio = orderPrio
        self._orderDate = orderDate
        self._orderId = orderId
        self._shipDate = shipDate
        self._unitsSold = unitsSold
        self._unitPrice = unitPrice
        self._unitCost = unitCost
        self._totalRevenue = totalRevenue
        self._totalCost = totalCost
        self._totalProfit = totalProfit
    
    def getCountry(self)->str:
        return self._country

    def getOrderPrio(self)->str:
        return self._orderPrio

    def getTotalRevenue(self)->str:
        return self._totalRevenue

    def getTotalCost(self)->str:
        return self._totalCost

    def getTotalProfit(self)->str:
        return self._totalProfit



class SalesManager:
    
    def __init__(self) -> None:
        self._lista_med_sales:list[Sales] = []


    def addSale(self, region, country, itemType, salesChannel, orderPrio, orderDate, orderId, shipDate, unitsSold, unitPrice, unitCost, totalRevenue, totalCost, totalProfit):
        self._lista_med_sales.append(Sales(region, country, itemType, salesChannel, orderPrio, orderDate, orderId, shipDate, unitsSold, unitPrice, unitCost, totalRevenue, totalCost, totalProfit))

    def GetRows(self, country:str, prio:str)->list[str]:
        list_of_results:list = []
        with open("100 sales Records.csv", "r") as csv_file:
            for row in csv_file:
                if country in row:
                    listan = row.split(",")
                    if listan[4].startswith(prio):
                        list_of_results.append(row)
                        list_of_results[-1] = list_of_results[-1].strip() #Tar bort \n
        return list_of_results

    def calcTotalRevenue(self)->float:
        summa = 0
        for sale in self._lista_med_sales:
            summa = summa + float(sale.getTotalRevenue())
        return summa

    def calcTotalCost(self)->float:
        summa = 0
        for sale in self._lista_med_sales:
            summa = summa + float(sale.getTotalCost())
        return summa

    def calcTotalProfit(self)->float:
        summa = 0
        for sale in self._lista_med_sales:
            summa = summa + float(sale.getTotalProfit())
        return summa

    
