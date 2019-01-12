import pyowm

owm = pyowm.OWM('2ebadb0ce2b75afd9f221d5942cd6f98')  # API key

def get_forecast():
    fcst = owm.three_hours_forecast('Tainan')

    if fcst.will_have_rain():
        for f in fcst.when_rain():
            print('{} {}\n'.format(f.get_reference_time('iso'), f.get_status()))

if __name__ == '__main__':
    print('Collecting weather data...')
    get_forecast()