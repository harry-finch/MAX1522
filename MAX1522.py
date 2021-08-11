# MAX1522 circuit generator by Stéphane Muller
#
# The script will calculate the values of the passive components needed given a Vin and a desired Vout.
# All formulas taken from the datasheet.
#
# Datasheet for MAX1522: https://datasheets.maximintegrated.com/en/ds/MAX1522-MAX1524.pdf
#
# > python3 MAX1522.py [Vin] [Vout]
# Arguments are optional, user will be prompted for values.

import sys

# elecUnits.py needs to be in the same directory
import elecUnits

def dcmDesign(Vinmin, Vout, Vd, Iloadmax, Ton, Tss, Rtwo, Vfb):
    Rone = Rtwo * ((Vout / Vfb) - 1)
    dutyCycle = ((Vout + Vd - Vinmin)/(Vout + Vd)) * 100
    Lideal = (Vinmin*Vinmin*Ton)/(3*(Vout+Vd)*Iloadmax)
    Coutmin = (Ton*Ton*Vinmin*Vinmin)/(2*Lideal*(Vout+Vd-Vinmin)*0.02*Vout)
    Coutmax = (Iloadmax*Tss)/Vout

    print()
    print("Vin(min) = {:.1f}V and Vout = {:.1f}V".format(Vinmin, Vout))
    print("Max duty cycle is {:.1f}% >> DCM design".format(dutyCycle))
    print()
    print("R1 = {}Ω and R2 = {}Ω".format(elecUnits.unitPrefix(Rone), elecUnits.unitPrefix(Rtwo)))
    print("L(ideal) = {}H".format(elecUnits.unitPrefix(Lideal)))
    print("Cout(min) = {}F and Cout(max) = {}F".format(elecUnits.unitPrefix(Coutmin), elecUnits.unitPrefix(Coutmax)))
    print()

def ccmDesign(Vinmin, Vout, Vd, Iloadmax, Ton, Tss, Rtwo, Vfb):
    Rone = Rtwo * ((Vout / Vfb) - 1)
    dutyCycle = ((Vout + Vd - Vinmin)/(Vout + Vd)) * 100
    Lideal = (Vinmin*Ton)/(0.3*Iloadmax)
    Coutmin = (Ton*Iloadmax)/(0.005*Vout)
    Coutmax = (Iloadmax*Tss)/Vout

    print()
    print("Vin(min) = {:.1f}V and Vout = {:.1f}V".format(Vout, Vout))
    print("Max duty cycle is {:.1f}% >> CCM design".format(dutyCycle))
    print()
    print("R1 = {}Ω and R2 = {}Ω".format(elecUnits.unitPrefix(Rone), elecUnits.unitPrefix(Rtwo)))
    print("L(ideal) = {}H".format(elecUnits.unitPrefix(Lideal)))
    print("Cout(min) = {}F and Cout(max) = {}F".format(elecUnits.unitPrefix(Coutmin), elecUnits.unitPrefix(Coutmax)))
    print()

# if Vin and Vout have not been passed as arguments, prompt user for all values
if len(sys.argv) != 3:
    Vinmin = elecUnits.prefixToValue(input("Vin (V) : "))
    while not Vinmin: Vinmin = elecUnits.prefixToValue(input("Vin (V) : "))

    Vout = elecUnits.prefixToValue(input("Vout (V) : "))
    while not Vout: Vout = elecUnits.prefixToValue(input("Vout (V) : "))

    Vd = elecUnits.prefixToValue(input("Vd (V - default O.5V) : "))
    if Vd is None: Vd = elecUnits.prefixAndUnitToValue("0.5V")
    
    Iloadmax = elecUnits.prefixToValue(input("Iloadmax (A - default 30mA) : "))
    if Iloadmax is None: Iloadmax = elecUnits.prefixAndUnitToValue("30mA")

    Ton = elecUnits.prefixToValue(input("Ton (s - default 3µs) : "))
    if Ton is None: Ton = elecUnits.prefixAndUnitToValue("3µs")

    Tss = elecUnits.prefixToValue(input("Tss (s - default 3.2ms) : "))
    if Tss is None: Tss = elecUnits.prefixAndUnitToValue("3.2ms")

    Rtwo = elecUnits.prefixToValue(input("R2 (default 30K - needs to be between 30K and 100K) : "))
    if Rtwo is None: Rtwo = elecUnits.prefixAndUnitToValue("30KΩ")

    Vfb = elecUnits.prefixToValue(input("Vfb (default 1.25V) : "))
    if Vfb is None: Vfb = elecUnits.prefixAndUnitToValue("1.25V")
else:
    Vinmin = float(sys.argv[1])
    Vout = float(sys.argv[2])
    Vd = elecUnits.prefixAndUnitToValue("0.5V")
    Iloadmax = elecUnits.prefixAndUnitToValue("30mA")
    Ton = elecUnits.prefixAndUnitToValue("3µs")
    Tss = elecUnits.prefixAndUnitToValue("3.2ms")
    Rtwo = elecUnits.prefixAndUnitToValue("30KΩ")
    Vfb = elecUnits.prefixAndUnitToValue("1.25V")

dutyCycle = ((Vout + Vd - Vinmin)/(Vout + Vd)) * 100

if dutyCycle<=45: Ton = elecUnits.prefixAndUnitToValue("0.5µs")

if dutyCycle>=80: dcmDesign(Vinmin, Vout, Vd, Iloadmax, Ton, Tss, Rtwo, Vfb)
else: ccmDesign(Vinmin, Vout, Vd, Iloadmax, Ton, Tss, Rtwo, Vfb)