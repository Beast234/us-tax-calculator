import pandas as pd
tax_info_url = "https://taxfoundation.org/2020-sales-taxes/"
dfs = pd.read_html(tax_info_url)
df = dfs[0]
"""comment to test git branch"""