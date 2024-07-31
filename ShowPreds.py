import ROOT
import os

test = False

#regions = ["50ias60","60ias70","70ias80","80ias90","50ias90","90ias100","99ias100","999ias100"]
#regions = ["90ias100","99ias100","999ias100"]
#regions = ["999ias100"]
#regions = ["50ias60","60ias70","70ias80","80ias90","50ias90"]
#regions = ["90ias100","99ias100","999ias100"]
#regions = ["999ias100"]
regions=["999ias100"]

#year = '2017'
#year = '2018'
year = '2017and2018'



if not test:
    for i in regions:
        #command = "python2.7 macroMass.py --ifile /opt/sbg/cms/ui3_data1/rhaeberl/HSCP_prod/Dylan/Unblinded/SingleMuon_{}_Raph_cutIndex3_rebinEta4_rebinIh4_rebinP2_rebinMass1_nPE200_test_v1.root --ofile mass_plot_data --region {} --odir Approval_checks".format(year,i)
        #command = "python2.7 macroMass_ratioAndPulls.py --ifile /opt/sbg/cms/ui3_data1/rhaeberl/HSCP_prod/Dylan/Unblinded/SingleMuon_{}_Raph_cutIndex3_rebinEta4_rebinIh4_rebinP2_rebinMass1_nPE200_test_v1.root --ofile mass_plot_data --region {} --odir Approval_checks".format(year,i)
        command = "python2.7 macroMass_allPanels.py --ifile /opt/sbg/cms/ui3_data1/rhaeberl/HSCP_prod/Dylan/Unblinded/SingleMuon_{}_Raph_cutIndex3_rebinEta4_rebinIh4_rebinP2_rebinMass1_nPE200_test_v1.root --ofile mass_plot_data --region {} --odir Approval_checks_allPanels".format(year,i)
        print("Running {}\n".format(command))
        os.system(command)


cutGi = '0p3'

if test:
    for i in regions:
        command = "python2.7 macroMass.py --ifile /opt/sbg/cms/ui4_data1/rhaeberl/CMSSW_10_6_30/src/HSCPTreeAnalyzer/macros/Data_good/massReco_pt70/{}/Mu{}_massCut_0_pT70_Vgi{}_Gstrip_cutIndex3_rebinEta4_rebinIh4_rebinP2_rebinMass1_nPE200_test_v1.root --ofile test_g{} --region {} --odir test_g0p3".format(cutGi,year,cutGi,cutGi,i)
        print("Running {}\n".format(command))
        os.system(command)
