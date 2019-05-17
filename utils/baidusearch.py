import requests


        
urls = [
    
"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=www.python3.vip%20%E7%99%BD%E6%9C%88%E9%BB%91%E7%BE%BD%20python%E6%95%99%E7%A8%8B&oq=python%25E6%2595%2599%25E7%25A8%258B%252Cpython%25E5%259F%25BA%25E7%25A1%2580%252Cpython%25E5%2585%25A5%25E9%2597%25A8%252Cpython%25E8%2587%25AA%25E5%25AD%25A6%252Cpython%25E7%25BB%2583%25E4%25B9%25A0%252Cpython%25E8%25AE%25BA%25E5%259D%259B&rsv_pq=aab1c7d200044435&rsv_t=5e27YbXm7wsmVPzK4pj9%2F%2FCPcZC74FL4QBuQI8rEfBUuPOBbBDYrX%2FJogqo&rqlang=cn&rsv_enter=1&rsv_sug3=27&bs=python%E6%95%99%E7%A8%8B%2Cpython%E5%9F%BA%E7%A1%80%2Cpython%E5%85%A5%E9%97%A8%2Cpython%E8%87%AA%E5%AD%A6%2Cpython%E7%BB%83%E4%B9%A0%2Cpython%E8%AE%BA%E5%9D%9B",
"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=www.python3.vip%20%E7%99%BD%E6%9C%88%E9%BB%91%E7%BE%BD%20python%E5%85%A5%E9%97%A8&oq=%25E7%2599%25BD%25E6%259C%2588%25E9%25BB%2591%25E7%25BE%25BD%2520python%25E5%2585%25A5%25E9%2597%25A8&rsv_pq=d464d8980004e2df&rsv_t=236eL3nWcggHfcwaJx0KNVuT6md3N47heqGH357mBjGFlXTlQwGbCkj99xM&rqlang=cn&rsv_enter=0",
"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=www.python3.vip%20%E7%99%BD%E6%9C%88%E9%BB%91%E7%BE%BD%20python%E8%87%AA%E5%AD%A6&oq=%25E7%2599%25BD%25E6%259C%2588%25E9%25BB%2591%25E7%25BE%25BD%2520python%25E6%2595%2599%25E7%25A8%258B&rsv_pq=d1409ac20004e691&rsv_t=b832yVywF5R%2FjXjCYOy9UayalyDNaYa4hq46Vfccf7R8CKZPkXZqCMIQPSQ&rqlang=cn&rsv_enter=0&inputT=3598&rsv_sug3=47&rsv_sug1=5&rsv_sug7=100&rsv_sug4=16561",
"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=www.python3.vip%20%E7%99%BD%E6%9C%88%E9%BB%91%E7%BE%BD%20python%E7%BB%83%E4%B9%A0&oq=%25E7%2599%25BD%25E6%259C%2588%25E9%25BB%2591%25E7%25BE%25BD%2520python%25E7%25BB%2583%25E4%25B9%25A0&rsv_pq=e36b7f4a0004ac30&rsv_t=a5983MZXLw7sLM%2F4Oa%2Bm%2BeWlcvpELCouqKM6vq95fKYG5NQV9HLMK8Jn9Cc&rqlang=cn&rsv_enter=0&rsv_sug3=51&rsv_sug4=625&rsv_sug=1",
"https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=www.python3.vip%20%E7%99%BD%E6%9C%88%E9%BB%91%E7%BE%BD%20python%E8%AE%BA%E5%9D%9B&oq=%25E7%2599%25BD%25E6%259C%2588%25E9%25BB%2591%25E7%25BE%25BD%2520python%25E7%25BB%2583%25E4%25B9%25A0&rsv_pq=c4b12601000480af&rsv_t=788b0E0TiTLjiVUp3pSVfs4jG8oVqpTzw7Yojb7LpZep9%2F3t8F26gCg9RsQ&rqlang=cn&rsv_enter=0&rsv_sug3=53&rsv_sug1=8&rsv_sug7=000&rsv_n=2&bs=%E7%99%BD%E6%9C%88%E9%BB%91%E7%BE%BD%20python%E7%BB%83%E4%B9%A0",

]


getHeads = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                 "Accept-Encoding": "gzip, deflate",
                 "Accept-Language": "en-us,en;q=0.5",
                 "Connection": "keep-alive",
                 "User-Agent":    "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/14.0.1"    ,
                    }


import time,traceback

try:
    for i in range(1):	
        print (i)
		
        for one in urls:
            response =  requests.get(one,  headers=getHeads)
            print(f"response: \n{response.text}\n\n")
            time.sleep(0.4)
		
		
		
except:    
    print (traceback.format_exc()    )