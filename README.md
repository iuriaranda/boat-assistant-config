# Boat automation configuration

This repository contains the configuration and software for the automation setup aboard my sailboat. The whole setup is based on [Home Assistant](https://www.home-assistant.io/) running on a Raspberry Pi 4B.

This project is still experimental and a work in progress.

## Goals

The goals of this project are:

- provide reliable and stable Internet on board from multiple Internet sources. Prioritizing the marina Wifi as it's usually unmetered, and falling back to 4G when shore Wifi is not available
- collect and aggregate data from the different boat instruments and sensors, including everything that goes through the NMEA 2000 network. These are a few examples:
  - water tank level
  - diesel tank level
  - battery status
  - GPS & AIS
  - temperature and humidity on the different cabins
  - barometric pressure
  - ball valves / seacocks state (open or closed)
  - water presense in the bilge
- provide some degree of automation, like turning on the anchor light at night or sending a notification if there's water in the bilge.

## Internet on board

Aboard a boat there are multiple ways to have an Internet connection, the two most common are Wifi from shore (normally the marina Wifi) and 3G/4G using either a Mifi router or your smartphone.

In reality, shore Wifi normally falls short of expectations, as it's unrelaiable and signal tends to be pretty weak.

A mobile connection (3G/4G) usually works quite well when you're close to the shore, but the downside is that those connections are usually mettered and limited in both bandwidth and data.

The idea is to build a router that creates a stable Wifi hotspot on board, and combines the two Internet sources together, automatically selecting the one that works best in each situation.

To provide some user-friendly control over the whole setup I use [RaspAP](https://raspap.com/), which provides some nice features.

- allows me to select which shore Wifi connection to use
- allows me to simply disconnect the "upstream" Wifi to only rely on the 4G connection
- shows some data usage metrics of the upstream Internet connections

## Home Assistant

## Acknowledgements

Inspiration and code was taken from many different sources:

- [Raspberry PI as a router gateway](https://sites.google.com/site/olewsaa/yacht-server/raspberry-pi-as-a-router-gateway) - Ole W. Saastad
- [Setup a Raspberry Pi to run a Web Browser in Kiosk Mode](https://die-antwort.eu/techblog/2017-12-setup-raspberry-pi-for-kiosk-mode/)
- [Linux fault tolerant router](https://github.com/drsound/fault_tolerant_router)
- [RaspAP](https://raspap.com/)

And special thanks to my friend Philip for his help and suggestions, and for the inspiration from his [Home Assitant configuration](https://github.com/duboisph/home-assistant-config).

## License

The code is available under the [MIT license](https://github.com/duboisph/home-assistant-config/blob/master/LICENSE).
