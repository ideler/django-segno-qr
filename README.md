# Django template tag for generating QR codes using [segno](https://github.com/heuer/segno/)
## Usage
```
{% load segno_qr %}
{% segno_qr "Your content goes here" %}
```

Parameters: See [segno.make Documentation](https://segno.readthedocs.io/en/stable/api.html#segno.make) for available parameters.
