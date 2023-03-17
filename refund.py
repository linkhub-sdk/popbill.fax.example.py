# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import FaxService, PopbillException, RefundForm

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원 포인트를 환불 신청합니다.
- https://developers.popbill.com/reference/fax/python/api/point#Refund
"""

try:
    print("=" * 15 + " 환불 신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 환불 신청 객체 정보
    refundForm = RefundForm(
        contactname="환불신청테스트",
        tel="01077777777",
        requestpoint="10",
        accountbank="국민",
        accountnum="123123123-123",
        accountname="예금주",
        reason="테스트 환불 사유",
    )

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    response = faxService.refund(CorpNum, refundForm, UserID)

    print(" code (요청에 대한 응답 상태 코드) : %s" % response.code)
    print(" message (요청에 대한 응답 메시지) : %s" % response.message)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
