from models import Picture
from rest_framework import serializers

class PictureSerializer(serializers.ModelSerializer):

    full_url = serializers.SerializerMethodField('get_full_url')
    date_format = serializers.SerializerMethodField('get_format_date')

    def get_full_url(self, obj):
        url = 'None'
        if obj:
            url = 'http://127.0.0.1:8000' + obj.photo.url
        return url

    def get_format_date(self, obj):
        date = 'None'
        if obj:
            date = obj.create_date.strftime('%Y-%m-%d %H:%M:%S')
        return date

    class Meta:
        model = Picture
