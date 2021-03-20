import os
import time
import pandas as pd
import uiautomation as auto
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


class MessgaeListener(object):
    def __init__(self,  group_name='你的QQ群名', key_words=['好东西', 'good thing']):
        self.dialog_box = auto.WindowControl(searchDepth=1, ClassName='TXGuiFoundation', Name=group_name)
        self.key_words = key_words
    
    def get_new_msg(self):
        self.dialog_box.SetActive()
        self.dialog_box.Maximize()
        message_win = self.dialog_box.ListControl(Name='消息', searchDepth=13)
        message_win.Click()
        auto.Click(800, 800)
        message_win.SendKeys('{Ctrl}A')
        message_win.SendKeys('{Ctrl}C')
        df = pd.read_clipboard(sep=r"\s+", encoding='utf-8', error_bad_lines=False)
        if not os.path.exists("message_tmp.txt"):
            df.to_csv('message_tmp.txt', index=False, sep=' ', encoding='utf_8_sig')
        with open("message_tmp.txt", "r", encoding='utf_8_sig') as f:
            ori_lines = f.readlines()
        df.to_csv('message_tmp.txt', index=False, sep=' ', encoding='utf_8_sig')
        with open("message_tmp.txt", "r", encoding='utf_8_sig') as f:
            cur_lines = f.readlines()
        new_lines = []
        for line in cur_lines:
            if line not in ori_lines:
                new_lines.append(line)
        return new_lines

    def check_key_words(self, lines):
        for line in lines:
            for kw in self.key_words:
                if kw in line:
                    return True
        return False

    def listen(self, time_interval=5):
        while True:
            new_lines = self.get_new_msg()
            if self.check_key_words(new_lines):
                print("Got target message!!!")
            time.sleep(time_interval)

    def send_mail(self, msg_text="有新的XXXX啦！！！"):
        from_addr = "你的QQ号@qq.com"
        from_pwd = "QQ SMTP的授权码"
        to_addr = "接收者的QQ号@qq.com"
        smtp_srv = "smtp.qq.com"
        msg = MIMEText(msg_text, "plain", "utf-8")
        msg['From'] = formataddr(["发送者的昵称", from_addr])
        msg['To'] = formataddr(["接收者的昵称", to_addr])
        msg['Subject'] = "随便写点什么"
        try:
            srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
            srv.login(from_addr, from_pwd)
            srv.sendmail(from_addr, [to_addr], msg.as_string())
            print('successfully sent')
        except Exception as e:
            print('error occured', e)
        finally:
            srv.quit()


if __name__ == '__main__':
    listener = MessgaeListener()
    listener.listen()
