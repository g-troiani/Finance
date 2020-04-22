from kedro.io import (DataCatalog, CSVDataSet)

io = DataCatalog({ "example": CSVDataSet(filepath="data/01_raw/GE.csv") })
