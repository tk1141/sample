import logging
import time
import os
import datetime

logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')

log_file_path = os.path.join(os.getcwd(), 'Practice', 'log.txt')
log_file = open(log_file_path, 'w')

for i in range(1, 5):
    key = '205007001000{}'.format(i)
    log_file.write('{} [STA] KEY={}\n'.format(
        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %f'), key))
    log_file.write('{} [INF] {}\n'.format(
        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %f'), 'Line001'))
    log_file.write('{} [INF] {}\n'.format(
        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %f'), 'Line002'))
    time.sleep(1)
    log_file.write('{} [END] {}\n'.format(
        datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S %f'), key))

log_file.close()
