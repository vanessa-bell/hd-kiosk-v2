Running and Deploying Hacker Dojo Kiosk
----------------------------------
1. Make sure you have the following: 
  - [Google App Engine SDK for Python][]
  - [Node.js][], [pip][], [virtualenv][]
  - [macOS][] or [Linux][] or [Windows][]
  - If needed, refer to the GAE-init docs on how to
[install the requirements](http://docs.gae-init.appspot.com/requirement/).

2. Clone this repo

3. Make sure [Gulp][] is installed within your project:
```bash
$ cd /path/to/hd-kiosk-v2
$ npm install gulp
```

   * If you want to install Gulp globally (recommended): 
```bash
$ npm install -g gulp
```

4. Ensure that you are using the latest version of Node.js (and npm) within your project:

```bash
$ node -v
$ npm -v
```

Compare the output to the latest versions listed [here](https://nodejs.org/en/).

5. Run the Development Environment:

 ```bash
$ cd /path/to/hd-kiosk-v2
$ npm install
$ gulp
```

 Test the site by visiting `http://localhost:3000` in your browser.

 * Note that on Windows you may have to try running gulp multiple times.

6. Deploying on Google App Engine:

 ```bash
$ gulp deploy --project=hackerdojo-kiosk-hrd
```

**Check out the GAE-init Slack channel if you run into problems:
[![Slack Status](https://gae-init-slack.herokuapp.com/badge.svg)](https://gae-init-slack.herokuapp.com)**

More about GAE-init:
----------------------------------

> **gae-init** is the easiest boilerplate to kick start new applications on Google
App Engine using Python, Flask, RESTful, Bootstrap and tons of other cool features.

Read the [documentation][], where you can find a complete [feature list][],
a detailed [tutorial][], the [how to][] section and more..

The latest version is always accessible from
[https://gae-init.appspot.com](https://gae-init.appspot.com)

Requirements
------------

  - [Google App Engine SDK for Python][]
  - [Node.js][], [pip][], [virtualenv][]
  - [macOS][] or [Linux][] or [Windows][]

Make sure you have all of the above or refer to the docs on how to
[install the requirements](http://docs.gae-init.appspot.com/requirement/).

Running the Development Environment
-----------------------------------

```bash
$ cd /path/to/project-name
$ gulp
```

To test it visit `http://localhost:3000` in your browser.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

For a complete list of commands:

```bash
$ gulp help
```

Initializing or Resetting the project
------------------------------------

```bash
$ cd /path/to/project-name
$ npm install
$ gulp
```

If something goes wrong you can always do:

```bash
$ gulp reset
$ npm install
$ gulp
```

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

To install [Gulp][] as a global package:

```bash
$ npm install -g gulp
```

Deploying on Google App Engine
------------------------------

```bash
$ gulp deploy
$ gulp deploy --project=foo
$ gulp deploy --project=foo --version=bar
$ gulp deploy --project=foo --version=bar --no-promote
```

Tech Stack
----------

  - [Google App Engine][], [NDB][]
  - [Jinja2][], [Flask][], [Flask-RESTful][], [Flask-WTF][]
  - [CoffeeScript][], [Less][]
  - [Bootstrap][], [Font Awesome][], [Social Buttons][]
  - [jQuery][], [Moment.js][]
  - [OpenID][] sign in (Google, Facebook, Twitter and more)
  - [Python 2.7][], [pip][], [virtualenv][]
  - [Gulp][], [Bower][]

[bootstrap]: http://getbootstrap.com/
[bower]: http://bower.io/
[coffeescript]: http://coffeescript.org/
[documentation]: http://docs.gae-init.appspot.com
[feature list]: http://docs.gae-init.appspot.com/features/
[flask-restful]: https://flask-restful.readthedocs.org
[flask-wtf]: https://flask-wtf.readthedocs.org
[flask]: http://flask.pocoo.org/
[font awesome]: http://fortawesome.github.com/Font-Awesome/
[google app engine sdk for python]: https://developers.google.com/appengine/downloads
[google app engine]: https://developers.google.com/appengine/
[gulp]: http://gulpjs.com
[how to]: http://docs.gae-init.appspot.com/howto/
[jinja2]: http://jinja.pocoo.org/docs/
[jquery]: https://jquery.com/
[less]: http://lesscss.org/
[linux]: http://www.ubuntu.com
[macos]: http://www.apple.com/macos/
[moment.js]: http://momentjs.com/
[ndb]: https://developers.google.com/appengine/docs/python/ndb/
[node.js]: http://nodejs.org/
[openid]: http://en.wikipedia.org/wiki/OpenID
[pip]: http://www.pip-installer.org/
[python 2.7]: https://developers.google.com/appengine/docs/python/python27/using27
[social buttons]: http://lipis.github.io/bootstrap-social/
[tutorial]: http://docs.gae-init.appspot.com/tutorial/
[virtualenv]: http://www.virtualenv.org/
[windows]: http://windows.microsoft.com/
