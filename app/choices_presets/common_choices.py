#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys


#LANGUAGES_CHOICES = ['Spanish', 'English', 'Portugues']
LANGUAGES_CHOICES = {
    ('pt', 'Portugues'),
    ('es', 'Spanish'),
    ('en', 'English')
}

SHORTENED_LANGUAGES = {
    'en': 'english',
    'es': 'spanish',
    'pt': 'portuguese'
}

LANGUAGESID_REGIS = {
    'spanish': '1',
    'english': '2',
    'portugues': '3'
}

GENDER = ['Female', 'Male']

CURRENCY_CHOICES = ['USD', 'EUR']

RESOURCES_TYPE = ('Video', 'Document', 'Picture', 'Link')

EXTENSION = ('mp4', 'mkv', 'avi', 'flv', 'docx', 'doc', 'pdf', 'xls', 'xlsx', 'ppt', 'pptx', 'other', 'jpeg', 'jpg', 'png', 'bmp', 'tiff', 'gif', 'other')

PROVIDER_TYPE = ('Kaltura', 'Youtube')

TESTIMONIES_TYPE = ('Text', 'Video')

GENDERS = {
    'female': {
        'spanish': 'Femenino',
        'english': 'Female',
        'portuguese': 'Femenino'
    },
    'male': {
        'spanish': 'Masculino',
        'english': 'Male',
        'portuguese': 'Masculino'
    }
}

LANGUAGES = {
    'spanish': {
        'spanish': 'Español',
        'english': 'Spanish',
        'portuguese': 'Espanhol'
    },
    'english': {
        'spanish': 'Inglés',
        'english': 'English',
        'portuguese': 'Inglês'
    },
    'portuguese': {
        'spanish': 'Portugués',
        'english': 'Portuguese',
        'portuguese': 'Português'
    }
}

TRANSLATED_RESOURCE_TYPES = {
    'Video': {
        'spanish': 'Video',
        'english': 'Video',
        'portuguese': 'Video'
    },
    'Document': {
        'spanish': 'Documento',
        'english': 'Document',
        'portuguese': 'Documento'
    },
    'Picture': {
        'spanish': 'Imagen',
        'english': 'Picture',
        'portuguese': 'Imagen'
    },
    'Link': {
        'spanish': 'Link',
        'english': 'Link',
        'portuguese': 'Link'
    }
}


LEVELS_OF_EDUCATION = {
    'HighSchool': {
        'spanish': 'Secundaria',
        'english': 'High-School',
        'portuguese': 'Ensino Médio'
    },
    'Undergraduate': {
        'spanish': 'Universitario',
        'english': 'Undergraduate',
        'portuguese': 'Graduando'
    },
    'Graduate': {
        'spanish': 'Graduado',
        'english': 'Graduate',
        'portuguese': 'Graduado'
    },
    'Postgraduate': {
        'spanish': 'Maestría',
        'english': 'Postgraduate',
        'portuguese': 'Pós-graduação'
    },
    'Other': {
        'spanish': 'Otro',
        'english': 'Other',
        'portuguese': 'Outro'
    }
}

GEOGRAPHIC_REGIONS = {
    'north-america': {
        'spanish': 'América del Norte',
        'english': 'North America',
        'portuguese': 'América do Norte'
    },
    'latin-america': {
        'spanish': 'América Latina',
        'english': 'Latin America',
        'portuguese': 'América Latina'
    },
    'europe': {
        'spanish': 'Europa',
        'english': 'Europe',
        'portuguese': 'Graduado'
    },
    'asia-pacific': {
        'spanish': 'Asia Pacífico',
        'english': 'Asia Pacific',
        'portuguese': 'Ásia-Pacífico'
    },
    'middle-east': {
        'spanish': 'Oriente Medio',
        'english': 'Middle East',
        'portuguese': 'Médio Oriente'
    },
    'africa': {
        'spanish': 'África',
        'english': 'Africa',
        'portuguese': 'Africa'
    },
    'south-america': {
        'spanish': 'América del Sur',
        'english': 'South America',
        'portuguese': 'América do Sul'
    },
    'central-america': {
        'spanish': 'América Central',
        'english': 'Central America',
        'portuguese': 'América Central'
    },
    'china': {
        'spanish': 'China',
        'english': 'China',
        'portuguese': 'China'
    },
    'oceania': {
        'spanish': 'Oceanía',
        'english': 'Oceania',
        'portuguese': 'Oceânia'
    },
    'asia': {
        'spanish': 'Asia',
        'english': 'Asia',
        'portuguese': 'Ásia'
    }
}
