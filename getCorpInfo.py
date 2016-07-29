# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 회사정보 확인 " + "=" * 15)

    ''' CorpInfo 구성
                ceoname     (담당자 아이디)
                corpName    (담당자 성명)
                addr        (이메일)
                bizType     (휴대폰번호)
                bizClass    (팩스번호)
    '''

    response = faxService.getCorpInfo(testValue.testCorpNum, testValue.testUserID)

    tmp = "ceonaem : " + response.ceoname + "\n"
    tmp += "corpName : " + response.corpName + "\n"
    tmp += "addr : " + response.addr + "\n"
    tmp += "bizType : " + response.bizType + "\n"
    tmp += "bizClass : " + response.bizClass + "\n"
    print(tmp);

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
