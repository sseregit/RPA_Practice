from imap_tools import MailBox
from account import *

# logout 처리까지해줘야함.
mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EAMIL_PASSWORD, initial_folder="INBOX")
mailbox.logout

# logout을 안해도됨.
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EAMIL_PASSWORD, initial_folder="INBOX") as mailbox:    
    #  전체 메일 다 가져오기.
    for msg in mailbox.fetch():
        print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일 가져오기 (UNSEEN) query이다.
    for msg in mailbox.fetch('(UNSEEN)'):
        print("[{}] {}".format(msg.from_, msg.subject))

    # 특정인이 보낸 메일 가져오기.
    for msg in mailbox.fetch('(FROM {})'.format(EMAIL_ADDRESS)):
        print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자가 포함하는 메일(제목 or 본문) 띄어쓰기로 단어 단어 구분됨.
    for msg in mailbox.fetch('(TEXT "test")'):
        print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자를 포함하는 메일 (제목만)
    for msg in mailbox.fetch('(SUBJECT "test")'):
        print("[{}] {}".format(msg.from_, msg.subject))

    # 어떤 글자(한글)을 포함하는 메일 필터링
    for msg in mailbox.fetch():
        if "테스트" in msg.subject:
            print("[{}] {}".format(msg.from_, msg.subject)) 
    
    # 특정 날짜 이후의 메일
    for msg in mailbox.fetch('(SENTSINCE 27-Nov-2021)'):
        print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜에 온 메일
    for msg in mailbox.fetch('(ON 07-Nov-2020)'):
        print("[{}] {}".format(msg.from_, msg.subject))

    # 2가지 이상의 조건을 모두 만족하는 메일
    # 띄어쓰기로 쿼리를 계속 이어가면됨.
    for msg in mailbox.fetch('(ON 27-Nov-2021 SUBJECT "test)'):                
        print("[{}] {}".format(msg.from_, msg.subject)) 

    # 2가지 이상의 조건중 하나만 만족하는 메일
    # 맨앞에 OR 추가
    for msg in mailbox.fetch('(OR ON 27-Nov-2021 SUBJECT "test)'):                
        print("[{}] {}".format(msg.from_, msg.subject)) 

    