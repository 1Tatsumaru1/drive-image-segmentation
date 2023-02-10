<h1 align="center">
  <br>
  <a href="https://portal.azure.com/">
    <img src="https://github.com/1Tatsumaru1/flight-bot/blob/master/notebook/img/bot-service_icon.png" alt="Azure Bot Service" width="200">
  </a>
  <br>
  ChatBot Azure
  <br>
</h1>

<h4 align="center">
  Built from this 
  <a href="https://www.microsoft.com/en-us/research/project/frames-dataset/#!download" target="_blank">Microsoft dataset</a>.
</h4>

![screenshot](https://github.com/1Tatsumaru1/flight-bot/blob/master/notebook/img/pipeline.png)

<p align="center">
  <a href="#description">Description</a> •
  <a href="#contents">Contents</a> •
  <a href="#credits">Credits</a> •
  <a href="#links">Links</a>
</p>

## Description

This project was part of my IA Engineering course at OpenClassrooms. 
The aim was to :<br>
* Build a LUIS (Language Understanding) schema and extract utterances based on <a href="https://www.microsoft.com/en-us/research/project/frames-dataset/#!download" target="_blank">this dataset</a> in order to train a Language Understanding model
* Develop a ChatBot based on the <a href="https://github.com/microsoft/botbuilder-python">Microsoft Bot SDK</a> and capable of placing a flight reservation for a customer
* Publish the ChatBot on Azure Bot Service and making it available from various channels (Microsoft Teams, Telegram for instance)
<br>
Here is a brief summary of the Bot's architecture :
<br>

![screenshot](https://github.com/1Tatsumaru1/flight-bot/blob/master/notebook/img/architecture.png)

## Contents

* **A notebook** (folder "notebook") where the LUIS schema and utterances are extracted. The LUIS model is also tested and evaluated there
* **The bot**, which entry point is the **app.py** file. Written in Python, it is ready to deploy to an Azure App Service slot and publish to a Bot ressource

## Credits

This project makes use of the following packages:

- [Requests](https://docs.python-requests.org/en/latest/index.html)
- [Unittest](https://docs.python.org/3/library/unittest.html)
- [Aiohttp](https://docs.aiohttp.org/en/stable/)
- [Emoji](https://emoji-python.readthedocs.io/en/stable/)

## Links

> <a href="https://anthony.ledouguet.com"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/world.png" alt="website" width="20" /> anthony.ledouguet.com</a><br>
> <a href="https://github.com/1Tatsumaru1"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/github.png" alt="github" width="20" /> GitHub</a><br>
> <a href="https://www.linkedin.com/in/anthony-le-douguet/"><img src="https://github.com/1Tatsumaru1/azure_reco_api/blob/main/img/linkedin.png" alt="linkedin" width="20" />
LinkedIn</a>
