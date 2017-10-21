import syslog
import weewx
from weewx.wxengine import StdService
from weewx.units import Converter

from Adafruit_BME280 import *

class BME280Service(StdService):
    def __init__(self, engine, config_dict):
        super(BME280Service, self).__init__(engine, config_dict)      
        d = config_dict.get('BME280Service', {})
        self.sensor = BME280(t_mode=BME280_OSAMPLE_8,
                             p_mode=BME280_OSAMPLE_8,
                             h_mode=BME280_OSAMPLE_8)
        self.converter = Converter()
        self.bind(weewx.NEW_ARCHIVE_RECORD, self.new_archive_record)
    
    def new_archive_record(self, event):
        try:
            sample = {'usUnits': weewx.METRIC,
                      'inTemp': self.sensor.read_temperature(),
                      'inHumidity': self.sensor.read_humidity(),
                      'pressure': self.sensor.read_pressure()/100}
            print 'BME280: raw sample: {}'.format(sample)
            sample = self.converter.convertDict(sample)
            print 'BME280: converted sample: {}'.format(sample)
            event.record.update(sample)
        except Exception as e:
            print 'BME280: error: {}'.format(e)
