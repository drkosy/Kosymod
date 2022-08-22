from common.base_prod import TECH_COST_MULTIPLIER

Tech(
    name="SHP_SINGULARITY_PROJECTOR",
    description="SHP_SINGULARITY_PROJECTOR_DESC",
    short_description="SHIP_PART_UNLOCK_SHORT_DESC",
    category = "SHIP_WEAPONS_CATEGORY",
    researchcost=300 * TECH_COST_MULTIPLIER,
    researchturns=4,
    tags=[ "PEDIA_SR_WEAPON_TECHS" ],
    prerequisites = [
        "LRN_ART_BLACK_HOLE",
        "PRO_ZERO_GEN",
    ],
    unlock=Item(type=UnlockShipPart, name="SR_SINGULARITY_PROJECTOR"),
    graphic="icons/ship_parts/PSP_Cannon.png",
)
