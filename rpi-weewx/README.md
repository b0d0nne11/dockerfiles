# rpi-weewx

Raspberry Pi compatible Docker image for [Weewx](http://weewx.com/).

Powers https://brendan.odonnell.xyz/weather/.

To build:
```
docker build --tag odonnell.xyz/rpi-weewx:latest .
```

To run:
```
docker run -d --name weewx -v /var/www/weewx:/home/weewx/public_html -v /etc/weewx/weewx.conf:/home/weewx/weewx.conf --privileged -v /dev/bus/usb:/dev/bus/usb -v /dev/i2c-1:/dev/i2c-1 odonnell.xyz/rpi-weewx:latest
```

To test the SDR module:
```
docker run -ti --rm -e PYTHONPATH=bin --privileged -v /dev/bus/usb:/dev/bus/usb odonnell.xyz/rpi-weewx:latest bin/user/sdr.py
```
