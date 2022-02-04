from odoo import fields, models, api

class My_profile(models.Model):
    _name = "myprofile"
    _description = "my profile"

   
    name = fields.Char(default="Your name")
    image = fields.Image()
    state = fields.Text()