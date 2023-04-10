from fastapi import HTTPException, APIRouter
from src.database.disease_prediction import predictDisease
from src.database.filter_user_symptoms import filterUserSymptom
from src.models.symptoms_model import Symptoms
from src.database.disease_descriptor import disease_descriptor
from src.database.disease_treatment import treatment_prediction

router = APIRouter(
    prefix="/api/predict_disease",
    tags=["predict_disease"],
    responses={404: {"description": "Not found"}},
)


@router.post("/getdisease")
def get_disease(data : Symptoms):
    print(type(data.symptoms))
    filtered_symptom = filterUserSymptom(data.symptoms)
    disease = predictDisease(filtered_symptom)
    description = disease_descriptor(disease)
    treatment = treatment_prediction(disease)
    response={"Disease":disease, "Description":description, "Treatment1":treatment[0],"Treatment2":treatment[1],"Treatment3":treatment[2],"Treatment4":treatment[3]}
    return response


