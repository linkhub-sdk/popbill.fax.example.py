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

    # 발신번호
    Sender = '07075103710'

    # 발신자명
    SenderName = '발신자명'

    # 파일경로
    filePath = 'test.jpeg'

    # 예약전송시간, 공백시 즉시전송, 작성형태 yyyyMMddHHmmss
    reserveDT = ''



    Receivers = [] # 수신정보 배열, 최대 1000개
    for x in range(0, 100):
        Receivers.append(
                    	FaxReceiver(receiveNum='010111222', # 수신번호
                        	        receiveName='수신자명'+str(x), # 수신자명
                            	   )
                    	)

    receiptNum = faxService.sendFax_multi(testValue.testCorpNum, Sender, SenderName, Receivers, filePath, reserveDT)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
