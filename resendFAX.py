# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest

'''
팩스를 재전송합니다.
- 전송일기준 180일이 경과되지 않은 팩스전송건만 재전송할 수 있습니다.
'''

try:
    print("=" * 15 + " 팩스 재전송. 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팩스 접수번호
    ReceiptNum = '017021616003700001'

    # 발신번호, 공백처리시 기존전송정보로 재전송
    Sender = '07043042991'

    # 발신자명, 공백처리시 기존전송정보로 재전송
    SenderName = '발신자명'

    # 수신번호/수신자명 모두 공백처리시 기존전송정보로 재전송
    # 수신번호
    Receiver = ''

    # 수신자명
    ReceiverName = ''

    receiptNum = faxService.resendFax(CorpNum, ReceiptNum, Sender, SenderName, Receiver, ReceiverName)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
