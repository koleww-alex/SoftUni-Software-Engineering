from abc import ABC


class HdmiConnector(ABC):

    def connect_to_device_via_hdmi_cable(self, device):
        ...


class RcaConnector(ABC):

    def connect_to_device_via_rca_cable(self, device):
        ...


class EthernetConnector(ABC):

    def connect_to_device_via_ethernet_cable(self, device):
        ...


class PowerOutletConnector(ABC):

    def connect_device_to_power_outlet(self, device):
        ...


class Television(RcaConnector, HdmiConnector, PowerOutletConnector):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(HdmiConnector, PowerOutletConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(HdmiConnector, EthernetConnector, PowerOutletConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EthernetConnector, PowerOutletConnector):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
