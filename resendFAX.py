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

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 팩스 접수번호
    ReceiptNum = '017071811581700001'

    # 발신번호, 공백처리시 기존전송정보로 재전송
    Sender = '07043042991'

    # 발신자명, 공백처리시 기존전송정보로 재전송
    SenderName = '발신자명'

    # 수신번호/수신자명 모두 공백처리시 기존전송정보로 재전송
    # 수신번호
    Receiver = ''

    # 수신자명
    ReceiverName = ''

    # 예약전송시간, 공백시 즉시전송, 작성형태 yyyyMMddHHmmss
    ReserveDT = ''

    # 팩스제목
    Title = '팩스 재전송 제목'

    receiptNum = faxService.resendFax(CorpNum, ReceiptNum, Sender, SenderName,
        Receiver, ReceiverName, ReserveDT, UserID, Title)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
