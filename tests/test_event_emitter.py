import event_emitter as ee


def test_emit_functions_exist():
    assert callable(ee.emit_start)
    assert callable(ee.emit_complete)
    assert callable(ee.emit_fail)


def test_emit_without_openlineage_client_does_not_raise(monkeypatch, capsys):
    """Sin openlineage-python instalado, _emit debe degradarse a un print, sin red."""
    monkeypatch.setattr(ee, "OpenLineageClient", None)
    ee.emit_start(
        job_namespace="test.ns",
        job_name="test_job",
        run_id="run-1",
        inputs=[],
        outputs=[],
    )
    out = capsys.readouterr().out
    assert "no disponible" in out.lower()


def test_emit_uses_client_without_real_network(monkeypatch):
    """Con un cliente 'instalado' pero falso, _emit no debe intentar red real."""
    calls = []

    class FakeClient:
        def __init__(self, url):
            calls.append(url)

        def emit(self, event):
            calls.append(event)

    monkeypatch.setattr(ee, "OpenLineageClient", FakeClient)
    ee.emit_complete(
        job_namespace="test.ns",
        job_name="test_job",
        run_id="run-1",
        inputs=[{"namespace": "ns", "name": "in"}],
        outputs=[{"namespace": "ns", "name": "out"}],
    )
    assert calls[0] == ee.CLIENT_URL
    assert len(calls) == 2
