## Read files with pandas
import pandas as pd

# Load spreadsheet: xl
xl = pd.ExcelFile(file)

# Print sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name
df1 = xl.parse('2004')

# Load a sheet into a DataFrame by index
df2 = xl.parse(0)
# Additional parameters:
# skiprows = List of rows to skip
# names = rename the columns as specified in this list
# parse_cols = list of columns to read