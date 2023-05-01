from django.test import TestCase
from core.models import AtividadesModel
from core.forms import AtividadesForm, AtividadesModelForm
from datetime import datetime

class AtividadeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_index(self):
        self.assertTemplateUsed(self.resp, 'index.html')

class CadastroAtividadeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro/')

    def test_200_response2(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_cadastro(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

class AtividadesModelTest(TestCase):
    def setUp(self):
        self.atividades = 'Projeto Integrador'
        self.mes = 4
        self.dia = 31
        self.cadastro = AtividadesModel(
            nome=self.atividades,  
            dia=self.dia,
            mes=self.mes,
        )
        self.cadastro.save()

    def test_created(self):
        self.assertTrue(AtividadesModel.objects.exists())

    def test_modificado_em(self):
        self.assertIsInstance(self.cadastro.modificado_em, datetime)

    def test_nome_atividade(self):
        nome = self.cadastro.__dict__.get('nome', '')
        self.assertEqual(nome, self.atividades)

    def test_dia_atividade(self):
        dia = self.cadastro.__dict__.get('dia', '')
        self.assertEqual(dia, self.dia)

class AtividadesFormTest(TestCase):
    def test_forms_has_fields(self):
        form = AtividadesModelForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome = 'Estudar Python')
        self.assertEqual('ESTUDAR PYTHON', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Estudar Python',
        dia=1, 
        mes=5
        )
        data = dict(valid, **kwargs)
        form = AtividadesForm(data)
        form.is_valid()
        return form
    
class AtividadesModelFormTest(TestCase):
    def test_forms_has_fields(self):
        form = AtividadesModelForm()
        expected = ['nome', 'dia', 'mes']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_be_capitalized(self):
        form = self.make_validated_form(nome = 'Estudar Python')
        self.assertEqual('ESTUDAR PYTHON', form.cleaned_data['nome'])
    
    def make_validated_form(self, **kwargs):
        valid = dict(
        nome='Estudar Python',
        dia=1, 
        mes=5
        )
        data = dict(valid, **kwargs)
        form = AtividadesForm(data)
        form.is_valid()
        return form