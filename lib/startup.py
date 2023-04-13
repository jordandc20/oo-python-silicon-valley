from .funding_round import FundingRound

class Startup:
   all=[]
   def __init__(self,name,founder,domain):
      self.name = name
      self.founder = founder
      self.domain = domain
      Startup.all.append(self)
   
   @property
   def name(self):
      return self._name

   @name.setter
   def name(self,input):
      if isinstance(input,str):
         self._name = input
      else:
         raise Exception('name must be a string')
      
   @property
   def founder(self):
      return self._founder 

   @founder.setter
   def founder(self,input):
      if not hasattr(self, 'founder'):
         if isinstance(input,str):
            self._founder = input
         else:
            raise Exception('founder must be a string')
      else:
         raise Exception('cannot rename founder')
      
   @property
   def domain(self):
      return self._domain

   @domain.setter
   def domain(self,input):
      if not hasattr(self, 'domain'):
         if isinstance(input,str):
            self._domain = input
         else:
            raise Exception('domain must be a string')
      else:
         raise Exception('cannot rename domain')
      
   def pivot(self,domain,name):
      if isinstance(domain,str) and isinstance(name,str):
         self._domain = domain
         self._name = name    
      else:
         raise Exception('domain  and name must be strings')
      # given a string of a domain and a string of a name, change the domain and name of the startup. This is the only public method through which the domain can be changed.
   
   @classmethod
   def find_by_founder(cls,founder):
      return next(startup for startup in cls.all if startup.founder == founder)
# given a string of a founder's name, returns the first startup instance whose founder's name matches

   @classmethod
   def domains(cls):
      return list(set([startup.domain for startup in cls.all] ))
# should return an list of all of the different startup domains


   def sign_contract(self,venture_capitalist,type,investment):
      FundingRound(self,venture_capitalist,type,investment)
# given a venture capitalist object, type of investment (as a string), and the amount invested (as a float), creates a new funding round and associates it with that startup and venture capitalist.

   def funds(self):
      funding_rounds = [round.investment for round in FundingRound.get_funding() if round.startup == self]
      return funding_rounds
   #helper
   
   def num_funding_rounds(self):
      return len(self.funds())
# Returns the total number of funding rounds that the startup has gotten
   
   def total_funds(self):
      return sum(self.funds())
# Returns the total sum of investments that the startup has gotten

   def investors(self):
      return list(set([round.venture_capitalist for round in FundingRound.get_funding()  if round.startup == self]))
# Returns a unique list of all the venture capitalists that have invested in this company

   def big_investors(self):
      from .venture_capitalist import VentureCapitalist
      overlap = list(set(self.investors()) & set(VentureCapitalist.tres_commas_club()))
      return overlap
# Returns a unique list of all the venture capitalists that have invested in this company and are in the Trés Commas club