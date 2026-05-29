import os
from dotenv import load_dotenv


load_dotenv()


# --- База данных --- #
DB_HOST = os.environ['DB_HOST']
DB_PORT = os.environ['DB_PORT']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_NAME = os.environ['DB_NAME']




# Секретный ключ Flask #
SECRET_KEY=os.environ["SECRET_KEY"]



# --- SMTP для админки пользователей ---
SMTP_HOST = os.environ['SMTP_HOST']
SMTP_PORT = os.environ['SMTP_PORT']
SMTP_USER = os.environ['SMTP_USER']
SMTP_PASS = os.environ['SMTP_PASS']
SMTP_USE_TLS = os.environ.get('SMTP_USE_TLS', 'False').lower() in ('true', '1', 't')
SMTP_USE_SSL = os.environ.get('SMTP_USE_SSL', 'True').lower() in ('true', '1', 't')


# --- Мастер-пароль ---
ADMIN_MASTER_PASSWORD = os.environ['ADMIN_MASTER_PASSWORD']
