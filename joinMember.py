# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import JoinForm,FaxService,PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

newMember = JoinForm(CorpNum = testValue.testCorpNum,
                        CorpName = "테스트가입상호",
                        CEOName = "테스트대표자성명",
                        Addr = "테스트 회사 주소",
                        ZipCode = "123-231",
                        BizType = "테스트업태",
                        BizClass = "테스트업종",
                        ID = "testUserID",
                        PWD = "testPassword",
                        ContactName = "담당자성명",
                        ContactTEL = "070-7510-6766",
                        ContactHP = "010-2222-3333",
                        ContactFAX = "070-7510-6767",
                        ContactEmail = "test@test.com")
try:
    print("연동회원 가입")
    result = faxService.joinMember(newMember)
    print("처리결과 : %d %s" % (result.code,result.message) )
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))