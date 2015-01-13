#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys


SUBTITLES_CHOICES = {
    ('spanish', 'Español'),
    ('english', 'Inglés'),
    ('portugues', 'Português')
}

PRIVACY_CHOICES = ['private', 'public', 'secret']
LIVE_EVENT_TYPE = ['Speciality', 'Mega', 'Regional']


PRIVACY = {
    'private': {
        'spanish': 'Privado',
        'english': 'Private',
        'portuguese': 'Privada'
    },
    'public': {
        'spanish': 'Público',
        'english': 'Public',
        'portuguese': 'Público'
    },
    'secret': {
        'spanish': 'Secreto',
        'english': 'Secret',
        'portuguese': 'Segredo'
    }
}


SUBTITLES = {
    'spanish': {
        'spanish': 'Español',
        'english': 'Spanish',
        'portuguese': 'Espanhol'
    },
    'english': {
        'spanish': 'Inglés',
        'english': 'Inglish',
        'portuguese': 'Inglês'
    },
    'portuguese': {
        'spanish': 'Portugués',
        'english': 'Portuguese',
        'portuguese': 'Português'
    }
}

DATES = {
    'past': {
        'spanish': 'Pasado',
        'english': 'Past',
        'portuguese': 'Passado'
    },
    'upcoming': {
        'spanish': 'Próximo',
        'english': 'Upcoming',
        'portuguese': 'Próximo'
    },
    'live': {
        'spanish': 'En Vivo',
        'english': 'Live',
        'portuguese': 'Ao Vivo'
    }
}

EXTERNAL_EVENT_TYPES = {
    'forum': {
        'spanish': 'Foro',
        'english': 'Forum',
        'portuguese': 'Fórum'
    },
    'debate': {
        'spanish': 'Debate',
        'english': 'Debate',
        'portuguese': 'Debate'
    },
    'panel': {
        'spanish': 'Panel',
        'english': 'Panel',
        'portuguese': 'Painel'
    },
    'seminar': {
        'spanish': 'Seminario',
        'english': 'Seminar',
        'portuguese': 'Seminário'
    },
    'symposium': {
        'spanish': 'Simposio',
        'english': 'Symposium',
        'portuguese': 'Simpósio'
    },
    'conference': {
        'spanish': 'Conferencia',
        'english': 'Conference',
        'portuguese': 'Conferência'
    },
    'convention': {
        'spanish': 'Convencion',
        'english': 'Convention',
        'portuguese': 'Convenção'
    },
    'fair': {
        'spanish': 'Feria',
        'english': 'Fair',
        'portuguese': 'Feira'
    }
}
