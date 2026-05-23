from pydantic import BaseModel
from typing import List, Dict, Optional




class Cart(BaseModel):
    user_id : int
    storr_name : Optional[str] = None
    items : List[str]
    quantites: Dict[str , int]
    takeBags : bool = False
    
    
FillCart = Cart(user_id=98 , items=["aam" , "Kela" , "Biscuit" ] , quantites={"kela" : 3 , "aam": 6 , "biscuit" : 70})
# ! but if you are creating the fill cart independinetly and then you send it in the cart you have to opne it with ** 

print(FillCart)