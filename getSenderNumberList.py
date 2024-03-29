# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import imp
import sys

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue
from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
팝빌에 등록한 연동회원의 팩스 발신번호 목록을 확인합니다.
- https://developers.popbill.com/reference/fax/python/api/sendnum#GetSenderNumberList
"""

try:
    print("=" * 15 + " 팩스전송 발신번호 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    senderList = faxService.getSenderNumberList(CorpNum)

    i = 1
    for f in senderList:
        print("SenderInfo[%d] : " % i)
        print("    number (발신번호) : %s" % f.number)
        print("    representYN (대표번호 지정여부) : %s" % f.representYN)
        print("    state (등록상태) : %s" % f.state)
        print("    memo (메모) : %s" % f.memo)
        i += 1

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
