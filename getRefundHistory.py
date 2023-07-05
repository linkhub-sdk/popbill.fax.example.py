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
연동회원의 포인트 환불신청내역을 확인합니다.
- https://developers.popbill.com/reference/fax/python/api/point#GetRefundHistory
"""

try:
    print("=" * 15 + " 환불 신청내역 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 목록 페이지 번호
    Page = 1

    # 페이지당 표시할 목록 갯수
    PerPage = 500

    # 팝빌회원 팝빌 아이디
    UserID = testValue.testUserID

    refundHistoryResult = faxService.getRefundHistory(CorpNum, Page, PerPage, UserID)

    print(" code (요청에 대한 응답 상태 코드) : %s" % refundHistoryResult.code)
    print(" total (총 검색결과 건수) : %s" % refundHistoryResult.total)
    print(" perPage (페이지당 검색 개수) : %s" % refundHistoryResult.perPage)
    print(" pageNum (페이지 번호) : %s" % refundHistoryResult.pageNum)
    print(" pageCount (페이지 개수) : %s" % refundHistoryResult.pageCount)

    for refundHistory in refundHistoryResult.list:
        print("=" * 15 + " RefundHistory (환불내역) " + "=" * 15)
        print("reqDT (신청일시) : %s" % refundHistory.reqDT)
        print("requestPoint (환불 신청포인트) : %s" % refundHistory.requestPoint)
        print("accountBank (환불계좌 은행명) : %s" % refundHistory.accountBank)
        print("accountNum (환불계좌번호) : %s" % refundHistory.accountNum)
        print("accountName (환불계좌 예금주명) : %s" % refundHistory.accountName)
        print("state (상태) : %s" % refundHistory.state)
        print("reason (환불사유) : %s" % refundHistory.reason)
        print("*" * 50)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
