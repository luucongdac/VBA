from thriver import *
from thriver.tcs_interface import *
from thriver.infoset import *
from thriver.infoset.tcsobject import *
from thriver.database.db_stub import *


from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Navigate_To_Radial_Probe import __M_S_RP_1__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_InitPosition_And_Speed import __M_S_RP_23__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_InitPosition_And_Speed import __M_S_RP_26__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Mode_And_Gain_Status import __M_S_RP_28__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Current_Information import __M_S_RP_30__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Current_Information import __M_S_RP_32__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Current_Information import __M_S_RP_33__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Current_Information import __M_S_RP_34__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Current_Information import __M_S_RP_35__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Position_And_Energy import __M_S_RP_36__
from procedures.thriver.test_itp_mcrhci.test_radialProbe.test_radialProbe_test_cases.M_S_RP_Position_And_Energy import __M_S_RP_37__


class test_radialProbe(ClinicalIntegrationTestProcedure):
    def __init__(self, test):
        name = "test_radialProbe"
        info_exchange = [
                        ]
        ClinicalIntegrationTestProcedure.__init__(self, test, name=name, info_exchange=info_exchange)
        self.applicable_rooms = ['mcr']
        self.setup =    [  
                        __M_S_RP_1__,
                        __M_S_RP_23__,
                        __M_S_RP_26__,
                        __M_S_RP_28__,
                        __M_S_RP_30__,
                        __M_S_RP_32__,
                        __M_S_RP_33__,
                        __M_S_RP_34__,
                        __M_S_RP_35__,
                        __M_S_RP_36__,
                        __M_S_RP_37__,
                        ]
        self.teardown_path = []