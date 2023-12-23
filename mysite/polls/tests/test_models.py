from django.test import TestCase
from ..models import Person, Team


class PersonModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        team = Team.objects.create(name='Example Team', country='Example Country')
        Person.objects.create(name='Jan', shirt_size='L', team=team)

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('name').max_length
        self.assertEqual(max_length, 60)

    def test_shirt_size_choices(self):
        person = Person.objects.get(id=1)
        choices = dict(person._meta.get_field('shirt_size').choices)
        self.assertEqual(choices, {'S': 'Small', 'M': 'Medium', 'L': 'Large'})

    def test_month_added_choices(self):
        person = Person.objects.get(id=1)
        choices = dict(person._meta.get_field('month_added').choices)
        self.assertEqual(choices, {1: 'Styczeń', 2: 'Luty', 3: 'Marzec', 4: 'Kwiecień', 5: 'Maj', 6: 'Czerwiec',
                                   7: 'Lipiec', 8: 'Sierpień', 9: 'Wrzesień', 10: 'Październik', 11: 'Listopad', 12: 'Grudzień'})

    def test_team_relation(self):
        person = Person.objects.get(id=1)
        team_name = person.team.name
        self.assertEqual(team_name, 'Example Team')


class TeamModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Team.objects.create(name='Example Team', country='Example Country')

    def test_name_label(self):
        team = Team.objects.get(id=1)
        field_label = team._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        team = Team.objects.get(id=1)
        max_length = team._meta.get_field('name').max_length
        self.assertEqual(max_length, 60)

    def test_country_label(self):
        team = Team.objects.get(id=1)
        field_label = team._meta.get_field('country').verbose_name
        self.assertEqual(field_label, 'country')

    def test_country_max_length(self):
        team = Team.objects.get(id=1)
        max_length = team._meta.get_field('country').max_length
        self.assertEqual(max_length, 20)
