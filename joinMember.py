# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import JoinForm, FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest

'''
팝빌 연동회원 가입을 요청합니다.
'''

try:
    print("=" * 15 + " 연동회원 가입요청 " + "=" * 15)

    # 회원정보
    newMember = JoinForm(

        # 회원아이디, 최대 20자
        ID = "testkorea1118",

        # 비밀번호, 최대 20자
        PWD = "this_is_password",

        # 사업자번호
        CorpNum = "1234567890",

        # 상호
        CorpName = "테스트가입상호",

        # 대표자성명
        CEOName = "테스트대표자성명",

        # 주소
        Addr = "테스트 회사 주소",

        # 업태
        BizType = "테스트업태",

        # 종목
        BizClass = "테스트업종",

        # 담당자 성명
        ContactName = "담당자성명",

        # 담당자 연락처
        ContactTEL = "070-4304-2991",

        # 담당자 휴대폰번호
        ContactHP = "010-2222-3333",

        # 담당자 팩스번호
        ContactFAX = "070-4304-2991",

        # 담당자 메일주소
        ContactEmail = "test@test.com"
    )

    result = faxService.joinMember(newMember)

    print("처리결과 : %d %s" % (result.code,result.message) )
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
