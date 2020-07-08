# 准备工作
1、VPS一台，系统随意（最好重置新系统，防止各种端口被占用而导致的错误）

2、域名一个，做好解析并已经生效（这一步不懂或是不会请去YouTube里面爬楼）

3、赋有极大热情和耐以折腾的精神。。。（这点至关重要）

4、大家一致需要的 V2rayN Trojan 版本来了（支持Trojan的V2rayN）：点击下载

# 开始搭建Trojan
## 1、检查SELinux是否为关闭状态
一般情况下，VPS的SELinux处于关闭状态，但是不排除所有，大家检查一下！
```
/usr/sbin/sestatus -v      ##如果返回参数为enabled即为开启，disabled为关闭
```
若是开启状态，如何关闭SELinux服务？

修改 /etc/selinux/config 文件

将 SELINUX=enforcing 改为 SELINUX=disabled

重启VPS以后SELinux即为关闭状态。

## 2、安装基础依赖环境
yum -y install wget    ##ContOS Yum 安装 wget
apt-get install wget   ##Debian Ubuntu 安装 wget

## 3、开始运行Trojan安装代码
代码很简单，三行代码，大家一行一行的复制进去运行，任何问题均有相关提示!

```
wget -N --no-check-certificate "https://raw.githubusercontent.com/V2RaySSR/Trojansh/master/trojan1.sh" && chmod +x trojan1.sh && ./trojan1.sh
```
```
wget -N --no-check-certificate "https://raw.githubusercontent.com/V2RaySSR/Trojansh/master/trojan2.sh" && chmod +x trojan2.sh && ./trojan2.sh
```
```
wget -N --no-check-certificate "https://raw.githubusercontent.com/V2RaySSR/Trojansh/master/trojan3.sh" && chmod +x trojan3.sh && ./trojan3.sh
```

## 4、安装BBRPLUS加速
```wget -N --no-check-certificate "https://github.com/ylx2016/Linux-NetSpeed/releases/download/sh/tcp.sh" && chmod +x tcp.sh && ./tcp.sh```

