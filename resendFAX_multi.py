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

'''
팩스를 재전송합니다.
- 전송일기준 180일이 경과되지 않은 팩스전송건만 재전송할 수 있습니다.
'''

try:
    print("=" * 15 + " 팩스 동보 재전송. (최대 1000건) " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팩스 접수번호
    ReceiptNum = '017021616224500001'

    # 발신번호, 공백처리시 기존전송정보로 재전송
    Sender = '07043042991'

    # 발신자명, 공백처리시 기존전송정보로 재전송
    SenderName = '발신자명'

    # 예약전송시간, 공백시 즉시전송, 작성형태 yyyyMMddHHmmss
    reserveDT = ''

    # 수신정보 배열 None 처리시 기존전송정보로 전송
    Receivers = None

    # 수신자 정보가 기존전송정보와 다를경우 아래의 코드 참조
    """
    Receivers = [] # 수신정보 배열, 최대 1000개
    for x in range(0, 10):
        Receivers.append(
        	FaxReceiver(
                receiveNum = '010111222', # 수신번호
            	receiveName = '수신자명'+str(x), # 수신자명
            )
        )
    """

    receiptNum = faxService.resendFax_multi(CorpNum, ReceiptNum, Sender,
        SenderName, Receivers, reserveDT)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
