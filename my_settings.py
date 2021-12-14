DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Owner_Dogs',
        'USER': 'root',
        'PASSWORD': '13245095',
        'HOST': '127.0.0.1',
        'PORT': '3306',
				'OPTIONS': {'charset': 'utf8mb4'}
    }
}

SECRET_KEY = 'django-insecure-w%9e+d*lfp$lxyzp)y&fd4u07uaz&y))xe_3_8s6i*n)znky_*' 
#settings.py에 있는 secret_key 를 사용합니다.