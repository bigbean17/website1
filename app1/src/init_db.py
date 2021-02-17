
from views.database import init_db as id

try:
    id()
    print("finish")
except Exception as e:
    print(e)

