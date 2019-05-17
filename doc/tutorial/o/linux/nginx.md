4. 1.1. root 用户 安装依赖包 packages
        yum -y install pcre-devel openssl openssl-devel
        
        
        4. 1.2. nginx 下载和安装


       wget   http://nginx.org/download/nginx-1.15.5.tar.gz
       tar zxvf nginx-1.15.5.tar.gz
       cd nginx-1.15.5;./configure --prefix=/usr/local/nginx --with-http_ssl_module
       make && make install
        
        
        配置 /usr/local/nginx/conf/nginx.conf 和模板里面保持一致，worker 在该配置文件中以jojo用户执行
        
         


        
 手工启动nginx必须以root用户启动 # /usr/local/nginx/sbin/nginx ，因为80端口只有root用户进程可以使用， master 是root用户身份，work 配置为 jojo用户        
      
        下面这些目前已经不需要了
        命令行参数
        nginx supports the following command-line parameters:
        
        -s signal — send a signal to the master process. The argument signal can be one of:
            stop — shut down quickly
            quit — shut down gracefully
            reload — reload configuration, start the new worker process with a new configuration, gracefully shut down old worker processes.
            reopen — reopen log files

        
        # chmod -R 755 /home/jojo /home/jojo/project_name/backend/static 目录不能被nginx 进程读取，如果不行，再执行 chmod o+x /home 

添加防火墙
firewall-cmd --zone=public --add-port=80/tcp --permanent
iptables -I INPUT -p TCP --dport 80 -j ACCEPT;/sbin/service iptables save

如果是阿里云添加安全组规则
![说明](https://images.gitee.com/uploads/images/2019/0317/204749_9ca6db51_2066991.png)