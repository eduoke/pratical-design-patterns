"""_summary_
Examples of how singleton design pattern can be used in real world applications/code components
1. As a logger
2. Mpesa user account
3. Multiplayer game level state
"""
class SingletonLogger:
    # Singleton design patter implementation in a logger
    __instance = None 
    # A private global variable instance
    # we are setting it to None here because the global getinstance method is the 
    # only one allowed to instantiate the singleton logger instance
    def __init__(self):
        # if someone tries to instantiate the singleton logger class by bypassing the
        # getinstance method we raise an exception
        raise RuntimeError("This is a singleton invoke get_instance instead")
    
    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
        return cls.__instance
    
    def log(self, ex: Exception):
        print(ex)
        
    def log(self, message: str):
        print(message)
        
        
        