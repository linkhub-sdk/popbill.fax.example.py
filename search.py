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

'''
검색조건을 사용하여 팩스전송 내역을 조회합니다.
- https://docs.popbill.com/fax/python/api#Search
'''

try:
    print("=" * 15 + " 팩스 전송내역 조회 " + "=" * 15)

    CorpNum = testValue.testCorpNum

    UserID = testValue.testUserID

    # 최대 검색기간 : 6개월 이내
    # 시작일자, 날짜형식(yyyyMMdd)
    SDate = "20200701"

    # 종료일자, 날짜형식(yyyyMMdd)
    EDate = "20201231"

    # 팩스전송상태 배열, 1(대기), 2(성공), 3(실패), 4(취소)
    State = ["1", "2", "3", "4"]

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

    for info in response.list:
        print("    state (전송상태 코드) : %s" % info.state)
        print("    result (전송결과 코드) : %s" % info.result)
        print("    sendNum (발신번호) : %s" % info.sendNum)
        print("    senderName (발신자명) : %s" % info.senderName)
        print("    receiveNum (수신번호) : %s" % info.receiveNum)
        print("    receiveName (수신자명) : %s" % info.receiveName)
        print("    title (팩스제목) : %s" % info.title)
        print("    sendPageCnt (전체 페이지수) : %s" % info.sendPageCnt)
        print("    successPageCnt (성공 페이지수) : %s" % info.successPageCnt)
        print("    failPageCnt (실패 페이지수) : %s" % info.failPageCnt)
        print("    refundPageCnt (환불 페이지수) : %s" % info.refundPageCnt)
        print("    cancelPageCnt (취소 페이지수) : %s" % info.cancelPageCnt)
        print("    reserveDT (예약일시) : %s" % info.reserveDT)
        print("    receiptDT (접수일시) : %s" % info.receiptDT)
        print("    sendDT (발송일시) : %s" % info.sendDT)
        print("    resultDT (전송결과 수신일시) : %s" % info.resultDT)
        print("    fileNames (전송 파일명 리스트) : %s" % info.fileNames)
        print("    receiptNum (접수번호) : %s" % info.receiptNum)
        print("    requestNum (요청번호) : %s" % info.requestNum)
        print("    chargePageCnt (과금 페이지수) : %s" % info.chargePageCnt)
        print("    tiffFileSize (변환파일용랑(단위 : byte)) : %s" % info.tiffFileSize + '\n')
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
