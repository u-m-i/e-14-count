import ijson

TARGET = 'data/allTransmissionCodes.json'

CACHE = 'artifacts' # folder to hold up the PDFs while they are being downloaded

RESULTS = 'documents' # folder to save the JSON after analysis and lately to be processed

BASE_URL = "https://divulgacione14presidente.registraduria.gov.co/"

PDF_ENDPOINT = "assets/temis/pdf"

"""

Correct
https://divulgacione14presidente.registraduria.gov.co/assets/temis/pdf/60/010/000/00/001/PRE/da8a0ec5a8f7df708bae53b9ea00394738de11707aadc05b959a5444f06999e1.pdf


Incorrect
https://divulgacione14presidente.registraduria.gov.co/assets/temis/pdf/48/001/99/16/004/PRE/9824162e36b0966175731ed2ea2ba01b81d9b984254dfb06b1cd1c9b6c14e535.pdf


It does not have a carry zero in the fourth insertable slug

How to instantiate a process for each department, municipality, zone, building and table?

Instead.

- Let's gather by zone.
- Let's cache department and municipality.

Cache every department on a semi-string:

dictionary = ['48': '001', '002']

dictionary = ['48/001', '48/002']

When a department is added. We lookup for the existing one.

Get the existing code, and return the semi string.

Template: 00/000/000/00/000
Prefix of name: /PRE/
Endpoint: https://divulgacione14presidente.registraduria.gov.co/assets/temis/pdf

"""

def get_pdf(department, municipality, zone, building, table, filename):

  endpoint = BASE_URL + PDF_ENDPOINT

  return f"{endpoint}/{department}/{municipality}/{zone}/{building}/{table}/PRE/{filename}"


def by_url():

  with open(TARGET, 'r') as file:

    nodes = ijson.items(file, 'data.status3.nodes.item')

    for node in nodes:
      url = get_pdf(node['idDepartmentCode'], node['municipalityCode'], node['idZoneCode'], node['standCode'], node['numberStand'], node['expectedName'])
      print(f"[TARGET]: {url}")


def by_pdf():

  with open(TARGET, 'r') as file:

    nodes = ijson.kvitems(file, 'data.status3.nodes.item')

    artifacts = (v for k,v in nodes if k == 'expectedName')

    for artifact in artifacts:
      print(f"[PDF]: {artifact}")

by_url()