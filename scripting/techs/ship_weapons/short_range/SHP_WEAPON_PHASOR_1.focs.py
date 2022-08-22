from common.base_prod import TECH_COST_MULTIPLIER
from techs.ship_weapons.ship_weapons import WEAPON_UPGRADE_CAPACITY_EFFECTS

Tech(
    name="SHP_WEAPON_PHASOR_1",
    description="SHP_WEAPON_PHASOR_1_DESC",
    short_description="SHIP_WEAPON_UNLOCK_SHORT_DESC",
    category="SHIP_WEAPONS_CATEGORY",
    researchcost=700 * TECH_COST_MULTIPLIER,
    researchturns=8,
    tags=[ "PEDIA_SR_WEAPON_TECHS" ],
    prerequisites = [
                    "SHP_WEAPON_3_1",
                    "LRN_NDIM_SUBSPACE",
                    ],
    unlock=Item(type=UnlockShipPart, name="SR_WEAPON_PHASOR"),
    effectsgroups=WEAPON_BASE_EFFECTS("SR_WEAPON_PHASOR"),
    graphic="icons/ship_parts/laser-red-1.png",
)
