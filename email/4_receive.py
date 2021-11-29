from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com",993)
# INBOX = 받은 편지함
mailbox.login(EMAIL_ADDRESS,EAMIL_PASSWORD, initial_folder="INBOX")

# limit = 제한수 / reverse = 최신부터 가져옴.
for msg in mailbox.fetch(limit=1, reverse=True):
    print(f"제목 : {msg.subject}")
    print(f"발신자 : {msg.from_}")
    print(f"수신자 : {msg.to}")
    print(f"참조자 : {msg.cc}")
    print(f"비밀참조자 : {msg.bcc}")
    print(f"날짜 : {msg.date}")
    print(f"본문 : {msg.text}")
    print(f"HTML 메시지 : {msg.html}")
    print("="*30)
    # 첨부 파일 
    for att in msg.attachments:
        print("첨부파일 이름 ", att.filename)
        print("첨부파일 타입 ", att.content_type)
        print("첨부파일 크기 ", att.size)

        # 파일 다운로드
        with open(f"download_{att.filename}".replace("/",""), "wb") as f:
            f.write(att.payload)
            print(f"첨부파일 {att.filename} 다운로드 완료")

mailbox.logout()