import syslog
import weewx
from weewx.wxengine import StdService
from weewx.units import Converter

from Adafruit_BME280 import *

class BME280Service(StdService):
    def __init__(self, engine, config_dict):
        super(BME280Service, self).__init__(engine, config_dict)      
        d = config_dict.get('BME280Service', {})
        self._init_sensor()
        self.converter = Converter()
        self.bind(weewx.NEW_ARCHIVE_RECORD, self.new_archive_record)

    def _init_sensor(self):
        try:
            self.sensor = BME280(t_mode=BME280_OSAMPLE_8,
                                 p_mode=BME280_OSAMPLE_8,
                                 h_mode=BME280_OSAMPLE_8)
        except Exception as e:
            print 'BME280: error initializing sensor: {}'.format(e)
            self.sensor = None
    
    def new_archive_record(self, event):
        if self.sensor is None:
            self._init_sensor()
        try:
            assert self.sensor is not None, "sensor is not initialized"
            self.sensor.read_temperature()
            self.sensor.read_humidity()
            sample = self.converter.convertDict({
                'usUnits': weewx.METRIC,
                'pressure': self.sensor.read_pressure()/100,
            })
            print 'BME280: sample: {}'.format(sample)
            event.record.update(sample)
        except Exception as e:
            print 'BME280: sampling error: {}'.format(e)
            self.sensor = None
