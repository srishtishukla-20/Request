import requests
import json
from requests.api import options, request
result=requests.get('https://saral.navgurukul.org/api/courses')
data=result.json()
with open("availableCourse.json","w") as f:
    json.dump(data,f,indent=4)
def opt(select,var2,slug,data2):
    while True:
        x=var2
        print("................")
        options=input("enter your option :up,next,exit,back ")
        if options=="up":
            print(x)
            x-=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[x]))
            r=req.json()
            print("content",r["content"])
            print(x)
        elif options=="next":
            x+=1
            req=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[x-1]))
            r1=req.json()
            print("content",r1["content"])
            print(x)
        elif options=="back":
            c=1
            for dic1 in data2["data"]:
                print(c,dic1["name"])
                c+=1
                for i in dic1["childExercises"]:
                    print("    ",c,i["name"])
                    c+=1
        else:
            break
def course():
    index=0
    for i in data["availableCourses"]:
        print(index+1,i["name"],i["id"])
        index+=1

    for courses in data["availableCourses"]:
        print("..................")
        course=int(input("select your course="))
        select=data["availableCourses"][course-1]["id"]
        var=requests.get("http://saral.navgurukul.org/api/courses/"+str(select)+"/exercises")
        data2=var.json()
        slug=[]
        count3=1
        for dic_data2 in data2["data"]:
            print(count3,dic_data2["name"])
            slug.append(dic_data2["slug"])
            count3+=1
            for child in dic_data2["childExercises"]:
                print("       ",count3,child["name"])
                slug.append(child["slug"])
                count3+=1
        print("...............")
        var2=int(input("select content slug:"))
        var3=requests.get("https://saral.navgurukul.org/api/courses/"+str(select)+"/exercise/getBySlug?slug="+str(slug[var2-1]))
        data3=var3.json()
        print(data3["content"])
        opt(select,var2,slug,data2)
course()