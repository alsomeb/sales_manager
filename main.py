from sales import Sales, SalesManager


manager = SalesManager()



while True:
    country_name = input("Country name: ").title()
    prio = input("Order Priority (HCLM): ").upper()
    print("\n")
    res = manager.GetRows(country_name, prio)

    # Lägger in objekten
    for row in res:
        res = row.split(",")
        manager.addSale(res[0],res[1],res[2],res[3],res[4],res[5],res[6],res[7],res[8],res[9],res[10],res[11],res[12],res[13])
    print(f"Total Revenue: {round(manager.calcTotalRevenue(), 2)}")
    print(f"Total Cost: {round(manager.calcTotalCost(), 2)}")
    print(f"Total Profit: {round(manager.calcTotalProfit(), 2)}")
    print("\n")
