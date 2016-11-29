beef的配置
=======

可能需要手动安装
```bash
gem install em-websocket
```
来解决问题

不知为何，打开程序一定要在root用户中通过
```bash
nohup ./beef &
```
来实现，而不能使用完整路径如
```bash
nohup /usr/share/beef-xss/beef &
```
