# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("팩스전송. 1파일 1건 전송")

    # 발신번호
    Sender = '07075103710'

    # 발신자명
    SenderName = '발신자명'

    # 수신번호
    Receiver = '010111222'

    # 수신자명
    ReceiverName = '수신자명'

    #파일경로
    FilePath = 'test2.jpeg'

    receiptNum = faxService.sendFax(testValue.testCorpNum, Sender, SenderName, Receiver, ReceiverName, FilePath)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
