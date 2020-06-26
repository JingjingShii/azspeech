Azure Speech Capabilities
=========================

This [MLHub](https://mlhub.ai) package provides a quick introduction
to the pre-built Speech models provided through Azure's Cognitive
Services. This service can, for example, take an audio signal and
transcribes it to return the text. It also supports speech synthesis.

In addition to the demonstration this package provides a collection of
commands that turn the service into a useful command line tool for
transcribing from the microphone or from an audio file, and
synthesising speech.

A free Azure subscription allowing up to 5,000 transactions per month
is available from https://azure.microsoft.com/free/. After subscribing
visit https://ms.portal.azure.com and Create a resource under AI and
Machine Learning called Speech Services. Once created you can access
the web API subscription key and endpoint from the portal. This will
be prompted for in the demo.

This package is part of the Azure on MLHub suite. Please note that
these Azure models, unlike the MLHub models in general, use *closed
source services* which have no guarantee of ongoing availability and
do not come with the freedom to modify and share.

Visit the github repository for more details:
<https://github.com/gjwgit/azspeech>

The Python code is based on the [Azure Speech Services Quick Start for
Python](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-python).

Quick Start
-----------

```console
$ ml demo azspeech
$ ml listen azspeech
$ wget https://github.com/realpython/python-speech-recognition/raw/master/audio_files/harvard.wav
$ ml transcribe azspeech harvard.wav
```

Usage
-----

- To install mlhub (Ubuntu)

```console
$ pip3 install mlhub
```

- To install and configure the demo:

```console
$ ml install   azspeech
$ ml configure azspeech
```

Command Line Tools
------------------

In addition to the *demo* presented below, the *azspeech2txt* package
provides a number of useful command line tools.

*Listen*

The *listen* command will listen for an utterance from the computer microphone
for up to 15 seconds and then transcribe it to standard output.

```console
$ ml listen azspeech
The machine learning hub is useful for demonstrating capability of 
models as well as providing command line tools.
```
We can pipe the output to other tools, such as to analyse the
sentiment of the spoken word. In the first instance you might say
*happy days* and in the second say *sad days*.

```console
$ ml listen azspeech | ml sentiment aztext
0.96

$ ml listen azspeech | ml sentiment aztext
0.07
```

*Transcribe*

The *transcribe* command takes an audio file and transcribes it to
standard output. For large audio files this can take some time.

```console
$ ml transcribe azspeech harvard.wav
The stale smell of old beer lingers it takes heat to bring out the odor.
A cold dip restore's health and Zest, a salt pickle taste fine with
Ham tacos, Al Pastore are my favorite a zestful food is the hot cross bun.
```

The audio file comes from Github:
https://github.com/realpython/python-speech-recognition/raw/master/audio_files/harvard.wav

Demonstration
-------------

```console
$ ml demo azspeech 

=====================
Azure Speech Services
=====================

Welcome to a demo of the pre-built models for Speech provided
through Azure's Cognitive Services. This cloud service accepts audio
and then converts that into text which it returns locally.

The following file has been found and is assumed to contain
an Azure Speech Services subscription key and region. We will load 
the file and use this information.

    /home/kt/.mlhub/azspeech/private.txt

Say something...

> Recognized: Welcome to a demo of the prebuilt models for speech to
> text provided through azure's cognitive services. This cloud service 
> accepts audio and then converts that into text, which it returns locally.

Thank you for exploring the 'azspeech model.
```

As you can see I read the first paragraph from the screen and the
Azure Speech to Text service was quite accurate in its
transcription. If the accuracy for the particular accent is good then
it is quite suitable, for example, to be used as a dictation tool.

Resources
---------

* [Quick Start for
  Speech2Text](https://github.com/Azure-Samples/cognitive-services-speech-sdk/blob/master/quickstart/python/from-microphone)
  
