from .models import TempSensor

def add_temp_reading_controller(params):
    if not params.get('temp'):
        return False
    new_entry = TempSensor()
    new_entry.reading = params.get('temp')
    new_entry.save()
    return True