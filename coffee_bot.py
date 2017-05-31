#!/usr/bin/python
"""Slack bot for fresh pots of coffee!"""

from scapy.all import *
import requests
import constants
SLACK_API_URL = 'https://slack.com/api/chat.postMessage'

def send_message():
    """Posts to Slack API with token auth and message payload"""
    data = {
        "token": constants.SLACK_TOKEN,
        "channel": constants.CHANNEL_ID,
        "text": ":coffee: Fresh pot of coffee in the kitchen! :coffee:",
        "as_user": "true"
    }
    requests.post(SLACK_API_URL, data)

def arp_display(pkt):
    """Sniffs network packets for the dash button press"""
    if pkt[ARP].op == 1:
        if pkt[ARP].psrc == '0.0.0.0':
            if pkt[ARP].hwsrc == constants.MAC_ADDRESS:
                send_message()


print sniff(prn=arp_display, filter="arp", store=0)
