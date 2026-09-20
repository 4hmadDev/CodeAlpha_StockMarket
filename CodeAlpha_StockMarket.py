stocks = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOG" : 150,
    "MSFT" : 400,
    "AMZN" : 180
}

stock_name = input("Enter the stock name: ")
quantity = int(input("Enter the stock quantity: "))

if stock_name in stocks:
  price = stocks[stock_name]
  total = price * quantity

  print("Stock Price: ", price)
  print("Quantity : ", quantity)
  print("Total Investment: ", total)

  file = open("portfolio.txt", "w")

  file.write(f"Stock Name:  {stock_name}\n")
  file.write(f"Price:  {price}\n")
  file.write(f"Quantity: {quantity}\n")
  file.write(f"Quantity: {quantity}\n")
  file.write(f"Total Investment: {total}\n")

  file.close()

  print("Result saved in portfolio.txt")

else:
  print("Stock not found")