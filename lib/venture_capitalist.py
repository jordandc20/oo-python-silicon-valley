
from .funding_round import FundingRound

class VentureCapitalist:
    all =[]
    def __init__(self, name, total_worth) -> None:
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

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
    def total_worth(self):
        return self._total_worth

    @total_worth.setter
    def total_worth(self,input):
        if isinstance(input, (float, int)):
            self._total_worth = input
        else:
            raise Exception('total_worth must be a number')
        
    @classmethod
    def tres_commas_club(cls):
        return [venture for venture in cls.all if venture.total_worth > 1_000_000_000]
# returns an list of all venture capitalist instances in the Trés Commas club (they have more then 1,000,000,000 total_worth)

    def offer_contract(self,startup ,type,investment):
        FundingRound(startup,self,type,investment)
# given a startup object, type of investment (as a string), and the amount invested (as a float), creates a new funding round and associates it with that startup and venture capitalist.

    def funding_rounds(self):
        funding_rounds= [round for round in FundingRound.get_funding() if round.venture_capitalist == self]
        return funding_rounds
# returns an list of all funding rounds for that venture capitalist
    
    def portfolio(self):
        return list(set([round.startup for round in self.funding_rounds()]))
# Returns a unique list of all startups this venture capitalist has funded
    
    def biggest_investment(self):
        pass
        # return max(self.funding_rounds(), key=lambda x:x['investment'])
# returns the largest funding round given by this venture capitalist
#This is a Python function that returns the maximum value of a list of dictionaries. The max() function is used to find the maximum value of a list of dictionaries based on a key. In this case, the key is ‘price’. The lambda function is used to specify that the key for comparison is ‘price’. The max() function then returns the dictionary with the highest value for ‘price’. The return statement then returns this dictionary.

    @classmethod
    def invested(cls,domain):
        pass
# given a domain string, returns the total amount invested in that domain