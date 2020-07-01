"""Platform for sensor integration."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from gpiozero import DigitalInputDevice
from enum import Enum


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([
        BallValve('Engine', 4, 3)
    ])


class BallValve(BinarySensorEntity):
    """Representation of a Sensor."""

    def __init__(self, name, pin_open, pin_closed):
        """Initialize the sensor."""
        self._name = name
        self._is_on = None
        self._description = None
        self._attributes = {}

        # Setup GPIO pins
        self._pinopen = DigitalInputDevice(pin_open, pull_up=True)
        self._pinclosed = DigitalInputDevice(pin_closed, pull_up=True)
        self._pinopen.when_activated = self.on_change
        self._pinopen.when_deactivated = self.on_change
        self._pinclosed.when_activated = self.on_change
        self._pinclosed.when_deactivated = self.on_change
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return "Ball valve " + self._name.lower()

    @property
    def is_on(self):
        """Indicate if the ball valve is open or closed (on/off)."""
        return self._is_on

    @property
    def available(self):
        """Indicate if we can read the state of the ball valve."""
        return self._is_on is not None

    @property
    def device_class(self):
        """Indicate the device class of the sensor."""
        return "lock"

    @property
    def icon(self):
        """Return the icon of the sensor."""
        if self._is_on is True: return "mdi:valve-open"
        elif self._is_on is False: return "mdi:valve-closed"
        else: return "mdi:valve"

    @property
    def device_state_attributes(self):
        """Return the attribute(s) of the sensor."""
        return self._attributes

    @property
    def should_poll(self):
        """Return False for push based updates."""
        return False

    def on_change(self):
        """Callback when any of the pins change state."""
        self.update()
        self.schedule_update_ha_state()

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        if self._pinopen.is_active and not self._pinclosed.is_active:
            self._is_on = True
            self._description = self._name + ' ball valve is Open'
        elif not self._pinopen.is_active and self._pinclosed.is_active:
            self._is_on = False
            self._description = self._name + ' ball valve is Closed'
        else:
            self._is_on = None  # means something is wrong
            self._description = 'Cannot read position of ' + self._name + ' ball valve'

        self._attributes = {
            'description': self._description
        }
