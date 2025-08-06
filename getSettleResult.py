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
연동회원 포인트 무통장 입금신청내역 1건을 확인합니다.
- https://developers.popbill.com/reference/fax/python/common-api/point#GetSettleResult
"""

try:
    print("=" * 15 + " 무통장 입금신청 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 정산코드
    SettleCode = "202303070000000052"

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    paymentHistory = faxService.getSettleResult(CorpNum, SettleCode, UserID)

    print("결제 내용 : %s" % paymentHistory.productType)
    print("정액제 상품명 : %s" % paymentHistory.productName)
    print("결제유형 : %s" % paymentHistory.settleType)
    print("담당자명 : %s" % paymentHistory.settlerName)
    print("담당자메일 : %s" % paymentHistory.settlerEmail)
    print("결제금액 : %s" % paymentHistory.settleCost)
    print("충전포인트 : %s" % paymentHistory.settlePoint)
    print("결제상태 : %s" % paymentHistory.settleState)
    print("등록일시 : %s" % paymentHistory.regDT)
    print("상태일시 : %s" % paymentHistory.stateDT)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
