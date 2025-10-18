from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI(title="Betting Ledger Grader", version="1.0.0")

class GradeReq(BaseModel):
    sheet_url: str
    date_from: date | None = None
    date_to: date | None = None
    timezone: str = "Australia/Brisbane"
    overwrite_results: bool = False
    write_back: bool = False

@app.get("/health")
def health():
    return {"ok": True, "service": "ledger-grader"}

@app.post("/grade_from_sheet")
def grade_from_sheet(req: GradeReq):
    # TODO: implement real grading
    return {
        "graded_csv_url": "https://example.com/graded_ledger.csv",
        "summary": {
            "window": {
                "date_from": str(req.date_from),
                "date_to": str(req.date_to),
                "timezone": req.timezone
            }
        },
        "notes": "Stub response. Replace with real grading."
    }
