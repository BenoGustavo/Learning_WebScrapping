import requests
import xlsxwriter
import datetime
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.br/gp/bestsellers/electronics/ref=zg_bs_electronics_sm"


def getProductName(request):
    html = BeautifulSoup(request.text, "html.parser")

    # Getting product name
    productsNames = html.find_all("div", class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")

    # Formating product name
    formatedProductsNames = []
    for product in productsNames:
        formatedProductsName = product.text
        formatedProductsNames.append(formatedProductsName)

    return formatedProductsNames


def getProductPrices(request):
    # Getting product prices
    html = BeautifulSoup(request.text, "html.parser")

    productsPrices = html.find_all("span", class_="p13n-sc-price")

    formatedProductPrices = []
    for product in productsPrices:
        formatedProductPrices.append(product.text)

    return formatedProductPrices


if __name__ == "__main__":
    request = requests.get(URL)
    productsName = getProductName(request)
    productPrice = getProductPrices(request)

    productPricesAndNames = list(zip(productsName, productPrice))

    workbook = xlsxwriter.Workbook("BestEletronicPricesAmazon.xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.write("A1", "Date")
    worksheet.write("B1", "ProductName")
    worksheet.write("C1", "ProductPrice")
    row = 3

    for product in productPricesAndNames:
        time = current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        worksheet.write("A" + str(row), time)
        worksheet.write("B" + str(row), product[0])
        worksheet.write("C" + str(row), product[1])
        row += 1

    workbook.close()
