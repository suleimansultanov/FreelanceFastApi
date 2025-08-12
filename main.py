from fastapi import FastAPI
from controllers import auth, tasks, messages
# import os
# if os.getenv("DEBUG", "false").lower() == "true":
#     import debugpy
#     debugpy.listen(("0.0.0.0", 5678))
#     print("✅ Waiting for debugger...")
#     debugpy.wait_for_client()


app = FastAPI()

app.include_router(tasks.router, prefix="/tasks")
app.include_router(messages.router, prefix="/messages")
app.include_router(auth.router, prefix="/auth")
