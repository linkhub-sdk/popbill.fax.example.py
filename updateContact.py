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
from popbill import ContactInfo, FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원의 담당자 정보를 수정합니다.
- https://developers.popbill.com/reference/fax/python/common-api/member#UpdateContact
"""

try:
    print("=" * 15 + " 담당자 정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    updateInfo = ContactInfo(

        # 담당자 아이디
        id=UserID,

        # 담당자 성명 (최대 100자)
        personName="담당자 성명",

        # 담당자 휴대폰 (최대 20자)
        tel="",

        # 담당자 메일 (최대 100자)
        email="",

        # 권한, 1(개인) 2(읽기) 3(회사)
        searchRole=1,
    )

    result = faxService.updateContact(CorpNum, updateInfo)

    print("처리결과 : [%d] %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
