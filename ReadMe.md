1、需要发邮件？\
    `修改【Auto_Ui】-【config】模块中的config.yml文件如下参数`
- title='报告标题',
- message='这是今天的测试报告，请查收！',
- receiver='收件邮箱账号',
- server='登陆邮箱服务器',
- sender='登陆邮箱账号',
- password='客户端登陆授权码',
- path=需要发送的文件，这里的reqort是【report】目录下的报告文件

2、编写测试用例\
    【Auto_Ui】-【test】-【case】模块
- 【api】 编写接口用例
- 【ui】 编写webUI用例

3、op模式 \
    【Auto_Ui】-【test】-【common】模块
- 【browser】 封装浏览器的一些操作
- 【page】 封装页面的一些操作

4、page页面\
    【Auto_Ui】-【test】-【common】模块，用于封装每一个页面的信息和方法

5、工具目录
- client模块 封装request网络请求框架
- config模块 封装读取配置类和目录路径常量
- file_reader模块 封装读取yml文件、xls文件的方法
- generator模块 封装faker数据生成器
- log模块 封装日志

6、vevn文件夹
    项目的运行环境文件
