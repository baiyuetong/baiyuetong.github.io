---
title: 白月销售管理系统 API 接口 1.0
---

## 概述

本接口用于 Bysms 系统 **管理员用户** 前后端系统 之间的数据 交互。

本接口中，所有请求 ( 除了登录请求之外 )，必须在cookie中携带有登录的成功后，服务端返回的sessionid。


<br><br>

## 登录系统

### 请求消息

```py
POST  /api/mgr/signin  HTTP/1.1
Content-Type:   application/x-www-form-urlencoded
```

### 请求参数

http 请求消息 body 中 参数以 格式 x-www-form-urlencoded 存储

需要携带如下参数，

- username 
  
    用户名

- password

    密码    


### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果登录成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示登录成功



如果登录失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg":  "用户名或者密码错误"
}
```

ret 不为 0 表示登录失败， msg字段描述登录失败的原因




<br><br>

## 客户数据

### 列出所有客户

#### 请求消息

```py
GET  /api/mgr/customers  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action 
  
    填写值为 list_customer


#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```json
{
    "ret": 0,
    "retlist": [
        {
            "address": "江苏省常州武进市白云街44号",
            "id": 1,
            "name": "武进市 袁腾飞",
            "phonenumber": "13886666666"
        },
        
        {
            "address": "北京海淀区",
            "id": 4,
            "name": "北京海淀区代理 蔡国庆",
            "phonenumber": "13990123456"
        }
    ]              
}
```

ret 为 0 表示登录成功

retlist 里面包含了所有的客户信息列表。

每个客户信息以如下格式存储

```json
{
   "address": "江苏省常州武进市白云街44号",
   "id": 1,
   "name": "武进市 袁腾飞",
   "phonenumber": "13886666666"
}
```



<br>

### 添加一个客户

#### 请求消息

```py
POST  /api/mgr/customers  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加客户的信息

消息体的格式是json，如下示例：


```json
{
    "action":"add_customer",
    "data":{
        "name":"武汉市桥西医院",
        "phonenumber":"13345679934",
        "address":"武汉市桥西医院北路"
    }
}
```

其中

```action``` 字段固定填写  ```add_customer``` 表示添加一个客户

```data``` 字段中存储了要添加的客户的信息

服务端接受到该请求后，应该在系统中增加一位这样的客户。



#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```json
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id  为 添加客户的id号。

如果添加失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "客户名已经存在"
}
```


ret 不为 0 表示失败， msg字段描述添加失败的原因






<br>

### 修改客户信息

#### 请求消息

```py
PUT  /api/mgr/customers  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带修改客户的信息

消息体的格式是json，如下示例：


```json
{
    "action":"modify_customer",
    "id": 6,
    "newdata":{
        "name":"武汉市桥北医院",
        "phonenumber":"13345678888",
        "address":"武汉市桥北医院北路"
    }
}
```

其中

```action``` 字段固定填写  ```modify_customer``` 表示修改一个客户的信息

```id``` 字段为要修改的客户的id号

```newdata``` 字段中存储了修改后的客户的信息

服务端接受到该请求后，应该在系统中增加一位这样的客户。


<br>

#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果修改失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "客户名已经存在"
}
```


ret 不为 0 表示失败， msg字段描述添加失败的原因






<br><br>

### 删除客户信息

#### 请求消息

```py
DELETE  /api/mgr/customers  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除客户的id

消息体的格式是json，如下示例：


```json
{
    "action":"del_customer",
    "id": 6
}
```

其中

```action``` 字段固定填写  ```del_customer``` 表示删除一个客户

```id``` 字段为要删除的客户的id号

服务端接受到该请求后，应该在系统中尝试删除该id对应的客户。


<br>

#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果删除成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果删除失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "id为 566 的客户不存在"
}
```


ret 不为 0 表示失败， msg字段描述添加失败的原因







<br><br>

## 药品

### 列出所有药品

#### 请求消息

```py
GET  /api/mgr/medicines  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action 
  
    填写值为 list_medicine


#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```json
{
    "ret": 0,
    "retlist": [
        {"id": 1, "name": "青霉素", "sn": "234324234234", "desc": "青霉素"},
        {"id": 2, "name": "红霉素", "sn": "234545534234", "desc": "红霉素"}
    ]              
}
```

ret 为 0 表示登录成功

retlist 里面包含了所有的药品信息列表。

每个药品信息以如下格式存储

```json
    {"id": 2, "name": "红霉素", "sn": "234545534234", "desc": "红霉素"}
```



<br>

### 添加一个药品

#### 请求消息

```py
POST  /api/mgr/medicines  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加药品的信息

消息体的格式是json，如下示例：


```json
{
    "action":"add_medicine",
    "data":{
        "desc": "青霉素 国字号",
        "name": "青霉素",
        "sn": "099877883837"
    }
}
```

其中

```action``` 字段固定填写  ```add_medicine``` 表示添加一个药品

```data``` 字段中存储了要添加的药品的信息

服务端接受到该请求后，应该在系统中增加这样的药品。



#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```json
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id  为 添加药品的id号。

如果添加失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "药品名已经存在"
}
```


ret 不为 0 表示失败， msg字段描述添加失败的原因






<br>

### 修改药品信息

#### 请求消息

```py
PUT  /api/mgr/medicines  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带修改药品的信息

消息体的格式是json，如下示例：


```json
{
    "action":"modify_medicine",
    "id": 6,
    "newdata":{
        "name":"武汉市桥北医院",
        "phonenumber":"13345678888",
        "address":"武汉市桥北医院北路"
    }
}
```

其中

```action``` 字段固定填写  ```modify_medicine``` 表示修改一个药品的信息

```id``` 字段为要修改的药品的id号

```newdata``` 字段中存储了修改后的药品的信息

服务端接受到该请求后，应该在系统中增加一位这样的药品。


<br>

#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果修改成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果修改失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "药品名已经存在"
}
```


ret 不为 0 表示失败， msg字段描述添加失败的原因






<br><br>

### 删除药品信息

#### 请求消息

```py
DELETE  /api/mgr/medicines  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带要删除药品的id

消息体的格式是json，如下示例：


```json
{
    "action":"del_medicine",
    "id": 6
}
```

其中

```action``` 字段固定填写  ```del_medicine``` 表示删除一个药品

```id``` 字段为要删除的药品的id号

服务端接受到该请求后，应该在系统中尝试删除该id对应的药品。


<br>

#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果删除成功，返回如下

```json
{
    "ret": 0
}
```

ret 为 0 表示成功。

如果删除失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "id为 566 的药品不存在"
}
```


ret 不为 0 表示失败， msg字段描述添加失败的原因







<br><br>

## 订单

### 列出所有订单

#### 请求消息

```py
GET  /api/mgr/orders  HTTP/1.1
```

#### 请求参数

http 请求消息 url 中 需要携带如下参数，

- action 
  
    填写值为 list_order


#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果获取信息成功，返回如下

```json
{
    "ret": 0,
    "retlist": [
        {id: 1, name: "华山医院订单001", create_date: "2018-12-26T14:10:15.419Z", customer_name: "华山医院",medicines_name: "青霉素"},
        {id: 2, name: "华山医院订单002", create_date: "2018-12-27T14:10:37.208Z", customer_name: "华山医院",medicines_name: "青霉素 | 红霉素 "}
    ]              
}
```

ret 为 0 表示登录成功

retlist 里面包含了所有的订单信息列表。

每个订单信息以如下格式存储

```json
    {
        id: 2, 
        name: "华山医院订单002", 
        create_date: "2018-12-27T14:10:37.208Z", 
        customer_name: "华山医院",
        medicines_name: "青霉素 | 红霉素 "
    }
```

其中 medicines_name 表示对应的药品，如果该订单有多个药品， 中间用 竖线隔开 


<br>

### 添加一个订单

#### 请求消息

```py
POST  /api/mgr/orders  HTTP/1.1
Content-Type:   application/json
```

#### 请求参数

http 请求消息 body 携带添加订单的信息

消息体的格式是json，如下示例：


```json
{
    "action":"add_order",
    "data":{
        "name":"华山医院订单002",
        "customerid":3,
        "medicineids":[1,2]
    }
}
```

其中

```action``` 字段固定填写  ```add_order``` 表示添加一个订单

```data``` 字段中存储了要添加的订单的信息

medicineids  是 该订单中药品的id 列表

服务端接受到该请求后，应该在系统中增加这样的订单。



#### 响应消息


```py
HTTP/1.1 200 OK
Content-Type: application/json
```

#### 响应内容

http 响应消息 body 中， 数据以json格式存储，

如果添加成功，返回如下

```json
{
    "ret": 0,
    "id" : 677
}
```

ret 为 0 表示成功。

id  为 添加订单的id号。

如果添加失败，返回失败的原因，示例如下

```json
{
    "ret": 1,    
    "msg": "订单名已经存在"
}
```


ret 不为 0 表示失败， msg字段描述添加失败的原因



<br>

### 修改订单


暂不支持



<br><br>

### 删除订单

暂不支持