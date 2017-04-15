from __future__ import unicode_literals

from django.db import models


class Footballers(models.Model):
    name = models.CharField(db_column='Name', max_length=25, blank=True, null=True)  # Field name made lowercase.
    nationality = models.CharField(db_column='Nationality', max_length=19, blank=True, null=True)  # Field name made lowercase.
    national_position = models.CharField(db_column='National_Position', max_length=3, blank=True, null=True)  # Field name made lowercase.
    national_kit = models.CharField(db_column='National_Kit', max_length=2, blank=True, null=True)  # Field name made lowercase.
    club = models.CharField(db_column='Club', max_length=17, blank=True, null=True)  # Field name made lowercase.
    club_position = models.CharField(db_column='Club_Position', max_length=3, blank=True, null=True)  # Field name made lowercase.
    club_kit = models.CharField(db_column='Club_Kit', max_length=2, blank=True, null=True)  # Field name made lowercase.
    club_joining = models.CharField(db_column='Club_Joining', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contract_expiry = models.CharField(db_column='Contract_Expiry', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=6, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=5, blank=True, null=True)  # Field name made lowercase.
    preffered_foot = models.CharField(db_column='Preffered_Foot', max_length=5, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.CharField(db_column='Birth_Date', max_length=10, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    preffered_position = models.CharField(db_column='Preffered_Position', max_length=9, blank=True, null=True)  # Field name made lowercase.
    work_rate = models.CharField(db_column='Work_Rate', max_length=15, blank=True, null=True)  # Field name made lowercase.
    weak_foot = models.IntegerField(db_column='Weak_foot', blank=True, null=True)  # Field name made lowercase.
    skill_moves = models.IntegerField(db_column='Skill_Moves', blank=True, null=True)  # Field name made lowercase.
    ball_control = models.IntegerField(db_column='Ball_Control', blank=True, null=True)  # Field name made lowercase.
    dribbling = models.IntegerField(db_column='Dribbling', blank=True, null=True)  # Field name made lowercase.
    marking = models.IntegerField(db_column='Marking', blank=True, null=True)  # Field name made lowercase.
    sliding_tackle = models.IntegerField(db_column='Sliding_Tackle', blank=True, null=True)  # Field name made lowercase.
    standing_tackle = models.IntegerField(db_column='Standing_Tackle', blank=True, null=True)  # Field name made lowercase.
    aggression = models.IntegerField(db_column='Aggression', blank=True, null=True)  # Field name made lowercase.
    reactions = models.IntegerField(db_column='Reactions', blank=True, null=True)  # Field name made lowercase.
    attacking_position = models.IntegerField(db_column='Attacking_Position', blank=True, null=True)  # Field name made lowercase.
    interceptions = models.IntegerField(db_column='Interceptions', blank=True, null=True)  # Field name made lowercase.
    vision = models.IntegerField(db_column='Vision', blank=True, null=True)  # Field name made lowercase.
    composure = models.IntegerField(db_column='Composure', blank=True, null=True)  # Field name made lowercase.
    crossing = models.IntegerField(db_column='Crossing', blank=True, null=True)  # Field name made lowercase.
    short_pass = models.IntegerField(db_column='Short_Pass', blank=True, null=True)  # Field name made lowercase.
    long_pass = models.IntegerField(db_column='Long_Pass', blank=True, null=True)  # Field name made lowercase.
    acceleration = models.IntegerField(db_column='Acceleration', blank=True, null=True)  # Field name made lowercase.
    speed = models.IntegerField(db_column='Speed', blank=True, null=True)  # Field name made lowercase.
    stamina = models.IntegerField(db_column='Stamina', blank=True, null=True)  # Field name made lowercase.
    strength = models.IntegerField(db_column='Strength', blank=True, null=True)  # Field name made lowercase.
    balance = models.IntegerField(db_column='Balance', blank=True, null=True)  # Field name made lowercase.
    agility = models.IntegerField(db_column='Agility', blank=True, null=True)  # Field name made lowercase.
    jumping = models.IntegerField(db_column='Jumping', blank=True, null=True)  # Field name made lowercase.
    heading = models.IntegerField(db_column='Heading', blank=True, null=True)  # Field name made lowercase.
    shot_power = models.IntegerField(db_column='Shot_Power', blank=True, null=True)  # Field name made lowercase.
    finishing = models.IntegerField(db_column='Finishing', blank=True, null=True)  # Field name made lowercase.
    long_shots = models.IntegerField(db_column='Long_Shots', blank=True, null=True)  # Field name made lowercase.
    curve = models.IntegerField(db_column='Curve', blank=True, null=True)  # Field name made lowercase.
    freekick_accuracy = models.IntegerField(db_column='Freekick_Accuracy', blank=True, null=True)  # Field name made lowercase.
    penalties = models.IntegerField(db_column='Penalties', blank=True, null=True)  # Field name made lowercase.
    volleys = models.IntegerField(db_column='Volleys', blank=True, null=True)  # Field name made lowercase.
    gk_positioning = models.IntegerField(db_column='GK_Positioning', blank=True, null=True)  # Field name made lowercase.
    gk_diving = models.IntegerField(db_column='GK_Diving', blank=True, null=True)  # Field name made lowercase.
    gk_kicking = models.IntegerField(db_column='GK_Kicking', blank=True, null=True)  # Field name made lowercase.
    gk_handling = models.IntegerField(db_column='GK_Handling', blank=True, null=True)  # Field name made lowercase.
    gk_reflexes = models.IntegerField(db_column='GK_Reflexes', blank=True, null=True)  # Field name made lowercase.
    player_img = models.CharField(db_column='Image_URL', max_length=200, blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'footballers'
