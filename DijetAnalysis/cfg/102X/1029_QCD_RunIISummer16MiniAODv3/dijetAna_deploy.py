#!/usr/bin/env python
import os

from Karma.Common.Tools.karmaAnalysisDeployers import KarmaAnalysisDeployerGC


CROSS_SECTION_LOOKUP = {
    #"QCD_Pt_15to30"     : 1820000000 ,
    "QCD_Pt_30to50"     : 138900000  ,
    "QCD_Pt_50to80"     : 19100000   ,
    "QCD_Pt_80to120"    : 2735000    ,
    "QCD_Pt_120to170"   : 467500     ,
    "QCD_Pt_170to300"   : 117400     ,
    "QCD_Pt_300to470"   : 7753       ,
    "QCD_Pt_470to600"   : 642.1      ,
    "QCD_Pt_600to800"   : 185.9      ,
    "QCD_Pt_800to1000"  : 32.05      ,
    "QCD_Pt_1000to1400" : 9.365      ,
    "QCD_Pt_1400to1800" : 0.8398     ,
    "QCD_Pt_1800to2400" : 0.1124     ,
    "QCD_Pt_2400to3200" : 0.006752   ,
    "QCD_Pt_3200toInf"  : 0.0001626  ,
}

NUMBER_OF_EVENTS_LOOKUP = {
    #"QCD_Pt_15to30"     : 39898460   ,
    "QCD_Pt_30to50"     : 9980050    ,
    "QCD_Pt_50to80"     : 9954370    ,
    "QCD_Pt_80to120"    : 6986740    ,
    "QCD_Pt_120to170"   : 6708572    ,
    "QCD_Pt_170to300"   : 6958708    ,
    "QCD_Pt_300to470"   : 4150588    ,
    "QCD_Pt_470to600"   : 3959986    ,
    "QCD_Pt_600to800"   : 3896412    ,
    "QCD_Pt_800to1000"  : 3992112    ,
    "QCD_Pt_1000to1400" : 2999069    ,
    "QCD_Pt_1400to1800" : 396409     ,
    "QCD_Pt_1800to2400" : 397660     ,
    "QCD_Pt_2400to3200" : 399226     ,
    "QCD_Pt_3200toInf"  : 391735     ,
}

if __name__ == "__main__":

    _deployer = KarmaAnalysisDeployerGC(
        nick="DijetAna_QCD_RunIISummer16MiniAODv3_2020-01-23",
        cmsrun_config="dijetAna_cfg.py",
        gc_config_base="{}/src/Karma/DijetAnalysis/cfg/gc/dijetAna_base_gc.conf".format(os.getenv("CMSSW_BASE")),
        work_directory="/portal/ekpbms3/home/{}/work/dijet_ana".format(os.getenv("USER")),
        files_per_job=5,
    )

    _skim_date = "2020-01-09"
    #_deployer.add_input_files("QCD_Pt_15to30",     "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_15to30_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_30to50",     "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_30to50_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_50to80",     "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_50to80_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_80to120",    "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_80to120_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_120to170",   "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_120to170_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_170to300",   "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_170to300_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_300to470",   "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_300to470_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_470to600",   "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_470to600_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_600to800",   "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_600to800_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_800to1000",  "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_800to1000_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_1000to1400", "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_1000to1400_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_1400to1800", "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_1400to1800_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_1800to2400", "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_1800to2400_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_2400to3200", "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_2400to3200_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))
    _deployer.add_input_files("QCD_Pt_3200toInf",  "/storage/gridka-nrg/dsavoiu/Dijet/skims/KarmaSkim_QCD_Pt_3200toInf_RunIISummer16MiniAODv3_{}/*.root".format(_skim_date))

    _deployer.replace_file_prefix('/storage/gridka-nrg/', 'root://cmsxrootd-1.gridka.de:1094//store/user/')

    _deployer.add_constant("GLOBALTAG", "94X_mcRun2_asymptotic_v3")
    _deployer.add_constant("IS_DATA", "False")
    _deployer.add_constant("JEC_VERSION", "Summer16_07Aug2017_V11")
    _deployer.add_constant("JER_VERSION", "Summer16_25nsV1")

    _deployer.add_lookup_parameter("CROSS_SECTION", CROSS_SECTION_LOOKUP, key="DATASETNICK")
    _deployer.add_lookup_parameter("NUMBER_OF_EVENTS", NUMBER_OF_EVENTS_LOOKUP, key="DATASETNICK")

    _deployer.deploy()
