from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess

router = APIRouter(
    prefix="/editor",
    tags=["Editor"]
)

class CodeExec(BaseModel):
    code: str

@router.post("/execute")
def execute_code(data: CodeExec):
    """
    Execute Python code and return stdout/stderr.
    WARNING: This is NOT safe for production with untrusted code!
    """
    try:
        # Run Python code with a timeout of 5 seconds
        result = subprocess.run(
            ["python3", "-c", data.code],
            capture_output=True,
            text=True,
            timeout=5
        )

        return {
            "output": result.stdout.strip(),
            "error": result.stderr.strip()
        }

    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=400, detail="Code execution timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Execution error: {str(e)}")
