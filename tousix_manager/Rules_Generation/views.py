#    Copyright 2015 Rémy Lapeyrade <remy at lapeyrade dot net>
#    Copyright 2015 LAAS-CNRS
#
#
#    This file is part of TouSIX-Manager.
#
#    TouSIX-Manager is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    TouSIX-Manager is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with TouSIX-Manager.  If not, see <http://www.gnu.org/licenses/>.

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from tousix_manager.Authentication.AdminMixin import AdminVerificationMixin
from tousix_manager.Database.models import Regles, Switch
from tousix_manager.Rules_Generation.manager import Manager
from tousix_manager.Rules_Generation.forms import SwitchChoiceForm


class SelectionSwitchView(FormView, AdminVerificationMixin):
    """
    Testing view for Rules_Generation app
    """
    form_class = SwitchChoiceForm
    template_name = "switches_list.html"

    def form_valid(self, form):
        switches = form.get_selected()
        manager = Manager()
        manager.create_rules(switches)
        rules = Regles.objects.values('regle')
        return render(self.request, "switches_list.html", context={"rules": rules})


class GenerateAllSwitchView(TemplateView, AdminVerificationMixin):
    template_name = "switches_list.html"

    def get_context_data(self, **kwargs):
        context = super(GenerateAllSwitchView, self).get_context_data()
        switches = Switch.objects.all()
        manager = Manager()
        manager.create_rules(switches)
        rules = Regles.objects.values('regle')
        context["rules"] = rules
        return context
