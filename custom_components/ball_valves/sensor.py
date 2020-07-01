"""Platform for sensor integration."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from gpiozero import InputDevice
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
        self._pinopen = InputDevice(pin_open, pull_up=True)
        self._pinclosed = InputDevice(pin_closed, pull_up=True)
        self._name = name
        self._is_on = None
        self._description = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def is_on(self):
        """Indicate if the ball valve is open or closed (on/off)."""
        return self._is_on

    @property
    def available(self):
        """Indicate if we can read the state of the ball valve."""
        return self._is_on == None

    @property
    def device_class(self):
        """Indicate the device class of the sensor."""
        return "lock"

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return "mdi:water-pump"

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        if self._pinopen.value == 1 and self._pinclosed.value == 0:
            self._is_on = True
            self._description = self._name + ' ball valve is Open'
        elif self._pinopen.value == 0 and self._pinclosed.value == 1:
            self._is_on = False
            self._description = self._name + ' ball valve is Closed'
        else:
            self._is_on = None  # means something is wrong
            self._description = 'Cannot read position of ' + self._name + ' ball valve'
