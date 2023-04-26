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
 * 포인트 환불에 대한 상세정보 1건을 확인합니다.
- https://developers.popbill.com/reference/fax/python/api/point#GetRefundInfo
"""

try:
    print("=" * 15 + " 환불 신청 상태 조회 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 환불코드
    RefundCode = "023040000017"

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    response = faxService.GetRefundInfo(CorpNum, RefundCode, UserID)

    print("reqDT (신청일시) : %s " % response.reqDT)
    print("requestPoint (환불 신청포인트) : %s " % response.requestPoint)
    print("accountBank (환불계좌 은행명) : %s " % response.accountBank)
    print("accountNum (환불계좌번호) : %s " % response.accountNum)
    print("accountName (환불계좌 예금주명) : %s " % response.accountName)
    print("state (상태) : %s " % response.state)
    print("reason (환불사유) : %s " % response.reason)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
