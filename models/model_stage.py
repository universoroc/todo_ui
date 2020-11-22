# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'
    # String fields:
    #name = fields.Char('Name', required=True)
    # Field attributes:
    name = fields.Char(
        string='Name',
        # Common field attributes:
        copy=False,
        default='New',
        groups="base.group_user,base.group_no_one",
        help='The title for the stage.',
        index=True,
        readonly=False,
        required=True,
        states={'done': [('readonly', False)]},
        # String only attributes:
        size=40,
        translate=True,
    )

    desc = fields.Text('Description')
    state = fields.Selection([('draft', 'New'), ('open', 'Started'), ('done', 'Closed')], 'State')
    docs = fields.Html('Documentation')
    # Numeric fields:
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float('% Complete', (3, 2))
    # Date fields:
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')
    # Other fields:
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

    # Stage class relationship with Tasks:
    # One2many inverse relation:
    tasks = fields.One2many(
        'todoroc_app.todoroc_app',   # related model
        'stage_id',  # field for "this" on related model
        'Tasks in this stage')

