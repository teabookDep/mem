# short key
## 显示
- F11	切换全屏模式 Toggle full screen
-
## 編輯
- Shift + Alt + A	切换 添加/取消 大块注释
- Shift + Alt + →(連擊多次)	从光标处扩展选中全行 Expand selection
- Shift + Alt + ←	收缩选择区域 Shrink selection
- Ctrl + Tab  /  Ctrl + P  /  PgUp or PgDown  左右切換Tab頁
- Ctrl + K P	复制当前打开文件的存放路径
## 多行操作
- Alt + Click	插入光标-支持多个
- Shift + Alt + I	插入光标到选中范围内所有行结束符 Insert cursor at end of each line selected
- Shift +(arrow key) / (Ctrl + Shift + Alt + (arrow key))    Box selection
- Shift + Alt + mouse click    Box selection
- Ctrl + Shift + L	选择所有跟當前行内容一樣的行-操作 Select all occurrences of current selection
- Ctrl + F2	匹配当前选中的词并插入光标 Select all occurrences of current word
## 查找和替换
- 在查找（Ctrl + F）框中 Ctrl + Enter 可以查找匹配跨行内容
- Enter	向後切換匹配的所有元素
- Alt + Enter	添加与选中元素匹配的所有元素
## 文件管理
- Ctrl + O	Open File...
- Ctrl + R	最近打开的文件夹的列表
- Ctrl + Shift + S	Save As...
- **Ctrl + K R**	打开文件所在文件夹
- Ctrl + K O	在新窗口打开当前文件


# REG

- 替換空行
  - ^\r?\n
  - ^\s*(?=\r?$)\n

- 匹配
  - Windows(?=95|98|NT|2000) 能匹配 Windows2000 中的 Windows，但不能匹配 Windows3.1 中的 Windows
  - Windows(?!95|98|NT|2000) 能匹配 Windows3.1 中的 Windows，但不能匹配 其他 中的 Windows


- 验证漢字
  - 2 到 9 位中文昵称：^[\u4e00-\u9fa5]{2,9}$

- 验证密码
  - 只能是字母、数字和下划线，长度不限制：^\w+$
  - 允许 小写字母 a-z、大写字母 A-Z、数字 0-9、下划线 _、 连接符 -，且长度在 6-18 位数：/^[a-zA-Z0-9_-]{6,18}$/
  - 必须包含数字+小写字母+大写字母的密码，且长度在8-10位之间：^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,10}$


- 验证 Email
  - 允许有一个字符符合 [A-Za-z0-9_] 之后可以为 [A-Za-z0-9_-+.] + @ + 允许有一个字符符合 [A-Za-z0-9_] 之后可以为 [A-Za-z0-9_-.] + . + 允许有一个字符符合 [A-Za-z0-9_] 之后可以有 [A-Za-z0-9_-.] 的邮箱：^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$


- 验证身份证
  - 18 位身份证号，尾数是数字或者字母 X：^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$
  - 15 或者 18 位身份证号，尾数可以是数字及 X 或者 x：(^\d{15}$)|(^\d{18}$)|(^\d{17}(\d|X|x)$)


- 验证手机号
  - 以 1 开头，第二位数是 3/4/5/7/8 的 11 位手机号码：^1[3,4,5,7,8,9]\d{9}$
  - 移动号码：^134[0-8]\d{7}$|^(?:13[5-9]|147|15[0-27-9]|178|1703|1705|1706|18[2-478])\d{7,8}$
  - 电信号码：^(?:133|153|1700|1701|1702|177|173|18[019])\d{7,8}$
  - 联通号码：^(?:13[0-2]|145|15[56]|176|1704|1707|1708|1709|171|18[56])\d{7,8}|$
