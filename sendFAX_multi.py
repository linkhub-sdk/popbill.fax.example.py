# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, FaxReceiver, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 팩스전송. 1파일 동보전송(최대 1000건) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID


    # 발신번호
    Sender = '07043042991'

    # 발신자명
    SenderName = '발신자명'

    # 파일경로 (해당파일에 읽기 권한이 설정되어 있어야 함. 최대 20개)
    FilePath = ['test.jpeg', 'test2.jpeg']

    # 광고팩스 전송여부
    AdsYN = False

    # 예약전송시간, None처리시 즉시전송, 작성형태 'yyyyMMddHHmmss'
    ReserveDT = None

    # 팩스제목
    Title = 'Python 팩스동보전송 제목'

    Receivers = [] # 수신정보 배열, 최대 1000개
    for x in range(0, 5):
        Receivers.append(
        	FaxReceiver(
                receiveNum = '070111222', # 수신번호
            	receiveName = '수신자명'+str(x), # 수신자명
            )
        )

    receiptNum = faxService.sendFax_multi(CorpNum, Sender, Receivers,
        FilePath, ReserveDT, UserID, SenderName, AdsYN, Title)

    print("receiptNum (접수번호) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
