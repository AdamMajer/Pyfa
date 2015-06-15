# shipMissileLightVelocityBonusCC2
#
# Used by:
# Ship: Caracal
# Ship: Osprey Navy Issue
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Cruiser").level
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Light Missiles"),
                                    "maxVelocity", ship.getModifiedItemAttr("shipBonusCC2") * level)
