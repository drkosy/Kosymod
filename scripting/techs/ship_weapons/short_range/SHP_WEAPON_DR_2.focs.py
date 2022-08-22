from common.base_prod import TECH_COST_MULTIPLIER
from techs.ship_weapons.ship_weapons import WEAPON_BASE_EFFECTS

Tech(
    name="SHP_WEAPON_DR_2",
    description="SHP_WEAPON_DR_2_DESC",
    short_description="SHIP_WEAPON_IMPROVE_SHORT_DESC",
    category="SHIP_WEAPONS_CATEGORY",
    researchcost=5000 * TECH_COST_MULTIPLIER,
    researchturns=12,
    tags=[ "PEDIA_SR_WEAPON_TECHS" ],
    prerequisites="SHP_WEAPON_DR",
    effectsgroups=WEAPON_UPGRADE_CAPACITY_EFFECTS("SR_WEAPON_DR", 7),
    graphic = "icons/ship_parts/ion_cannon.png",
)
