# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 21:36:47 2023

@author: SOba
"""

from flask import Flask, redirect, url_for, request, render_template 
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(spaceid=row[0], name=row[1], code=row[2], floor=row[3], room=row[4], rating=row[5] ) for row in model.select()]
        model.close
        return render_template('index.html',entries=entries)
    
    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.remove(request.form['spaceid'])   
        model.close
        return redirect(url_for('index'))