import paramiko

#创建ssh对象
ssh=paramiko.SSHClient()

#把要连接的机器添加到known_hosts文件中
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接
ssh.connect(hostname='ssskming.51vip.biz',port=22865,username='root',password='Huawei12#$')

#cmd = 'ls'
cmd = 'ifconfig\n'
#cmd = 'ipmcset -d powerstate -v 1'
stdin,stdout,stderr = ssh.exec_command(cmd)
#port1=ssh.get_transport()
#print(port1.decode())
result = stdout.read()
if not result:
    result = stderr.read()
ssh.close()

#print(result.decode())


