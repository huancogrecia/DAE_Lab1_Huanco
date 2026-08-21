from django.shortcuts import render


def inicio(request):
    contexto = {
        'curso': 'Desarrollo de Aplicaciones Empresariales',
        'semana': 1,
        'tema': 'Introducción al Desarrollo de Aplicaciones Empresariales',
        'objetivos': [
            'Comprender qué es una aplicación empresarial y su rol en las organizaciones.',
            'Identificar los tipos de sistemas empresariales: ERP, CRM, SCM y BI.',
            'Reconocer las capas de una arquitectura empresarial moderna.',
            'Conocer el plan del curso, metodología y sistema de evaluación.',
        ],
        'contenidos': [
            {
                'titulo': 'Presentación del curso',
                'detalle': 'Sílabo, metodología de trabajo, resultados de aprendizaje y cronograma del ciclo.',
                'icono': '📋',
            },
            {
                'titulo': '¿Qué es una aplicación empresarial?',
                'detalle': 'Software que soporta procesos críticos del negocio: alta concurrencia, integridad, seguridad y escalabilidad.',
                'icono': '🏢',
            },
            {
                'titulo': 'Tipos de sistemas empresariales',
                'detalle': 'ERP (recursos), CRM (clientes), SCM (cadena de suministro) y BI (inteligencia de negocio).',
                'icono': '⚙️',
            },
            {
                'titulo': 'Arquitectura empresarial',
                'detalle': 'Capas de presentación, negocio y datos. Introducción a monolitos, microservicios y la nube.',
                'icono': '🏗️',
            },
            {
                'titulo': 'Ciclo de vida del desarrollo',
                'detalle': 'Análisis, diseño, implementación, pruebas, despliegue y mantenimiento. Metodologías ágiles.',
                'icono': '🔄',
            },
            {
                'titulo': 'Herramientas del curso',
                'detalle': 'Python, Django, bases de datos relacionales y Git como stack base del curso.',
                'icono': '🛠️',
            },
        ],
        'evaluacion': [
            {'item': 'Tareas y prácticas semanales', 'peso': '30%'},
            {'item': 'Examen parcial', 'peso': '20%'},
            {'item': 'Proyecto final (aplicación empresarial)', 'peso': '30%'},
            {'item': 'Examen final', 'peso': '20%'},
        ],
        'bibliografia': [
            'Sommerville, I. — Ingeniería de Software (10.ª edición).',
            'Pressman, R. — Ingeniería del Software: Un Enfoque Práctico.',
            'Documentación oficial de Django: docs.djangoproject.com',
            'Fowler, M. — Patterns of Enterprise Application Architecture.',
        ],
    }
    return render(request, 'semana1/inicio.html', contexto)
