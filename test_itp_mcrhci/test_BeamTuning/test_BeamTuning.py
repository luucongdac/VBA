from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *

from procedures.thriver.test_itp_mcrhci.test_BeamTuning.test_BeamTuning_test_cases.M_BT_1 import __M_BT_1__
from procedures.thriver.test_itp_mcrhci.test_BeamTuning.test_BeamTuning_test_cases.M_BT_Display_text import __M_BT_10__,__M_BT_13__, __M_BT_14__, __M_BT_15__, __M_BT_16__, __M_BT_17__, __M_BT_18__

class test_BeamTuning(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "test_BeamTuning_screen"
		info_exchange = [
						]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
		self.applicable_rooms = ['mcr']
		self.setup =	[      
						__M_BT_1__,
						__M_BT_10__,
						__M_BT_13__,
						__M_BT_14__,
						__M_BT_15__,
						__M_BT_16__,
						__M_BT_17__,
						__M_BT_18__
						]
		self.teardown_path = []