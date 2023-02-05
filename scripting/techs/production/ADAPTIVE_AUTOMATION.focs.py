from common.base_prod import TECH_COST_MULTIPLIER
from common.priorities import TARGET_AFTER_2ND_SCALING_PRIORITY
from common.misc import PLANETS_OWNED_BY_EMPIRE

Tech(
    name="PRO_ADAPTIVE_AUTOMATION",
    description="PRO_ADAPTIVE_AUTOMATION_DESC",
    short_description="INDUSTRY_SHORT_DESC",
    category="PRODUCTION_CATEGORY",
    researchcost=180 * TECH_COST_MULTIPLIER,
    researchturns=5,
    tags=["PEDIA_PRODUCTION_CATEGORY"],
    prerequisites=["LRN_ALGO_ELEGANCE", "PRO_NANOTECH_PROD"],
    effectsgroups=[
        EffectsGroup(
            scope=ProductionCenter
            & OwnedBy(empire=Source.Owner)
            & TargetPopulation(low=0.0001)
            & Happiness(low=NamedReal(name="PRO_ADAPTIVE_AUTO_MIN_STABILITY", value=10)),
            priority=TARGET_AFTER_2ND_SCALING_PRIORITY,
            effects=[
                SetTargetIndustry( value = Value + NamedReal(name="PRO_ADAPTIVE_AUTO_TARGET_INDUSTRY_FLAT", value = 1)),
                SetTargetIndustry( value = Value + MaxOf(float, 1.0, (0.15 * Target.Population - 0.05 * PLANETS_OWNED_BY_EMPIRE)) * StatisticIf(float, condition=EmpireHasAdoptedPolicy(empire=Source.Owner, name = "PLC_METROPOLES"))),
                SetTargetIndustry( value = Value + StatisticIf(float, condition= EmpireHasAdoptedPolicy(empire=Source.Owner, name = "PLC_INTERSTELLAR_INFRA")) * ((0.02 * PLANETS_OWNED_BY_EMPIRE) + 0.5)),
            ],
        ),
    ],
    graphic="icons/tech/basic_autofactories.png",
)
