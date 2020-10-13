import os
import re
import datetime

log_file_path = os.path.join(os.getcwd(), 'Practice', 'log.txt')
log_file = open(log_file_path)


start_end_log_regex = re.compile(r'''(
    (.+)        #開始時刻
    \s
    \[STA\]
    \s
    KEY=(.+)    #キー
    [\s\S]*?
    (.+)        #終了時刻
    \s
    \[END\]
    )''', re.VERBOSE)

text = log_file.read()
print(text)

matches = []
for groups in start_end_log_regex.findall(text):
    start_time = groups[1]
    key = groups[2]
    end_time = groups[3]

    start = datetime.datetime.strptime(start_time, '%Y/%m/%d %H:%M:%S %f')
    end = datetime.datetime.strptime(end_time, '%Y/%m/%d %H:%M:%S %f')
    delta = end - start
    print('{}:delta={}'.format(key, delta))

log_file.close()
