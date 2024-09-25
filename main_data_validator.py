import sys
import data_validator

if len(sys.argv) != 2:
    print("Usage: python data_validator.py DD.MM.YYYY")
sys.exit(1)

data_input = sys.argv[1]

if data_validator.is_valid_data(data_input):
    print("True")
else:
    print("False")