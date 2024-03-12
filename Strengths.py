from pydantic import BaseModel

class Strength(BaseModel):
    Age : int
    Fly_Ash : float
    Average_Aggregate : float
    Water_Cement_Ratio : float
    Blast_Furnace_Slag : float
    Super_Plasticizer : float
    