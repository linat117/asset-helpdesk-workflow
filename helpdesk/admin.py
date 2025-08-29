from django.contrib import admin
from .models import TicketCategory, Ticket, TicketComment, TicketUpdateLog

@admin.register(TicketCategory)
class TicketCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'category', 'reported_by', 'assigned_to', 'linked_asset', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at', 'assigned_to__role')
    search_fields = ('title', 'description', 'reported_by__first_name', 'reported_by__last_name')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('reported_by', 'assigned_to', 'linked_asset', 'category')
    list_per_page = 25
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category', 'linked_asset')
        }),
        ('Status & Priority', {
            'fields': ('status', 'priority')
        }),
        ('Assignment', {
            'fields': ('reported_by', 'assigned_to')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at')

@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'commenter', 'comment_text', 'comment_time')
    list_filter = ('comment_time', 'commenter__role')
    search_fields = ('comment_text', 'ticket__title', 'commenter__first_name', 'commenter__last_name')
    ordering = ('-comment_time',)
    date_hierarchy = 'comment_time'
    raw_id_fields = ('ticket', 'commenter')
    list_per_page = 20

@admin.register(TicketUpdateLog)
class TicketUpdateLogAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'updated_by', 'update_note', 'update_time')
    list_filter = ('update_time', 'updated_by__role')
    search_fields = ('update_note', 'ticket__title', 'updated_by__first_name', 'updated_by__last_name')
    ordering = ('-update_time',)
    date_hierarchy = 'update_time'
    raw_id_fields = ('ticket', 'updated_by')
    list_per_page = 20