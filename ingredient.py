from dataclasses import Dataclass

@dataclass
class Ingredient
	"""Ingredient with values in SI units or proportions
    
    None stands for uknwown
    0. stands for absence
    
    The proportions of chemical elements stands for elements' forms that can be absorbed after and eventual transformation from soil's life.
    """
	density: float | None = None    #: Density in SI units. Kg/m^3 or g/L.
	PH: float | None = None			#: PH value in the 1.-14. scale.
    EC: float | None = None			#: Siemens per metre (S/m)
    dry: float | None = None		#: Proportion in mass of dry matter
    liquid: float | None = None		#: Proportion in mass of liquid matter
	aeration: float | None = 0.		#: Proportion in volume of aeration medium (Perlite, Pumice, volcanic rocks...)
    substrat: float | None = 0.		#: Proporition in volume of substrat (Peat Mosse, Coco coir...)
    compost: float | None = 0.		#: Proportion in volume of compost
    mulch: float | None = 0.		#: Proporiton in volume of Mulch
    carbon: float | None = 0.		#: Proporition in mass of Carbon (C)
    nitrogen: float | None = 0.		#: Proportion in mass of Nitrogen (N)
    phosphore: float | None = None  #: Proportion in mass of Phosphore (P)
    potassium: float | None = None  #: Proportion in mass of Potassium (K)
    calcium: float | None = None    #: Proportion in mass of Calcium (Ca)
    magnesium: float | None = None  #: Proportion in mass of Magnesium (Mg)
    iron: float | None = None       #: Proportion in mass of Iron (Fe)
    molybdenium: float | None = None  #: Proportion in mass of Molybdenium (Mo)
    copper: float | None = None     #: Proportion in mass of copper (Cu)
    chlore: float | None = None     #: Proportion in mass of chlore (Cl)
    bore: float | None = None       #: Proportion in mass of bore (B)
    silicium: float | None = None   #: Proportion in mass of silicium (Si)
    sulfure: float | None = None    #: Proportion in mass of sulfure (S)
    recomended_dosage: Dosage | None = None  	#: Recommended dosage from the ingredient's manufacturer
    by: Company | List[Company] = None 			#: Name of the manufacturing company
    description: str | None = None				#: Description of the ingredient in English
    
 	@property
    def kg_per_liter(self) -> float:
        """Density in Kg/L"""
        return self.density / 1000
    
    @kg_per_liter.setter
    def kg_per_liter(self, value: float):
        self.density = value * 1000
        