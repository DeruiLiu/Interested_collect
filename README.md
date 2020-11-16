# Interested_collect
收集一些感兴趣的项目信息，方便自己查找和学习
# 博客类项目
1.[优秀的计算机编程类博客和文章](https://github.com/edagarli/tuiblogs) 
优秀的计算机编程类博客和文章 share excellent blogs and sites

2.[计算机科学自学](https://github.com/ossu/computer-science)
一个计算机自学的开源项目

3.[高频面试题](https://github.com/resumejob/interview-questions)
根据国内外论坛收集超过 1700 篇真实面经整理的腾讯，阿里，字节跳动，Shopee，美团，滴滴等公司的真实高频面试题

# C++资源收集项目
1. <B>[c++线程池实现  C++11](https://github.com/mtrebi/thread-pool)</B>
2. [内存池实现1](https://github.com/cacay/MemoryPool)
3. [内存池实现2](https://github.com/DGuco/shmqueue)
4. [stl源码剖析3.3](https://github.com/steveLauwh/SGI-STL)

1. [awesome-cpp](https://github.com/fffaraz/awesome-cpp)
精选的关于C++的一系列资源
2. [design-patterns-cpp](https://github.com/JakubVojvoda/design-patterns-cpp)
C++设计模式实现
3. [interview](https://github.com/huihut/interview)
 C/C++ 技术面试基础知识总结，包括语言、程序库、数据结构、算法、系统、网络、链接装载库等知识及面试经验、招聘、内推等信息。
4. [CPlusPlusThings](https://github.com/Light-City/CPlusPlusThings)
```diff
 - C++那些事
```
5. [MyTinySTL](https://github.com/Alinshans/MyTinySTL)
很多人表示学完C++不知道用来干什么，我觉得学完C++的第一个练手的好机会那就是自己试着实现一个小型的STL库。MyTinySTL的作者它就用 C++11 重新复写了一个小型 STL（容器库＋算法库）。代码结构清晰规范、包含中文文档与注释，并且自带一个简单的测试框架，非常适合新手学习与参考！
6. [netdata](https://github.com/netdata/netdata)
Netdata是针对系统和应用程序的分布式，实时性能和运行状况监视。它是您在所有系统和容器上安装的高度优化的监视代理。
7. <B> [C++后端开发](https://github.com/balloonwj/CppGuide)</B>
相关资料

# C 网络编程项目

1. <B>[Libevent](https://github.com/libevent/libevent)
 不需要多说什么</B>
 
2. [libhv](https://github.com/ithewei/libhv)
像一样libevent, libev, and libuv， libhv提供具有非阻塞IO和计时器的事件循环，但具有更简单的API和更丰富的协议。
3. [redis](https://github.com/redis/redis)
redis
4. [redis注释](https://github.com/huangz1990/redis-3.0-annotated)
redis设计与实现
10. [memcached](https://github.com/memcached/memcached)
memcached是一套分布式的高速缓存系统。其网络部分也是基于libevent来实现

# C++ 网络编程项目

1. <B> [WebServer](https://github.com/linyacool/WebServer)</B> 
```diff
 - 本项目为C++11编写的Web服务器，解析了get、head请求，可处理静态资源，支持HTTP长连接，支持管线化请求，并实现了异步日志，记录服务器运行状态。
 ```

2. [TinyWebServer](https://github.com/qinguoyi/TinyWebServer)
Linux下C++轻量级Web服务器，助力初学者快速实践网络编程，搭建属于自己的服务器.

- 使用 线程池 + 非阻塞socket + epoll(ET和LT均实现) + 事件处理(Reactor和模拟Proactor均实现) 的并发模型
- 使用状态机解析HTTP请求报文，支持解析GET和POST请求
- 访问服务器数据库实现web端用户注册、登录功能，可以请求服务器图片和视频文件
- 实现同步/异步日志系统，记录服务器运行状态
- 经Webbench压力测试可以实现上万的并发连接数据交换

1. [Tinyhttpd](https://github.com/EZLippi/Tinyhttpd)
Tinyhttpd 是J. David Blackstone在1999年写的一个不到 500 行的超轻量型 Http Server，用来学习非常不错，可以帮助我们真正理解服务器程序的本质
2. [ThreadPool](https://github.com/progschj/ThreadPool)
一个简单的C ++ 11线程池实现。
3. [Muduo](https://github.com/chenshuo/muduo)
Muduo是一个基于以下内容的多线程C ++网络库：基于libevent实现
4. [Websocket](https://github.com/zaphoyd/websocketpp)
WebSocket ++是仅标头的C ++库，实现RFC6455 WebSocket协议。它允许将WebSocket客户端和服务器功能集成到C ++程序中。它使用可互换的网络传输模块，包括一个基于原始字符缓冲区的模块，一个基于C ++ iostream的模块和一个基于Asio的模块（通过Boost或独立）。最终用户可以根据需要编写其他传输策略以支持其他网络或事件库。
5. [MPMCQueue](https://github.com/rigtorp/MPMCQueue)
用C ++ 11编写的有界多生产者多消费者无锁队列。
6. [evpp](https://github.com/Qihoo360/evpp)
其网络编程部分是基于libevent
evpp是一个现代C ++网络库，用于使用TCP / UDP / HTTP协议开发高性能的网络服务。 evpp提供了一个TCP服务器来支持多线程非阻塞事件驱动服务器，还提供了一个HTTP，UDP服务器来支持HTTP和UDP协议。
7. [handy](https://github.com/yedf/handy)
简洁易用的C++11网络库

8. [CppNet](https://github.com/caozhiyi/CppNet)
CppNet一个封装在 TCP 协议上的 Proactor 模式 multi-thread 网络库。包含 OS 接口调用、回调处理、定时器、缓存管理等，这里有从操作系统到应用层的所有网络细节，便于初学者学习和实践。
简单：只导出了最少量的接口，其声明都类似系统 socket API。对客户端而言，只新增了一个 buffer 类型
快速：采用性能最优的 epoll 和 IOCP 做事件驱动。每个连接都独享一个内存池，从内存池中申请的内存都由智能指针管理
清晰：结构上分为事件驱动，会话管理，接口三层，通过回调向上通知。模块之间职责分工明确，最大的类不超过 500 行代码
9. [oatpp](https://github.com/oatpp/oatpp)
我们知道Java领域的Web框架非常繁荣，最知名的当属Spring全家桶，而C语言和C++阵营则几乎没有。那oatpp则是一个轻量、跨平台、高性能、完全零依赖，用纯 C++ 实现的 Web 框架，实在是难得，小伙伴们可以学习学习
10. [leveldb](https://github.com/google/leveldb)
LevelDB是Google编写的快速键值存储库，提供了从字符串键到字符串值的有序映射。 基于C++
11. [TeamTalk](https://github.com/meili/TeamTalk)
一个简单的整体实战的开源项目

