# MAX1522 circuit generator
The script will calculate the values of the passive components needed given a Vin and a desired Vout.
All formulas taken from the datasheet.

Datasheet for MAX1522: https://datasheets.maximintegrated.com/en/ds/MAX1522-MAX1524.pdf

Arguments are optional, user will be prompted for values.

```
> python3 MAX1522.py [Vin] [Vout]
> python3 MAX1522.py 3.6 30

Vin(min) = 3.6V and Vout = 30.0V
Max duty cycle is 88.2% >> DCM design

R1 = 690KΩ and R2 = 30KΩ
L(ideal) = 14µH
Cout(min) = 255nF and Cout(max) = 3.0µF

```

# elecUnits
elecUnits is a library to convert numbers into a prefix notation or vice versa.

**unitPrefix()** converts a very large or very small number into a more readable prefix notation (string).
```
unitPrefix(1000)      # returns 10.0K
unitPrefix(0.000001)  # returns 1.0µ
```

**prefixToValue()** converts a prefix notation to a float.
```
prefixToValue("10K") # returns 1000
prefixToValue("1µ")  # returns 0.000001
prefixToValue("")    # returns None
```


**prefixAndUnitToValue()** converts a prefix notation (string) - including the unit - to a float.
```
prefixAndUnitToValue("10KV") # returns 1000
prefixAndUnitToValue("1µA")  # returns 0.000001
prefixAndUnitToValue("")     # returns None
```

