import pandas as pd

# Employees DataFrame
employees = pd.DataFrame({
    "EmpID": [101, 102, 103, 104],
    "Name": ["Aman", "Riya", "Vikas", "Meena"],
    "DeptID": [1, 2, 1, 3]
})

# Departments DataFrame
departments = pd.DataFrame({
    "DeptID": [1, 2, 3],
    "Department": ["IT", "HR", "Finance"]
})

# Merge DataFrames DeptID ke basis pe
merged_df = pd.merge(employees, departments, on="DeptID", how="inner")
print(merged_df)

print(employees.shape)