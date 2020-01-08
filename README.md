# django-pwa

Library for adding progressive web app functionality in your django project.

## Table of content
- [Introduction](#introduction)
- [Installing](#installing)
- [Configuration](#configuration)
- [Usage](#usage)
- [Links](#links)

## Introduction
This Django library adds [progressive web app](https://developers.google.com/web/progressive-web-apps/) functionality in your django project.

When you open your site from your mobile browser, will prompt you to add the site to your home screen as an application.

## Installing
```
pip install django-progressive
```

## Configuration
Add django-progressive ```django_pwa``` to your installed apps ```INSTALLED_APPS```
in django ```settings.py```
```python
INSTALLED_APPS = [
    '...',
    'django_pwa'
    '...'
]
```
Define ```STATICFILES_DIRS```

In ```settings.py``` using the prefix PWA_ and the keys from [the web app manifest](#https://developers.google.com/web/fundamentals/web-app-manifest)
all in capital you can configure the pwa manifest.

```python
PWA_NAME = 'test app'
PWA_SHORT_NAME = 'test_app'
PWA_ICONS = [
    {
        "src": "/static/icons/icon-128x128.png",
        "sizes": "128x128",
        "type": "image/png"
    }, {
        "src": "/static/icons/icon-144x144.png",
        "sizes": "144x144",
        "type": "image/png"
    }, {
        "src": "/static/icons/icon-152x152.png",
        "sizes": "152x152",
        "type": "image/png"
    }, {
        "src": "/static/icons/icon-192x192.png",
        "sizes": "192x192",
        "type": "image/png"
    }, {
        "src": "/static/icons/icon-256x256.png",
        "sizes": "256x256",
        "type": "image/png"
    }, {
        "src": "/static/icons/icon-512x512.png",
        "sizes": "512x512",
        "type": "image/png"
    }
]
```
You can change the default worker location with
```PWA_WORKER_LOCATION```.
```python
PWA_WORKER_LOCATION = join('static', 'django_pwa_demo', 'service-worker.js')
```

## Usage
Add `django_pwa` urls to your `urls.py`
```python
from django.urls import path, include

urlpatterns = [
    '...',
    path('', include('django_pwa.urls')),
    '...'
]
```
You can add `{% load pwa_extras %}` to use `{% load_manifest %}` template tag to load the `manifest.json` and `{% load_worker %}` to load the `worker-app.js`.
```html
{% load pwa_extras %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PWA Test</title>
    {% load_manifest %}
</head>
<body>
<h1>Hello world!!!</h1>

{% load_worker %}
</body>
</html>
```

## Links

- [Progressive Web Apps](#https://developers.google.com/web/fundamentals/web-app-manifest)
- [Wikipedia](#https://en.wikipedia.org/wiki/Progressive_web_application)
- [WPA Manifest](#https://developers.google.com/web/fundamentals/web-app-manifest)