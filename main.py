import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vgsales.csv")

eu_and_jp=[]
eu_and_na=[]
eu_and_other=[]

jp_and_na=[]
jp_and_other=[]
na_and_other=[]

for index, row in df.iterrows():
    year=row["Year"]
    eu = row["EU_Sales"]
    na = row["NA_Sales"]
    jp = row["JP_Sales"]
    other = row["Other_Sales"]
    gb = row["Global_Sales"]

    if eu != 0 and jp != 0  :
        diff = abs((eu - jp) / gb) * 100
        eu_and_jp.append((year,round(diff,2)))

        
       
      
    if eu != 0 and na != 0  :
        diff = abs((eu - na) / gb) * 100
        eu_and_na.append((year,round(diff,2)))



    if eu != 0 and other != 0  :
        diff = abs((eu - other) / gb) * 100
        eu_and_other.append((year,round(diff,2)))
    if na != 0 and jp != 0  :
        diff = abs((na - jp) / gb) * 100
        jp_and_na.append((year,round(diff,2)))
        

    if jp != 0 and other != 0 :
        diff = abs((other - jp) / gb) * 100
        jp_and_other.append((year,round(diff,2)))
        


    

    if other != 0 and na != 0  :
        diff = abs((na - other) / gb) * 100
        na_and_other.append((year,round(diff,2)))
    

jp_and_other.sort(key=lambda x: x[1])

years0, values0 = zip(*jp_and_other)


mean=sum(values0)/len(jp_and_other)

plt.figure(figsize=(10,6))

plt.axhline(
    y=mean,
    linestyle="--",
    color="orange",  
    label=f"Mean = {mean:.2f}%"
)

x = range(len(values0))
plt.bar( x,values0, label="JP and Others",color="Yellow")






plt.ylabel("Difference on sales (%)")
plt.legend()
plt.tight_layout()
plt.show()
