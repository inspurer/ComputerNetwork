import os
import time
import logging

#返回一个logger实例，如果没有指定name，返回root logger。
# 只要name相同，返回的logger实例都是同一个而且只有一个，即name和logger实例是一一对应的。
# 这意味着，无需把logger实例在各个模块中传递。只要知道name，就能得到同一个logger实例。
logger = logging.getLogger('mylogger')
# 设置总日志级别, 也可以给不同的handler设置不同的日志级别
#设置logger的level， level有以下几个级别：
# 级别高低顺序：NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
# 如果把looger的级别设置为INFO， 那么小于INFO级别的日志都不输出， 大于等于INFO级别的日志都输出　
logger.setLevel(logging.DEBUG)

# 控制台日志和日志文件使用同一个formatter,formatter用于描述日志的格式
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s[line:%(lineno)d] - <%(threadName)s %(thread)d>' +
    '- <Process %(process)d> - %(levelname)s: %(message)s'
)
# asctime:日志产生的时间；filename:产生日志的脚本文件名；lineno:该脚本文件哪一行代码产生了日志
# threadName: 当前线程名；thread: 当前进程名；Process进程同thread线程
# levelname: logger的级别；meesage: 具体的日志信息


# 创建Handler, 输出日志到控制台和文件
# 日志文件FileHandler
basedir = os.path.abspath('.') #返回脚本所在的绝对路径
log_dir = os.path.join(basedir, 'logs')  # 日志文件所在目录,即‘脚本路径/logs'
if not os.path.isdir(log_dir):
    os.mkdir(log_dir)
filename = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + '.log'  # 日志文件名，以当前时间命名
file_handler = logging.FileHandler(os.path.join(log_dir, filename))  # 创建日志文件handler
file_handler.setFormatter(formatter)  # 设置Formatter
file_handler.setLevel(logging.INFO)  # 单独设置日志文件的日志级别

# 控制台日志StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
# stream_handler.setLevel(logging.INFO)  # 单独设置控制台日志的日志级别，注释掉则使用总日志级别

# 将handler添加到logger中

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

#如有不懂，参见博客：https://www.jb51.net/article/42626.htm