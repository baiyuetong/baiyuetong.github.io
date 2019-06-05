import requests


        
urls = [
    
"http://www.python3.vip/",
"http://www.python3.vip/doc/tutorial/python/0001/",

# "http://www.python3.vip/doc/tutorial/python/level2/2004/",
]




import time,traceback

try:
    for one in urls:
        print (one)
        response =  requests.post(
                'http://data.zz.baidu.com/urls?site=www.python3.vip&token=c8B8rNPiMg29JTQC',
                headers={"Content-Type": "text/plain"},
                data=one
        )
        print(f"response: \n{response.json()}\n\n")
        time.sleep(0.4)
		
		
		
except:    
    print (traceback.format_exc()    )