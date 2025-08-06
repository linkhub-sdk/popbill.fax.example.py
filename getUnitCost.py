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
팩스 전송단가를 확인합니다.
- https://developers.popbill.com/reference/fax/python/common-api/point#GetUnitCost
"""

try:
    print("=" * 15 + " 팩스 전송단가 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 수신번호 유형 : "일반" / "지능" 중 택 1
    # └ 일반망 : 지능망을 제외한 번호
    # └ 지능망 : 030*, 050*, 070*, 080*, 대표번호
    receiveNumType = "지능"

    unitCost = faxService.getUnitCost(CorpNum, receiveNumType)

    print("전송단가 : %f" % unitCost)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
