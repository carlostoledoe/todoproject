from rest_framework.throttling import SimpleRateThrottle

class LoginThrottle(SimpleRateThrottle):
    scope = 'login'  # este nombre se usará en settings.py

    def get_cache_key(self, request, view):
        # Usa la IP del cliente como clave (también puedes usar user.id si está autenticado)
        return self.get_ident(request)
        