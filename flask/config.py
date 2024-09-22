import urllib

class Config():
    SECRET_KEY = 'some secret key'
    params = urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-79EIPER\\SQLEXPRESS;DATABASE=login_page_db;Trusted_Connection=yes')
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" %params
    SQLALCHEMY_TRACK_NOTIFICATIONS = False