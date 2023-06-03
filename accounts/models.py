from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UserManager(BaseUserManager):
    # アカウント作成時に呼び出し
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('Users mus have an email')

        # メールアドレスを正規化
        email=self.normalize_email(email)
        email=email.lower()

        # ユーザーモデルを作成
        user=self.model(
            email=email,
            name=name
        )

        # パスワードをハッシュ化して保存
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    # 管理者アカウントを登録する時
    def create_superuser(self,email,name,password=None):
        # 通常のユーザーアカウントを作成
        user=self.create_user(email,name,password)
        
        # 管理者としてのフラグを設定
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField("メールアドレス",max_length=255,unique=True)
    name=models.CharField("名前",max_length=255)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    # カスタムのユーザーマネージャーを設定
    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def __str__(self):
        return self.email