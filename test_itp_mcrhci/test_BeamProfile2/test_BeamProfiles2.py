from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_BeamProfile2.test_BeamProfiles2_test_cases.M_BF2_1_CheckstartScreen import __M_BF2_1__
from procedures.thriver.test_itp_mcrhci.test_BeamProfile2.test_BeamProfiles2_test_cases.M_BF2_ClickButton import __M_BF2_2__, __M_BF2_3__, __M_BF2_4__
from procedures.thriver.test_itp_mcrhci.test_BeamProfile2.test_BeamProfiles2_test_cases.M_BF2_Display_text import __M_BF2_5__, __M_BF2_6__, __M_BF2_7__, 	\
	__M_BF2_8__, __M_BF2_9__, __M_BF2_10__, __M_BF2_11__, __M_BF2_12__, __M_BF2_13__, __M_BF2_14__, __M_BF2_15__, __M_BF2_16__, __M_BF2_17__, __M_BF2_18__, \
	__M_BF2_19__, __M_BF2_20__, __M_BF2_21__, __M_BF2_22__, __M_BF2_23__, __M_BF2_24__, __M_BF2_25__, __M_BF2_26__, __M_BF2_27__, __M_BF2_28__,	 			\
	__M_BF2_29__, __M_BF2_30__, __M_BF2_31__, __M_BF2_32__, __M_BF2_33__, __M_BF2_34__, __M_BF2_35__, __M_BF2_36__, __M_BF2_37__, __M_BF2_38__, 			\
	__M_BF2_39__, __M_BF2_40__, __M_BF2_41__, __M_BF2_42__, __M_BF2_43__, __M_BF2_44__, __M_BF2_45__, __M_BF2_46__, __M_BF2_47__, __M_BF2_48__,				\
	__M_BF2_49__, __M_BF2_50__, __M_BF2_51__, __M_BF2_52__, __M_BF2_53__, __M_BF2_54__, __M_BF2_55__, __M_BF2_56__, __M_BF2_57__, __M_BF2_58__,				\
	__M_BF2_59__, __M_BF2_60__, __M_BF2_61__, __M_BF2_62__, __M_BF2_63__, __M_BF2_64__, __M_BF2_65__, __M_BF2_66__, __M_BF2_67__, __M_BF2_68__, 			\
	__M_BF2_69__, __M_BF2_70__, __M_BF2_71__, __M_BF2_72__, __M_BF2_73__, __M_BF2_74__, __M_BF2_75__, __M_BF2_76__, __M_BF2_77__, __M_BF2_78__, __M_BF2_79__

class test_BeamProfiles2(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "test_BeamProfiles2_screen"
		info_exchange = [
						]
		treatment_test_list = ["mcr_treatment_beam_control", "mcr_treatment_set_range1", "mcr_treatment_beam_tuning", "mcr_treatment_beam_menu",
			 				"mcr_treatment_main_menu", "mcr_treatment_beam_profiles2"]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, treatment_test_list = treatment_test_list)
		self.applicable_rooms = ['mcr']
		self.setup =	[      
						__M_BF2_1__,
						__M_BF2_2__,
						__M_BF2_3__,
						__M_BF2_4__,
						__M_BF2_5__,
						__M_BF2_6__,
						__M_BF2_7__,
						__M_BF2_8__,
						__M_BF2_9__,
						__M_BF2_10__,
						__M_BF2_11__,
						__M_BF2_12__,
						__M_BF2_13__,
						__M_BF2_14__,
						__M_BF2_15__,
						__M_BF2_16__,
						__M_BF2_17__,
						__M_BF2_18__,
						__M_BF2_19__,
						__M_BF2_20__,
						__M_BF2_21__,
						__M_BF2_22__,
						__M_BF2_23__,
						__M_BF2_24__,
						__M_BF2_25__,
						__M_BF2_26__,
						__M_BF2_27__,
						__M_BF2_28__,
						__M_BF2_29__,
						__M_BF2_30__,
						__M_BF2_31__,
						__M_BF2_32__,
						__M_BF2_33__,
						__M_BF2_34__,
						__M_BF2_35__,
						__M_BF2_36__,
						__M_BF2_37__,
						__M_BF2_38__,
						__M_BF2_39__,
						__M_BF2_40__,
						__M_BF2_41__,
						__M_BF2_42__,
						__M_BF2_43__,
						__M_BF2_44__,
						__M_BF2_45__,
						__M_BF2_46__,
						__M_BF2_47__,
						__M_BF2_48__,
						__M_BF2_49__,
						__M_BF2_50__,
						__M_BF2_51__,
						__M_BF2_52__,
						__M_BF2_53__,
						__M_BF2_54__,
						__M_BF2_55__,
						__M_BF2_56__,
						__M_BF2_57__,
						__M_BF2_58__,
						__M_BF2_59__,
						__M_BF2_60__,
						__M_BF2_61__,
						__M_BF2_62__,
						__M_BF2_63__,
						__M_BF2_64__,
						__M_BF2_65__,
						__M_BF2_66__,
						__M_BF2_67__,
						__M_BF2_68__,
						__M_BF2_69__,
						__M_BF2_70__,
						__M_BF2_71__,
						__M_BF2_72__,
						__M_BF2_73__,
						__M_BF2_74__,
						__M_BF2_75__,
						__M_BF2_76__,
						__M_BF2_77__,
						__M_BF2_78__,
						__M_BF2_79__,
						]
		self.teardown_path = []