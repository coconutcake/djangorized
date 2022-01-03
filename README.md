<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="http://mign.pl/img/logodjangorized.png" alt="Project logo"></a>
</p>

<h3 align="center">Djangorized</h3>

<div align="center">

[![Build Status](https://app.travis-ci.com/coconutcake/djangorized.svg?branch=main)](https://app.travis-ci.com/coconutcake/djangorized)
[![Requirements Status](https://requires.io/github/coconutcake/djangorized/requirements.svg?branch=main)](https://requires.io/github/coconutcake/djangorized/requirements/?branch=main)

</div>

---

<p align="center"> Zintegrowany projekt aplikacji django na kontenerach dockera
    <br> 
</p>

## 📝 Zawartość
- 🧐 [O projekcie](#about)
- 📰 [Założenia projektowe](#zalozenia)
- 🧑‍🔬 [Technologia i metodyka](#tech)
- 🚀 [Uruchomienie](#getting_started)
  - 🔧 [Przygotowanie na RPI (*ARMv7 based CPU)](#rpi)
  - 🔧 [Przygotowanie na WINDOWS](#windows)
  - 🔧 [Dalsze, wspolne kroki instalacyjne](#mutual)
- 🌎 [Endpointy](#endpoints)
- 📜 [Uwagi koncowe](#result)

## 🧐 O projekcie <a name = "about"></a>
---

Projekt aplikacji django na kontenerach dockera wraz z zintegrowana baza postgres oraz serwerem nginx

## 📰 Założenia projektowe <a name = "zalozenia"></a>
---

#### Konteneryzacja i usługi:
1. Utworzenie spójnego modelu konteneryzacji z uwzględnieniem plików `Dockerfile` w osobnych folderach dla każdego kontenera.
2. Utworzenie i skonfigurowanie bazy danych postgres na osobnym kontenerze dla aplikacji i testów
3. Utworzenie kontenera dla serwera upstreamowego Nginx oraz wystawienie za jego pomoca dwuch serwerów - HTTP oraz HTTPS
4. Dodatkowa konfiguracja serwera nginx - dodanie certyfikatów SSL oraz konfiguracja proxy-reverse
5. Implementacja zmiennych środowiskowych w pliku `docker-compose.yml` za pomocą których, aplikacja oraz zależne od niej kontenery będą wstępnie prekonfigowalne na etapie developingu oraz wdrażania np. dla rozwiazania chmurowego
6. Utworzenie modułu inicjującego dla aplikacji Django celem radzenia sobie z typowymi operacjami na pliku `manage.py`

#### Aplikacja Django:
1. Przekonfigurowanie modelu logowania za pomocą email i hasła
2. Dostarczenie przeglądarki API


## 🧑‍🔬Technologia i metodyka <a name = "tech"></a>
---

#### Podział kontenerów Dockera:
- Python 3.8 z django
- Baza Postgres dla django
- Adminer
- Upstream server nginx

#### Aplikacja:

- Aplikacja wykonana wg metodyki TDD. 
- Krycie testami na poziomie ~90% 
- Projekt został zintegrowany z Travis CI -> https://travis-ci.org/github/coconutcake/djangorized
- Wersje zależności requirements -> https://requires.io/github/coconutcake/djangorized/requirements/?branch=main
- Projekt wykorzystuje konteneryzacje docker wraz composerem do uruchomienia środowisk tj: aplikacji django na pythonie 3.8, bazy danych postgresql, aplikacji adminer, oraz serwer upstream nginx
- Model usera został przebudowany w celu umozliwienia logowania za pomocą email
- W projekcie wykorzystano bibliteke wait-for-it w celu kolejkowania uruchamianych kontenerów
- Folder ./initial miescie pliki inicjujace w tym ustawienia nginxa,aplikacji django
- dostepna jest przegladarka API (Swagger)


## ⚙️ Konfiguracja <a name = "config"></a>
---

1. Za pomocą `docker-compose.yml` możliwa jest konfiguracja stacku za pomocą zmiennych środowiskowych dla poszczególnych usług:

- postgres:

  ```
  # Nazwa bazy danych dla aplikacji
  POSTGRES_DB: app

  # Nazwa Usera django do logowania na baze postgres
  POSTGRES_USER: django_app

  # Hasło Usera aplikacji django do logowania na baze postgres
  POSTGRES_PASSWORD: asdasd123
  ```
- djangoapp:

    ```
    # Adres serwera django
    ADDRESS=0.0.0.0

    # Port servera django
    PORT=8877

    # Adres servera nginx na którego bedą wysyłane zapytania (Swagger), zmień na adres cloudowy jeśli pracujesz na chmurze!
    SERVER_URL=https://127.0.0.1:5555/

    # Silnik bazodanowy dla django
    DB_ENGINE=django.db.backends.postgresql

    # Nazwa bazy danych postgres
    DB_NAME=app

    # Nazwa Usera django do logowania na baze postgres
    DB_USER=django_app

    # Hasło Usera aplikacji django do logowania na baze postgres
    DB_PASSWORD=asdasd123

    # Adres kontenera z bazą danych
    DB_ADDRESS=postgres

    # Port bazy postgres
    DB_PORT=5432

    # Nazwa bazy do testów
    DB_TESTS=tests

    # Typ uruchomianego serwera opcje: developer, production
    APPSERVER=developer
    ```

- nginx:

    ```
    # Adres aplikacji django, która zostanie upstremowana do servera nginx
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





## 🚀 Uruchomienie <a name = "getting_started"></a>
---


## 🔧 RPI <a name = "rpi"></a>
---

1. **Zainstaluj biblioteke `libseccomp2`**

    Mozesz doswiadczyc problemow z odpaleniem bazy postgres - (blad segmentacji 11). Aby rozwiazac ten problem doinstaluj konkrente biblioteki `libseccomp2`:
  
    Zdalne:

    ```
    wget http://ftp.debian.org/debian/pool/main/libs/libseccomp/libseccomp2_2.5.1-1_armhf.deb && sudo dpkg -i libseccomp2_2.5.1-1_armhf.deb
    ```

    Biblioteka jest wrzucona rowniez lokalnie w glownym folderze.



## 🔧 WINDOWS <a name = "windows"></a>
---

1. **Przygotuj subsystem**


    Celem przygotowanie subsystemu z linuxem jest unikniecie problemow z kompatybilnoscia kodu, ktory jest zgodny z linuxowym. Dlatego pierwszym krokiem bedzie sprawdzenie czy mamy zainstalowany pakiet obslugujace te maszyny.

    Powershell as admin:

    ```
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
    ```

    Zainstaluj Debian:

    ```
    wsl.exe --install -d Debian
    ```

    Przekonwertuj wsl 1 na wsl 2:

    ```
    wsl --set-version Debian 2
    ```

    Sprawdz zainstalowana wersje:

    ```
    wsl -l -v
    ```

    Jesli wersja wsl wskazuje na 2, przejdz do nastepnrgo kroku

2. **Przygotowanie uzytkownika**

    Uruchom maszyne:

    ```
    wsl --distribution Debian
    ```


3. **Zintegruj obsluge dockera z wsl:**

    ![use_wsl_engine](https://github.com/coconutcake/djangorized/blob/main/adds/use_wsl_engine.png?raw=true)

    ![wsl_docker_integration](https://github.com/coconutcake/djangorized/blob/main/adds/wsl_docker_integration.png?raw=true)

4. **Skonfiguruj VSCODE**

    Zainstaluj Docker i SSH na remote:
    
    ```
    CTRL + SHIFT + X > Docker
    ```

5. **Podlacz do DEBIAN wsl**

    ```
    CTRL + SHIFT + P > wsl di
    ```

    ![wsl_select](https://github.com/coconutcake/djangorized/blob/main/adds/wsl_select.png?raw=true)

    ![wsl_debian](https://github.com/coconutcake/djangorized/blob/main/adds/wsl_debian.png?raw=true)

6. **Ustaw dostepy usera do docker.socket**

    
    Dodaj go do grupy docker:

    ```
    sudo usermod -aG docker $USER
    ```

    Nadaj dodatkowe prawa dla docker.socket:

    ```
    sudo chmod 666 /var/run/docker.sock
    ```



## 🔧 Kontynuacja wspolna dla wszystich systemow <a name = "mutual"></a>
---


1. **Wykonaj klona jesli masz juz zainstalowanego dockera:**

    ```
    git clone https://github.com/coconutcake/djangorized.git
    ```

2. **Po pobraniu klona, przejdz do folderu i zbuduj obrazy poleceniem:**

    `TIP` : *Mozesz wylaczyc tryb `buildkit` aby wyswietlic tryb debugowania:*

    ```
    export DOCKER_BUILDKIT=0 && export COMPOSE_DOCKER_CLI_BUILD=0
    ```

    ```
    docker-compose up --build
    ```

    Aplikacja powinna być dostępna.

3. **Aby zalogować sie na panel administracyjny należy pierw utworzyć konto superadmina.**

    ```
    docker exec -it djangoapp sh -c "python3 app/manage.py createsuperuser"
    ```


4. **Aby sworzyc token dla utworzonego usera - USER to login (email)**

    ```
    docker exec -it djangoapp sh -c "python3 app/manage.py drf_create_token USER" 
    ```

    `TIP`: *Możliwe jest równiez utworzenie tokena przez wbudowany CMS*


5. **Zgraj pliki `static`:**
    ```
    docker exec -it djangoapp sh -c "python app/manage.py collectstatic"
    ```




## 🌎 Endpointy (wg. domyślnej konfiguracji) <a name = "endpoints"></a>:
---


- 🔐 **HTTPS(nginx)** -> https://127.0.0.1:5555/
- 🔓 **HTTP(nginx)** -> https://127.0.0.1:8833/

![ready](https://github.com/coconutcake/djangorized/blob/main/adds/ready.png?raw=true)


## 📜 Uwagi końcowe <a name = "result"></a>
---

- Dla serwera lokalnego ADRES moze być adresem petli zwrotnej - 127.0.0.1, dla cloudowego bedzie do adres servera cloudowego. Pamietaj o konfiguracji `docker-compose.yml` opisanej w sekcji Konfiguracja. 
- Rekomendowane jest ustawienie maskarady `harpin nat` w celu uzywania adresu zewnetrznego.
- pole <(pk)> w adreach to pk obiektu do ktorego sie odwołujemy
