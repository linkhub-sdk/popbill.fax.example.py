# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import ContactInfo, FaxService ,PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

newContact = ContactInfo (
                        id = "testkorea_0729",
                        pwd = "popbill",
                        personName = "정씨네",
                        tel = "010-1234-1234",
                        hp = "010-4324-5117",
                        fax = "070-7510-3710",
                        email = "code@linkhub.co.kr",
                        searchAllAllowYN = True,
                        mgrYN = True
                        )
try:
    print("=" * 15 + " 담당자 등록 " + "=" * 15)

    result = faxService.registContact(testValue.testCorpNum, newContact, testValue.testUserID)

    print("처리결과 : [%d] %s" % (result.code,result.message))
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
