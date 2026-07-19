from scrapy.selector import Selector
from scrapy.http import HtmlResponse

BASE_URL = "https://divulgacione14presidente.registraduria.gov.co/"

PDF_ENDPOINT = "assets/temis/pdf/"

def get_pdf(department, municipality, zone, building, table, filename):

  endpoint = BASE_URL + PDF_ENDPOINT

  return f"{endpoint}/{department}/{municipality}/{zone}/{building}/{table}/PRE/{filename}"


def get_department(token: str):
    endpoint = BASE_URL + "departamentos/"

    uri = endpoint + token

    return uri


"""
Example to take a selector


Filters per page:

Department:
Municipality:
Zone:
Building:

Parent of selector: div.card container-filter card-container-g

Our target

items per building: div.card.item-table.card-mini.isAvailable.__web-inspector-hide-shortcut__


"""

endpoint = get_department("60")

site = HtmlResponse(url=endpoint, body="", encoding="utf-8")

# result = Selector(response=site).xpath("/div").getall()

result = site.css("div").getall()

print(result)


"""
Weird and not complete:

    Mesa 02 Zona 03 Puesto 01 ARAUCA
    Mesa 04 Zona 03 Puesto 01 ARAUCA
    Mesa 16 Zona 01 Puesto 02 Municipio 010 ARAUQUITA
    Mesa 01 Zona 02 Puesto 02 Municipio 010 ARAUQUITA

"""

