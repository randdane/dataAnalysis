"""
    Get port number with:    xp_readerrorlog 0, 1, N'Server is listening on', 'any', NULL, NULL, N'asc' 
"""
import pymssql
import pandas as pd


conn = pymssql.connect(server="10.0.12.2", user="kcxsa",password="some_fake_password", port=1433)
query = "SELECT TOP 1000
        FROM [KCXPOS].[dbo].[tblVendors]"
df = pd.read_sql(query,conn)
df.head(5)
