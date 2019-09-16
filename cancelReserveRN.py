# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
팩스전송요청시 할당한 전송요청번호(requestNum)로 팩스 예약전송건을 취소합니다.
- 예약전송 취소는 예약전송시간 10분전까지 가능합니다.
'''

try:
    print("=" * 15 + " 예약팩스 전송취소 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 예약 팩스전송 요청시 할당한 전송요청번호(requestNum)
    requestNum = "20190117-001"

    result = faxService.cancelReserveRN(CorpNum, requestNum)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
