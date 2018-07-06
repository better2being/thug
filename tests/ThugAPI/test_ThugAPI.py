import os
import shutil
import logging

import yara
import pytest

from thug.ThugAPI.ThugAPI import ThugAPI

log = logging.getLogger("Thug")


class TestThugAPI:
    thug_api = ThugAPI()
    # thug_api()
    url = "../log-dir-example"

    def test_version(self):
        with pytest.raises(SystemExit):  # TODO: Needs assert statement by mocking print
            self.thug_api.version()

    def test_useragent(self):
        assert self.thug_api.get_useragent() in ('winxpie60', )

        self.thug_api.set_useragent('winxpchrome20')
        assert self.thug_api.get_useragent() in ('winxpchrome20', )

    def test_events(self):
        assert self.thug_api.get_events() in ([], )

        self.thug_api.set_events('event1,event2,event2,event3')
        assert self.thug_api.get_events() in (['event1', 'event2', 'event3'], )

    def test_delay(self):
        assert self.thug_api.get_delay() in (0,)

        self.thug_api.set_delay(10)
        assert self.thug_api.get_delay() in (10,)

    def test_attachment(self):
        assert not self.thug_api.get_attachment()

        self.thug_api.set_attachment()
        assert self.thug_api.get_attachment()

    def test_file_logging(self):
        assert not self.thug_api.get_file_logging()

        self.thug_api.set_file_logging()
        assert self.thug_api.get_file_logging()

    def test_json_logging(self):
        assert not self.thug_api.get_json_logging()

        self.thug_api.set_json_logging()
        assert self.thug_api.get_json_logging()

    def test_maec_logging(self):
        assert not self.thug_api.get_maec11_logging()

        self.thug_api.set_maec11_logging()
        assert self.thug_api.get_maec11_logging()

    def test_elasticsearch_logging(self):  # TODO: Check for logging.level?
        assert not self.thug_api.get_elasticsearch_logging()

        self.thug_api.set_elasticsearch_logging()
        assert self.thug_api.get_elasticsearch_logging()

    def test_referer(self):
        assert self.thug_api.get_referer() in ('about:blank', )

        self.thug_api.set_referer('https://www.example.com')
        assert self.thug_api.get_referer() in ('https://www.example.com', )

    def test_proxy(self):
        assert self.thug_api.get_proxy() is None

        self.thug_api.set_proxy('http://www.example.com')
        assert self.thug_api.get_proxy() in ('http://www.example.com', )

    def test_raise_for_proxy(self):
        assert self.thug_api.get_raise_for_proxy()

        self.thug_api.set_raise_for_proxy(False)
        assert not self.thug_api.get_raise_for_proxy()

    def test_no_fetch(self):
        assert not log.ThugOpts.no_fetch

        self.thug_api.set_no_fetch()
        assert log.ThugOpts.no_fetch

    def test_verbose(self):  # TODO: Check for logging.level
        assert not log.ThugOpts.verbose

        self.thug_api.set_verbose()
        assert log.ThugOpts.verbose

    def test_debug(self):  # TODO: Check for logging.level
        assert not log.ThugOpts.debug

        self.thug_api.set_debug()
        assert log.ThugOpts.debug

    def test_ast_debug(self):
        assert not log.ThugOpts.ast_debug

        self.thug_api.set_ast_debug()
        assert log.ThugOpts.ast_debug

    def test_http_debug(self):
        assert log.ThugOpts.http_debug in (0, )

        self.thug_api.set_http_debug()
        assert log.ThugOpts.http_debug in (1, )

        self.thug_api.set_http_debug()
        assert log.ThugOpts.http_debug in (2, )

    def test_acropdf_pdf(self):
        assert log.ThugVulnModules.acropdf_pdf in ('9.1.0', )

        self.thug_api.set_acropdf_pdf('1.0.0', )
        assert log.ThugVulnModules.acropdf_pdf in ('1.0.0',)

    def test_disable_acropdf(self):
        assert not log.ThugVulnModules.acropdf_disabled

        self.thug_api.disable_acropdf()
        assert log.ThugVulnModules.acropdf_disabled

    def test_shockwave_flash(self):
        assert log.ThugVulnModules.shockwave_flash in ('10.0.64.0', )

        self.thug_api.set_shockwave_flash('8.0', )
        assert log.ThugVulnModules.shockwave_flash in ('8.0',)

    def test_disable_shockwave_flash(self):
        assert not log.ThugVulnModules.shockwave_flash_disabled

        self.thug_api.disable_shockwave_flash()
        assert log.ThugVulnModules.shockwave_flash_disabled

    def test_javaplugin(self):
        assert log.ThugVulnModules.javaplugin in ('160_32', )

        self.thug_api.set_javaplugin('1.0', )
        assert log.ThugVulnModules.javaplugin in ('100_00',)

    def test_disable_javaplugin(self):
        assert not log.ThugVulnModules.javaplugin_disabled

        self.thug_api.disable_javaplugin()
        assert log.ThugVulnModules.javaplugin_disabled

    def test_silverlight(self):
        assert log.ThugVulnModules.silverlight in ('4.0.50826.0', )

        self.thug_api.set_silverlight('1.0', )
        assert log.ThugVulnModules.silverlight in ('1.0',)

    def test_disable_silverlight(self):
        assert not log.ThugVulnModules.silverlight_disabled

        self.thug_api.disable_silverlight()
        assert log.ThugVulnModules.silverlight_disabled

    def test_threshold(self):
        assert self.thug_api.get_threshold() in (0, )

        self.thug_api.set_threshold(5)
        assert self.thug_api.get_threshold() in (5, )

    def test_extensive(self):
        assert not self.thug_api.get_extensive()

        self.thug_api.set_extensive()
        assert self.thug_api.get_extensive()

    def test_timeout(self):
        assert self.thug_api.get_timeout() in (600, )

        self.thug_api.set_timeout(300)
        assert self.thug_api.get_timeout() in (300, )

    def test_connect_timeout(self):
        assert self.thug_api.get_connect_timeout() in (10, )

        self.thug_api.set_connect_timeout(20)
        assert self.thug_api.get_connect_timeout() in (20, )

    def test_broken_url(self):
        assert not self.thug_api.get_broken_url()

        self.thug_api.set_broken_url()
        assert self.thug_api.get_broken_url()

    def test_web_tracking(self):
        assert not self.thug_api.get_web_tracking()

        self.thug_api.set_web_tracking()
        assert self.thug_api.get_web_tracking()

    def test_honeyagent(self):
        assert log.ThugOpts.honeyagent

        self.thug_api.disable_honeyagent()
        assert not log.ThugOpts.honeyagent

    def test_code_logging(self):
        self.thug_api.enable_code_logging()
        assert log.ThugOpts.code_logging

        self.thug_api.disable_code_logging()
        assert not log.ThugOpts.code_logging

    def test_cert_logging(self):
        self.thug_api.enable_cert_logging()
        assert log.ThugOpts.cert_logging

        self.thug_api.disable_cert_logging()
        assert not log.ThugOpts.cert_logging

    def test_log_init(self):
        log.ThugOpts.file_logging = True
        url = "../thugapi-example"
        self.thug_api.log_init(url)

        base_dir = log.ThugLogging.baseDir
        log_path = os.path.dirname(os.path.dirname(base_dir))  # TODO: Make this neat
        assert os.path.isdir(base_dir)

        shutil.rmtree(log_path)
        assert not os.path.isdir(base_dir)

    def test_log_dir(self):
        self.url = "../log-dir-example"
        self.thug_api.set_log_dir(self.url)
        assert os.path.isdir(self.url)

        shutil.rmtree(self.url)
        assert not os.path.isdir(self.url)

    def test_log_output(self):
        file = "test-filehandler"
        self.thug_api.set_log_output(file)
        assert isinstance(log.handlers[0], logging.FileHandler)
        assert os.path.isfile(file)

        os.remove(file)
        assert not os.path.isfile(file)

    def test_log_quiet(self):
        pass

    def test_vt_query(self):
        assert not log.ThugOpts.vt_query

        self.thug_api.set_vt_query()
        assert log.ThugOpts.vt_query

    def test_vt_submit(self):
        assert not log.ThugOpts.vt_submit

        self.thug_api.set_vt_submit()
        assert log.ThugOpts.vt_submit

    def test_vt_runtime_apikey(self):
        assert self.thug_api.get_vt_runtime_apikey() is None

        self.thug_api.set_vt_runtime_apikey('sample-key')
        assert self.thug_api.get_vt_runtime_apikey() in ('sample-key', )

    def test_mongodb_address(self):
        assert self.thug_api.get_mongodb_address() is None

        self.thug_api.set_mongodb_address('127.0.0.1:27017')
        assert self.thug_api.get_mongodb_address() in ('127.0.0.1:27017', )

    def test_add_htmlclassifier(self):
        self.thug_api.add_htmlclassifier("test_yara")
        rules = log.HTMLClassifier._rules
        assert rules['namespace1'] in ("test_yara", )

    def test_add_urlclassifier(self):
        self.thug_api.add_urlclassifier("test_yara")
        rules = log.URLClassifier._rules
        assert rules['namespace1'] in ("test_yara", )

    def test_add_jsclassifier(self):
        self.thug_api.add_jsclassifier("test_yara")
        rules = log.JSClassifier._rules
        assert rules['namespace1'] in ("test_yara", )

    def test_add_vbsclassifier(self):
        self.thug_api.add_vbsclassifier("test_yara")
        rules = log.VBSClassifier._rules
        assert rules['namespace1'] in ("test_yara", )

    def test_add_textclassifier(self):
        self.thug_api.add_textclassifier("test_yara")
        rules = log.TextClassifier._rules
        assert rules['namespace1'] in ("test_yara", )

    def test_add_sampleclassifier(self):
        self.thug_api.add_sampleclassifier("test_yara")
        rules = log.SampleClassifier._rules
        assert rules['namespace1'] in ("test_yara", )

    def test_add_htmlfilter(self):
        self.thug_api.add_htmlfilter("test_yara")
        filters = log.HTMLClassifier._filters
        assert filters['namespace1'] in ("test_yara", )

    def test_add_urlfilter(self):
        self.thug_api.add_urlfilter("test_yara")
        filters = log.URLClassifier._filters
        assert filters['namespace1'] in ("test_yara", )

    def test_add_jsfilter(self):
        self.thug_api.add_jsfilter("test_yara")
        filters = log.JSClassifier._filters
        assert filters['namespace1'] in ("test_yara", )

    def test_add_vbsfilter(self):
        self.thug_api.add_vbsfilter("test_yara")
        filters = log.VBSClassifier._filters
        assert filters['namespace1'] in ("test_yara", )

    def test_add_textfilter(self):
        self.thug_api.add_textfilter("test_yara")
        filters = log.TextClassifier._filters
        assert filters['namespace1'] in ("test_yara", )

    def test_add_samplefilter(self):
        self.thug_api.add_samplefilter("test_yara")
        filters = log.SampleClassifier._filters
        assert filters['namespace1'] in ("test_yara", )

    def test_log_event(self, caplog):
        caplog.clear()
        log.ThugOpts.file_logging = True

        self.thug_api.log_event()
        assert 'Thug analysis logs saved' in caplog.text
        assert os.path.isdir(self.url)

        shutil.rmtree(self.url)
        assert not os.path.isdir(self.url)

    def test_run_local(self):
        pass
        # self.thug_api.run_local("https://www.example.com")

    def test_analyse(self):
        with pytest.raises(NotImplementedError) as exc:
            self.thug_api.analyze()
        assert "method analyze is abstract" in exc.value

