from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.transferLogs    = True
config.General.transferOutputs = True

config.section_("JobType")
config.JobType.pluginName  = 'Analysis'

config.section_("Data")
config.Data.publication  = False
#################################################################
# ALLOWS NON VALID DATASETS
config.Data.allowNonValidInputDataset = True

config.section_("Site")
# Where the output files will be transmitted to
#config.Site.storageSite = 'T2_CH_CERN'
config.Site.storageSite = 'T3_KR_KISTI'

#config.Data.splitting = 'LumiBased'
config.Data.splitting = 'Automatic'

## Something that can be changed frequently
import os
config.Data.inputDataset = "/PADoubleMuon/PARun2016C-PromptReco-v1/AOD"

config.JobType.psetName    = 'tp_from_aod_Data.py'

username = os.environ['USER']

##config.Data.lumiMask = '../data/LumiJSON/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_MuonPhys.txt'

#submitdate = dt.now().strftime('%Y%m%d')+'_1'
submitdate = '201808DY_1'
config.Data.outLFNDirBase = '/store/user/%s/DYTNP/%s' % (username, submitdate)
config.General.requestName = "DYTNP"

#config.Data.runRange = '318877'
#config.Data.lumiMask = 'notFinishedLumis.json'

