"""_summary_
  A singleton design class implementation that creates an instance of an object
  and returns it's attributes
"""

class SingletonObject(object):
    class __SingletonObject():
        """_summary_
         This is the class definition of the SingletonObject, which is a private class
         and should never be used outside this class implementation
        """
        def __init__(self):
            self.value = None
            
        def __str__(self):
            return '{0!r} {1}'.format({self}, {self.value})
    
    #  a class attribute instance, which is fixed for all objects 
    #   instantiated from the SingletonObject class    
    instance = None 
    def __new__(cls):
        # A class method. that does not take the object as a parameter, it receives the class as a 
        # parameter and then uses the class definition to construct a new instance of the class.
        if not SingletonObject.instance:
            # check the class variable instance to see if there is such an instance in existence. 
            # If there is no existing instance, it creates a new instance of the private class 
            # and assigns it to the instance class variable.
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance 
    
    # Alter the call to the attributes found in the private class saved in the instance class variable. 
    # This relays the call to the object housed in the instance variable as if the outer 
    # object has the attributes.
    def __getattr__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        # The self.val attribute is set just to show that the object remains the same even 
        # though the script attempts to instantiate it more than once.
        return setattr(self.instance, name)
    
    