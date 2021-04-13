'''
This porgram is not for implementation is just wrote for my example explanation about database flip
'''

from DB1connection import DB1Connection
from DB2connection import DB2Connection
from service import EMMA, AMMA, product
from databaseflip
import os
import functools
import time
import logging


#if count cross the threshold we should flip DB1 to DB2

def dbhealth_check(db1count,db2count):

    flipstatus = False
    logging.basicConfig(filename='log1.log', format="%(asctime)s %(message)s", filemode='a')
    # Creating an object
    logger = logging.getLogger()
    # Setting a threshold for logger
    logger.setLevel(logging.DEBUG)
    logger.info(f"The backlog count for Db1 and DB2 is {db1count} and {db2count}")

    if not flipstatus and db1count > 100000 and 30000>db2count>10000:
        logger.warning("Backlog for DB1 crossed the Threshold")
        os.system("nslookup iqcbmhudsonp01.com")
        # give ip address of the Db server1 192.160.20.164
        logger.info("DB1 and DB2 for ready for flip")
        databaseflip.flipP01ToP11()
        os.system("nslookup iqcbmhudsonp01.com")
        # ip address of DB server1 now 192.160.35.92
        logger.info("Successfully flipped from Db1 to DB2")
        flipstatus = True
        #this flip function actually changes the DNS entry DB1 got the ip address of DB2 and viseversa.
        #so the requests for server1 redirected to server2 and viseversa



    #if count of backlog reduces flip it back
    elif flipstatus and db1count < 10000 and 30000>db2count>10000:
        logger.info("The backlog count is back to Normal")
        logger.info("Database1 pointing to the address")
        ip1 = os.popen("nslookup iqcbmhudsonp01.com").read().rstrip()
        # After flip ip address of the Db server1 192.160.35.92
        databaseflip.flipP11ToP01()

        logger.info("Successfully flipped from Db2 to DB1")
        logger.info("Database1 pointing to the address")
        ip2 = os.system("nslookup iqcbmhudsonp01.com").read().rstrip()
        if (ip1 != ip2):
            flipstatus = False
        else :
            raise "exception"
        # ip address of DB server1 now change back to 192.160.20.164


while True:
    try:
        db1count = DB1Connection.get_count()
        db2count = DB2Connection.get_count()
        dbhealth_check(db1count, db1count)
    except:
        raise "DB Connection issue"
    time.sleep(120)



    '''
    run cron job if python process is not found in ps -aux | grep DBflip.py 
    nohup python DBflip.py
    if already running skip
    cron job have script which check the Dplip process running in background or not if it not running
    it restart the process.
    '''