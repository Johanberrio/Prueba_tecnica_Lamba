from celery import shared_task
import requests
from .models import Document
from django.core.files.base import ContentFile

@shared_task
def download_document():
    url = 'https://www.dane.gov.co/files/operaciones/PM/anex-PM-TotalNacional-2023.xlsx'
    response = requests.get(url)

    if response.status_code == 200:
        document = Document()
        document.file.save('estadisticas_pobreza.pdf', ContentFile(response.content))
        document.save()
        print("Document saved correctly")
    else:
        print("Error downloading document")
