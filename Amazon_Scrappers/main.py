import requests
import xlsxwriter
import datetime
from bs4 import BeautifulSoup

PAGE1_URL = "https://www.amazon.com.br/gp/bestsellers/electronics/ref=zg_bs_electronics_sm"
PAGE2_URL = "https://www.amazon.com.br/gp/bestsellers/electronics/ref=zg_bs_pg_2_electronics?ie=UTF8&pg=2"

def getProductName(requestPage1,requestPage2):
    html = BeautifulSoup(requestPage1.text, "html.parser")
    htmlPage2 = BeautifulSoup(requestPage2.text, "html.parser")

    # Getting product name
    productsNames = html.find_all("div", class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
    productsNamesPage2 = htmlPage2.find_all("div", class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")

    # Formating product name
    formatedProductsNames = []
    for product in productsNames:
        formatedProductsNames.append(product.text)

    for product in productsNamesPage2:
        formatedProductsNames.append(product.text)

    return formatedProductsNames


def getProductPrices(requestPage1,requestPage2):
    # Getting product prices
    html = BeautifulSoup(requestPage1.text, "html.parser")
    htmlPage2 = BeautifulSoup(requestPage2.text, "html.parser")

    productsPrices = html.find_all("span", class_="p13n-sc-price")
    productsPrices2 = htmlPage2.find_all("span", class_="p13n-sc-price")

    formatedProductPrices = []
    for product in productsPrices:
        formatedProductPrices.append(product.text)

    for product in productsPrices2:
        formatedProductPrices.append(product.text)

    return formatedProductPrices


if __name__ == "__main__":
    request_page1 = requests.get(PAGE1_URL)
    request_page2 = requests.get(PAGE2_URL)

    productsName = getProductName(request_page1,request_page2)
    productPrice = getProductPrices(request_page1,request_page2)

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

    print("Scrap Concluido")