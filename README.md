# Google TTS Module (unofficial)
This is a python module which brings the facility of Google Text to Speech in python (Unofficial).

### How to use this module ?
Add this file along with the sounds directory to your python path. Then fire up the python interpreter and type :
>import googletts

>googletts.tts('hello world')

This will return you a path of the sound that was downloaded after TTS.

This module will only work on systems which have wget installed and have it included in the path variable. This module will more likely work on most of the linux based OS like Ubuntu etc. The module will be made wget independent in the future.
