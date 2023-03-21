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
연동회원의 포인트 사용내역을 확인합니다.
- https://developers.popbill.com/reference/fax/python/api/point#GetUseHistory
"""

try:
    print("=" * 15 + " 포인트 사용내역 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회 기간의 시작일자 (형식 : yyyyMMdd)
    SDate = "20230101"

    # 조회 기간의 종료일자 (형식 : yyyyMMdd)
    EDate = "20230131"

    # 목록 페이지번호 (기본값 1)
    Page = 1

    # 페이지당 표시할 목록 개수 (기본값 500, 최대 1,000)
    PerPage = 500

    # 거래일자를 기준으로 하는 목록 정렬 방향 ("D"(기본값), "A" 중 택 1)
    Order = "D"

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    useHistoryResult = faxService.getUseHistory(CorpNum,SDate,EDate,Page,PerPage,Order,UserID)

    print(" code (요청에 대한 응답 상태 코드) : %s" % useHistoryResult.code)
    print(" total (총 검색결과 건수) : %s" % useHistoryResult.total)
    print(" perPage (페이지당 검색 개수) : %s" % useHistoryResult.perPage)
    print(" pageNum (페이지 번호) : %s" % useHistoryResult.pageNum)
    print(" pageCount (페이지 개수) : %s" % useHistoryResult.pageCount)

    for useHistory in useHistoryResult.list:
        print(" itemCode (서비스코드) : %s" % useHistory.itemCode)
        print(" txType (포인트 증감 유형) : %s" % useHistory.txType)
        print(" txPoint (증감 포인트) : %s" % useHistory.txPoint)
        print(" balance (잔여포인트) : %s" % useHistory.balance)
        print(" txDT (포인트 증감 일시) : %s" % useHistory.txDT)
        print(" userID (담당자 아이디) : %s" % useHistory.userID)
        print(" userName (담당자명) : %s" % useHistory.userName)
        print("*" * 50)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
