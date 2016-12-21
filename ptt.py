#coding=utf-8 
import telnetlib
import sys
import time

# CTRL  | http://donsnotes.com/tech/charsets/ascii.html#cntrl
# ESC   | http://www.comptechdoc.org/os/linux/howlinuxworks/linux_hlvt100.html

HOST = 'ptt.cc'

user = input("Enter your account: ")
password =input("Enter your password: ")

def login():
    global tn
    tn = telnetlib.Telnet(HOST)
    
    tn.read_until("請輸入代號".encode('big5'))
    print ("輸入帳號中...")
    tn.write(user.encode('ascii') +b"\r\n")
    
    tn.read_until("請輸入您的密碼".encode('big5'))
    print ("輸入密碼中...")
    tn.write(password.encode('ascii') +b"\r\n")

    time.sleep(5)
    content = tn.read_very_eager().decode('big5','ignore')
    if u"密碼不對" in content:
        print ("密碼不對或無此帳號。程式結束")
        sys.exit()
    if u"請按任意鍵繼續" in content:
        print ("資訊頁面，按任意鍵繼續...")
        tn.write(b"\r\n" )
        content = tn.read_very_eager().decode('big5','ignore')        
    if u"刪除其他重複登入的連線嗎" in content:
        print ("刪除其他重複登入的連線...")
        tn.write(b"Y\r\n" )
        tn.read_until('按任意鍵繼續'.encode('big5'))        
        print ("資訊頁面，按任意鍵繼續...")
        tn.write(b"\r\n" )
        
    if u"刪除以上錯誤" in content:
        tn.write(b"Y\r\n")
        print('刪除錯誤的記錄中...')
        tn.read_until('按任意鍵繼續'.encode('big5'))        
        print ("資訊頁面，按任意鍵繼續...")
        tn.write(b"\r\n" ) 
    print ("----------------------------------------------")
    print ("------------------ 登入完成 ------------------")
    print ("----------------------------------------------")

def logout():
    print("登出中...")
    
    tn.write(b"\EOD\EOD\EOD")
    tn.read_until('主功能表'.encode('big5'))
    
    tn.write(b"g\r\ny\r\n" )
    print ("----------------------------------------------")
    print ("------------------ 登出完成 ------------------")
    print ("----------------------------------------------")
    

def sendemail():
    tn.read_until('主功能表'.encode('big5'))
    print ("成功進入主功能表")
    
    tn.write(b"m\r\n")
    tn.read_until('電子郵件'.encode('big5'))
    print ("成功進入電子郵件")
    
    tn.write(b"s\r\n")
    tn.read_until('站內寄信'.encode('big5'))
    print ("開始使用站內寄信")
    
    print ("輸入使用者ID...")    
    tn.write(b"vocolboy\r\n")    
   
    tn.read_until('主題'.encode('big5'))
    print ("輸入主題中...")        
    tn.write(b"vocolboy\r\n")

    tn.read_until('編輯文章'.encode('big5'))
    print ("輸入內容中...")        
    tn.write(b"vocolboy\r\n")

    print ("檔案處理中...")        
    tn.write(b"\x18")

    tn.read_until('檔案處理'.encode('big5'))
    print ("發信")            
    tn.write(b"S\r\n")

    tn.read_until('已順利寄出'.encode('big5'))
    print ("已順利寄出，是否自存底稿 (現在不存)")        
    tn.write(b"n\r\n")

    tn.read_until('按任意鍵繼續'.encode('big5'))
    print ("按任意鍵繼續...") 

def main():
    login()
    sendemail()
    logout()

if __name__=="__main__" :
    main()


