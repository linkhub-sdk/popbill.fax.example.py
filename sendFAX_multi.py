# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, FaxReceiver, PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("팩스전송. 1파일 동보전송(수신번호 최대 1000개)")

    Sender = '07075103710' # 발신번호
    filePath = 'test.jpeg' # 파일경로
    reserveDT = "20150327200000" # 예약전송시간, 작성형태 yyyyMMddHHmmss

    Receivers = [] # 수신정보 배열, 최대 1000개

    for x in range(0, 100):
        Receivers.append(
                    	FaxReceiver(receiveNum='010111222', # 수신번호
                        	        receiveName='수신자명'+str(x), # 수신자명
                            	   )
                    	)

    receiptNum = faxService.sendFax_multi(testValue.testCorpNum, Sender, Receivers, filePath, reserveDT)    

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))