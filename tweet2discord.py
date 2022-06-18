#!/usr/bin/python3

import os
import time
import datetime
from datetime import datetime
import subprocess
from discord_webhook import DiscordWebhook, DiscordEmbed


import requests
import json
import re
import sys, getopt
from json import loads
import shutil



######
#### Variable-Config
#### Please insert your Discord webhook, Twitter bearer token, username and the message text.
#### You can use the discord markups and emojis.
######

###-->Twitter
vT_Bearer =''
vT_Username =''

###-->Discord
webhook_url =''
vcontent =''

###### END OF SETTINGS ######


##->Fetch real name and profile image
url = 'https://api.twitter.com/2/users/by/username/'+vT_Username+'?user.fields=profile_image_url'
response = requests.get(url, headers={'Authorization' : 'Bearer '+vT_Bearer+''})
name = loads(response.text)['data']['name']
ppic = loads(response.text)['data']['profile_image_url']

##->Fetch tweet id and tweet text
url = 'https://api.twitter.com/2/tweets/search/recent?query=from%3A'+vT_Username+'%20%22%23Discord%22'
response = requests.get(url, headers={'Authorization' : 'Bearer '+vT_Bearer+''})
if response.text != '{"meta":{"result_count":0}}':
    id = loads(response.text)['data'][0]['id']
    text = loads(response.text)['data'][0]['text']
    text = text.replace('https://', '\n➡ https://')
else:
    name = 'ERROR'
##->Lookup the last tweet id
if name != 'ERROR':
    tw_last_post = open('/opt/jdscx_pybot/tmp/tw__last-post.txt','r')
    for line in tw_last_post:
        last_tweet=line.rstrip()
    tw_last_post.close()
    ##->If the last tweet not published in the discord channel
    if last_tweet != id:
        tw_last_post = open('/opt/jdscx_pybot/tmp/tw__last-post.txt','w')
        tw_last_post.write(id)
        tw_last_post.close()
        ##->Fetch the media url
        url = 'https://api.twitter.com/2/tweets?ids='+id+'&expansions=attachments.media_keys&media.fields=duration_ms,height,media_key,preview_image_url,public_metrics,type,url,width,alt_text'
        response = requests.get(url, headers={'Authorization' : 'Bearer '+vT_Bearer+''})
        if  'includes' in response.text:
            photo = loads(response.text)['includes']['media'][0]['url']
        else:
            photo =''

    else:
        name = 'ERROR'
#
if name!= 'ERROR':
    ##### Discord-Send via webhook
    webhook = DiscordWebhook(url=webhook_url, content='@here \n'+vcontent+'\n\nhttps://twitter.com/'+vT_Username+'/status/'+id)
    embed = DiscordEmbed(description=text ,color=1942002)
    embed.set_author(name=name+' (@'+vT_Username+')', url='https://twitter.com/'+vT_Username, icon_url=ppic)
    embed.set_image(url=photo)
    embed.set_footer(text="Posted by JDSCX-pyBot 🔷 https://jadastudio.cx")
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()

