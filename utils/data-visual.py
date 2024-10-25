import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../event_log_collector/security_logs.csv')
df.hist(bins=50, figsize=(20, 15))
plt.show()
