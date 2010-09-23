from django.contrib.auth.models import User
from django.db import models
from polls import settings
from tagging.fields import TagField
from published_manager.managers import PublishedManager
from django.utils.translation import ugettext as _

class Poll(models.Model):
    """
    A poll 
    """
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True, help_text=_("Not Required"))
    slug = models.SlugField(unique=True, verbose_name=_("Slug Field"))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Published"))
    user = models.ForeignKey(User, verbose_name=_("User"))
    state = models.CharField(max_length=1, choices=settings.STATE_CHOICES, default=settings.STATE_DEFAULT, verbose_name=_("State of object"))
    ip_address = models.IPAddressField(verbose_name=_("Author's IP Address"))
    tags = TagField(help_text=_("Enter key terms seperated with a space that you want to associate with this Poll"), verbose_name=_("Tags"))
    objects = models.Manager()
    published_objects = PublishedManager()

    def get_absolute_url(self):
        return "/polls/%s/" % self.slug

    def __unicode__(self):
        return _(self.title)

    class Meta:
        ordering = ['pub_date']
        get_latest_by = "pub_date"
        verbose_name = _("Poll")
        verbose_name_plural = _("Polls")
       

class Choice(models.Model):
    """
    A choice 
    """
    poll = models.ForeignKey(Poll, null=False, blank=False, verbose_name=_("Poll"))
    choice = models.CharField(max_length=200, verbose_name=_("Choice"))
    objects = models.Manager()

    def __unicode__(self):
        return _(self.choice)

    def get_vote_count(self):
        return self.vote_set.all().count()

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")

class Vote(models.Model):
    """
    A vote
    """
    poll = models.ForeignKey(Poll, verbose_name=_("Poll"))
    choice = models.ForeignKey(Choice, verbose_name=_("Choice"))
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Published"))
    user = models.ForeignKey(User, verbose_name=_("User"), related_name='polls_vote')
    ip_address = models.IPAddressField(verbose_name=_("Author's IP Address"))

    def __unicode__(self):
        return _(self.choice.choice)

    class Meta:
        unique_together = (("user", "poll"),)
        ordering = ['pub_date']
        get_latest_by = "pub_date"
        verbose_name = _("Vote")
        verbose_name_plural = _("Votes")
