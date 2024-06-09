#!/usr/local/bin/python3.12
#l(" ▚   ▗▘")
#l("  ▚▄▄▘")
#l("  ▌▖▖▌")
#l("  ▚▄▄▘ VK-notify")

vkbot_token = "токен вк"
vkbot_gid = 123123123 # подставьте GID группы с ботом
peer_id="123123123"   # подставьте свой ID
 
def l(t):
    print(f"[VK-Notify] {t}")

l("VK-Notify: start")

try:
    import time, random
    import vk_api
    from vk_api import VkApi
    from vk_api import VkUpload
    from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
    from math import ceil
    import argparse
except Exception as e:
    print(f"Error: {e}")

def rid():
    return random.randint(-2147483647, 2147483647)

def convertint(stime): # convertint, but by aGrIk and better :D
    days = int(stime // 86400)
    mod = int(stime % 86400)
    hours = mod // 3600
    mod = mod % 3600
    minutes = mod // 60
    seconds = mod % 60

    ret = ""
    if days != 0:
        ret += str(days)
        last_days = days % 10
        if last_days == 0 or 5 <= last_days <= 9 or days // 10 == 1:
            ret += " дней "
        elif last_days == 1:
            ret += " день "
        else:
            ret += " дня "

    if hours != 0:
        ret += str(hours)
        last_hours = hours % 10
        if last_hours == 0 or 5 <= last_hours <= 9 or hours // 10 == 1:
            ret += " часов "
        elif last_hours == 1:
            ret += " час "
        else:
            ret += " часа "

    if minutes != 0:
        ret += str(minutes)
        last_minutes = minutes % 10
        if last_minutes == 0 or 5 <= last_minutes <= 9 or minutes // 10 == 1:
            ret += " минут "
        elif last_minutes == 1:
            ret += " минута "
        else:
            ret += " минуты "

    if ret == "" or seconds != 0:
        ret += str(seconds)
        last_sec = seconds % 10
        if last_sec == 0 or 5 <= last_sec <= 9 or seconds // 10 == 1:
            ret += " секунд"
        elif last_sec == 1:
            ret += " секунда"
        else:
            ret += " секунды"
    return ret

def message(msg="", peer_id=None, attachment="", keyboard="", intent="default", disable_mentions=0, dont_parse=1, reply_to=0):
    msg = dailyformat(msg)
    if msg != "":
        for i in range(ceil(len(msg) / 4096)):
            #if peer_id == 242722587: message(i)
            if not i + 1 == ceil(len(msg) / 4096):
                vk.messages.send(random_id=rid(), peer_id=peer_id, message=msg[i*4096:(i+1)*4096], attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse_links=dont_parse, reply_to=reply_to)
            else:
                vk.messages.send(random_id=rid(), peer_id=peer_id, message=msg[i*4096:], attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse_links=dont_parse, reply_to=reply_to)
    else:
        vk.messages.send(random_id=rid(), peer_id=peer_id, message="", attachment=attachment, keyboard=keyboard, intent=intent, disable_mentions=disable_mentions, dont_parse_links=dont_parse, reply_to=reply_to)

def dailyformat(text):
    return text

try:
    #vk_api.VkApi.RPS_DELAY = 1/20
    vk_session = VkApi(token=vkbot_token)
    longpoll = VkBotLongPoll(vk_session, vkbot_gid)
    vk = vk_session.get_api()
except Exception as e:
    print(f"test_vkbot: Authorization failure: {e}")

try:
    parser = argparse.ArgumentParser()

    parser.add_argument('--send', type=str, required=True)
    args = parser.parse_args()

    message(msg=f"УВАГА БЛЯДЬ: {args.send}", peer_id=peer_id)

    l("Sent!")
except Exception as e:
    l(f"Failure while trying to send: {e}. Короче, динаху бля")

#test_vkbot_work = True
#while test_vkbot_work:
#    try:
#        for event in longpoll.listen():
#            if (event.type == VkBotEventType.MESSAGE_NEW or event.type == VkBotEventType.MESSAGE_EDIT):
#                event.object = event.object["message"]
#                user_id = event.object['from_id']
#                peer_id = event.object['peer_id']
#                msgtext = event.object['text']
#                handletxt = msgtext.lower()
#                if handletxt == "ping":
#                    message(msg="pong", peer_id=peer_id)
#                elif handletxt == 'getprojobj':
#                    message(msg=str(projobj), peer_id=peer_id)
#                elif handletxt == 'sendreporting':
#                    message(msg="\n".join(getreporting(projid)), peer_id=peer_id)
#    except Exception as e:
#        print(f"test_vkbot just failed the main cycle - {e}")
#        time.sleep(0.5)

#projobj[project_id] = {}
#projobj[project_id]["throbj"] = Thread(target=mainthr, args=(project_id,))
#projobj[project_id]["throbj"].start()
#projobj[project_id]["reporting"] = [f"{time.ctime()} started"]
#createprocess(project_id, mainthr, project_id)
