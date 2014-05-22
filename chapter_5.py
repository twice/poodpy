############## Page 87 ##############
class Trip(object):

    # this 'mechanic' argument could be of any class
    def prepare(self, mechanic):
            mechanic.prepare_bicycles(self.bicycles)

    @property
    def bicycles(self):
        return self.__bicycles

    @property
    def customers(self):
        return self.__customers

    @property
    def vehicle(self):
        return self.__vehicle

    # ...


# if you happen to pass an instance of *this* class,
# it works
class Mechanic(object):
    def prepare_bicycles(self, bicycles):
        return [self.prepare_bicycle(bicycle) for bicycle in bicycles]

    def prepare_bicycle(self, bicycle):
        pass

    #...

############## Page 88 ##############


# Trip preparation becomes more complicated
class Trip(object):

    def prepare(self, preparers):
        for preparer in preparers:
            if isinstance(preparer, Mechanic):
                preparer.prepare_bicycles(self.bicycles)
            elif isinstance(preparer, TripCoordinator):
                preparer.buy_food(self.customers)
            elif isinstance(preparer, Driver):
                preparer.gas_up(self.vehicle)
                preparer.fill_water_tank(self.vehicle)


# when you introduce TripCoordinator and Driver
class TripCoordinator(object):
    def buy_food(self, customers):
        pass


class Driver(object):
    def gas_up(self, vehicle):
        pass

    def fill_water_tank(self, vehicle):
        pass

############## Page 93 ##############
# Trip preparation becomes easier
class Trip(object):

    def prepare(self, preparers):
        for preparer in preparers:
            preparer.prepare_trip(self)

    @property
    def bicycles(self):
        return self.__bicycles

    @property
    def customers(self):
        return self.__customers

    @property
    def vehicle(self):
        return self.__vehicle


# when every preparer is a Duck
# that responds to 'prepare_trip'
class Mechanic(object):
    def prepare_trip(self, trip):
        for bicycle in trip.bicycles:
            self.prepare_bicycle(bicycle)

    # ...


class TripCoordinator(object):
    def prepare_trip(self, trip):
        self.buy_food(trip.customers)

    # ...


class Driver(object):
    def prepare_trip(self, trip):
        vehicle = trip.vehicle
        self.gas_up(vehicle)
        self.fill_water_tank(vehicle)

    # ...


############## Page 96 ##############
class Trip(object):

    def prepare(self, preparers):
        for preparer in preparers:
            if isinstance(preparer, Mechanic):
                preparer.prepare_bicycles(self.bicycles)
            elif isinstance(preparer, TripCoordinator):
                preparer.buy_food(self.customers)
            elif isinstance(preparer, Driver):
                preparer.gas_up(self.vehicle)
                preparer.fill_water_tank(self.vehicle)

    @property
    def bicycles(self):
        return self.__bicycles

    @property
    def customers(self):
        return self.__customers

    @property
    def vehicle(self):
        return self.__vehicle


############## Page 97 ##############

if isinstance(preparer, Mechanic):
    preparer.prepare_bicycles(self.bicycle)
elif isinstance(preparer, TripCoordinator):
    preparer.buy_food(self.customers)
elif isinstance(preparer, Driver):
    preparer.gas_up(self.vehicle)
    preparer.fill_water_tank(self.vehicle)

############## Page 97 ##############
if hasattr(preparer, 'prepare_bicycles'):
    preparer.prepare_bicycles(self.bicycle)
elif hasattr(preparer, 'buy_food'):
    preparer.buy_food(self.customers)
elif hasattr(preparer, 'gas_up'):
    preparer.gas_up(self.vehicle)
    preparer.fill_water_tank(self.vehicle)

# A suboptimal implemantation which may be found in the wild may
# like the following:
if 'prepare_bicycles' in dir(preparer):
    preparer.prepare_bicycles(self.bicycle)
# ...


############## Page 99 ##############

# The following is an exercise of vanities. I tried to do a literal translation
# to python of the Rails class. So it probably makes little to no sense. Actually the
# latest rails code has greatly refactored this method.

# A convenience wrapper for <tt>find(:first, *args)</tt>.
# You can pass in all the same arguments to this
# method as you can to <tt>find(:first)</tt>.
def first(self, *args):
    if args:
        if isinstance(args[0], (int, long)) or (self.loaded() and not isinstance(args[0], dict)):
            limit = args[0]
            return list(self)[:limit]
        else:
            return self.apply_finder_options(args[0]).first()
    else:
        return self.find_first()
# !x
