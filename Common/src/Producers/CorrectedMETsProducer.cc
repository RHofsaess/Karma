#include "Karma/Common/interface/Producers/CorrectedMETsProducer.h"

#include "DataFormats/METReco/interface/CorrMETData.h"

// -- constructor
karma::CorrectedMETsProducer::CorrectedMETsProducer(const edm::ParameterSet& config) :
    m_configPSet(config),
    typeICorrectionMinJetPt_(m_configPSet.getParameter<double>("typeICorrectionMinJetPt")),
    typeICorrectionMaxTotalEMFraction_(m_configPSet.getParameter<double>("typeICorrectionMaxTotalEMFraction")),
    typeICorrectionJECReferenceLevel_(m_configPSet.getParameter<std::string>("typeICorrectionJECReferenceLevel")) {

    // -- register products
    produces<karma::METCollection>();

    // -- process configuration

    // -- declare which collections are consumed and create tokens
    karmaEventToken = consumes<karma::Event>(m_configPSet.getParameter<edm::InputTag>("karmaEventSrc"));
    karmaMETCollectionToken = consumes<karma::METCollection>(m_configPSet.getParameter<edm::InputTag>("karmaMETCollectionSrc"));
    karmaCorrectedJetCollectionToken = consumes<karma::JetCollection>(m_configPSet.getParameter<edm::InputTag>("karmaCorrectedJetCollectionSrc"));
}


// -- destructor
karma::CorrectedMETsProducer::~CorrectedMETsProducer() {
}


// -- member functions

void karma::CorrectedMETsProducer::produce(edm::Event& event, const edm::EventSetup& setup) {
    std::unique_ptr<karma::METCollection> outputMETCollection(new karma::METCollection());

    // -- get object collections for event

    // pileup density
    karma::util::getByTokenOrThrow(event, this->karmaEventToken, this->karmaEventHandle);
    // MET collection
    karma::util::getByTokenOrThrow(event, this->karmaMETCollectionToken, this->karmaMETCollectionHandle);
    // jet collection
    karma::util::getByTokenOrThrow(event, this->karmaCorrectedJetCollectionToken, this->karmaCorrectedJetCollectionHandle);

    assert(this->karmaMETCollectionHandle->size() == 1);  // only allow MET collections containing a single MET object

    // calculate Type-I correction (https://twiki.cern.ch/twiki/bin/view/CMS/METType1Type2Formulae#3_The_Type_I_correction)
    CorrMETData metCorrectionTypeI;
    for (const auto& jet : (*this->karmaCorrectedJetCollectionHandle)) {
        // skip jets with corrected pT below configured threshold
        if (jet.p4.Pt() < typeICorrectionMinJetPt_)
            continue;

        // skip jets with total EM fraction below configured threshold
        if ((jet.chargedEMFraction + jet.neutralEMFraction) > typeICorrectionMaxTotalEMFraction_)
            continue;

        // construct Type-I correction from difference in JEC levels
        const karma::LorentzVector& jetJECReferenceLV = jet.transientLVs_.at(typeICorrectionJECReferenceLevel_);
        metCorrectionTypeI.mex   -= (jet.p4.Px() - jetJECReferenceLV.Px());
        metCorrectionTypeI.mey   -= (jet.p4.Py() - jetJECReferenceLV.Py());
        metCorrectionTypeI.sumet -= (jet.p4.Pt() - jetJECReferenceLV.Pt());
    }

    // -- populate outputs

    // copy MET to output
    outputMETCollection->push_back(this->karmaMETCollectionHandle->at(0));
    karma::MET& outputMET = outputMETCollection->back();

    // apply type-I MET correction
    outputMET.p4 = outputMET.getCorrectedP4(metCorrectionTypeI);
    outputMET.sumEt = outputMET.uncorSumEt - metCorrectionTypeI.sumet;

    // move outputs to event tree
    event.put(std::move(outputMETCollection));
}


void karma::CorrectedMETsProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    // The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}


//define this as a plug-in
using KarmaCorrectedMETsProducer = karma::CorrectedMETsProducer;
DEFINE_FWK_MODULE(KarmaCorrectedMETsProducer);
