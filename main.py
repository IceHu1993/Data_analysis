import pandas as pd
s = pd.Series([1, 3, 5, np.nan, 6, 8])
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
