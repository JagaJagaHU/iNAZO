from .base import *

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'local': {
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'local',
        },
    },
    'loggers': {
        # 自作したログ出力
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # Djangoのエラー・警告・開発WEBサーバのアクセスログ
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        # 実行SQL
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
