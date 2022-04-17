from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

# this class is needed for the users registration process specfically when they need to activate registration link in email 
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            text_type(user.pk) + text_type(timestamp) +
            text_type(user.is_active)
        )

account_activation_token = TokenGenerator()