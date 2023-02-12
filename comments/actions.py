def disapprove_comments(modeladmin,request,queryset):
    queryset.update(approved = False)

def approve_comments(modeladmin,request,queryset):
    queryset.update(approved = True)

disapprove_comments.short_description = "Reprovar Comentario"
approve_comments.short_description = "Aprovar Comentario"
