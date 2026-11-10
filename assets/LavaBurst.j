function LavaBurst takes unit source, unit center, real radius, real amount returns nothing
    local real x = GetUnitX(center)
    local real y = GetUnitY(center)
    local group targets = CreateGroup()
    local unit u
    set udg_LavaProcs = udg_LavaProcs + 1
    call DestroyEffect(AddSpecialEffect("Abilities\\Spells\\Other\\Volcano\\VolcanoDeath.mdl", x, y))
    call GroupEnumUnitsInRange(targets, x, y, radius, null)
    loop
        set u = FirstOfGroup(targets)
        exitwhen u == null
        call GroupRemoveUnit(targets, u)
        if GetWidgetLife(u) > 0.405 and IsUnitEnemy(u, GetOwningPlayer(source)) then
            call UnitDamageTarget(source, u, amount, false, false, ATTACK_TYPE_NORMAL, DAMAGE_TYPE_FIRE, WEAPON_TYPE_WHOKNOWS)
        endif
    endloop
    call DestroyGroup(targets)
    set targets = null
endfunction
