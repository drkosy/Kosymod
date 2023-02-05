from common.base_prod import TECH_COST_MULTIPLIER

Tech(
    name="SHP_HYPER_DAM_CONT",
    description="SHP_HYPER_DAM_CONT_DESC",
    short_description="STRUCTURE_SHORT_DESC",
    category="SHIP_PARTS_CATEGORY",
    researchcost=32000 * TECH_COST_MULTIPLIER,
    researchturns=15,
    tags=["PEDIA_DAMAGE_CONTROL_PART_TECHS"],
    prerequisites=["SHP_ADV_DAM_CONT"],
    effectsgroups=[
        EffectsGroup(
            scope=Ship
            & OwnedBy(empire=Source.Owner)
            & InSystem()
            & Stationary
            & Turn(low=LocalCandidate.System.LastTurnBattleHere + 1),
            effects=SetStructure(value=Value + (Target.MaxStructure / 10)),
        )
    ],
)
