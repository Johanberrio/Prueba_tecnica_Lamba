import os
import sys
import django

# Adding the project directory to the system path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Setting up the Django environment to access models and configurations
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')  


# Initi the Django application
django.setup()

from users.models import Document

# Adding the backend_app directory to the system path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'backend_app')))

import requests
from django.core.files.base import ContentFile


url = 'https://www.dane.gov.co/files/operaciones/PM/anex-PM-TotalNacional-2023.xlsx'

# Make the request to download the document
response = requests.get(url)
print(response)
if response.status_code == 200:
    # Save document into database
    document = Document()
    document.file.save('estadisticas_pobreza.xlsx', ContentFile(response.content))
    document.save()
    print("Document saved successfully")
else:
    print("Error downloading the document")
