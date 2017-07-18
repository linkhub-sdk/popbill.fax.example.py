# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest

'''
검색조건을 사용하여 팩스전송 내역을 조회합니다.
'''

try:
    print("=" * 15 + " 팩스 전송내역 조회 " + "=" * 15)

    CorpNum = testValue.testCorpNum

    UserID = testValue.testUserID

    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20170101"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20170731"

    # 팩스전송상태 배열, 1(대기), 2(성공), 3(실패), 4(취소)
    State = ["1","2","3","4"]

    # 예약전송 검색여부, True-예약전송건 조회, False-전체조회
    ReserveYN = False

    # 개인조회 여부, True-개인조회, False-회사조회
    SenderOnly = False

    # 페이지 번호
    Page = 1

    # 페이지당 목록갯수, 기본값 500
    PerPage = 10

    # 정렬방향, D-내림차순, A-오름차순
    Order = "D"

    response = faxService.search(CorpNum, SDate, EDate, State, ReserveYN, SenderOnly,
        Page, PerPage, Order, UserID)

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
            print("    %s : %s" % (key, value))
        i += 1
        print("")



except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
