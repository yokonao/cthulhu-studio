from django.forms import ModelForm
from .models import Chara


class CharaForm(ModelForm):

    class Meta:
        model = Chara
        fields = ('name', 'picture', 'profession', 'background', 'birthplace', 'gender', 'age',
                  'strength', 'constitution', 'size', 'dexterity', 'appearance', 'intelligence',
                  'power', 'education', 'idea', 'luck', 'knowledge', 'sanity_point',
                  'max_sanity_point', 'magic_point', 'durability', 'damage_bonus',)


class SkillForm(ModelForm):
    class Meta:
        model = Chara
        fields = ('deception', 'medicine', 'driving', 'first_aid', 'occult', 'avoidance',
                  'chemistry', 'picking', 'hide', 'hidden', 'machine_repair', 'listen',
                  'cthulhu_mythos', 'art', 'accounting', 'archaeology', 'computer',
                  'sneaking', 'photography', 'heavy_machine_operation', 'horse_riding',
                  'trust', 'psychology', 'anthropology', 'swimming', 'psychoanalysis',
                  'biology', 'persuasion', 'geology', 'jumpping', 'chase', 'electrical_repair',
                  'electronics', 'astronomy', 'throwing', 'climbing', 'library', 'navigate',
                  'discount', 'natural_history', 'physics', 'disguise', 'law', 'mother_tongue',
                  'eye_star', 'pharmacy', 'history', 'survival', 'punch', 'kick', 'nelson_hold',
                  'heading', 'budo', 'martial_arts', 'iai', 'handgun', 'submachinegun', 'shotgun',
                  'machinegun', 'rifle', 'original_skill', )


class FreespaceForm(ModelForm):
    class Meta:
        model = Chara
        fields = ('freespace', )
