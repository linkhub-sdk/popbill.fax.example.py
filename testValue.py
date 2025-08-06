# -*- coding: utf-8 -*-

"""
팝빌 팩스 API Python SDK Example

Python 연동 튜토리얼 안내 : https://developers.popbill.com/guide/fax/python/getting-started/tutorial
업데이트 일자 : 2025-08-06
연동 기술지원 연락처 : 1600-9854
연동 기술지원 이메일 : code@linkhubcorp.com
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

# 팝빌회원 사업자번호
testCorpNum = "1234567890"

# 팝빌회원 아아디
testUserID = "testkorea"
