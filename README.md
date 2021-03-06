# Tuise-bot

## Changes
go to [changes](./docs/changes.md)

## Installation

[MAC OS GUIDE](./docs/mac.md)

[WINDOWS GUIDE](./docs/windows.md)

**[LINUX or Raspberry Pi]**

Make sure you have recording and python installed

    $ sudo apt-get install libav-tools portaudio19-dev python-setuptools python-pip

Install [pyvona](https://github.com/zbears/pyvona) and its dependencies

    $ sudo pip install pyvona requests pygame

Install virtualenv

    $ sudo apt-get install python-virtualenv


**\[optional\](see [Usage](#usage))**

Download and Install [wolframAlpha python library](https://github.com/jaraco/wolframalpha)

    $ sudo python setup.py build

    $ sudo python setup.py

<hr>

## Usage

Create a virtual environment and install wolframalpha (if you didn't before) and pyramid.

    $ mkdir venv
    $ export VENV=path-to-your-dir/venv
    $ virtualenv --system-site-packages $VENV
    $ . $VENV/bin/activate
    (venv) $ $VENV/bin/pip install wolframalpha
    (venv) $ $VENV/bin/pip install "pyramid==1.7.3"
    (venv) $ $VENV/bin/pip install python-socketio
    (venv) $ $VENV/bin/pip install eventlet
    (venv) $ $VENV/bin/pip install lxml
    (venv) $ $VENV/bin/pip install geopy

### For Windows

    > mkdir venv
    > SET VENV=path-to-your-dir\venv
    > python -m virtualenv --system-site-packages %VENV%
    > %VENV%\Scripts\activate
    (venv) > %VENV%\Scripts\pip install wolframalpha
    (venv) > %VENV%\Scripts\pip install "pyramid==1.7.3"
    (venv) > %VENV%\Scripts\pip install python-socketio
    (venv) > %VENV%\Scripts\pip install eventlet
    (venv) > %VENV%\Scripts\pip install lxml
    (venv) > %VENV%\Scripts\pip install geopy

#### Note
If you can't install lxml using the above command, in windows, try downloading the [lxml-3.7.2-cp27-cp27m-win32.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml), copy it to the project root and run `%VENV%\Scripts\pip install lxml-3.7.2-cp27-cp27m-win32.whl`

<hr>

Get an [WolframAlpha API](http://products.wolframalpha.com/api/) APP-ID

Get an [IFTTT maker key](https://ifttt.com/maker) just press connect and go to settings the url there should have the key `https://maker.ifttt.com/use/KEY-IS-HERE`

Get an [IVONA Speech Cloud Account](https://www.ivona.com/us/for-business/speech-cloud/) and generate credentials: Access and Secret Key


Create configuration file `config.cfg` inside the `config/` folder

```
[main]
app_id = YOUR-APIKEYHERE
ifttt_key = IFTTT-KEYHERE
access_key = IVONA_ACCESS_KEY
secret_key = IVONA_SECRET_KEY
```

```
Not necessary at the moment, there are working API keys in the current config already!
```

Edit the bot configuration file `bot_config.json` inside the `config/` folder

```
{
	"triggers": ['dude', 'hey dude', 'hey mate', 'ok dude', 'okay dude'],
	"greetings": ["Sire?", "One is glad to be of service!", "How can I help?", "What is it!?! Can't you see I'm busy?", "WHAT???"],
  "commands": {
    "ping": { "triggers": [ "ping" ] },
    "play song on android": { "triggers": [ "play song on android", "play song in android", "play song android", "play android song" ] },
    "question": { "triggers": [ "question" ] }
  },
	"voice": {"voice_name": "Brian", "language": "en-GB", "gender": "Male"}
}
```

- **triggers**: the triggers that "wake" the bot (words you say so that the bot know you want to execute a command)
- **grettings**: the bot responses to being woken
- **commands**: the commands that the bot will execute
- **voice**: the voice configuration from ivona

## Note (pyOpenSSL)
Before running check your pyOpenSSL version. It needs to be **>= 0.14**.

Run this to check the version:

    $  python -c 'import OpenSSL; print(OpenSSL.__version__)'

Run this to update it:    

    (venv) $ $VENV/bin/pip install -U pyOpenSSL

In Windows:

    > python -m pip install -U pyOpenSSL

## Run

    (venv) $ $VENV/bin/python api_dudebot.py

In Windows:

    (venv) > %VENV%\Scripts\python api_dudebot.py

The app will start listening on port: `8080`.
Open the browser into [localhost:8080](http://localhost:8080) and you should see the bot.

Read the [site README](./site) to know how to interact with the bot.

## Stop running bot/venv

    CTRL+C
    (venv) $ deactivate

### Note (Browser)
Run in Google Chrome has this uses `Speech Recognition API` and currently only Chrome and Opera have partial support for it.

## Docs
[docs](./docs)

## Resources

- [Raspberry Pi Voice Recognition Works Like Siri](https://oscarliang.com/raspberry-pi-voice-recognition-works-like-siri/)
- [Pyvona - A python wrapper for Amazon's IVONA API](http://zacharybears.com/pyvona/)
- [BEST VOICE RECOGNITION SOFTWARE FOR RASPBERRY PI](http://diyhacking.com/best-voice-recognition-software-for-raspberry-pi/)
