"""
Using slack for simple push notifications instead of sending mails everytime

"""
from slackclient import SlackClient

def slack_message(message, channel):
    token ='Your token'
    sc = SlackClient(token)

    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='rohithrajr',
                icon_emoji=':robot_face:')

def main():
    slack_message("hello","general")

if __name__=='__main__':
    main()
