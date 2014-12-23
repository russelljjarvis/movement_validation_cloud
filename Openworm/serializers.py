from rest_framework import serializers
from models import Strain, Worm, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class StrainSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Strain
        fields = ('owner', 'strain_name', 'gene', 'genotype', 'allele', 'chromosome', 'simulated')

class WormSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    strain = serializers.PrimaryKeyRelatedField(queryset=Worm.objects.all())

    class Meta:
        model = Worm
        fields = ('owner', 'strain', 'sex', 'thawed_date', 'generations_since_thawing','habituation')