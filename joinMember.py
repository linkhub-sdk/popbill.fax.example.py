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

from popbill import JoinForm, FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
사용자를 연동회원으로 가입처리합니다.
- https://developers.popbill.com/reference/fax/python/api/member#JoinMember
"""

try:
    print("=" * 15 + " 연동회원 가입요청 " + "=" * 15)

    # 회원정보
    newMember = JoinForm(
        # 아이디 (6자 이상 50자 미만)
        ID="join_id_test",
        # 비밀번호 (8자 이상 20자 미만)
        # 영문, 숫자, 특수문자 조합
        Password="password123!@#",
        # 사업자번호 "-" 제외
        CorpNum="0000000000",
        # 대표자성명 (최대 100자)
        CEOName="테스트대표자성명",
        # 상호 (최대 200자)
        CorpName="테스트가입상호",
        # 주소 (최대 300자)
        Addr="테스트회사주소",
        # 업태 (최대 100자)
        BizType="테스트업태",
        # 종목 (최대 100자)
        BizClass="테스트업종",
        # 담당자 성명 (최대 100자)
        ContactName="담당자성명",
        # 담당자 이메일주소 (최대 100자)
        ContactEmail="",
        # 담당자 연락처 (최대 20자)
        ContactTEL="",
    )

    result = faxService.joinMember(newMember)

    print("처리결과 : %d %s" % (result.code, result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
