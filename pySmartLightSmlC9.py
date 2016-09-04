import binascii
from bluepy import btle


class SmartLight(btle.Peripheral):
    def __init__(self, addr):
        btle.Peripheral.__init__(self, addr)
        self.delegate = NotificationDelegate()
        self.setDelegate(self.delegate)
        self.light_svc = self.getServiceByUUID('33160fb9-5b27-4e70-b0f8-ff411e3ae078')
        self.light_cmd_ch = self.light_svc.getCharacteristics('217887f8-0af2-4002-9c05-24c9ecf71600')[0]

    def on(self):
        self.light_cmd_ch.write(binascii.unhexlify('01'))

    def off(self):
        self.light_cmd_ch.write(binascii.unhexlify('00'))


class NotificationDelegate(btle.DefaultDelegate):
    def __init__(self):
        btle.DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        bytes_data = bytearray(data)
        # debug
        print("rx notif %s=%s" % (cHandle, binascii.hexlify(bytes_data)))

# pySmartLightSmlC9 sample: turn on light for 2s
if __name__ == '__main__':
    import time

    # connect to the light with bluetooth address
    light = SmartLight('98:7b:f3:61:17:c5')

    # cycle power
    light.on()
    time.sleep(2.0)
    light.off()
