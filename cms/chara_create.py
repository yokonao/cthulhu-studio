from random import randint


def nDn(a, b):  # nDnのダイスロール
    return sum([randint(1, b) for _ in range(a)])


def dice_ability():
    abs = {
        'strength': nDn(3, 6),  # 能力値をダイスロールで決定
        'constitution': nDn(3, 6),
        'size': nDn(2, 6) + 6,
        'dexterity': nDn(3, 6),
        'appearance': nDn(3, 6),
        'intelligence': nDn(2, 6) + 6,
        'power': nDn(3, 6),
        'education': nDn(3, 6) + 3,
        }

    if abs['education'] > 20:  # 知識の値が100を超えないように調整
        knowledge = 100
    else:
        knowledge = abs['education'] * 5

    db = abs['strength'] + abs['size']  # STRとSIZを元にダメージボーナスを計算
    if db >= 33:
        db = '1D6'
    elif db >= 25:
        db = '1D4'
    elif db >= 17:
        db = '0'
    elif db >= 13:
        db = '-1D4'
    else:
        db = '-1D6'
        
    abs2 = {  # 未設定の能力値を設定し辞書結合
        'idea': abs['intelligence'] * 5,
        'luck': abs['power'] * 5,
        'knowledge': knowledge,
        'sanity_point': abs['power'] * 5,
        'magic_point': abs['power'],
        'durability': int((abs['size'] + abs['constitution']) / 2),
        'damage_bonus': db,
    }
    abs.update(abs2)
    return abs
