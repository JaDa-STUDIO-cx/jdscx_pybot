# JDSCX pyBot

## Beschreibung
JaDa STUDIO.CX pyBot ist eine Sammlung verschiedener Bots für Content-Creator und Streamer, 
um unhabhängig verschiedene externe Benachrichtungen im Discord und Twitter zu automatisieren.

Die Bots sind in Python umgesetzt und müssen auf einem kleinen VPS betrieben werden.

Momentan sind folgende Bots enthalten:

Ruft Tweet mit dem Hashtag #discord von einem bestimmten Account ab:
#-> tweet2discord.py


## Systemvoraussetzung / Installation
->min. Debian Buster
->Python 3

-> Python-Addon: Discord-Webhook
`pip install discord-webhook`

-> JDSCX pyBot muss sich im Order-Pfad */opt/jdscx_pybot* befinden
`mkdir sudo /opt/jdscx_pybot`

-> Einrichtung des Crontabs
`sudo crontab -e`
`* * * * * /opt/jdscx_pybot/tweet2discord.py >/dev/null 2>&1`


## HINWEIS
Im oberen Abschnitt müssen folgende Variablen eingetragen werden:
- Twitter Bearer Token
- Twitter Username
- Discord Webhook URL
- Benachrichtigungstext oberhalb der Embed-Nachricht

```
######
#### Variable-Config
#### Please insert your Discord webhook, Twitter bearer token, username and the message text.
#### You can use the discord markups and emojis.
######

###-->Twitter
vT_Bearer =''   <-- Twitter Token
vT_Username ='' <-- Twitter Username

###-->Discord
webhook_url ='' <-- Discord Webhoook URL
vcontent =''    <-- Nachrichtentext für Discord

###### END OF SETTINGS ######

````


Weitere Infos unter
[https://jadastudio.cx](https://jadastudio.cx/)