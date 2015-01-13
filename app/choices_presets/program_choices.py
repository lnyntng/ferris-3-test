# -- coding: utf-8 --
import os
import sys

ACCOMMODATION_TYPE_CHOICES = [
    ('On Campus'),
    ('Off Campus')
]

PROGRAM_TYPE_CHOICES = [
    ('Events'),
    ('International Curriculum'),
    ('Language Programs'),
    ('Short Term Program'),
    ('Study Abroad'),
    ('Dual Degree'),
    ('Joint Research'),
    ('Visiting Faculty and Fellows'),
    ('International Internships'),
    ('Certificate'),
    ('Signature Products'),
    ('Other')
]


AUDIENCE_TYPE_CHOICES = [
    ('HighSchool'),
    ('Undergraduate'),
    ('Graduate'),
    ('Postgraduate'),
    ('Other')
]


DELIVERY_METHOD_CHOICES = {
    ('OnCampus'),
    ('Hybrid'),
    ('Online'),
}

VISA_TYPE_CHOICES = [
    ('Not Applicable'),
    ('Tourist'),
    ('Student'),
    ('Work'),
]


DISCIPLINE_TYPES_CHOICES = [
    ('BusinessandManagement', 'Business and Management'),
    ('EngineeringandIT', 'Engineering and IT'),
    ('ArchitectureArtandDesign', 'Architecture, Art and Design'),
    ('HealthSciences', 'Health Sciences'),
    ('Communications', 'Communications'),
    ('LawandLegalStudies', 'Law and Legal Studies'),
    ('Education', 'Education'),
    ('HospitalityManagementandCulinaryArts', 'Hospitality Management and Culinary Arts'),
    ('AcademicPrograms', 'Academic Programs'),
    ('GeneralStudies', 'General Studies')
]


ACCOMMODATION_TYPES = {
    'on-campus': {
        'spanish': 'En Campus',
        'english': 'On Campus',
        'portuguese': 'No Campus'
    },
    'off-campus': {
        'spanish': 'Fuera de Campus',
        'english': 'Off Campus',
        'portuguese': 'Fora do campus'
    }
}


PROGRAM_TYPES = {
    'events': {
        'spanish': 'Eventos',
        'english': 'Events',
        'portuguese': 'Eventos'
    },
    'international-curriculum': {
        'spanish': 'Plan de Estudio Internacional',
        'english': 'International Curriculum',
        'portuguese': 'Currículo Internacional'
    },
    'language-programs': {
        'spanish': 'Programas de Idiomas',
        'english': 'Language Programs',
        'portuguese': 'Programas de Idiomas'
    },
    'short-term-program': {
        'spanish': 'Programa de Corto Plazo',
        'english': 'Short Term Program',
        'portuguese': 'Programa a Curto Prazo'
    },
    'study-abroad': {
        'spanish': 'Estudio en el Exterior',
        'english': 'Study Abroad',
        'portuguese': 'Estudar no estrangeiro'
    },
    'dual-degree': {
        'spanish': 'Doble titulación',
        'english': 'Dual Degree',
        'portuguese': 'Diploma duplo'
    },
    'joint-research': {
        'spanish': 'Investigación Conjunta',
        'english': 'Joint Research',
        'portuguese': 'Pesquisa Conjunta'
    },
    'visiting-faculty-and-fellows': {
        'spanish': 'Profesores Visitantes y Profesores Invitados',
        'english': 'Visiting Faculty and Fellows',
        'portuguese': 'Docentes e Outros Vonvidados'
    },
    'international-internships': {
        'spanish': 'Pasantía internacional',
        'english': 'International Internships',
        'portuguese': 'Estágios internacionais'
    },
    'other': {
        'spanish': 'Otro',
        'english': 'Other',
        'portuguese': 'Outro'
    },
    'certificate': {
        'spanish': 'Certificado',
        'english': 'Certificate',
        'portuguese': 'Certificado'
    }
}

DELIVERY_METHODS = {
    'OnCampus': {
        'spanish': 'En campus',
        'english': 'On campus',
        'portuguese': 'No campus'
    },
    'Hybrid': {
        'spanish': 'Híbrido',
        'english': 'Student',
        'portuguese': 'Híbrido'
    },
    'Online': {
        'spanish': 'En línea',
        'english': 'Online',
        'portuguese': 'On-line'
    }
}


DISCIPLINE_TYPES = {
    'business-and-management': {
        'spanish': 'Comercio y Administración',
        'english': 'Business and Management',
        'portuguese': 'Administração de empresas e Negócios'
    },
    'engineering-and-it': {
        'spanish': 'Ingeniería y TI',
        'english': 'Engineering and IT',
        'portuguese': 'Engenharia e TI'
    },
    'architecture-art-and-design': {
        'spanish': 'Arquitectura, Arte y Diseño',
        'english': 'Architecture, Art and Design',
        'portuguese': 'Arquitetura, Artes e Design'
    },
    'health-sciences': {
        'spanish': 'Ciencias de la Salud',
        'english': 'Health Sciences',
        'portuguese': 'Ciências da saúde'
    },
    'communications': {
        'spanish': 'Comunicaciones',
        'english': 'Communications',
        'portuguese': 'Comunicações'
    },
    'law-and-legal-studies': {
        'spanish': 'Derecho y Ciencias Jurídicas',
        'english': 'Law and Legal Studies',
        'portuguese': 'Direito e estudos jurídicos'
    },
    'education': {
        'spanish': 'Educación',
        'english': 'Education',
        'portuguese': 'Educação'
    },
    'hospitality-management-and-culinary-arts': {
        'spanish': 'Administración Hospitalaria y Artes Culinarias',
        'english': 'Hospitality Management and Culinary Arts',
        'portuguese': 'Hotelaria e Culinária'
    },
    'academic-programs': {
        'spanish': 'Programas académicos',
        'english': 'Academic Programs',
        'portuguese': 'Programas acadêmicos'
    },
    'general-studies': {
        'spanish': 'Estudios generales',
        'english': 'General Studies',
        'portuguese': 'Estudos gerais'
    },
}


VISA_TYPES = {
    'not-applicable': {
        'spanish': 'No Aplicable',
        'english': 'Not Applicable',
        'portuguese': 'Não aplicável'
    },
    'tourist': {
        'spanish': 'Turista',
        'english': 'Tourist',
        'portuguese': 'Turista'
    },
    'student': {
        'spanish': 'Estudiante',
        'english': 'Student',
        'portuguese': 'Estudante'
    },
    'work': {
        'spanish': 'Trabajo',
        'english': 'Work',
        'portuguese': 'Trabalho'
    }
}


LEVELS_OF_EDUCATION = {
    'high-school': {
        'spanish': 'Secundaria',
        'english': 'High School',
        'portuguese': 'Ensino Médio'
    },
    'undergraduate': {
        'spanish': 'Universitario',
        'english': 'Undergraduate',
        'portuguese': 'Graduando'
    },
    'graduate': {
        'spanish': 'Maestría',
        'english': 'Graduate',
        'portuguese': 'Graduando'
    },
    'alumni': {
        'spanish': 'En línea',
        'english': 'Alumni',
        'portuguese': 'Pós-graduação'
    },
    'other': {
        'spanish': 'Otros',
        'english': 'Other',
        'portuguese': 'Outros'
    }
}

AT_HOME_PROGRAM_TYPES = {
    'clase-espejo': {
        'spanish': 'Clase Espejo',
        'english': 'Clase Espejo',
        'portuguese': 'Clase Espejo'
    },
    'international-lecture': {
        'spanish': 'Clase Magistral Internacional',
        'english': 'International Lecture',
        'portuguese': 'Palestra Internacional'
    }
}
