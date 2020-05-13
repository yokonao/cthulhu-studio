from django.forms import ModelForm
from .models import Chara


class CharaForm(ModelForm):

    class Meta:
        model = Chara
        fields = ('name', 'picture', 'profession', 'background', 'birthplace', 'gender', 'age',
                  'strength', 'constitution', 'size', 'dexterity', 'appearance', 'intelligence',
                  'power', 'education', 'idea', 'luck', 'knowledge', 'sanity_point',
                  'max_sanity_point', 'magic_point', 'durability', 'damage_bonus',)


class NormalSkillForm(ModelForm):
    class Meta:
        model = Chara
        fields = ('deception', 'medicine', 'driving', 'first_aid', 'occult', 'avoidance',
                  'original_skill')


class FreespaceForm(ModelForm):
    class Meta:
        model = Chara
        fields = ('freespace', )
