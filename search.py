# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService,PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 팩스 전송내역 조회 " + "=" * 15)

    SDate = "20160601"
    EDate = "20160831"
    State = ["1","2","3","4"]
    ReserveYN = False
    SenderOnly = False
    Page = 1
    PerPage = 10
    Order = "D"

    response = faxService.search(testValue.testCorpNum, SDate, EDate, State, ReserveYN,
                        SenderOnly, Page, PerPage, Order, testValue.testUserID)
    print("code (응답코드) : %s " % response.code)
    print("message (응답메시지) : %s " % response.message)
    print("total (검색결과 건수) : %s " % response.total)
    print("perPage (페이지당 검색개수) : %s " % response.perPage)
    print("pageNum (페에지 번호) : %s " % response.pageNum)
    print("pageCount (페이지 개수) : %s \n" % response.pageCount)

    i = 1
    for info in response.list :
        print("====== 팩스 전송정보 [%d] ======"% i)
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        i += 1
        print("")



except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
