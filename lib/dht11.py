{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aa40f49f-bae9-40b9-994b-9f6cd2e43d91",
   "metadata": {},
   "outputs": [],
   "source": [
    "# DHT11/DHT22 driver for MicroPython on ESP8266\n",
    "# MIT license; Copyright (c) 2016 Damien P. George\n",
    "\n",
    "import sys\n",
    "import machine\n",
    "\n",
    "if hasattr(machine, \"dht_readinto\"):\n",
    "    from machine import dht_readinto\n",
    "elif sys.platform.startswith(\"esp\"):\n",
    "    from esp import dht_readinto\n",
    "elif sys.platform == \"pyboard\":\n",
    "    from pyb import dht_readinto\n",
    "else:\n",
    "    dht_readinto = __import__(sys.platform).dht_readinto\n",
    "\n",
    "del machine\n",
    "\n",
    "\n",
    "class DHTBase:\n",
    "    def __init__(self, pin):\n",
    "        self.pin = pin\n",
    "        self.buf = bytearray(5)\n",
    "\n",
    "    def measure(self):\n",
    "        buf = self.buf\n",
    "        dht_readinto(self.pin, buf)\n",
    "        if (buf[0] + buf[1] + buf[2] + buf[3]) & 0xFF != buf[4]:\n",
    "            raise Exception(\"checksum error\")\n",
    "\n",
    "\n",
    "class DHT11(DHTBase):\n",
    "    def humidity(self):\n",
    "        return self.buf[0]\n",
    "\n",
    "    def temperature(self):\n",
    "        return self.buf[2]\n",
    "\n",
    "\n",
    "class DHT22(DHTBase):\n",
    "    def humidity(self):\n",
    "        return (self.buf[0] << 8 | self.buf[1]) * 0.1\n",
    "\n",
    "    def temperature(self):\n",
    "        t = ((self.buf[2] & 0x7F) << 8 | self.buf[3]) * 0.1\n",
    "        if self.buf[2] & 0x80:\n",
    "            t = -t\n",
    "        return t\n",
    "\n",
    "\n",
    "__version__ = '0.1.0'\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
