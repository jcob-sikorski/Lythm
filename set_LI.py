def set_LI():
    '''What phase of a day is now? Func receives data about light intensity in the environment and returns a thereshold.'''

    from DayPhase import DayPhase
    from recv_light import recv_light
    from datetime import datetime

    current_time = datetime.now()
    current_hour = current_time.hour
    
    light_intensity = recv_light()
    day_phase = DayPhase()

    if light_intensity <= day_phase.MORNING and current_hour <= 8:
        return "MORNING"
    elif light_intensity <= day_phase.MIDDAY and current_hour <= 13:
        return "MIDDAY"
    elif light_intensity <= day_phase.AFTERNOON and current_hour <= 19:
        return "ATERNOON"
    elif light_intensity <= day_phase.EVENING and current_hour <= 22:
        return "EVENING"
    else:
        return "NIGHT"
