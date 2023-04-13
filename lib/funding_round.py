class FundingRound:
    all =[]
    def __init__(self, startup, venture_capitalist, type, investment) -> None:
        self.startup = startup
        self.venture_capitalist = venture_capitalist
        self.type = type
        self.investment = investment
        FundingRound.all.append(self)
        
    @property
    def startup(self):
        return self._startup
    
    @startup.setter
    def startup(self,input):
        from .startup import Startup
        if isinstance(input, Startup):
            if not hasattr(self, 'startup'):
                self._startup = input
            else:
                raise Exception('startup for funding round cannot be modified')
        else:
            raise Exception('invalid startup')
            
    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    
    @venture_capitalist.setter
    def venture_capitalist(self,input):
        from .venture_capitalist import VentureCapitalist
        if isinstance(input, VentureCapitalist):
            if not hasattr(self, 'venture_capitalist'):
                self._venture_capitalist = input 
            else:
                raise Exception('venture_capitalist for funding round cannot be modified')
        else:
            raise Exception('invalid VC')
            
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self,input):
        if isinstance(input,str):
            self._type = input
        else:
            raise Exception('type must be a string')      

    @property
    def investment(self):
        return self._investment
    
    @investment.setter
    def investment(self,input):
        if type(input) == float:
            if input>=0 :
                self._investment = input
            else:
                raise Exception('investment must be a positive integer')
        else:
            raise Exception('investment must be a float')

    @classmethod
    def get_funding(cls):
        return cls.all


