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
from popbill import FaxService, PaymentForm, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원 포인트 충전을 위해 무통장입금을 신청합니다.
- https://developers.popbill.com/reference/fax/python/api/point#PaymentRequest
"""

try:
    print("=" * 15 + " 무통장 입금신청 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 입금신청 객체정보
    paymentForm = PaymentForm(
        # 담당자명
        settlerName="담당자",

        # 담당자 이메일
        settlerEmail="settler@Email.com",

        # 담당자 휴대폰
        notifyHP="01012341234",

        # 입금자명
        paymentName="입금자이름",

        # 결제금액
        settleCost="10000",
    )

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    paymentResponse = faxService.paymentRequest(CorpNum, paymentForm, UserID)

    print("code (응답코드) : %s" % paymentResponse.code)
    print("message (응답메시지) : %s" % paymentResponse.message)
    print("settleCode (정산코드) : %s" % paymentResponse.settleCode)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
