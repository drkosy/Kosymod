from common.base_prod import TECH_COST_MULTIPLIER
from common.priorities import TARGET_POPULATION_AFTER_SCALING_PRIORITY

Tech(
    name="GRO_HYPER_HAB",
    description="GRO_HYPER_HAB_DESC",
    short_description="POPULATION_SHORT_DESC",
    category="GROWTH_CATEGORY",
    researchcost=48000 * TECH_COST_MULTIPLIER,
    researchturns=20,
    tags=["PEDIA_GROWTH_CATEGORY"],
    prerequisites=[
        "GRO_ENERGY_META",
        "LRN_GATEWAY_VOID",
        "CON_NDIM_STRC",
        ],
    effectsgroups=[
        EffectsGroup(
            scope=HasSpecies() & OwnedBy(empire=Source.Owner),
            accountinglabel="GRO_TECH_ACCOUNTING_LABEL",
            priority=TARGET_POPULATION_AFTER_SCALING_PRIORITY,
            effects=SetTargetPopulation(value=Value + 1 * Target.HabitableSize),
        )
    ],
    graphic="icons/tech/subterranean_construction.png",
)
