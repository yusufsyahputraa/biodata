import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')  # ← ganti ke blog

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from mangum import Mangum
handler = Mangum(application)