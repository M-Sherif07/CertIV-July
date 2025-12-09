{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1d68583-cdf8-4f51-a42f-8f81d959ca33",
   "metadata": {},
   "outputs": [],
   "source": [
    "from machine import Pin, PWM\n",
    "\n",
    "class Servo:\n",
    "    # these defaults work for the standard TowerPro SG90\n",
    "    __servo_pwm_freq = 50\n",
    "    __min_u10_duty = 26 - 0 # offset for correction\n",
    "    __max_u10_duty = 123- 0  # offset for correction\n",
    "    min_angle = 0\n",
    "    max_angle = 180\n",
    "    current_angle = 0.001\n",
    "\n",
    "\n",
    "    def __init__(self, pin):\n",
    "        self.__initialise(pin)\n",
    "\n",
    "\n",
    "    def update_settings(self, servo_pwm_freq, min_u10_duty, max_u10_duty, min_angle, max_angle, pin):\n",
    "        self.__servo_pwm_freq = servo_pwm_freq\n",
    "        self.__min_u10_duty = min_u10_duty\n",
    "        self.__max_u10_duty = max_u10_duty\n",
    "        self.min_angle = min_angle\n",
    "        self.max_angle = max_angle\n",
    "        self.__initialise(pin)\n",
    "\n",
    "\n",
    "    def move(self, angle):\n",
    "        # round to 2 decimal places, so we have a chance of reducing unwanted servo adjustments\n",
    "        angle = round(angle, 2)\n",
    "        # do we need to move?\n",
    "        if angle == self.current_angle:\n",
    "            return\n",
    "        self.current_angle = angle\n",
    "        # calculate the new duty cycle and move the motor\n",
    "        duty_u10 = self.__angle_to_u10_duty(angle)\n",
    "        self.__motor.duty(duty_u10)\n",
    "\n",
    "    def __angle_to_u10_duty(self, angle):\n",
    "        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u10_duty\n",
    "\n",
    "\n",
    "    def __initialise(self, pin):\n",
    "        self.current_angle = -0.001\n",
    "        self.__angle_conversion_factor = (self.__max_u10_duty - self.__min_u10_duty) / (self.max_angle - self.min_angle)\n",
    "        self.__motor = PWM(Pin(pin))\n",
    "        self.__motor.freq(self.__servo_pwm_freq)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "MicroPython - USB",
   "language": "micropython",
   "name": "micropython"
  },
  "language_info": {
   "name": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
