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

try:
    print("=" * 15 + " 팩스전송. 1파일 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID


    # 발신번호
    Sender = '07043042991'

    # 발신자명
    SenderName = '발신자명'

    # 수신번호
    Receiver = '070111222'

    # 수신자명
    ReceiverName = '수신자명'

    # 파일경로
    FilePath = 'test2.jpeg'

    # 예약전송일시, None처리시 즉시전송, 작성형태 'yyyyMMddHHmmss'
    ReserveDT = None

    # 광고팩스 전송여부
    AdsYN = False

    # 팩스제목
    Title = "Python 팩스단건 제목"

    receiptNum = faxService.sendFax(CorpNum, Sender, Receiver, ReceiverName,
        FilePath, ReserveDT, UserID, SenderName, AdsYN, Title)

    print("receiptNum (접수번호) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
