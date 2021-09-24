# suvat-calc
Calculates SUVAT values using 20 SUVAT equations.

Usage:

Create object with Suvat(s,u,v,a,t,mode), where s,u,v,a and t are float/int.

Find desired value with myObject.s1(), u1(), v1(), a1(), t1() (function name corresponds with desired value).

myObject.all() returns a dictionary containing all SUVAT values.

Pass '?' as an attribute when you are missing a value.

Modes: c and r. 'r' stands for 'raw', which returns the raw value (as float), and 'c' stands for 'Context', which returns 'Displacement is {s} m' (for example), to avoid confusion.
Mode r is the default mode.

