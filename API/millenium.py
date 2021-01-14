import requests # In Python, the most common library for making requests and working with APIs is the requests library.
import json

def fun(s,p):
 
    httpw="https://jsonmock.hackerrank.com/api/countries/search?name="
    link=httpw+s
    '''
    #this link will give json data having total countries with string 's'
    In our example link="https://jsonmock.hackerrank.com/api/countries/search?name=nd" total 46 countries came after including the given string 'nd'
    "page": 1,
    "per_page": 10, #this means per page having 10 countries. So 46 countries displying in 5 pages and last page have 6 countris
    "total": 46,
    "total_pages": 5
    '''
    resp=requests.get(link) #get method used to make APi request...it retrive the data from server
    s_data=resp.json() # method used to see the data we received back from the API....its in the form of dictionary.So s_data is now dictionary holds the recieved data
    totalpages=s_data["total_pages"]
    lgreator=[] #list to store countries having population greator than p
    lless=[]
    maincount=0
    pno="&page="
    con_count =s_data["total"]#countries count per page
    for i in range(1,totalpages):#this loop is for iterating pages
        plink=link+pno+str(i) # https://jsonmock.hackerrank.com/api/countries/search?name=nd&page=2 we are making pagewise link
        page_resp=requests.get(plink)
        page_data=page_resp.json()
        
        print(con_count)
        if con_count>page_data["per_page"]:
            cons_perpage=page_data["per_page"]
        else:
            cons_perpage=cou_count
        count_perpage=0 
        
        for j in range(cons_perpage):#this loop is for iterating per page
            if ((page_data["data"][j]["population"])>p):
                lgreator.append([page_data["data"][j]["name"],page_data["data"][j]["population"]])
                count_perpage+=1
            else:
                lless.append([page_data["data"][j]["name"],page_data["data"][j]["population"]])
        
        con_count-=page_data["per_page"]
        maincount=maincount+count_perpage
    
    def jprint(obj):
    # create a formatted string of the Python JSON object
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)
    
    jprint(lgreator)
    return maincount
    
    
    
    
output=fun('nd',10000)
print(output)
'''
l=requests.get("https://jsonmock.hackerrank.com/api/countries/search?name=nd&page=2")
#print(l.json())
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)    
jprint(l.json())
'''