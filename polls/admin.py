from django.contrib import admin
from polls.models import Choice, Poll


class ChoiceInLine(admin.TabularInline):
	model = Choice
	extra = 3


class PollAdmin(admin.ModelAdmin):
	list_display = ('question','pub_date')
	list_filter = ['pub_date']
	search_fields = ['question']
	fieldsets= [
		(None,  {'fields' :['question']}),
		('date information', {'fields' :['pub_date'],'classes' :['collapse']}),
	]

	inlines = [ChoiceInLine]
	
	

admin.site.register(Poll,PollAdmin)
#admin.site.register(Choice)


