# -*- coding: utf-8 -*-

from odoo import models, fields, api

#
# class Tag(models.Model):
#     _name = 'todo.task.tag'
#     _description = 'To-do Tag'
#     name = fields.Char('Name', required=True)
#     _parent_store = True
#     # _parent_name = 'parent_id'
#     parent_id = fields.Many2one(
#        'todo.task.tag', 'Parent Tag', ondelete='restrict')
#     parent_left = fields.Integer('Parent Left', index=True)
#     parent_right = fields.Integer('Parent Right', index=True)
#
#     child_ids = fields.One2many(
#         'todo.task.tag', 'parent_id', 'Child Tags')
#
#     # Tag class relationship to Tasks:
#     task_ids = fields.Many2many(
#         'todoroc_app.todoroc_app',  # related model
#         string='Tasks')
#
#
# class Stage(models.Model):
#     _name = 'todo.task.stage'
#     _description = 'To-do Stage'
#     _order = 'sequence,name'
#     # String fields:
#     name = fields.Char('Name', required=True)
#     desc = fields.Text('Description')
#     state = fields.Selection([('draft', 'New'), ('open', 'Started'), ('done', 'Closed')], 'State')
#     docs = fields.Html('Documentation')
#     # Numeric fields:
#     sequence = fields.Integer('Sequence')
#     perc_complete = fields.Float('% Complete', (3, 2))
#     # Date fields:
#     date_effective = fields.Date('Effective Date')
#     date_changed = fields.Datetime('Last Changed')
#     # Other fields:
#     fold = fields.Boolean('Folded?')
#     image = fields.Binary('Image')
#     # Stage class relationship with Tasks:
#     tasks = fields.One2many(
#         'todoroc_app.todoroc_app',   # related model
#         'stage_id',  # field for "this" on related model
#         'Tasks in this stage')


# class TodoTask(models.Model):
#     _inherit = 'todoroc_app.todoroc_app'
#     stage_id = fields.Many2one('todo.task.stage', 'Stage')
#     tag_ids = fields.Many2many('todo.task.tag', string='Tags')
#
#     stage_fold = fields.Boolean(
#         'Stage Folded?',
#         compute='_compute_stage_fold',
#         # store=False,  # the default
#         search='_search_stage_fold',
#         inverse='_write_stage_fold'
#     )
#
#     @api.depends('stage_id.fold')
#     def _compute_stage_fold(self):
#         for task in self:
#             task.stage_fold = task.stage_id.fold
#
#     @staticmethod
#     def _search_stage_fold(operator, value):
#         return [('stage_id.fold', operator, value)]
#
#     def _write_stage_fold(self):
#         self.stage_id.fold = self.stage_fold
#
#     stage_state = fields.Selection(
#         related='stage_id.state',
#         string='Stage State')
