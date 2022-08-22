from common.base_prod import TECH_COST_MULTIPLIER
from techs.ship_weapons.ship_weapons import WEAPON_BASE_EFFECTS

Tech(
    name="SHP_WEAPON_DR",
    description="SHP_WEAPON_DR_DESC",
    short_description="SHIP_WEAPON_UNLOCK_SHORT_DESC",
    category="SHIP_WEAPONS_CATEGORY",
    researchcost = 1,
    researchturns = 1,
    researchable=False,
    tags=[ "PEDIA_SR_WEAPON_TECHS" ],
    unlock=Item(type=UnlockShipPart, name="SR_WEAPON_DR"),
    effectsgroups=WEAPON_BASE_EFFECTS("SR_WEAPON_DR"),
    graphic="icons/ship_parts/ion_cannon.png",
)
