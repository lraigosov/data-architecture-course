"""Helper para emitir eventos OpenLineage (simplificado).
Requiere: openlineage-python instalado (expone el paquete openlineage.client).

Uso:
from helpers.event_emitter import emit_start, emit_complete
emit_start(job_namespace="curso.mid", job_name="transform_ventas", run_id="abc123", inputs=[{"namespace":"postgres.public","name":"sales_orders"}], outputs=[])
... proceso ...
emit_complete(job_namespace="curso.mid", job_name="transform_ventas", run_id="abc123", inputs=[...], outputs=[{"namespace":"delta.lakehouse","name":"ventas_limpias"}])
"""
from datetime import datetime
try:
    from openlineage.client import OpenLineageClient
    from openlineage.client.run import RunEvent, RunState, Run, Job, Dataset
except ImportError:  # Fallback para entorno sin librería: definir stubs mínimos para evitar NameError
    OpenLineageClient = None
    class _Stub:
        def __init__(self, *args, **kwargs):
            pass
    class RunEvent(_Stub):
        pass
    class RunState:
        START = type("_S", (), {"name": "START"})()
        COMPLETE = type("_S", (), {"name": "COMPLETE"})()
        FAIL = type("_S", (), {"name": "FAIL"})()
    class Run(_Stub):
        def __init__(self, runId: str):
            self.runId = runId
    class Job(_Stub):
        def __init__(self, namespace: str, name: str):
            self.namespace = namespace
            self.name = name
    class Dataset(_Stub):
        def __init__(self, namespace: str, name: str):
            self.namespace = namespace
            self.name = name

CLIENT_URL = "http://localhost:5000"  # Ajustar según despliegue Marquez / DataHub
PRODUCER = "https://github.com/lraigosov/data-architecture-course/tree/main/04-recursos/helpers/event_emitter.py"


def _dataset(obj: dict) -> Dataset:
    return Dataset(namespace=obj["namespace"], name=obj["name"])


def _emit(state: RunState, job_namespace: str, job_name: str, run_id: str, inputs, outputs):
    if OpenLineageClient is None:
        print("[OpenLineage] Librería no disponible, evento no enviado.")
        return
    client = OpenLineageClient(url=CLIENT_URL)
    event = RunEvent(
        eventType=state,
        eventTime=datetime.utcnow().isoformat()+"Z",
        run=Run(runId=run_id),
        job=Job(namespace=job_namespace, name=job_name),
        producer=PRODUCER,
        inputs=[_dataset(d) for d in inputs],
        outputs=[_dataset(d) for d in outputs]
    )
    client.emit(event)
    print(f"[OpenLineage] Emitido {state.name} para {job_name}:{run_id}")


def emit_start(job_namespace: str, job_name: str, run_id: str, inputs, outputs):
    """Emite evento START"""
    _emit(RunState.START, job_namespace, job_name, run_id, inputs, outputs)


def emit_complete(job_namespace: str, job_name: str, run_id: str, inputs, outputs):
    """Emite evento COMPLETE"""
    _emit(RunState.COMPLETE, job_namespace, job_name, run_id, inputs, outputs)


def emit_fail(job_namespace: str, job_name: str, run_id: str, inputs, outputs):
    """Emite evento FAIL"""
    _emit(RunState.FAIL, job_namespace, job_name, run_id, inputs, outputs)
