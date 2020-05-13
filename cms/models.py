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
    #  オリジナル技能(自由記入)
    original_skill = models.TextField('オリジナル技能', blank=True, null=True)
    #  自由記入欄
    freespace = models.TextField('自由記入欄', blank=True, null=True)

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
            {'応急手当': self.first_aid, 'オカルト': self.occult, '回避': self.avoidance}
        ]
        return triplets

    def __str__(self):
        return self.name
