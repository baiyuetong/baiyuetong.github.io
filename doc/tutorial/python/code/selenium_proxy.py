# from selenium import webdriver

# PROXY = "localhost:1080"

# # Create a copy of desired capabilities object.
# desired_capabilities = webdriver.DesiredCapabilities.CHROME.copy()
# # Change the proxy properties of that copy.
# desired_capabilities['proxy'] = {
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "noProxy":None,
#     "proxyType":"MANUAL",
#     "class":"org.openqa.selenium.Proxy",
#     "autodetect":False
# }

# wd = webdriver.Chrome(desired_capabilities=desired_capabilities)
# wd.get('https://google.com')

# wd.find_element_by_id('lst-ib').send_keys('中国网络防火墙\n')




from selenium import webdriver

PROXY = "localhost:1080" 

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

wd = webdriver.Chrome(chrome_options=chrome_options)
wd.get('https://google.com')
wd.find_element_by_id('lst-ib').send_keys('中国历代帝王\n')
