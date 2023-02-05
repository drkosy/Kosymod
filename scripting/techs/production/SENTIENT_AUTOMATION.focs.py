from common.base_prod import TECH_COST_MULTIPLIER
from common.priorities import TARGET_AFTER_2ND_SCALING_PRIORITY
from common.misc import PLANETS_OWNED_BY_EMPIRE

Tech(
    name="PRO_SENTIENT_AUTOMATION",
    description="PRO_SENTIENT_AUTOMATION_DESC",
    short_description="INDUSTRY_AND_SLOT_SHORT_DESC",
    category="PRODUCTION_CATEGORY",
    researchcost=800 * TECH_COST_MULTIPLIER,
    researchturns=8,
    tags=["PEDIA_PRODUCTION_CATEGORY"],
    prerequisites=["LRN_PSIONICS", "PRO_ADAPTIVE_AUTOMATION"],
    unlock=[
        Item(type=UnlockPolicy, name="PLC_AUTOMATION"),
    ],
    effectsgroups=[
        EffectsGroup(
            scope=ProductionCenter
            & OwnedBy(empire=Source.Owner)
            & TargetPopulation(low=0.0001)
            & Focus(type=["FOCUS_INDUSTRY"])
            & Happiness(low=0),
            priority=TARGET_AFTER_2ND_SCALING_PRIORITY,
            effects=[
                SetTargetIndustry(value=Value + NamedReal(name="PRO_SENTIENT_AUTO_TARGET_INDUSTRY_FLAT", value=2)),
                SetTargetIndustry( value = Value + MaxOf(float, 3.0, (0.25 * Target.Population - 0.15 * PLANETS_OWNED_BY_EMPIRE)) * StatisticIf(float, condition=EmpireHasAdoptedPolicy(empire=Source.Owner, name = "PLC_METROPOLES"))),
                SetTargetIndustry( value = Value + StatisticIf(float, condition= EmpireHasAdoptedPolicy(empire=Source.Owner, name = "PLC_INTERSTELLAR_INFRA")) * ((0.05 * PLANETS_OWNED_BY_EMPIRE) + 2)),
                ],
        ),
        EffectsGroup(
            scope=Source,
            effects=SetEmpireMeter(empire=Source.Owner, meter="ECONOMIC_CATEGORY_NUM_POLICY_SLOTS", value=Value + 1),
        ),
    ],
    graphic="icons/tech/basic_autofactories.png",
)
