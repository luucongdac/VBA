from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.SETUP.setup_mcrhci_beam_tuning import *
from procedures.thriver.test_itp_mcrhci.SETUP.setup_utilities import SETUP_SET_VARIABLE


class VALIDATE_BEAM_TUNING_BLOCK_ID(SETUP_VALIDATE_BEAM_TUNING_BLOCK_ID): pass
class VALIDATE_NBR_TUNING_LOOP(SETUP_VALIDATE_NBR_TUNING_LOOP): pass
class VALIDATE_NBR_ACQUISITION(SETUP_VALIDATE_NBR_ACQUISITION): pass
class VALIDATE_CENTROID_X(SETUP_VALIDATE_CENTROID_X): pass
class VALIDATE_SIGMA_X(SETUP_VALIDATE_SIGMA_X): pass
class VALIDATE_CENTROID_Y(SETUP_VALIDATE_CENTROID_Y): pass
class VALIDATE_SIGMA_Y(SETUP_VALIDATE_SIGMA_Y): pass

class SET_MESSAGE_BEAM_TUNING_BLOCK_ID(SETUP_SET_VARIABLE):
	name = "Set mcr_ecubtcu_beamtuning_blockid to 10"
	var_name = "mcr_ecubtcu_beamtuning_blockid"
	value = 10
class SET_MESSAGE_NBR_TUNING_LOOP(SETUP_SET_VARIABLE):
	name = "Set mcr_ecubtcu_beamtuning_nbrtuningloop to 24"
	var_name = "mcr_ecubtcu_beamtuning_nbrtuningloop"
	value = 24
class SET_MESSAGE_NBR_ACQUISITION(SETUP_SET_VARIABLE):
	name = "Set mcr_ecubtcu_beamtuning_nbracquisition to 25"
	var_name = "mcr_ecubtcu_beamtuning_nbracquisition"
	value = 25
class SET_MESSAGE_CENTROID_X(SETUP_SET_VARIABLE):
	name = "Set mcr_ecubtcu_beamtuning_centroidx to 20"
	var_name = "mcr_ecubtcu_beamtuning_centroidx"
	value = 20
class SET_MESSAGE_SIGMA_X(SETUP_SET_VARIABLE):
	name = "Set mcr_ecubtcu_beamtuning_sigmax to 21"
	var_name = "mcr_ecubtcu_beamtuning_sigmax"
	value = 21
class SET_MESSAGE_CENTROID_Y(SETUP_SET_VARIABLE):
	name = "Set mcr_ecubtcu_beamtuning_centroidy to 22"
	var_name = "mcr_ecubtcu_beamtuning_centroidy"
	value = 22	
class SET_MESSAGE_SIGMA_Y(SETUP_SET_VARIABLE):
	name = "Set mcr_ecubtcu_beamtuning_sigmay to 23"
	var_name = "mcr_ecubtcu_beamtuning_sigmay"
	value = 23


class __M_BT_10__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Simulate and validate Beam Tuning Block ID in Beam Tuning screen'

		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_BEAM_TUNING_BLOCK_ID,			
						VALIDATE_BEAM_TUNING_BLOCK_ID
						]
		self.teardown_path = []


class __M_BT_13__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Simulate and validate nbr tuning loop in Beam Tuning screen'

		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_NBR_TUNING_LOOP,
						VALIDATE_NBR_TUNING_LOOP
						]
		self.teardown_path = []

		
class __M_BT_14__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Simulate and validate nbr acquisition in Beam Tuning screen'
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[
						SET_MESSAGE_NBR_ACQUISITION,			  
						VALIDATE_NBR_ACQUISITION
						]
		self.teardown_path = []			


class __M_BT_15__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Simulate and validate centroid X in Beam Tuning screen'
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[
						SET_MESSAGE_CENTROID_X,  
						VALIDATE_CENTROID_X
						]
		self.teardown_path = []	

	
class __M_BT_16__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Simulate and validate sigma X in Beam Tuning screen'
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[  
						SET_MESSAGE_SIGMA_X,
						VALIDATE_SIGMA_X
						]
		self.teardown_path = []		

		
class __M_BT_17__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Simulate and validate centroid Y in Beam Tuning screen'
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[ 
						SET_MESSAGE_CENTROID_Y, 
						VALIDATE_CENTROID_Y
						]
		self.teardown_path = []		
		
   
class __M_BT_18__(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = 'Simulate and validate sigma Y in Beam Tuning screen'
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[	
						SET_MESSAGE_SIGMA_Y,					  
						VALIDATE_SIGMA_Y
						]
		self.teardown_path = []	
