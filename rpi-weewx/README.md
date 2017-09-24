# rpi-weewx

Raspberry Pi compatible Docker image for [Weewx](http://weewx.com/).

Powers https://brendan.odonnell.xyz/weather.

To build:
```
docker build --tag odonnell.xyz/rpi-weewx:latest .
```

To run:
```
docker run -d --name weewx-data -v /home/weewx/archive busybox:latest /bin/true
docker run -d --name weewx --volumes-from weewx-data -v /var/www/brendan.odonnell.xyz/weather:/home/weewx/public_html --privileged -v /dev/bus/usb:/dev/bus/usb odonnell.xyz/rpi-weewx:latest
```
