import json, urllib.request
from openpyxl import Workbook
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json"
with urllib.request.urlopen(url) as r:
    all_jobs = json.loads(r.read().decode())
print(f"Total jobs loaded: {len(all_jobs)}")

def get_number_of_jobs_T(technology):
    count = sum(1 for j in all_jobs if technology.lower() in j.get("Key Skills", "").lower())
    return technology, count

def get_number_of_jobs_L(location):
    count = sum(1 for j in all_jobs if location.lower() in j.get("Location", "").lower())
    return location, count

wb = Workbook()
ws = wb.active
ws.title = "Job Postings by Location"
ws.append(["Location", "Number of Jobs"])
locations = ["Los Angeles", "New York", "San Francisco", "Washington DC", "Seattle", "Austin", "Detroit"]
print("\n--- Job Postings by Location ---")
for loc in locations:
    l, c = get_number_of_jobs_L(loc)
    ws.append([l, c])
    print(f"{l}: {c}")

ws_tech = wb.create_sheet(title="Job Postings by Technology")
ws_tech.append(["Technology", "Number of Jobs"])
technologies = ["C", "C#", "C++", "Java", "JavaScript", "Python", "Scala", "Oracle", "SQL Server", "MySQL Server", "PostgreSQL", "MongoDB"]
print("\n--- Job Postings by Technology ---")
for tech in technologies:
    t, c = get_number_of_jobs_T(tech)
    ws_tech.append([t, c])
    print(f"{t}: {c}")

wb.save("job-postings.xlsx")
print("\nSaved: job-postings.xlsx")

df_loc = pd.read_excel("job-postings.xlsx", sheet_name="Job Postings by Location")
df_tech = pd.read_excel("job-postings.xlsx", sheet_name="Job Postings by Technology")
print("Sheet 1 shape:", df_loc.shape, "| Sheet 2 shape:", df_tech.shape)
print("\nAll done!")
