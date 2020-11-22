# -*- coding: utf-8 -*-

from odoo import models, fields, api
#from odoo.addons.base.models. res import res_request
from odoo.exceptions import ValidationError

# def referencable_models(self):
#     return res_request.referencable_models(
#         self, self.env.cr, self.env.uid, context=self.env.context)


class TodoTask(models.Model):
    _inherit = 'todoroc_app.todoroc_app'
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')
    refers_to = fields.Reference(
        [('res.user', 'User'), ('res.partner', 'Partner')],
        'Refers to')

    stage_fold = fields.Boolean(
        'Stage Folded?',
        compute='_compute_stage_fold',
        # store=False,  # the default
        search='_search_stage_fold',
        inverse='_write_stage_fold'
    )

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold

    @staticmethod
    def _search_stage_fold(operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    stage_state = fields.Selection(
        related='stage_id.state',
        string='Stage State')

# Constraints
    _sql_constraints = [(
        'todo_task_name_unique',
        'UNIQUE (name, user_id, active)',
        'Task title must be unique!'
    )]

 #   @api.one
    @api.constrains('name')
    def _check_name_size(self):
        if len(self.name) < 5:
            raise ValidationError('Title must have 5 chars!')

 #   @api.one
    def compute_user_todo_count(self):
        self.user_todo_count = self.search_count(
            [('user_id', '=', self.user_id.id)])

    user_todo_count = fields.Integer(
        'User To-Do Count',
        compute='compute_user_todo_count'
    )
    effort_estimate = fields.Integer('Effort Estimate')