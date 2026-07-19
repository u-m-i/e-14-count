import ijson

TARGET = 'data/allTransmissionCodes.json'

CACHE = 'artifacts' # folder to hold up the PDFs while they are being downloaded

RESULTS = 'documents' # folder to save the JSON after analysis and lately to be processed

BASE_URL = "https://divulgacione14presidente.registraduria.gov.co/"

PDF_ENDPOINT = "assets/temis/pdf"

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