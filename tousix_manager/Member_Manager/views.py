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

from tousix_manager.Member_Manager.create import CreateMemberView
from tousix_manager.Member_Manager.update.view import UpdateMemberView
from tousix_manager.Member_Manager.update.noc import NOCUpdateView
from tousix_manager.Member_Manager.update.billing import BillingUpdateView
from tousix_manager.Member_Manager.update.password import PasswordChangeView
from tousix_manager.Member_Manager.update.technical import TechnicalUpdateView
from tousix_manager.Member_Manager.update.router import RouterUpdateView