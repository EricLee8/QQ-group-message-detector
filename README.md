# QQ-group-message-detector
## Description
This is a repo containing a tool that can automatically detect the new message (only text) from a QQ group, and once it gets a new message containing some certain keywords, it will send an E-mail to a mail address that you can choose.
## requirement
- python3
- pandas
- uiautomation
## usage
After installing all requirement, you need to:  
- Seperate the QQ group window. (在消息列表中右键QQ群，选择分离当前会话）
- Modify some customized information in the code (group name, your interested keywords and the mail address etc.)
- Run the code with Python
For QQ SMTP authorization code, follow [this blog](https://blog.csdn.net/mao_hui_fei/article/details/105548814)
