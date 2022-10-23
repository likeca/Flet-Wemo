import flet, re, requests
from flet import alignment, border_radius, ButtonStyle, colors, Column, Container, ElevatedButton, icons, IconButton, Page, Row, Text, TextField, Slider
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder

def wemo(ip, command):        # on | off |  get_state | get_name | find
    url = f'http://{ip}:49153/upnp/control/basicevent1'
    
    if command == 'on':
        switch = 1                  # 1: ON, 0: OFF
        operation = 'Set'           # Get or Set, GetBinaryState, SetBinaryState, GetSignalStrength, 
        option = 'BinaryState'
    if command == 'off':
        switch = 0                  # 1: ON, 0: OFF
        operation = 'Set'           # Get or Set, GetBinaryState, SetBinaryState, GetSignalStrength, 
        option = 'BinaryState'
    if command == 'get_state':
        switch = 0                  # 1: ON, 0: OFF
        operation = 'Get'           # Get or Set, GetBinaryState, SetBinaryState, GetSignalStrength, 
        option = 'BinaryState'
    if command == 'get_name':
        switch = 0                  # 1: ON, 0: OFF
        operation = 'Get'           # Get or Set, GetBinaryState, SetBinaryState, GetSignalStrength, 
        option = 'FriendlyName'

    headers = {
        'Accept': '*/*',
        'content-type': 'text/xml; charset="utf-8"',
        'SOAPACTION': f'"urn:Belkin:service:basicevent:1#{operation}{option}"'
    }
    data = f'''
        <?xml version="1.0" encoding="utf-8"?>
        <s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
            <s:Body>
                <u:{operation}{option} xmlns:u="urn:Belkin:service:basicevent:1">
                    <{option}>{switch}</{option}>
                </u:{operation}{option}>
            </s:Body>
        </s:Envelope>
    '''

    try:
        response = requests.post(url, data=data, headers=headers, timeout=1)
        if command == 'get_name':
            state = re.search("<FriendlyName>(.*)</FriendlyName>", response.text)
            return state.group(1)
        else:
            state = re.search("<BinaryState>(.)</BinaryState>", response.text)
            return state.group(1)
    except:
        return '-1'

def main(page: Page):
    page.bgcolor = '#ffffff'
    page.title = 'WeMo Light Switch'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    page.window_height = 350
    page.window_width = 550

    def btn_click(ip):
        if int(wemo(ip=ip, command='get_state')):
            wemo(ip=ip, command='off')
        else:
            wemo(ip=ip, command='on')
        items.clear()
        get_all_state()
        page.update()

    items = []
    def get_all_state():
        devices = {}
        for i in range(2, 10):
            devices[f'192.168.1.10{i}'] = [wemo(ip=f'192.168.1.10{i}', command='get_name'), int(wemo(ip=f'192.168.1.10{i}', command='get_state'))]

        if devices['192.168.1.102'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.102'][0], on_click=lambda e: btn_click(ip='192.168.1.102'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.102'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.102'][0], on_click=lambda e: btn_click(ip='192.168.1.102'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.102'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.102'][0], on_click=lambda e: btn_click(ip='192.168.1.102'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

        if devices['192.168.1.103'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.103'][0], on_click=lambda e: btn_click(ip='192.168.1.103'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.103'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.103'][0], on_click=lambda e: btn_click(ip='192.168.1.103'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.103'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.103'][0], on_click=lambda e: btn_click(ip='192.168.1.103'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

        if devices['192.168.1.104'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.104'][0], on_click=lambda e: btn_click(ip='192.168.1.104'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.104'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.104'][0], on_click=lambda e: btn_click(ip='192.168.1.104'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.104'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.104'][0], on_click=lambda e: btn_click(ip='192.168.1.104'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

        if devices['192.168.1.105'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.105'][0], on_click=lambda e: btn_click(ip='192.168.1.105'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.105'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.105'][0], on_click=lambda e: btn_click(ip='192.168.1.105'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.105'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.105'][0], on_click=lambda e: btn_click(ip='192.168.1.105'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

        if devices['192.168.1.106'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.106'][0], on_click=lambda e: btn_click(ip='192.168.1.106'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.106'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.106'][0], on_click=lambda e: btn_click(ip='192.168.1.106'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.106'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.106'][0], on_click=lambda e: btn_click(ip='192.168.1.106'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

        if devices['192.168.1.107'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.107'][0], on_click=lambda e: btn_click(ip='192.168.1.107'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.107'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.107'][0], on_click=lambda e: btn_click(ip='192.168.1.107'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.107'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.107'][0], on_click=lambda e: btn_click(ip='192.168.1.107'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

        if devices['192.168.1.108'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.108'][0], on_click=lambda e: btn_click(ip='192.168.1.108'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.108'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.108'][0], on_click=lambda e: btn_click(ip='192.168.1.108'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.108'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.108'][0], on_click=lambda e: btn_click(ip='192.168.1.108'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

        if devices['192.168.1.109'][1] == 1:
            button = ElevatedButton(text=devices['192.168.1.109'][0], on_click=lambda e: btn_click(ip='192.168.1.109'), bgcolor='blue', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.109'][1] == 0:
            button = ElevatedButton(text=devices['192.168.1.109'][0], on_click=lambda e: btn_click(ip='192.168.1.109'), bgcolor='blueGrey', color='white', width=200, height=50)
            items.append(button)
        elif devices['192.168.1.109'][1] == -1:
            button = ElevatedButton(text=devices['192.168.1.109'][0], on_click=lambda e: btn_click(ip='192.168.1.109'), bgcolor='blueGrey', color='white', width=200, height=50, disabled=True)
            items.append(button)

    get_all_state()

    page.add(
        Row(
            items,
            alignment='center',
            run_spacing=10,
            spacing=10,
            wrap=True
        ),
    )

flet.app(target=main)
