本地push代码，使用http时，由于某些原因失败，需要使用ssh的方式，密钥配置步骤如下

# 配置代码仓为ssh
 git remote set-url origin git@github.com:cyixxxx/aXXXX.git
 git remote -v

# 本地生成ssh密钥
- ssh-keygen.exe -t rsa -C "xxxxxxx@xx.com"  # 连续回车，生成无密码密钥
- 进入c盘，用户，获取key，路径： C:\Users\xxxx\.ssh\id_rsa.pub

# github上添加本地生成的密钥
- 登录github，添加sshkey，配置路径：`settings` -> `SSH and GPG keys` ->  `New SSH key`