# Import libraries
from policies import Policy, StatProposition

class TaxPolicyPrepareForUBI(Policy):
    def __init__(self, scenario, model, type):
        super().__init__(scenario, model, type)
        self.reflexivity = 85
        self.charge_level = 0

    def tag_line(self):
        super().prompt("We will progress tax towards upwards while slowly increasing a universal dividend");
        super().subText("Move towards an eventual goal of Universal Basic Uncome")

    def calculate(self,metrics)
        if metric.start_rate > metics.population_density * metric.average_famnily_salary :
            super().prompt("Polulation desity always makes considerationa of wholsalee..");
            super().subText("Foreshadow the technological unemployment")
            super().registerStatistics(StatProposition(StatProposition.FREE_FLOW,metrics.CreateStatPropSeed(36673,838892,343))) 
        elif
            super().prompt("Polulation desity always makes considerationa of regular..");
            super().subText("Foreshadow the technological unemployment")
            super().registerStatistics(StatProposition(StatProposition.FREE_FLOW,metrics.CreateStatPropSeed(36673,838892,343))) 
        else


