# shipArmorTHResistanceAF1
#
# Used by:
# Ship: Astero
# Ship: Malice
# Ship: Punisher
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Amarr Frigate").level
    fit.ship.boostItemAttr("armorThermalDamageResonance", ship.getModifiedItemAttr("shipBonusAF") * level)
