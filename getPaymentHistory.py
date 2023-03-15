# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
연동회원의 포인트 결제내역을 확인합니다.
- https://developers.popbill.com/reference/fax/python/api/point#GetPaymentHistory
'''

try:
    print("=" * 15 + " 포인트 결제내역 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 조회 기간의 시작일자 (형식 : yyyyMMdd)
    SDate	= "20230101"

    # 조회 기간의 종료일자 (형식 : yyyyMMdd)
    EDate	= "20230107"

    # 목록 페이지번호 (기본값 1)
    Page	= 1

    # 페이지당 표시할 목록 개수 (기본값 500, 최대 1,000)
    PerPage	= 500

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    paymentHistoryResult = faxService.getPaymentHistory(CorpNum, SDate,EDate,Page,PerPage, UserID)

    print(" code (요청에 대한 응답 상태 코드) : %s" % paymentHistoryResult.code)
    print(" total (총 검색결과 건수) : %s" % paymentHistoryResult.chargeMethod)
    print(" perPage (페이지당 검색 개수) : %s" % paymentHistoryResult.chargeMethod)
    print(" pageNum (페이지 번호) : %s" % paymentHistoryResult.chargeMethod)
    print(" pageCount (페이지 개수) : %s" % paymentHistoryResult.rateSystem)

    for paymentHistory in paymentHistoryResult:
        print(" 결제 내용 : '포인트' / '정액제' / '미수금' 중 반환 %s" %paymentHistory.productType)
        print(" 정액제 상품명 %s" %paymentHistory.productName)
        print(" 결제유형 : '무통장' / '신용카드' / '실시간계좌이체' 중 반환 %s" %paymentHistory.settleType)
        print(" 담당자명 %s" %paymentHistory.settlerName)
        print(" 담당자메일 %s" %paymentHistory.settlerEmail)
        print(" 결제금액 %s" %paymentHistory.settleCost)
        print(" 충전포인트 %s" %paymentHistory.settlePoint)
        print(" 결제상태 : 1 / 2 / 3 / 4 / 5 중 반환 %s" %paymentHistory.settleState)
        print(" 등록일시 (형식 : yyyyMMddHHmmss) %s" %paymentHistory.regDT)
        print(" 상태일시 (형식 : yyyyMMddHHmmss) %s" %paymentHistory.stateDT)
        print("*" * 50)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
