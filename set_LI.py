def set_LI():
    '''What phase of a day is now? Func receives data about light intensity in the environment and returns a thereshold.'''

    from DayPhase import DayPhase
    from recv_light import recv_light

    light_intensity = recv_light()
    day_phase = DayPhase()

    if light_intensity <= day_phase.MORNING:
        return 1
    elif light_intensity <= day_phase.MIDDAY:
        return 2
    elif light_intensity <= day_phase.AFTERNOON:
        return 3
    elif light_intensity <= day_phase.EVENING:
        return 4
    else:
        return 5
