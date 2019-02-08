# cat-like-eating-fish
使用python+pygame开发的小游戏，控制猫吃鱼获得分数，并且躲避炸弹。
aodamiao.py 为程序源代码
make.py是打包发布成exe文件时所使用的py文件。
具体如何将python程序打包成exe可以参考此博客：http://www.cnblogs.com/msxh/p/4886628.html
<a href="https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/" target="_blank">sourceforge|py2exe</a>
<a href="https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download" target="_blank">py2exe-0.6.9.win32-py2.7.exe</a>
<a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#py2exe" target="_blank">py2exe.whl</a>

<a href="https://www.cnblogs.com/gopythoner/p/6337543.html" target="_blank">安装pywin32</a>
```
pip install pywin32
```

<a href="https://blog.csdn.net/qq_26877377/article/details/80357349" target="_blank">PyInstaller的安装和使用</a>
<a href="https://www.pyinstaller.org/downloads.html" target="_blank">PyInstaller官网</a>
PyInstaller
```
#失败
pip install PyInstaller
```
<a href="https://github.com/pyinstaller/pyinstaller/releases" target="_blank">PyInstaller|releases包</a>
```
#成功，windows注意下载zip版
python setup.py install
pyinstaller -F /path/to/file.py
```
<a href="https://download.lfd.uci.edu/pythonlibs/r5uhg2lo/PyInstaller-3.4-py2.py3-none-any.whl" target="_blank">PyInstaller-3.4-py2.py3-none-any.whl</a>
```
pip install PyInstaller-3.4-py2.py3-none-any.whl
```
