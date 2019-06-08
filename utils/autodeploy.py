
HOST   = 'www.python3.vip'   # '192.168.0.103'
PORT   = 22
USER   = 'root'
PASSWD = 'ohmyjcy1!'
BUILD_DIR     = 'd:/tmp/tmpbuild'
REMOTE_DIR     = '/usr/local/nginx/sites'

import paramiko
import sys,os,shutil


switchTable = ['free','v1']


# 检查当前工作目录是否为项目根目录
if not (os.path.exists('byhy_run.bat') and os.path.exists('CNAME')):
    print('!! 必须在项目根目录下面运行')
    sys.exit(2)

# 用户输入选项
toWhich = input('\n\n发布 free还是v1？:')

if toWhich not in switchTable:
    print(f'no such config:{toWhich}')
    sys.exit(2)

# 切换目标
print(f'\n切换版本为: {toWhich}')
os.system(f'python utils\switch\switch.py {toWhich}')    

# 确保 _config.yml中 incremental: false
with open('_config.yml',encoding='utf8') as f:
    content = f.read()   
    if 'incremental: false' not in content:
        print('!! _config.yml中 必须设置 incremental: false')
        sys.exit(2)

print('\n执行 bundle exec jekyll build...\n')
ret = os.system('bundle exec jekyll build')    
print(f'\nbundle exec jekyll build 执行结果:{ret}')    


cont = input(f'\n\n继续部署操作吗？[y/n]:')
if cont != 'y':
    sys.exit(1)


# 如果打包目录已经存在，先删除
if os.path.exists(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)


# 确定最终的远程拷贝目录
REMOTE_DIR += '/' + toWhich

#创建SSHClient 实例对象
ssh = paramiko.SSHClient()

#调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程机器  地址、端口、用户名密码
ssh.connect(HOST,PORT,USER, PASSWD)


def remoteRun(cmd, printOutput=True):
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode('utf8')
    errinfo = stderr.read().decode()
    if printOutput:
        print(output+errinfo)
    return output+errinfo



print('打包 _site')
shutil.make_archive(BUILD_DIR + '/_site', 
                    format = 'zip', 
                    root_dir=None,
                    base_dir='_site')


print('上传安装包..')
sftp = ssh.open_sftp()
sftp.put(BUILD_DIR + '/_site.zip', REMOTE_DIR + '/_site.zip')
sftp.close()



print('备份原来的安装目录')
remoteRun(f'cd {REMOTE_DIR}; rm -rf _site.bak;mv _site _site.bak')


print('解压安装包...',end='')
remoteRun(f'cd {REMOTE_DIR}; unzip _site.zip',printOutput=False)
print('ok')



ssh.close()

print('\n==== 部署操作结束 ====')

