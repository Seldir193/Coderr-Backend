from django.contrib import admin
from .models import BusinessProfile, CustomerProfile, Order, Offer, OfferDetail, Review
from django.utils.html import format_html

class CustomerProfileAdmin(admin.ModelAdmin):
    # Custom admin interface for CustomerProfile model
    list_display = ('id', 'user', 'first_name', 'last_name', 'created_at', 'profile_image_preview')
    search_fields = ('user__username', 'first_name', 'last_name')
    ordering = ('created_at',)

    def profile_image_preview(self, obj):
        """
        Displays a preview of the profile image if available.
        """
        if obj.file:
            return format_html(f'<img src="{obj.file.url}" style="width: 50px; height: 50px;" />')
        return "No Image"
    
    profile_image_preview.short_description = "Profile Image"

class BusinessProfileAdmin(admin.ModelAdmin):
    # Custom admin interface for BusinessProfile model
    list_display = (
        'id', 'company_name', 'company_address', 'created_at',
        'get_username', 'get_email', 'tel', 'location', 'working_hours',
        'profile_image_preview'
    )
    search_fields = (
        'company_name', 'company_address', 'user__username', 
        'user__email', 'tel', 'location'
    )
    ordering = ('created_at',)

    def get_username(self, obj):
        """
        Retrieves the username of the associated user.
        """
        return obj.user.username if obj.user else "N/A"
    get_username.short_description = "Username"

    def get_email(self, obj):
        """
        Retrieves the email of the associated user.
        """
        return obj.user.email if obj.user else "N/A"
    get_email.short_description = "Email"
    
    def profile_image_preview(self, obj):
        """
        Displays a preview of the profile image for BusinessProfile.
        """
        if obj.profile_image:
            return format_html(f'<img src="{obj.profile_image.url}" style="width: 50px; height: 50px;" />')
        return "No Image"

    profile_image_preview.short_description = "Profile Image"

class OfferAdmin(admin.ModelAdmin):
    # Custom admin interface for Offer model
    list_display = ('id', 'title', 'price', 'created_at')
    list_filter = ('price', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('created_at',)

class OrderAdmin(admin.ModelAdmin):
    # Custom admin interface for Order model
    list_display = (
        'id', 
        'user', 
        'business_user', 
        'offer', 
        'offer_detail_id', 
        'status', 
        'option', 
        'created_at', 
    )
    search_fields = ('user__username', 'business_user__username', 'offer__title')
    list_filter = ('status', 'option')
    ordering = ('created_at',)

class ReviewAdmin(admin.ModelAdmin):
    # Custom admin interface for Review model
    list_display = ('id', 'reviewer', 'business_user', 'rating', 'created_at')
    search_fields = ('reviewer__username', 'business_user__username')
    list_filter = ('rating', 'created_at')
    ordering = ('created_at',)

class OfferDetailAdmin(admin.ModelAdmin):
    # Custom admin interface for OfferDetail model
    list_display = ('id', 'offer', 'variant_title', 'variant_price', 'delivery_time_in_days', 'offer_type')
    search_fields = ('variant_title', 'offer__title')
    list_filter = ('offer_type',)
    ordering = ('offer',)

# Register the models with their custom admin interfaces
admin.site.register(BusinessProfile, BusinessProfileAdmin)
admin.site.register(CustomerProfile, CustomerProfileAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(OfferDetail, OfferDetailAdmin)
admin.site.register(Review, ReviewAdmin)
