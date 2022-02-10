import socket
import logging
import textwrap
from emoji import demojize
from string import Template

logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])


"""
Get token here: https://twitchapps.com/tmi/
"""

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'TwitchStreamer'
token = 'oauth:gibberish'
channels = ['#channel1','#channel2']


def main():
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    for irc in channels:
        sock.send(f"JOIN {irc}\r\n".encode('utf-8'))

    try:
        while True:
            resp = sock.recv(2048).decode('utf-8')
            if resp.startswith('PING'):
                # sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                if resp.find('PRIVMSG') != -1 and not(resp.startswith(':streamelements')) and not(resp.startswith(':nightbot')) and not(resp.startswith(':streamlabs')):
                    channel = resp[resp.find('#'):resp.find(' ', resp.find('#'))]
                    chatname = resp[1:resp.find('!')]
                    chattext = demojize(resp[resp.find(':', 1) + 1:resp.find('\n')])
                    output = Template('$who in $where: $what').substitute(where=channel, who=chatname, what=chattext)
                    logging.info(textwrap.fill(output, 40))

    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()
