from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_Beamprofile1.test_BeamProfiles1_test_cases.M_BF1_1_CheckstartScreen import __M_BF1_1__
from procedures.thriver.test_itp_mcrhci.test_Beamprofile1.test_BeamProfiles1_test_cases.M_BF1_ClickButton import __M_BF1_2__, __M_BF1_3__, __M_BF1_4__
from procedures.thriver.test_itp_mcrhci.test_Beamprofile1.test_BeamProfiles1_test_cases.M_BF1_Display_text import __M_BF1_5__, __M_BF1_6__, __M_BF1_7__, 	\
	__M_BF1_8__, __M_BF1_9__, __M_BF1_10__, __M_BF1_11__, __M_BF1_12__, __M_BF1_13__, __M_BF1_14__, __M_BF1_15__, __M_BF1_16__, __M_BF1_17__, __M_BF1_18__, \
	__M_BF1_19__, __M_BF1_20__, __M_BF1_21__, __M_BF1_22__, __M_BF1_23__, __M_BF1_24__, __M_BF1_25__, __M_BF1_26__, __M_BF1_27__, __M_BF1_28__,	 			\
	__M_BF1_29__, __M_BF1_30__, __M_BF1_31__, __M_BF1_32__, __M_BF1_33__, __M_BF1_34__, __M_BF1_35__, __M_BF1_36__, __M_BF1_37__, __M_BF1_38__, 			\
	__M_BF1_39__, __M_BF1_40__, __M_BF1_41__, __M_BF1_42__, __M_BF1_43__, __M_BF1_44__, __M_BF1_45__, __M_BF1_46__, __M_BF1_47__, __M_BF1_48__,				\
	__M_BF1_49__, __M_BF1_50__, __M_BF1_51__, __M_BF1_52__, __M_BF1_53__, __M_BF1_54__, __M_BF1_55__, __M_BF1_56__, __M_BF1_57__, __M_BF1_58__,				\
	__M_BF1_59__, __M_BF1_60__, __M_BF1_61__, __M_BF1_62__, __M_BF1_63__, __M_BF1_64__, __M_BF1_65__, __M_BF1_66__, __M_BF1_67__, __M_BF1_68__, 			\
	__M_BF1_69__, __M_BF1_70__, __M_BF1_71__, __M_BF1_72__, __M_BF1_73__, __M_BF1_74__, __M_BF1_75__, __M_BF1_76__, __M_BF1_77__, __M_BF1_78__, __M_BF1_79__

class test_BeamProfiles1(ClinicalIntegrationTestProcedure):
	def __init__(self, test):
		name = "test_BeamProfiles1_screen"
		info_exchange = [
						]
		treatment_test_list = ["mcr_treatment_beam_control" ,"mcr_treatment_set_range1" , "mcr_treatment_beam_tuning" 
			 				,"mcr_treatment_beam_menu", "mcr_treatment_main_menu", "mcr_treatment_beam_profiles1"]
		ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange, treatment_test_list = treatment_test_list)
		self.applicable_rooms = ['mcr']
		self.setup =	[      
						__M_BF1_1__,
						__M_BF1_2__,
						__M_BF1_3__,
						__M_BF1_4__,
						__M_BF1_5__,
						__M_BF1_6__,
						__M_BF1_7__,
						__M_BF1_8__,
						__M_BF1_9__,
						__M_BF1_10__,
						__M_BF1_11__,
						__M_BF1_12__,
						__M_BF1_13__,
						__M_BF1_14__,
						__M_BF1_15__,
						__M_BF1_16__,
						__M_BF1_17__,
						__M_BF1_18__,
						__M_BF1_19__,
						__M_BF1_20__,
						__M_BF1_21__,
						__M_BF1_22__,
						__M_BF1_23__,
						__M_BF1_24__,
						__M_BF1_25__,
						__M_BF1_26__,
						__M_BF1_27__,
						__M_BF1_28__,
						__M_BF1_29__,
						__M_BF1_30__,
						__M_BF1_31__,
						__M_BF1_32__,
						__M_BF1_33__,
						__M_BF1_34__,
						__M_BF1_35__,
						__M_BF1_36__,
						__M_BF1_37__,
						__M_BF1_38__,
						__M_BF1_39__,
						__M_BF1_40__,
						__M_BF1_41__,
						__M_BF1_42__,
						__M_BF1_43__,
						__M_BF1_44__,
						__M_BF1_45__,
						__M_BF1_46__,
						__M_BF1_47__,
						__M_BF1_48__,
						__M_BF1_49__,
						__M_BF1_50__,
						__M_BF1_51__,
						__M_BF1_52__,
						__M_BF1_53__,
						__M_BF1_54__,
						__M_BF1_55__,
						__M_BF1_56__,
						__M_BF1_57__,
						__M_BF1_58__,
						__M_BF1_59__,
						__M_BF1_60__,
						__M_BF1_61__,
						__M_BF1_62__,
						__M_BF1_63__,
						__M_BF1_64__,
						__M_BF1_65__,
						__M_BF1_66__,
						__M_BF1_67__,
						__M_BF1_68__,
						__M_BF1_69__,
						__M_BF1_70__,
						__M_BF1_71__,
						__M_BF1_72__,
						__M_BF1_73__,
						__M_BF1_74__,
						__M_BF1_75__,
						__M_BF1_76__,
						__M_BF1_77__,
						__M_BF1_78__,
						__M_BF1_79__,
						]
		self.teardown_path = []