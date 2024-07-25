from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from taggit.managers import TaggableManager
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    def get_context(self, request):
        context = super().get_context(request)
        context['latest_events'] = EventPage.objects.live().order_by('-first_published_at')[:6]
        return context

class EventPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'EventPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class EventPage(Page):
    date = models.DateField("Event date")
    start_time = models.TimeField("Start time")
    end_time = models.TimeField("End time")
    venue = models.CharField(max_length=255)
    description = RichTextField()
    header_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    tags = ClusterTaggableManager(through=EventPageTag, blank=False)
    registration_required = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    capacity = models.IntegerField(null=True, blank=True)
    registration_url = models.URLField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('tags'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('header_image'),
            FieldPanel('date'),
            FieldPanel('start_time'),
            FieldPanel('end_time'),
            FieldPanel('venue'),
        ], heading="Event Details"),
        FieldPanel('description'),
        FieldPanel('tags'),
        MultiFieldPanel([
            FieldPanel('registration_required'),
            FieldPanel('price'),
            FieldPanel('capacity'),
            FieldPanel('registration_url'),
        ], heading="Registration Information"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        return context

class EventIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        event_pages = self.get_children().live().type(EventPage).order_by('eventpage__date')
        context['event_pages'] = event_pages
        return context