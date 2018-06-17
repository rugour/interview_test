from django.db import models
from django.utils.translation import ugettext as _
from django.utils.html import format_html

class APIUser(models.Model):
    """docstring for User"""
    id = models.IntegerField(primary_key=True)
    login = models.CharField(_('Login Username'), unique=True, max_length=200)
    node_id = models.CharField(_('Node Id'), max_length=200)
    avatar_url = models.CharField(_('Avatar'), max_length=200, null=True, blank=True)
    gravatar_id = models.CharField(_('Gravatar_id'), max_length=255, null=True, blank=True)
    url = models.CharField(_('Url'), max_length=200, null=True, blank=True)
    html_url = models.CharField(_('HTML Url'), max_length=200, null=True, blank=True)
    followers_url = models.CharField(_('Followers Url'), max_length=100, null=True, blank=True)
    following_url = models.CharField(_('Following Url'), max_length=100, null=True, blank=True)
    gists_url = models.CharField(max_length=100, null=True, blank=True)
    starred_url = models.CharField(max_length=100, null=True, blank=True)
    subscriptions_url = models.CharField(max_length=100, null=True, blank=True)
    organizations_url = models.CharField(max_length=100, null=True, blank=True)
    repos_url = models.CharField(max_length=100, null=True, blank=True)
    events_url = models.CharField(max_length=100, null=True, blank=True)
    received_events_url = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    site_admin = models.NullBooleanField(default=False, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    blog = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    hireable = models.NullBooleanField(default=False, null=True, blank=True)
    bio = models.CharField(max_length=100, null=True, blank=True)
    public_repos = models.IntegerField(null=True, blank=True)
    public_gists = models.IntegerField(null=True, blank=True)
    followers = models.IntegerField(_('Followers'), null=True, blank=True)
    following = models.IntegerField(_('Following'), null=True, blank=True)
    created_at = models.DateTimeField(_('Create Date'))
    updated_at = models.DateTimeField(_('Update Date'))
    added_on = models.DateField(_('Added on Date'), auto_now_add=True)

    def __str__(self):
        return self.login

    def avatar(self):
        return format_html(
            '<img src="{}" style="width: 75px;">',
            self.avatar_url,
        )