import paramiko

#创建ssh对象
ssh=paramiko.SSHClient()

#把要连接的机器添加到known_hosts文件中
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接
ssh.connect(hostname='39.104.102.49',port=22,username='root',password='linux.526526')

cmd = 'ps'
stdin,stdout,stderr = ssh.exec_command(cmd)

result = stdout.read()
if not result:
    result = stderr.read()
ssh.close()

print(result.decode())