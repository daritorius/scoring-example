from core.emails.models import EmailTemplate, Email
from django.contrib import admin


class EmailsAdmin(admin.ModelAdmin):
    list_display = ('email_to', 'format_date', 'subject', 'status')
    list_filter = ('status',)
    search_fields = ('email_to', 'subject')
    date_hierarchy = 'date_update'

    def format_date(self, obj):
        return obj.date_create.strftime('%Y-%m-%d %H:%M')
    format_date.short_description = 'Date'
    format_date.allow_tags = True


class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject')
    search_fields = ('title', 'subject')

admin.site.register(EmailTemplate, EmailTemplateAdmin)
admin.site.register(Email, EmailsAdmin)