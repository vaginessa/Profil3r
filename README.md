<p align=center>
  <img src="doc/profil3r_logo.png" width="200" height="200"/>
  <br>
  <a target="_blank" href="https://discord.gg/TjHfREggZS" title="Python version">Discord 💬</a></br>
  <code>pip3 install profil3r && profil3r --help</code></br></br>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
  <a target="_blank" href="https://www.python.org/downloads/" title="Python version"><img src="https://img.shields.io/badge/python-%3E=_3.6-green.svg"></a>
  <a target="_blank" href="LICENSE" title="License: MIT"><img src="https://img.shields.io/badge/License-MIT-blue.svg"></a>
  <a target="_blank" title="Downloads"><img src="https://static.pepy.tech/badge/profil3r"></a>
  <a target="_blank" href="https://twitter.com/Rog3rSm1th" title="Python version"><img src="https://img.shields.io/badge/-@Rog3rSm1th-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/Rog3rSm1th"></a>
  <br>
  <span><i>Find the profiles of a person on social networks, as well as their email addresses</i></span>
</p>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#features">Features</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#contact">Contact</a>
</p>


Profil3r is an [OSINT](https://en.wikipedia.org/wiki/Open-source_intelligence) tool that allows you to find potential profiles of a person on social networks, as well as their email addresses. This program also alerts you to the presence of a data leak for the found emails.

![](doc/demo_cli.gif)
## 💡 Prerequisites
[Python 3](https://www.python.org/)

## Installation

#### Install with pip (recommended)

```bash
pip3 install profil3r
```

#### Or build from source

Recommended for developers. It automatically clones the main branch from the Profil3r repo, and installs from source.

```bash
# Automatically clone the Profil3r repository and install profil3r from source
bash <(wget -q https://raw.githubusercontent.com/Rog3rSm1th/Profil3r/main/scripts/autoinstall.sh -O -)
```

## Features

#### 📙 Domain
- [x] TLD (.com, .org, .net, etc...)

#### ✉️ Emails 
- [x] Data leaks
- [x] Emails

#### 🌐 Social

|Service      | Profile Scraping |
|-------------|------------------|
| Instagram   | Yes ✔️            |
| Facebook    | No               |
| Twitter     | Yes ✔️            |
| Tiktok      | No               |
| Pinterest   | No               |
| Linktr.ee   | Yes ✔️            |
| MySpace     | Yes ✔️            |
| Flickr      | Yes ✔️            |
| DeviantArt  | No               |
| GoodReads   | No               |
| Ello        | No               |
| Chirpty     | Yes ✔️            |

#### 🎵 Music

|Service      | Profile Scraping |
|-------------|------------------|
| Soundcloud  | No               |
| Spotify     | No               |
| Smule       | No               |
| bandcamp    | Yes ✔️            |

#### ‍💻 Programming

|Service      | Profile Scraping |
|-------------|------------------|
| Github      | Yes ✔️            |
| Pastebin    | Yes ✔️            |
| LessWrong   | Yes ✔️            |
| Repl.it     | No               |
| Cracked.to  | No               |
| PyPi        | Yes ✔️            |
| NPM         | Yes ✔️            |
| Asciinema   | No               |
| CodeMentor  | No               |
| Ifttt       | No               |

#### 💬 Forum

|Service        | Profile Scraping |
|---------------|------------------|
| 0x00sec.org   | No               |
| Hackernews    | Yes ✔️            |
| Jeuxvideo.com | Yes ✔            |

#### 🗣️ Tchat

|Service        | Profile Scraping |
|---------------|------------------|
| Skype         | No               |

#### 📺 Entertainment

|Service        | Profile Scraping |
|---------------|------------------|
| Dailymotion   | No               |
| Vimeo         | No               |
| DeviantArt    | Yes ✔            |
| Dribbble      | Yes ✔            |

#### 🚫 Porn

|Service        | Profile Scraping |
|---------------|------------------|
| PornHub       | Yes ✔            |
| RedTube       | No               |
| XVideos       | No               |

#### 💸 Money

|Service        | Profile Scraping |
|---------------|------------------|
| BuyMeACoffee  | No               |
| Patreon       | No               |
| CashApp       | No               |

#### 🕸️ Web Hosting

|Service        | Profile Scraping |
|---------------|------------------|
| AboutMe       | Yes ✔            |
| SlideShare    | Yes ✔            |
| WordPress     | No               |

#### 🎮 Gaming 

|Service        | Profile Scraping |
|---------------|------------------|
| Steam         | No               |
| Op.gg         | Yes ✔            |
| Dota2         | Yes ✔            |
| Kongregate    | Yes ✔            |

#### 📰 Medias

|Service        | Profile Scraping |
|---------------|------------------|
| Medium        | No               |
| Dev.to        | No               |
| Hubpages      | Yes ✔            |
| LiveJournal   | No               |

#### ✈️ Travel

|Service        | Profile Scraping |
|---------------|------------------|
| TripAdvisor   | No               |

#### 👥 Collaborative

|Service        | Profile Scraping |
|---------------|------------------|
| Wikipedia     | No               |
| Instructables | Yes ✔            |

#### 🏆 CTF

|Service        | Profile Scraping |
|---------------|------------------|
| Root-me       | Yes ✔            |

#### 👀 Privacy

|Service        | Profile Scraping |
|---------------|------------------|
| Keybase       | Yes ✔            |

## Report

To further analyze the data collected by Profil3r, it is possible to generate reports in different formats using the argument ```-r/--report <path of the reports>```  

#### JSON

A report in JSON format is generated in the `reports/json` folder

#### CSV

A report in CSV format is generated in the `reports/csv` folder

#### HTML

A report in HTML format is generated in the `reports/html` folder, you can access it in your webbrowser

![](doc/demo_web.gif)

## Usage 

```
usage: profil3r [-h] -p PROFILE [PROFILE ...] [-r REPORT]

optional arguments:
  -h, --help            show this help message and exit
  -p PROFILE [PROFILE ...], --profile PROFILE [PROFILE ...]
                        parts of the username that you are looking for, e.g. : john doe
  -r REPORT, --report REPORT
                        path to the report directory, e.g. : ./OSINT
```

## 📚 Example

```bash
profil3r -p john doe -r ./OSINT
```

## 📝 License

This project is under the MIT license.

## Contact 

for any remark, suggestion or job offer, you can contact me at r0g3r5@protonmail.com or on twitter [@Rog3rSm1th](https://twitter.com/Rog3rSm1th)
