[loggers]
keys=root,infoLogger

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[logger_infoLogger]
handlers=consoleHandler,fileHandler
qualname=infoLogger
propagate=0

[handlers]
keys=consoleHandler,fileHandler

[handler_consoleHandler]
class=StreamHandler
level=INFO
formatter=form02
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=INFO
formatter=form01
args=('/Users/didi/Desktop/python/oo/logs_test/runlogs.log','a+')


[formatters]
keys=form01,form02

[formatter_form01]
format=%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s

[formatter_form02]
format=%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s