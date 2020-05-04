from lib.db_manager import db_manager
from lib.settings import *

lm = db_manager(HOST, USERNAME, PASSWORD)
lm.menu()
