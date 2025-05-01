import os
import datetime
from django.conf import settings
import subprocess

def sauvegarder_base_de_donnees():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = os.path.join(settings.BASE_DIR, 'backups')
    os.makedirs(backup_dir, exist_ok=True)
    backup_file = os.path.join(backup_dir, f'backup_{timestamp}.sql')
    
    # Commande pg_dump pour PostgreSQL
    commande = f'pg_dump -U {settings.DATABASES["default"]["USER"]} -h {settings.DATABASES["default"]["HOST"]} {settings.DATABASES["default"]["NAME"]} > {backup_file}'
    subprocess.run(commande, shell=True, env={'PGPASSWORD': settings.DATABASES['default']['PASSWORD']})
    print(f"Sauvegarde effectuée : {backup_file}")

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quincaillerie.settings')
    import django
    django.setup()
    sauvegarder_base_de_donnees()