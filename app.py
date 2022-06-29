
from instabot import Bot
bot = Bot()
user_name = input("eneter your username for instagram : ")
pass_word = input("Enter the password for your account : ")
bot.login(username = user_name , password = pass_word)


query = input("what do you want to do ? ")

if 'follow' in query :
    p_tofollor = input("enter the username of person to follow : ")
    bot.follow(p_tofollor)
elif 'post' in query:
    file_toupload = input("drag the file to this folder and enter the name here : ")
    caption = input("enter the caption to insert ; ")
    bot.upload_photo(file_toupload , caption)
elif 'message' in query :
    msg = input("enter the message that is to be sent")
    msgto_ap = input("enter the id of person to whom the message is to be sent: ")
    bot.send_message(msg,msgto_ap)
elif 'messsage to a group' in query :
    msg_g = input("enter the message that is to sent")
    person1 = input("enter the id of first person  : ")
    person2 = input("enter the id of second person  : ")
    group1 = [person1 , person2]
    bot.send_message(msg_g , group1)
elif 'block' in query :
    user_targetted = input("enter the id of person that is to be blocked : ")
    bot.block(user_targetted)
elif 'download' in query :
    urll = input("enter the url : ")
    bot.download_photo(urll , "downloaded_media" , "download.png" ,False)
elif 'comment' in query :
    comment__t = input("enter the comment : ")
    url_l = input("enter the url of the media : ")
    bot.comment(url_l , comment__t)
elif 'followers' in query:
    targetted_user = input("who is to be targetted ; ")
    foll_owers = bot.get_user_followers(targetted_user)
    print(foll_owers)
    

