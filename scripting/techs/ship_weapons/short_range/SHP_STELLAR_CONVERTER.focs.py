from common.base_prod import TECH_COST_MULTIPLIER

Tech(
    name="SHP_STELLAR_CONVERTER",
    description="SHP_STELLAR_CONVERTER_DESC",
    short_description="SHIP_PART_UNLOCK_SHORT_DESC",
    category="SHIP_WEAPONS_CATEGORY",
    researchcost=500 * TECH_COST_MULTIPLIER,
    researchturns = 6,
    tags=[ "PEDIA_SR_WEAPON_TECHS" ],
    prerequisites=[
        "SHP_WEAPON_4_4",
        "PRO_ZERO_GEN",
    ],
    unlock=Item(type=UnlockShipPart, name="SR_STELLAR_CONVERTER"),
    graphic="icons/ship_parts/Stellarconv.png",
)
