import os

# Your original code
code = '''
import sys, os, time, re
import numpy as np
#from common_functions import *
from optparse import OptionParser
parser = OptionParser(usage="Usage: python %prog codeVersion")
(opt,args) = parser.parse_args()

datasetList=[
    #"\/opt\/sbg\/cms\/ui3_data1\/dapparu\/HSCP\/Production\/crab\_Analysis\_SingleMuon\_Run2017\_CodeVUnB\_v1\_v1",
    #"\/opt\/sbg\/cms\/ui3_data1\/dapparu\/HSCP\/Production\/crab\_Analysis\_SingleMuon\_Run2018\_CodeVUnB\_v1\_v1"
    "\/opt\/sbg\/cms\/ui3_data1\/rhaeberl\/HSCP_prod\/Dylan\/Unblinded\/SingleMuon\_2017\_Raph",
    "\/opt\/sbg\/cms\/ui3_data1\/rhaeberl\/HSCP_prod\/Dylan\/Unblinded\/SingleMuon\_2018\_Raph"
    #"\/opt\/sbg\/cms\/ui4_data1\/rhaeberl\/CMSSW_10_6_30\/src\/HSCPTreeAnalyzer\/macros\/Data_good\/massReco_pt70\/Mu2017\_massCut\_0\_pT70\_Vdyl\_Gstrip",
    #"\/opt\/sbg\/cms\/ui4_data1\/rhaeberl\/CMSSW_10_6_30\/src\/HSCPTreeAnalyzer\/macros\/Data_good\/massReco_pt70\/Mu2018\_massCut\_0\_pT70\_Vdyl\_Gstrip"
]
tagKC=[
    "data2017",
    "data2018",
]
odir=[
    "test\_2017\_label\_UnB_v1_v2\/",
    "test\_2018\_label\_UnB_v1_v2\/",
]

nPE="200"

config=[
    #["nominal", "4", "4", "2", "0", "0", "1", "1"],
    #["etaup", "2", "4", "2", "0", "0", "1", "1"],
    #["etadown", "8", "4", "2", "0", "0", "1", "1"],
    #["ihup", "4", "2", "2", "0", "0", "1", "1"],   
    #["ihdown", "4", "8", "2", "0", "0", "1", "1"],
    #["momup", "4", "4", "1", "0", "0", "1", "1"],
    #["momdown", "4", "4", "4", "0", "0", "1", "1"],
    #["corrIh", "4", "4", "2", "1", "0", "1", "1"],
    #["corrMom", "4", "4", "2", "0", "1", "1", "1"],
    #["FitIhUp", "4", "4", "2", "0", "0", "2", "1"],
    #["FitIhDown", "4", "4", "2", "0", "0", "0", "1"],
    #["FitMomUp", "4", "4", "2", "0", "0", "1", "2"],
    #["FitMomDown", "4", "4", "2", "0", "0", "1", "0"],
]


i=0
for dataset in datasetList:
    print("Launch on dataset: "+dataset)
    os.system("cp configFile_readHist_template.txt configFile_readHisto_toLaunch_tmp.txt")
    os.system("sed -i 's/sample/"+dataset+"/g' configFile_readHisto_toLaunch_tmp.txt")
    os.system("sed -i 's/tag_KC/"+tagKC[i]+"/g' configFile_readHisto_toLaunch_tmp.txt")
    os.system("sed -i 's/dir/"+odir[i]+"/g' configFile_readHisto_toLaunch_tmp.txt")
    os.system("sed -i 's/nPE/"+nPE+"/g' configFile_readHisto_toLaunch_tmp.txt")
    for conf in config:
        os.system("cp configFile_readHisto_toLaunch_tmp.txt configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/label/"+conf[0]+"/g' configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/rebinEta/"+conf[1]+"/g' configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/rebinIh/"+conf[2]+"/g' configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/rebinMom/"+conf[3]+"/g' configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/corrTemplateIh/"+conf[4]+"/g' configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/corrTemplateMom/"+conf[5]+"/g' configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/fitIh/"+conf[6]+"/g' configFile_readHisto_toLaunch.txt")
        os.system("sed -i 's/fitMom/"+conf[7]+"/g' configFile_readHisto_toLaunch.txt")

        os.system("cat configFile_readHisto_toLaunch.txt")
        os.system("time root -l -q -b step2_backgroundPrediction.C")    
    i+=1
'''

# Split the code by lines
lines = code.split('\n')

# Find the index where the configs start
config_start_index = lines.index('config=[')

# Iterate through the configs
for i in range(config_start_index + 1, config_start_index + 14):
    # Uncomment the config line
    lines[i] = lines[i].replace('#', '')

    # Run the modified code
    print('\n'.join(lines))
    exec('\n'.join(lines))
    
    # Comment the config line again for the next iteration
    lines[i] = '#' + lines[i]

