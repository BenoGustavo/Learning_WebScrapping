import requests
import xlsxwriter
import datetime
from bs4 import BeautifulSoup

PAGE1_URL = (
    "https://www.amazon.com.br/gp/bestsellers/electronics/ref=zg_bs_electronics_sm"
)
PAGE2_URL = "https://www.amazon.com.br/gp/bestsellers/electronics/ref=zg_bs_pg_2_electronics?ie=UTF8&pg=2"


def isTheRequestValid(request: requests) -> bool:
    if request.ok:
        return True
    raise ConnectionError(request.reason)


def getProductName(requestPage1, requestPage2):
    html = BeautifulSoup(requestPage1.text, "html.parser")
    htmlPage2 = BeautifulSoup(requestPage2.text, "html.parser")

    # Getting product name
    productsNames = html.findAll("div", class_="zg-grid-general-faceout")
    productsNamesPage2 = htmlPage2.findAll("div", class_="zg-grid-general-faceout")

    # Formating text to return the array
    formatedProductsNames = []
    for names in productsNames:
        name = names.findAll("span")
        formatedProductsNames.append(name[0].text)

    for names in productsNamesPage2:
        name = names.findAll("span")
        formatedProductsNames.append(name[0].text)

    return formatedProductsNames


def getProductPrices(requestPage1, requestPage2):
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

    if isTheRequestValid(request_page1) and isTheRequestValid(request_page2):
        productsName = getProductName(request_page1, request_page2)
        productPrice = getProductPrices(request_page1, request_page2)

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

    print("Scrap Falhou")
