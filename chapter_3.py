###################### My own Descriptor, not directly code equivalent found in
###################### the book ###############################################
class Accessor(object):
    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data.get(instance)

    def __set__(self, value):
        self.data[instance] = value

############## Page 36 ##############


class Gear(object):
    def __init_(self, chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__rim = rim
        self.__tire = tire

    def gear_inches(self):
        return self.ratio() * Wheel(self.rim, self.tire).diameter()

    def ratio(self):
        return self.chainring / float(self.cog)

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire
# ...

class Wheel(object):
    def __init__(self, rim, tire):
        self.__rim = rim
        self.__tire = tire

    def diameter(self):
        self.rim + (self.tire * 2)

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire
# ...

Gear(52, 11, 26, 1.5).gear_inches()

############## Page 39 ##############

class Gear(object):

    def __init__(self, chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__rim = rim
        self.__tire = tire

    def gear_inches(self):
        return self.ratio() * Wheel(self.rim, self.tire).diameter()

    @property
    def chairing(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire
# ...

Gear(52, 11, 26, 1.5).gear_inches()

############## Page 41 ##############

class Gear(object):
    def __init__(self, chainring, cog, wheel):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def wheel(self):
        return self.__wheel
# ...

# Gear expects a 'Duck' that knows 'diameter'
Gear(52, 11, Wheel(26, 1.5)).gear_inches()

############## Page 43 ##############
class Gear(object):
    def __init__(chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = Wheel.new(rim, tire)

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()
# ...

############## Page 43 ##############

class Gear(object):
    def __init__(chainring, cog, rim, tire):
        self.__chainring = chainring
        self.__cog = cog
        self.__rim = rim
        self.__tire = tire

    def gear_inches(self):
        return self.ratio() * self.wheel().diameter()

    def wheel(self):
        self.__wheel = self.__wheel or Wheel(self.rim, self.tire)
        return self.__wheel
# ...

############## Page 44 ##############
    def gear_inches(self):
        return self.ratio() * self.wheel().diameter()

############## Page 44 ##############

    def gear_inches(self):
        #... a few lines of scary math
        foo = some_intermediate_result * self.wheel.diameter()
        #... more lines of scary math

############## Page 45 ##############

    def gear_inches(self):
        #... a few lines of scary math
        foo = some_intermediate_result * self.diameter()
        #... more lines of scary math

    def diameter(self):
        return self.wheel.diameter()

############## Page 46 ##############


class Gear(object):
    def __init__(self, chainring, cog, wheel):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel
  #...

Gear(52, 11, Wheel(26, 1.5)).gear_inches()

############## Page 47 ##############


class Gear(object):
    def __init__(self, **kwargs):
        self.__chainring = kwargs['chainring']
        self.__cog = kwargs['cog']
        self.__wheel = kwargs['wheel']
  #...

Gear(chainring=52, cog=11, wheel=Wheel(26, 1.5)).gear_inches()

############## Page 48 ##############
  # specifying defaults using `get` (ruby `fetch`)

    def __init__(self, wheel, **kwargs):
        self.__chainring = kwargs.get('chainring', 40)
        self.__cog = kwargs.get('cog', 18)
        self.__wheel = wheel

        # Alternative implementation afforded by python keyword args

    def __init__(self, wheel, chainring=40, cog=18):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel

############## Page 49 ##############
  # specifying defaults using python `get' instead of ruby `fetch`
    def __init__(**kwargs):
        self.__chainring = kwargs.get('chainring', 40)
        self.__cog = kwargs.get('cog', 18)
        self.__wheel = kwargs[:wheel]

############## Page 49 ##############
    # specifying defaults by merging a defaults hash
    def __init__(**kwargs):
        kwargs = self.defaults().update(kwargs)
        self.__chainring = kwargs['chainring']
    #   ...

    def defaults(self):
        return {'chainring': 40, 'cog': 18}

############## Page 50 ##############
# When Gear is part of an external interface
# inside some someframework
class Gear(object):
    def __init__(self, chainring, cog, wheel):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel
  # ...

# wrap the interface to protect yourself from changes
class GearWrapper(object):
    @classmethod
    def gear(**kwargs):
        from someframework import Gear
        return Gear(kwargs.get('chainring'), kwargs.get('cog'), kwargs.get('wheel'))

# Now you can create a new Gear using an arguments hash.
GearWrapper.gear(chainring=52, cog=11, wheel=Wheel(26, 1.5)).gear_inches()

############## Page ?? ##############
# This is the complete code for example above
# in some module SomeFramework
class Gear(object):
    def __init__(self, chainring, cog, wheel):
        self.__chainring = chainring
        self.__cog = cog
        self.__wheel = wheel

    def gear_inches(self):
        return self.ratio() * self.wheel.diameter()

    def ratio(self):
        return self.chainring / float(self.cog)

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

    @property
    def wheel(self):
        return self.__wheel

class Wheel(object):
    def __init__(self, rim, tire):
        self.__rim = rim
        self.__tire = tire

    def diameter(self):
        return self.rim + (self.tire * 2)

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire

class GearWrapper(object):
    @classmethod
    def gear(**kwargs):
        from someframework import Gear
        return Gear(kwargs.get('chainring'), kwargs.get('cog'), kwargs.get('wheel'))

GearWrapper.gear(chainring=52, cog=11, wheel=Wheel(26, 1.5)).gear_inches()

############## Page 52 ##############
class Gear(object):
    def __init__(self, chainring, cog):
        self.__chainring = chainring
        self.__cog = cog

    def gear_inches(self, diameter):
        return self.ratio() * diameter

    def ratio(self):
        return self.chainring / float(self.cog)

    @property
    def chainring(self):
        return self.__chainring

    @property
    def cog(self):
        return self.__cog

#  ...

class Wheel(object):
    def __init__(self, rim, tire, chainring, cog):
        self.__rim = rim
        self.__tire = tire
        self.__gear = Gear(chainring, cog)

    def diameter(self):
        return self.rim + (self.tire * 2)

    def gear_inches(self):
        return self.gear.gear_inches(self.diameter())

    @property
    def rim(self):
        return self.__rim

    @property
    def tire(self):
        return self.__tire

    @property
    def gear(self):
        return self.__gear
#  ...

Wheel(26, 1.5, 52, 11).gear_inches()
