import os
from dotenv import load_dotenv

load_dotenv(encoding="utf-8")

XL_BASE_NAME = os.getenv("XL_BASE_NAME")
A2_DEFAULT = os.getenv("A2_VALUE")
EMPLOYEE_NAME = os.getenv("EMPLOYEE_NAME")