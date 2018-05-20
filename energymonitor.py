import minimalmodbus
import serial
import sys
import os
import string
import subprocess

new_string = ''

def _calculte_mantissa(bin_number, exponent):
    val = 1 if exponent > -127 else 0
    bit_count = -1
    bit_length = 0
    while bit_length <= 22:
        val += int(bin_number[bit_length]) * 2**bit_count
        bit_count -= 1
        bit_length += 1
    return val


def convert_ieee754(hex_val):
    bin_pos = format(int(hex_val, 16), "0>32b")
    sign = (-1)**int(bin_pos[0], 2)
    _exponent = int(bin_pos[1:9], 2) - 127
    mantissa = _calculte_mantissa(bin_pos[9:], _exponent)
    exponent = _exponent if _exponent > -127 else -126
    position = sign * 2**exponent * mantissa
    return position

#if __name__ == "__main__":
#    argvs = sys.argv
#    print convert_ieee754(argvs[1])
#    sys.exit()

def ReadVoltage():
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    instrument.serial.port
    instrument.serial.baudrate = 19200
    instrument.serial.bytesize
    instrument.serial.parity = serial.PARITY_EVEN
    VoltajMSB = instrument.read_register(3027)
    VoltajLSB = instrument.read_register(3026)
	#   Frecventa = instrument.read_register(3109)
    print (hex(VoltajMSB))
    print (hex(VoltajLSB))
#   print (hex(Frecventa))
    TotalVoltage = hex(VoltajMSB) + hex(VoltajLSB)
    str(TotalVoltage)
    new_str =  string.replace(TotalVoltage, '0x', '')
#   print new_str
#   string = new_str
#   cmd="./float32 "+new_string
#   os.system (cmd)
    FinalValue = convert_ieee754(new_str)
#   print FinalValue
    return FinalValue

def TotalEnergy():
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    instrument.serial.port
    instrument.serial.baudrate = 19200
    instrument.serial.bytesize
    instrument.serial.parity = serial.PARITY_EVEN
    TotalEnergyMSB = instrument.read_register(3205)
    TotalEnergyLSB = instrument.read_register(3206)
#   int(TotalEnergyMSB)
#   int(TotalEnergyLSB)
    TotalEnergy_INT64 = TotalEnergyMSB * 65535 + TotalEnergyLSB
    return TotalEnergy_INT64

def Frequency():
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    instrument.serial.port
    instrument.serial.baudrate = 19200
    instrument.serial.bytesize
    instrument.serial.parity = serial.PARITY_EVEN
    eFrequencyMSB = instrument.read_register(3109)
    eFrequencyLSB = instrument.read_register(3109)
    TotalFrequency = hex(eFrequencyMSB) + hex(eFrequencyLSB)
    str(TotalFrequency)
    frq =  string.replace(TotalFrequency, '0x', '')
    FinalFreq = convert_ieee754(frq)
    return FinalFreq

def main():
    voltaj = ReadVoltage()
    energy = TotalEnergy()
    freq = Frequency()
    print voltaj
    print energy/1000
    print freq
    return
main()

