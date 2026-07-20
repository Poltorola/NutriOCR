# Настройка Git и GitHub Actions Runner в WSL Ubuntu

Ниже приведена практичная схема:

- Git работает через SSH и не просит логин или token.
- Настройки Git применяются только к `NutriOCR`.
- GitHub Actions Runner установлен как Linux-служба внутри WSL.
- Runner запускает тесты на домашнем компьютере и имеет доступ к Ollama.

## 1. Настройка Git без global config

GitHub больше не принимает пароль учётной записи для `git push`. Рекомендуется SSH: токен хранить не придётся, а настройки конкретного remote находятся в `.git/config` текущего репозитория. [GitHub рекомендует SSH-ключи для работы без постоянного ввода логина и PAT](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh).

### 1.1. Задай имя и email только для NutriOCR

Открой WSL и перейди в репозиторий:

```bash
cd /home/k3l/projects/NutriOCR
```

Установи локальные параметры:

```bash
git config --local user.name "YOUR_GITHUB_USERNAME"
git config --local user.email "YOUR_EMAIL@example.com"
```

Проверь источник настроек:

```bash
git config --local --list
```

Они будут записаны только в:

```text
/home/k3l/projects/NutriOCR/.git/config
```

### 1.2. Проверь существующие SSH-ключи

```bash
ls -la ~/.ssh
```

Если уже существуют `id_ed25519` и `id_ed25519.pub`, можно использовать их. Не перезаписывай существующий ключ, если не уверен, для чего он используется.

### 1.3. Создай отдельный ключ для GitHub

```bash
ssh-keygen -t ed25519 -C "YOUR_EMAIL@example.com" -f ~/.ssh/github_nutriocr
```

Будет предложено задать passphrase.

Есть два варианта:

- оставить passphrase пустой — Git вообще не будет ничего спрашивать;
- установить passphrase — безопаснее, но после перезапуска WSL её потребуется один раз ввести в `ssh-agent`.

Для домашней машины разумнее установить passphrase и использовать агент. Если runner должен выполнять `git push` полностью автоматически, лучше вообще не выдавать ему твой личный SSH-ключ: для CI безопаснее использовать `GITHUB_TOKEN`.

Закрой доступ к приватному ключу:

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/github_nutriocr
chmod 644 ~/.ssh/github_nutriocr.pub
```

### 1.4. Добавь ключ в ssh-agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/github_nutriocr
```

Это запомнит passphrase до завершения текущего агента или сеанса WSL.

Покажи публичный ключ:

```bash
cat ~/.ssh/github_nutriocr.pub
```

Скопируй всю строку. Приватный файл `~/.ssh/github_nutriocr` никуда не отправляй.

На GitHub открой:

```text
Profile → Settings → SSH and GPG keys → New SSH key
```

Вставь публичный ключ и выбери тип `Authentication Key`. Подробные официальные шаги: [генерация и добавление SSH-ключа](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux).

### 1.5. Привяжи этот ключ к GitHub

Создай либо отредактируй `~/.ssh/config`:

```sshconfig
Host github-nutriocr
    HostName github.com
    User git
    IdentityFile ~/.ssh/github_nutriocr
    IdentitiesOnly yes
```

Затем:

```bash
chmod 600 ~/.ssh/config
```

`github-nutriocr` — локальный SSH-псевдоним. Он позволяет использовать именно этот ключ, не меняя глобальную конфигурацию Git.

Проверь соединение:

```bash
ssh -T git@github-nutriocr
```

При первом подключении подтверди fingerprint командой `yes`. Успешный результат выглядит примерно так:

```text
Hi USERNAME! You've successfully authenticated...
```

Команда при этом может вернуть код `1` — для теста GitHub SSH это нормально. [Проверка SSH-соединения описана здесь](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection?platform=linux).

### 1.6. Переключи только этот репозиторий с HTTPS на SSH

Сначала посмотри текущий remote:

```bash
cd /home/k3l/projects/NutriOCR
git remote -v
```

Установи новый URL, заменив владельца репозитория:

```bash
git remote set-url origin git@github-nutriocr:OWNER/NutriOCR.git
```

Проверь:

```bash
git remote -v
git fetch origin
```

Теперь `git pull` и `git push` не должны спрашивать логин или token.

Проверить, что global config не менялся, можно так:

```bash
git config --show-origin --get-regexp 'user\.|credential\.|core\.sshCommand'
```

## 2. Подготовка WSL для Runner

### 2.1. Проверь WSL 2

В Windows PowerShell:

```powershell
wsl --version
wsl --list --verbose
```

Напротив Ubuntu должна быть версия `2`.

При необходимости:

```powershell
wsl --update
wsl --set-version Ubuntu 2
```

Название дистрибутива возьми из `wsl --list --verbose`.

### 2.2. Проверь systemd

В Ubuntu WSL:

```bash
systemctl is-system-running
```

Если systemd работает, можно переходить дальше.

Если получаешь ошибку, добавь в `/etc/wsl.conf`:

```ini
[boot]
systemd=true
```

После этого в PowerShell полностью останови WSL:

```powershell
wsl --shutdown
```

Снова открой Ubuntu и проверь:

```bash
systemctl is-system-running
```

В актуальных установках Ubuntu systemd обычно уже включён. Для старых дистрибутивов Microsoft описывает включение отдельно: [systemd в WSL](https://learn.microsoft.com/en-us/windows/wsl/systemd).

## 3. Создание self-hosted runner на GitHub

Открой репозиторий на GitHub:

```text
Repository → Settings → Actions → Runners
→ New self-hosted runner
```

Выбери:

```text
Runner image: Linux
Architecture: x64
```

Если компьютер ARM — выбери `ARM64`.

GitHub покажет актуальные команды скачивания. Используй именно их: версия runner и регистрационный token со временем меняются. Регистрационный token действует ограниченное время, обычно около часа. [Официальная инструкция по добавлению runner](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners).

## 4. Установка runner в WSL

В WSL создай отдельный каталог вне репозитория:

```bash
mkdir -p ~/actions-runner
cd ~/actions-runner
```

Дальше выполни команды, показанные GitHub. Они будут похожи на:

```bash
curl -o actions-runner-linux-x64-VERSION.tar.gz -L \
  https://github.com/actions/runner/releases/download/vVERSION/actions-runner-linux-x64-VERSION.tar.gz

tar xzf actions-runner-linux-x64-VERSION.tar.gz
```

Не копируй буквально `VERSION`: возьми полный актуальный URL со страницы GitHub.

Настрой runner командой, также показанной GitHub:

```bash
./config.sh \
  --url https://github.com/OWNER/NutriOCR \
  --token REGISTRATION_TOKEN
```

Во время настройки можно указать:

```text
Runner name: home-wsl-runner
Additional labels: ollama,nutriocr
Work folder: _work
```

Рабочий каталог runner будет отдельным:

```text
~/actions-runner/_work/
```

Runner не выполняет job прямо в твоём открытом `/home/k3l/projects/NutriOCR`: action `checkout` создаёт отдельную рабочую копию. Это правильно — незакоммиченные локальные изменения не должны попадать в CI.

## 5. Тестовый запуск вручную

Из каталога runner:

```bash
cd ~/actions-runner
./run.sh
```

При успехе появится:

```text
Connected to GitHub
Listening for Jobs
```

На странице GitHub:

```text
Settings → Actions → Runners
```

runner должен получить статус `Idle`.

Остановить ручной запуск можно через `Ctrl+C`.

## 6. Установка runner как systemd-службы

После успешного выполнения `config.sh`:

```bash
cd ~/actions-runner
sudo ./svc.sh install
sudo ./svc.sh start
sudo ./svc.sh status
```

GitHub официально поддерживает управление Linux runner через сгенерированный `svc.sh`: [настройка runner как службы](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/configure-the-application?platform=linux).

Дополнительно проверь:

```bash
systemctl list-units --type=service 'actions.runner*'
```

Посмотреть журнал:

```bash
journalctl -u 'actions.runner.*' --since today
```

Команды управления:

```bash
sudo ./svc.sh stop
sudo ./svc.sh start
sudo ./svc.sh status
```

### Особенность WSL

Служба запускается при старте дистрибутива Ubuntu, но WSL не обязательно запускается автоматически после включения Windows.

После перезагрузки Windows можно вручную активировать дистрибутив:

```powershell
wsl -d Ubuntu --exec true
```

Затем проверь runner на GitHub. Если нужна полная автоматизация после входа в Windows, эту команду можно добавить в Windows Task Scheduler.

При выключенной Windows runner будет `Offline`, а workflow останется в очереди до установленного GitHub срока ожидания.

## 7. Проверка Ollama от имени runner

Сначала выясни, под каким пользователем установлена служба:

```bash
cd ~/actions-runner
sudo ./svc.sh status
```

Runner лучше устанавливать под тем же непривилегированным WSL-пользователем, который имеет доступ к Ollama и проектным зависимостям.

Проверь Ollama:

```bash
curl --fail http://127.0.0.1:11434/api/tags
ollama list
```

Если Ollama установлена внутри того же WSL, `127.0.0.1:11434` подходит.

Если Ollama запущена в Windows, доступ через `localhost` часто работает благодаря WSL networking, но это нужно проверить именно из Ubuntu:

```bash
curl --fail http://127.0.0.1:11434/api/tags
```

Если не работает, потребуется адрес Windows-хоста или настройка mirrored networking. Не публикуй порт `11434` в интернет.

Важно: systemd-служба runner не загружает твой интерактивный `.bashrc`. Поэтому Python, Ollama или виртуальное окружение, доступные в терминале, могут отсутствовать в `PATH` службы. Надёжнее использовать абсолютные пути либо создавать окружение непосредственно в workflow.

## 8. Минимальный workflow для проверки

Создай `.github/workflows/self-hosted-check.yml`:

```yaml
name: Self-hosted check

on:
  workflow_dispatch:

jobs:
  check:
    runs-on: [self-hosted, linux, ollama, nutriocr]

    timeout-minutes: 30

    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Show environment
        run: |
          uname -a
          python3 --version

      - name: Check Ollama
        run: |
          curl --fail --show-error http://127.0.0.1:11434/api/tags
```

Закоммить и отправь:

```bash
git add .github/workflows/self-hosted-check.yml
git commit -m "Add self-hosted runner check"
git push
```

Затем открой:

```text
GitHub → Actions → Self-hosted check → Run workflow
```

## 9. Безопасность

Self-hosted runner выполняет команды workflow непосредственно на домашней машине. Поэтому:

- запускай его под отдельным непривилегированным пользователем;
- не давай ему доступ к личным SSH-ключам;
- не запускай недоверенный код из чужих pull request;
- для публичного репозитория не запускай self-hosted job автоматически на событие `pull_request`;
- используй `GITHUB_TOKEN` внутри CI, а не личный PAT;
- не добавляй регистрационный token runner в файлы или commits;
- не запускай runner через `sudo`.

GitHub также отдельно предупреждает о риске выполнения кода из fork на self-hosted runner, особенно для публичных репозиториев. [Рекомендации GitHub](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/add-runners).
