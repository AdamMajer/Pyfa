# eliteBonusViolatorsRepairSystemsArmorDamageAmount2
#
# Used by:
# Ship: Kronos
# Ship: Paladin
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Marauders").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Repair Systems"),
                                  "armorDamageAmount", ship.getModifiedItemAttr("eliteBonusViolators2") * level)
