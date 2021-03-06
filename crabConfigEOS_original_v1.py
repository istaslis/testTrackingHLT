from WMCore.Configuration import Configuration
config = Configuration()
config.section_("General")
config.General.requestName   = 'HeavyFlavourHLT_MVA_45_original_v1'
config.General.transferLogs = True
config.section_("JobType")
config.JobType.pluginName  = 'Analysis'
config.JobType.inputFiles = ['rssLimit']
config.JobType.psetName    = 'hlt_MC_stage1_HFmenu_original.py'
config.General.requestName = 'HeavyFlavourHLT_MVA_45_original_v1'

config.General.workArea = 'crab_projectsEOS'
config.section_("Data")
config.Data.inputDataset = '/Pyquen_D0tokaonpion_D0pt15p0_Pthat15_TuneZ2_Unquenched_5020GeV_GENSIM_75x_v2/mnguyen-D0pthat15-RECO_v2-2fbe1a61b2b7a96a0ed51c8b458e4279/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase= '/store/group/phys_heavyions/ginnocen/HeavyFlavourHLT_MVA_45_original_v1'
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'

