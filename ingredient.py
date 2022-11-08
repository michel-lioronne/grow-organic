from dataclasses import Dataclass

@dataclass
class Ingredient
	PH: float = 0.
    EC: float = 0
    dry: float = 0.
    liquid: float = 0.
	aeration: float = 0.
    substrat: float = 0.
    compost: float = 0.
    mulch: float = 0.
    carbon: float = 0.
    nitrogen: float = 0.
    phosphore: float = 0.
    potassium: float = 0.
    calcium: float = 0.
    magnesium: float  = 0.
    iron: float = 0.
    potassium: float = 0.
    molybdenium: float = 0.
    copper: float = 0.
    chlore: float = 0.
    bore: float = 0.
    silicium: float = 0
    sulfure: float = 0
    recomended_dosage: Dosage | None = None