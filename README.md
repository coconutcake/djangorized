<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="http://mign.pl/img/logodjangorized.png" alt="Project logo"></a>
</p>

<h3 align="center">Djangorized</h3>

<div align="center">

[![Stauts](https://img.shields.io/travis/coconutcake/djangorized)](https://travis-ci.org/github/coconutcake/djangorized)
[![Requirements Status](https://requires.io/github/coconutcake/djangorized/requirements.svg?branch=main)](https://requires.io/github/coconutcake/djangorized/requirements/?branch=main)

</div>

---

<p align="center"> Zintegrowany projekt aplikacji django na kontenerach dockera
    <br> 
</p>

## 馃摑 Zawarto艣膰
- [O projekcie](#about)
- [Za艂o偶enia projektowe](#zalozenia)
- [Technologia i metodyka](#tech)
- [Uruchomienie](#getting_started)
- [API](#api)

## 馃 O projekcie <a name = "about"></a>  

Projekt aplikacji django na kontenerach dockera wraz z zintegrowana baza postgres oraz serwerem nginx

## 馃摪 Za艂o偶enia projektowe <a name = "zalozenia"></a>

#### Konteneryzacja i us艂ugi:
1. Utworzenie sp贸jnego modelu konteneryzacji z uwzgl臋dnieniem plik贸w `Dockerfile` w osobnych folderach dla ka偶dego kontenera.
2. Utworzenie i skonfigurowanie bazy danych postgres na osobnym kontenerze dla aplikacji i test贸w
3. Utworzenie kontenera dla serwera upstreamowego Nginx oraz wystawienie za jego pomoca dwuch serwer贸w - HTTP oraz HTTPS
4. Dodatkowa konfiguracja serwera nginx - dodanie certyfikat贸w SSL oraz konfiguracja proxy-reverse
5. Implementacja zmiennych 艣rodowiskowych w pliku `docker-compose.yml` za pomoc膮 kt贸rych, aplikacja oraz zale偶ne od niej kontenery b臋d膮 wst臋pnie prekonfigowalne na etapie developingu oraz wdra偶ania np. dla rozwiazania chmurowego
6. Utworzenie modu艂u inicjuj膮cego dla aplikacji Django celem radzenia sobie z typowymi operacjami na pliku `manage.py`

#### Aplikacja Django:
1. Przekonfigurowanie modelu logowania za pomoc膮 email i has艂a
2. Dostarczenie przegl膮darki API


## 馃鈥嶐煍琓echnologia i metodyka <a name = "tech"></a>

#### Podzia艂 kontener贸w Dockera:
- Python 3.8 z django
- Baza Postgres dla django
- Adminer
- Upstream server nginx

#### Aplikacja:

- Aplikacja wykonana wg metodyki TDD. 
- Krycie testami na poziomie ~90% 
- Projekt zosta艂 zintegrowany z Travis CI -> https://travis-ci.org/github/coconutcake/djangorized
- Wersje zale偶no艣ci requirements -> https://requires.io/github/coconutcake/djangorized/requirements/?branch=main
- Projekt wykorzystuje konteneryzacje docker wraz composerem do uruchomienia 艣rodowisk tj: aplikacji django na pythonie 3.8, bazy danych postgresql, aplikacji adminer, oraz serwer upstream nginx
- Model usera zosta艂 przebudowany w celu umozliwienia logowania za pomoc膮 email
- W projekcie wykorzystano bibliteke wait-for-it w celu kolejkowania uruchamianych kontener贸w
- Folder ./initial miescie pliki inicjujace w tym ustawienia nginxa,aplikacji django
- dostepna jest przegladarka API (Swagger)


## 鈿欙笍 Konfiguracja <a name = "config"></a>

Za pomoc膮 `docker-compose.yml` mo偶liwa jest konfiguracja stacku za pomoc膮 zmiennych 艣rodowiskowych dla poszczeg贸lnych us艂ug:

#### postgres:

```
# Nazwa bazy danych dla aplikacji
POSTGRES_DB: app

# Nazwa Usera django do logowania na baze postgres
POSTGRES_USER: django_app

# Has艂o Usera aplikacji django do logowania na baze postgres
POSTGRES_PASSWORD: asdasd123
```

#### djangoapp:

```
# Adres serwera django
ADDRESS=0.0.0.0

# Port servera django
PORT=8877

# Adres servera nginx na kt贸rego bed膮 wysy艂ane zapytania (Swagger), zmie艅 na adres cloudowy je艣li pracujesz na chmurze!
SERVER_URL=https://127.0.0.1:5555/

# Silnik bazodanowy dla django
DB_ENGINE=django.db.backends.postgresql

# Nazwa bazy danych postgres
DB_NAME=app

# Nazwa Usera django do logowania na baze postgres
DB_USER=django_app

# Has艂o Usera aplikacji django do logowania na baze postgres
DB_PASSWORD=asdasd123

# Adres kontenera z baz膮 danych
DB_ADDRESS=postgres

# Port bazy postgres
DB_PORT=5432

# Nazwa bazy do test贸w
DB_TESTS=tests

# Typ uruchomianego serwera opcje: developer, production
APPSERVER=developer
```

#### nginx:

```
# Adres aplikacji django, kt贸ra zostanie upstremowana do servera nginx
UPSTREAM_APP_URL=djangoapp:8877

# Proxy pass
PROXY_PASS=djangoapp

# Port wystawianego servera HTTP
HTTP_SERVER_PORT=8833

# Port wystawianego servera HTTPS
HTTPS_SERVER_PORT=5555

# Ip lub domena severa (zmiana niekonieczna)
SERVER_NAME=default_server_ip
```





## 馃殌 Uruchomienie <a name = "getting_started"></a>

Wykonaj klona jesli masz juz zainstalowanego dockera:
```
git clone https://github.com/coconutcake/djangorized.git
```

Po pobraniu klona, przejdz do folderu i zbuduj obrazy poleceniem:

```
docker-compose up --build
```

Aplikacja powinna by膰 dost臋pna.
Aby zalogowa膰 sie na panel administracyjny nale偶y pierw utworzy膰 konto superadmina.

```
docker exec -it djangoapp sh -c "python3 app/manage.py createsuperuser"
```

jesli uzywasz Windowsa, bedziesz musial u偶y膰 winpty:

```
winpty docker exec -it djangoapp sh -c "python3 app/manage.py createsuperuser"
```


Aby sworzyc token dla utworzonego usera - USER to login (email)

```
docker exec -it djangoapp sh -c "python3 app/manage.py drf_create_token USER" 
```

Mo偶liwe jest r贸wniez utworzenie tokena przez wbudowany CMS


## 馃殌 Uwagi ko艅cowe <a name = "result"></a>

- Dla serwera lokalnego ADRES moze by膰 adresem petli zwrotnej - 127.0.0.1, dla cloudowego bedzie do adres servera cloudowego. Pamietaj o konfiguracji `docker-compose.yml` opisanej w sekcji Konfiguracja
- pole <(pk)> w adreach to pk obiektu do ktorego sie odwo艂ujemy
