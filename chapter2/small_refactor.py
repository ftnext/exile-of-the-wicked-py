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


def version2(
    player_arm_power,
    player_weapon_power,
    enemy_body_defence,
    enemy_armor_defence,
):
    total_player_attack_power = player_arm_power + player_weapon_power
    total_enemy_defence = enemy_body_defence + enemy_armor_defence

    damage_amount = total_player_attack_power - total_enemy_defence // 2
    if damage_amount < 0:
        damage_amount = 0
    return damage_amount


def sum_up_player_attack_power(
    player_arm_power: int, player_weapon_power: int
) -> int:
    return player_arm_power + player_weapon_power


def sum_up_enemy_defence(
    enemy_body_defence: int, enemy_armor_defence: int
) -> int:
    return enemy_body_defence + enemy_armor_defence


def estimate_damage(
    total_player_attack_power: int, total_enemy_defence: int
) -> int:
    damage_amount = total_player_attack_power - total_enemy_defence // 2
    if damage_amount < 0:
        return 0
    return damage_amount


def version3(
    player_arm_power,
    player_weapon_power,
    enemy_body_defence,
    enemy_armor_defence,
):
    total_player_attack_power = sum_up_player_attack_power(
        player_arm_power, player_weapon_power
    )
    total_enemy_defence = sum_up_enemy_defence(
        enemy_body_defence, enemy_armor_defence
    )
    damage_amount = estimate_damage(
        total_player_attack_power, total_enemy_defence
    )
    return damage_amount


assert (
    version0(30, 50, 40, 20)
    == version1(30, 50, 40, 20)
    == version2(30, 50, 40, 20)
    == version3(30, 50, 40, 20)
    == 50
)
