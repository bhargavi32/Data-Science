import pandas as pd
series1 = pd.Series([1,2,3])
print(series1)
data = {"Name": ["emp1","emp2","emp3","emp4","emp5"],
        "Age":[20,30,40,50,60],
        "Salary":[200,300,400,500,600]}
res = pd.DataFrame(data)
print(res.head(2))
