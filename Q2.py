import json
def years(year):
    for i in year:
        if((i%4==0 and i%100!=0) or i%400==0):
            dict[i]=True
        else:
            dict[i]=False
def export(dict):
    ans=json.dumps(dict)
    print(ans)
dict={}
year= list(map(int, input().split()))
years(year)
print(dict)
export(dict)