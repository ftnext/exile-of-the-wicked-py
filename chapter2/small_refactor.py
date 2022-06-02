"""ダメージ計算ロジックのリファクタリング"""


def version0(p1, p2, d1, d2):
    d = 0
    d = p1 + p2
    d = d - ((d1 + d2) // 2)
    if d < 0:
        d = 0
    return d


def version1(
    player_arm_power,
    player_weapon_power,
    enemy_body_defence,
    enemy_armor_defence,
):
    damage_amount = 0
    damage_amount = player_arm_power + player_weapon_power
    damage_amount = damage_amount - (
        (enemy_body_defence + enemy_armor_defence) // 2
    )
    if damage_amount < 0:
        damage_amount = 0
    return damage_amount


assert version0(30, 50, 40, 20) == version1(30, 50, 40, 20) == 50
