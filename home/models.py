from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class EventPage(Page):
    date = models.DateField("Event date")
    start_time = models.TimeField("Start time")
    end_time = models.TimeField("End time")
    venue = models.CharField(max_length=255)
    description = RichTextField(blank=True)
    organizer = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, help_text="Comma-separated list of tags")

    search_fields = Page.search_fields + [
        index.SearchField('description'),
        index.SearchField('tags'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('start_time'),
            FieldPanel('end_time'),
        ], heading="Event Date and Time"),
        FieldPanel('venue'),
        FieldPanel('description'),
        FieldPanel('organizer'),
        FieldPanel('tags'),
    ]

class EventIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        event_pages = self.get_children().live().order_by('eventpage__date')
        context['event_pages'] = event_pages
        return context