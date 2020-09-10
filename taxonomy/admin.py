# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from taxonomy.models import Skill, CourseSkills, JobSkills, Job

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name', 'created', 'modified')
    search_fields = ('external_id', 'name')

@admin.register(CourseSkills)
class CourseSkillsTitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'course_id', 'created', 'modified')
    search_fields = ('course_id',)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created', 'modified')
    search_fields = ('name',)


@admin.register(JobSkills)
class JobSkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'job', 'significance', 'unique_postings', 'created', 'modified')
    search_fields = ('name', 'significance',)