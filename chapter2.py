############## Page 18 ##############
chainring = 52                    # number of teeth
cog = 11
ratio = chainring / cog.to_f
print ratio                        # -> 4.72727272727273

chainring = 30
cog = 27
ratio = chainring / cog.to_f
print ratio                        # -> 1.11111111111111

############## Page 19 ##############


class Gear(object):
    def __init__(self, chainring, cog):
        self._chainring = chainring
        self._cog = cog

    def ratio(self):
        self._chainring / float(self._cog)

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

print Gear(52, 11).ratio()        # -> 4.72727272727273
print Gear(30, 27).ratio()        # -> 1.11111111111111

############## Page 20 ##############


class Gear(object):
    def __init__(self, chainring, cog, rim, tire):
        self._chainring = chainring
        self._cog = cog
        self._rim = rim
        self._tire = tire

    def ratio(self):
        self.chainring / float(self.cog)

    def gear_inches(self):
        # tire goes around rim twice for diameter
        self.ratio * (self.rim + (self.tire * 2))

    @property
    def chainring(self):
        return self._chainring

    @property
    def cog(self):
        return self._cog

    @property
    def rim(self):
        return self._rim

    @property
    def tire(self):
        return self._tire


print Gear(52, 11, 26, 1.5).gear_inches()
# -> 137.090909090909

print Gear(52, 11, 24, 1.25).gear_inches()
# -> 125.272727272727

############## Page 20 ##############


print Gear(52, 11).ratio()  # didn't this used to work?
#  Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  TypeError: __init__() takes exactly 5 arguments (3 given)

############## Page 24 ##############


class Gear(object):
    def __init__(self, chainring, cog):
            self._chainring = chainring
            self._cog = cog

    def ratio(self):
        self._chainring / float(self._cog)      # <-- road to ruin

############## Page 25 ##############


class Gear(object):
    def __init__(self, chainring, cog):
        self._chainring = chainring
        self._cog = cog

    def ratio(self):
        self.chainring / float(self.cog)        # <-------

    @property
    def chainring(self):                        # <-------
        return self._chainring

    @property
    def cog(self):                              # <-------
        return self._cog()

############## Page 25 ##############
  # default implementation via attr_reader - * Python has no attr_reader
#  def cog(self):
#      return self._cog

############## Page 25 ##############
  # a simple reimplementation of cog
    def cog(self):
        self.cog * unanticipated_adjustment_factor

############## Page 25 ##############
  # a more complex one
    def cog(self):
        return self.cog * (bar_adjustment if self.foo() else baz_adjustment)

############## Page 26 ##############


class ObscuringReferences(object):
    def __init__(self, data):
        self._data = data

    def diameters(self):
        # 0 is rim, 1 is tire
        return [cell[0] + (cell[1] * 2) for cell in self.data]

    @property
    def data(self):
        return self._data

  # ... many other methods that index into the array

############## Page 27 ##############
# rim and tire sizes (now in milimeters!) in a 2d array
self.data = [[622, 20], [622, 23], [559, 30], [559, 40]]

############## Page 28 ##############
from collections import namedtuple


class RevealingReferences(object):
    def __init__(self, data):
        self.wheels = data

    def diameters(self):
        return [wheel.rim + (wheel.tire * 2) for wheel in self.wheels]

    @property
    def wheels(self):
        return self._wheels

    Wheel = namedtuple('Wheel', ['rim', 'tire'])

    @wheels.setter
    def wheels(self, value):
        self._wheels = [self.Wheel(cell[0], cell[1]) for cell in value]

############## Page 29 ##############
    def diameters(self):
        return [wheel.rim + (wheel.tire * 2) for wheel in self.wheels]

############## Page 29 ##############
  # first - iterate over the array
    def diameters(self):
        return [self.diameter(wheel) for wheel in self.wheels]

  # second - calculate diameter of ONE wheel
    def diameter(self, wheel):
        return wheel.rim + (wheel.tire * 2)

############## Page 30 ##############
  def gear_inches
      # tire goes around rim twice for diameter
    ratio * (rim + (tire * 2))
  end

############## Page 30 ##############
  def gear_inches
    ratio * diameter
  end

  def diameter
    rim + (tire * 2)
  end

############## Page 32 ##############
class Gear
  attr_reader :chainring, :cog, :wheel
  def initialize(chainring, cog, rim, tire)
    @chainring = chainring
    @cog       = cog
    @wheel     = Wheel.new(rim, tire)
  end

  def ratio
    chainring / cog.to_f
  end

  def gear_inches
    ratio * wheel.diameter
  end

  Wheel = Struct.new(:rim, :tire) do
    def diameter
      rim + (tire * 2)
    end
  end
end

############## Page 33 ##############
class Gear
  attr_reader :chainring, :cog, :wheel
  def initialize(chainring, cog, wheel=nil)
    @chainring = chainring
    @cog       = cog
    @wheel     = wheel
  end

  def ratio
    chainring / cog.to_f
  end

  def gear_inches
    ratio * wheel.diameter
  end
end

class Wheel
  attr_reader :rim, :tire

  def initialize(rim, tire)
    @rim       = rim
    @tire      = tire
  end

  def diameter
    rim + (tire * 2)
  end

  def circumference
    diameter * Math::PI
  end
end

@wheel = Wheel.new(26, 1.5)
puts @wheel.circumference
# -> 91.106186954104

puts Gear.new(52, 11, @wheel).gear_inches
# -> 137.090909090909

puts Gear.new(52, 11).ratio
# -> 4.72727272727273

