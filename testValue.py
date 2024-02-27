# -*- coding: utf-8 -*-

"""
팝빌 팩스 API Python SDK Example

Python 연동 튜토리얼 안내 : https://developers.popbill.com/guide/fax/python/getting-started/tutorial
업데이트 일자 : 2024-02-27
연동 기술지원 연락처 : 1600-9854
연동 기술지원 이메일 : code@linkhubcorp.com

<테스트 연동개발 준비사항>
1) API Key 변경 (연동신청 시 메일로 전달된 정보)
    - LinkID : 링크허브에서 발급한 링크아이디
    - SecretKey : 링크허브에서 발급한 비밀키
2) SDK 환경설정 옵션 설정
    - IsTest : 연동환경 설정, True-테스트, False-운영(Production), (기본값:True)
    - IPRestrictOnOff : 인증토큰 IP 검증 설정, True-사용, False-미사용, (기본값:True)
    - UseStaticIP : 통신 IP 고정, True-사용, False-미사용, (기본값:False)
    - UseLocalTimeYN : 로컬시스템 시간 사용여부, True-사용, False-미사용, (기본값:True)
3) 발신번호 사전등록을 합니다. (등록방법은 사이트/API 두가지 방식이 있습니다.)
    - 1. 팝빌 사이트 로그인 > [문자/팩스] > [팩스] > [발신번호 사전등록] 메뉴에서 등록
    - 2. getSenderNumberMgtURL API를 통해 반환된 URL을 이용하여 발신번호 등록
"""

# 링크아이디
LinkID = "TESTER"

# 비밀키
SecretKey = "SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I="

# 연동환경 설정, True-테스트, False-운영(Production), (기본값:True)
IsTest = True

# 인증토큰 IP 검증 설정, True-사용, False-미사용, (기본값:True)
IPRestrictOnOff = True

# 통신 IP 고정, True-사용, False-미사용, (기본값:False)
UseStaticIP = False

# 로컬시스템 시간 사용여부, True-사용, False-미사용, (기본값:True)
UseLocalTimeYN = True

# 테스트 회원 사업자번호
testCorpNum = "1234567890"

# 테스트 회원 팝빌 아아디
testUserID = "testkorea"
