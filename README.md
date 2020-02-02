# Purpose

Utility Discord bot for the [Distributed YouTube Archive](https://archives.team/).

The purpose of the Distributed YouTube Archive is to preserve valuable YouTube content, and here's a blurb from our purpose statement:


> Welcome to the Distributed Youtube Archive!
> 
> This [Discord] server exists to organize a distributed archive of youtube channels and videos.
> YouTube hosts a variety of valuable content, and as its policies change over time, some of that content becomes at risk of being deleted.
> To prevent valuable channels and videos from being lost, the contributors here at the Archive download channels and store them.
> 
> To make that data available to others we record that we have it in a public index spreadsheet. A central, cloud-hosted video storage solution is also in the works.


## To run:

1. Install Python 3.7+ and do `pip install -r requirements.txt`
2. Create a new project in the [Google Cloud Console](https://console.cloud.google.com)
3. Create a service account and share the tracking spreadsheet with the service account email
4. Download the service account authentication file (should end in `.json`) and put it in the root directory
5. Create a new application and associated bot account in [Discord Developer Portal](https://discordapp.com/developers/applications/), copying the bot token
6. Generate a OAuth2 link (use `bot` for scope) with send message and embed link permissions; use said link to add bot to server
7. Copy `config.example.ini` to `config.ini` and fill out the fields within (full name of the service account auth file goes in `auth_file`, other fields should be self-explanatory)
8. Do `py -3 bot.py` in terminal (or just double-click `bot.py` and 🤞)


---

*This project is licensed under the MIT license. For more information, please see [LICENSE](./LICENSE).*
