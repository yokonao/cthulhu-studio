# branch test
from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .forms import CharaForm, SkillForm, FreespaceForm
from .models import Chara
from .chara_create import dice_ability
from django.http import Http404, HttpResponseRedirect
from django.db.models import Q


class CharaList(ListView):
    # キャラシートの一覧
    model = Chara
    paginate_by = 10

    def get_queryset(self):
        q_word = self.request.GET.get('query')

        if q_word:
            object_list = Chara.objects.filter(
                Q(name__icontains=q_word) | Q(profession__icontains=q_word))
        else:
            object_list = Chara.objects.all()
        return object_list


class CharaDetail(TemplateView):
    # キャラシートの詳細
    template_name = 'cms/chara_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        chara = get_object_or_404(Chara, pk=pk)
        what = self.kwargs['what']
        context = {'chara': chara, 'what': what}
        if self.kwargs['what'] == 'ability':
            context['abilities'] = chara.get_ability_triplets()
            return context
        elif self.kwargs['what'] == 'skill':
            context['normalskills'] = chara.get_normalskill_triplets()
            context['battleskills'] = chara.get_battleskill_triplets()
            return context
        elif self.kwargs['what'] == 'freespace':
            return context
        else:
            raise Http404('')


class CharaAdd(CreateView):
    template_name = 'cms/chara_edit.html'
    model = Chara
    form_class = CharaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.kwargs['r_or_c'] == 'register':
            return context
        elif self.kwargs['r_or_c'] == 'create':
            default_data = dice_ability()
            form = CharaForm(initial=default_data)
            context['form'] = form
        else:
            raise Http404('')

        return context

    def form_valid(self, form):
        chara = form.save(commit=False)
        chara.avoidance = chara.dexterity * 2  # 初期値はDEXの2倍
        chara.mother_tongue = chara.knowledge  # 母国語の初期値は知識と同じ値
        chara.save()  # 技能値は初期値で作成
        self.object = chara
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('cms:chara_detail', kwargs={'pk': self.object.id,
                                                   'what': 'ability'})


class CharaUpdate(UpdateView):
    template_name = 'cms/chara_edit.html'
    model = Chara

    def get_form_class(self):
        if self.kwargs['what'] == 'ability':
            return CharaForm
        elif self.kwargs['what'] == 'skill':
            return SkillForm
        elif self.kwargs['what'] == 'freespace':
            return FreespaceForm

    def get_success_url(self):
        print(self.kwargs)
        return reverse('cms:chara_detail', kwargs={'pk': self.object.id,
                                                   'what': self.kwargs['what']})


class CharaDelete(DeleteView):
    model = Chara
    success_url = reverse_lazy('cms:chara_list')

    def delete(self, request, *args, **kwargs):
        self.get_object().picture.delete()
        result = super().delete(self, request, *args, **kwargs)
        return result
