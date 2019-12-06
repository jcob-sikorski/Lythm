def recv_light():
    import socket
    import xml.etree.ElementTree as ET
    from re import search

    '''Receives data about light intensity in xml data format and extracts from it light intensity float(value).'''

    '''WARNING: disable FIREWALL!!!!!'''

    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(("", port))
    print('\n', 'waiting on port:', port)

    while 1:
        # receiving data from a socket
        data, addr = s.recvfrom(1024)

        print(f'IP of sender: {addr}')
        print('\n', f'recv data: {data}')
        break
    # decode data
    dec_xml = data.decode('utf-8')
    # search for LightIntensity value
    result = search('<LightIntensity>(.*)</LightIntensity>', dec_xml)
    # convert str(value) to int
    light_intesity = float(result.group(1))
    print('\n', f'light intensity: {light_intesity}')

    return light_intesity
