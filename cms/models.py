from django.db import models


class Chara(models.Model):  # キャラクターシート
    name = models.CharField('名前', max_length=255)
    picture = models.ImageField(upload_to='cms/', verbose_name='添付画像', blank=True, null=True, )
    # キャラクターのプロフィール
    profession = models.CharField('職業', max_length=255, blank=True, null=True)
    background = models.CharField('学校・学位', max_length=255, blank=True, null=True,)
    birthplace = models.CharField('出身', max_length=255, blank=True, null=True,)
    gender = models.CharField('性別', max_length=255, blank=True, null=True,)
    age = models.IntegerField('年齢', blank=True, null=True,)
    # キャラクターの能力値
    strength = models.IntegerField('STR', default=9, )
    constitution = models.IntegerField('CON', default=9, )
    size = models.IntegerField('SIZ', default=9, )
    dexterity = models.IntegerField('DEX', default=9, )
    appearance = models.IntegerField('APP', default=9, )
    intelligence = models.IntegerField('INT', default=9, )
    power = models.IntegerField('POW', default=9, )
    education = models.IntegerField('EDU', default=12, )
    idea = models.IntegerField('アイデア', default=50, )
    luck = models.IntegerField('幸運', default=50, )
    knowledge = models.IntegerField('知識', default=50, )
    sanity_point = models.IntegerField('SAN値', default=50, )
    max_sanity_point = models.IntegerField('最大正気度', default=99, )
    magic_point = models.IntegerField('マジックポイント', default=9, )
    durability = models.IntegerField('耐久力', default=9, )
    damage_bonus = models.CharField(
        'ダメージ・ボーナス',
        max_length=10,
        default="0",
        choices=(
            ('0', '0'), ('-1D6', '-1D6'), ('-1D4', '-1D4'), ('1D4', '1D4'), ('1D6', '1D6'),
        )
    )
    # 一般技能
    deception = models.IntegerField('言いくるめ', default=5, )
    medicine = models.IntegerField('医学', default=5, )
    driving = models.IntegerField('運転', default=20, )
    first_aid = models.IntegerField('応急手当', default=30, )
    occult = models.IntegerField('オカルト', default=5, )
    avoidance = models.IntegerField('回避', default=21,)
    chemistry = models.IntegerField('化学', default=1,)
    picking = models.IntegerField('鍵開け', default=1,)
    hide = models.IntegerField('隠す', default=15,)
    hidden = models.IntegerField('隠れる', default=10,)
    machine_repair = models.IntegerField('機械修理', default=20,)
    listen = models.IntegerField('聞き耳', default=25,)
    cthulhu_mythos = models.IntegerField('クトゥルフ神話', default=0,)
    art = models.IntegerField('芸術', default=5,)
    accounting = models.IntegerField('経理', default=10,)
    archaeology = models.IntegerField('考古学', default=1,)
    computer = models.IntegerField('コンピューター', default=1,)
    sneaking = models.IntegerField('忍び歩き', default=10,)
    photography = models.IntegerField('写真術', default=10,)
    heavy_machine_operation = models.IntegerField('重機械操作', default=1,)
    horse_riding = models.IntegerField('乗馬', default=5,)
    trust = models.IntegerField('信用', default=15,)
    psychology = models.IntegerField('心理学', default=5,)
    anthropology = models.IntegerField('人類学', default=1,)
    swimming = models.IntegerField('水泳', default=25,)
    psychoanalysis = models.IntegerField('精神分析', default=1,)
    biology = models.IntegerField('生物学', default=1,)
    persuasion = models.IntegerField('説得', default=15,)
    geology = models.IntegerField('地質学', default=1,)
    jumpping = models.IntegerField('跳躍', default=15,)
    chase = models.IntegerField('追跡', default=10,)
    electrical_repair = models.IntegerField('電気修理', default=10,)
    electronics = models.IntegerField('電子工学', default=1,)
    astronomy = models.IntegerField('天文学', default=1,)
    throwing = models.IntegerField('投擲', default=25,)
    climbing = models.IntegerField('登坂', default=40,)
    library = models.IntegerField('図書館', default=25,)
    navigate = models.IntegerField('ナビゲート', default=10,)
    discount = models.IntegerField('値切り', default=5,)
    natural_history = models.IntegerField('博物学', default=10,)
    physics = models.IntegerField('物理学', default=1,)
    disguise = models.IntegerField('変装', default=1,)
    law = models.IntegerField('回避', default=5,)
    mother_tongue = models.IntegerField('母国語', default=60,)
    eye_star = models.IntegerField('目星', default=25,)
    pharmacy = models.IntegerField('薬学', default=1,)
    history = models.IntegerField('歴史', default=20,)
    survival = models.IntegerField('サバイバル', default=10,)
    #  戦闘技能
    punch = models.IntegerField('こぶし', default=50,)
    kick = models.IntegerField('キック', default=25,)
    nelson_hold = models.IntegerField('組みつき', default=25,)
    heading = models.IntegerField('頭突き', default=10,)
    budo = models.IntegerField('武道', default=1,)
    martial_arts = models.IntegerField('マーシャルアーツ', default=1,)
    iai = models.IntegerField('居合', default=1,)
    handgun = models.IntegerField('拳銃', default=20,)
    submachinegun = models.IntegerField('サブマシンガン', default=15,)
    shotgun = models.IntegerField('ショットガン', default=30,)
    machinegun = models.IntegerField('マシンガン', default=15,)
    rifle = models.IntegerField('ライフル', default=25,)
    #  オリジナル技能(自由記入)
    original_skill = models.TextField('オリジナル技能', blank=True, null=True)
    #  自由記入欄
    freespace = models.TextField('自由記入欄', blank=True, null=True)

    def get_ability(self):
        return {k: v for k, v in self.__dict__.items() if k.startswith('abl')}

    def get_ability_triplets(self):
        triplets = [
            {'STR': self.strength, 'CON': self.constitution, 'SIZ': self.size},
            {'DEX': self.dexterity, 'APP': self.appearance, 'INT': self.intelligence},
            {'POW': self.power, 'EDU': self.education, 'アイデア': self.idea},
            {'幸運': self.luck, '知識': self.knowledge, 'SAN値': self.sanity_point},
            {'MP': self.magic_point, '耐久力': self.durability}
        ]
        return triplets

    def get_normalskill_triplets(self):
        triplets = [
            {'言いくるめ': self.deception, '医学': self.medicine, '運転': self.driving},
            {'応急手当': self.first_aid, 'オカルト': self.occult, '回避': self.avoidance},
            {'化学': self.chemistry, '鍵開け': self.picking, '隠す': self.hide},
            {'隠れる': self.hidden, '機械修理': self.machine_repair, '聞き耳': self.listen},
            {'クトゥルフ神話': self.cthulhu_mythos, '芸術': self.art, '経理': self.accounting},
            {'考古学': self.archaeology, 'コンピューター': self.computer, '忍び歩き': self.sneaking},
            {'写真術': self.photography, '重機械操作': self.heavy_machine_operation,
             '乗馬': self.horse_riding},
            {'信用': self.trust, '心理学': self.psychology, '人類学': self.anthropology},
            {'水泳': self.swimming, '精神分析': self.psychoanalysis, '生物学': self.biology},
            {'説得': self.persuasion, '地質学': self.geology, '跳躍': self.jumpping},
            {'追跡': self.chase, '電気修理': self.electrical_repair, '電子工学': self.electronics},
            {'天文学': self.astronomy, '投擲': self.throwing, '登坂': self.climbing},
            {'図書館': self.library, 'ナビゲート': self.navigate, '値切り': self.discount},
            {'博物学': self.natural_history, '物理学': self.physics, '変装': self.disguise},
            {'法律': self.law, '母国語': self.mother_tongue, '目星': self.eye_star},
            {'薬学': self.pharmacy, '歴史': self.history, 'サバイバル': self.survival},
        ]
        return triplets

    def get_battleskill_triplets(self):
        triplets = [
            {'こぶし': self.punch, 'キック': self.kick, '組みつき': self.nelson_hold},
            {'頭突き': self.heading, '武道': self.budo, 'マーシャルアーツ': self.martial_arts},
            {'居合': self.iai, '拳銃': self.handgun, 'サブマシンガン': self.submachinegun},
            {'ショットガン': self.shotgun, 'マシンガン': self.machinegun, 'ライフル': self.rifle},
        ]
        return triplets

    def __str__(self):
        return self.name
