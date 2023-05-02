# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:38:37 2023

@author: SOba
"""

from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['code'], request.form['floor'], request.form['room'], request.form['rating'])
        return redirect(url_for('index'))
    
