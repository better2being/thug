import os
import logging

from thug.ThugAPI.ThugAPI import ThugAPI

log = logging.getLogger("Thug")


class TestMiscSamplesIE(object):
    thug_path = os.path.dirname(os.path.realpath(__file__)).split("thug")[0]
    misc_path = os.path.join(thug_path, "thug", "samples/misc")

    def do_perform_test(self, caplog, sample, expected):
        thug = ThugAPI()

        thug.set_useragent('winxpie70')
        thug.set_events('click')
        thug.disable_cert_logging()
        thug.set_features_logging()
        thug.log_init(sample)
        thug.run_local(sample)

        records = [r.message for r in caplog.records]

        matches = 0

        for e in expected:
            for record in records:
                if e in record:
                    matches += 1

        assert matches >= len(expected)

    def test_plugindetect1(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.6.html")
        expected = ['AdobeReader version: 9.1.0.0',
                    'Flash version: 10.0.64.0']

        self.do_perform_test(caplog, sample, expected)

    def test_plugindetect2(self, caplog):
        sample   = os.path.join(self.misc_path, "PluginDetect-0.7.8.html")
        expected = ['AdobeReader version: 9,1,0,0',
                    'Flash version: 10,0,64,0',
                    'Java version: 1,6,0,32',
                    'ActiveXObject: javawebstart.isinstalled.1.6.0.0',
                    'ActiveXObject: javaplugin.160_32']

        self.do_perform_test(caplog, sample, expected)

    def test_test1(self, caplog):
        sample   = os.path.join(self.misc_path, "test1.html")
        expected = ['[Window] Alert Text: one']
        self.do_perform_test(caplog, sample, expected)

    def test_test2(self, caplog):
        sample   = os.path.join(self.misc_path, "test2.html")
        expected = ['[Window] Alert Text: Java enabled: true']
        self.do_perform_test(caplog, sample, expected)

    def test_test3(self, caplog):
        sample   = os.path.join(self.misc_path, "test3.html")
        expected = ['[Window] Alert Text: foo']
        self.do_perform_test(caplog, sample, expected)

    def test_testAppendChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testAppendChild.html")
        expected = ['Don\'t care about me',
                    'Just a sample',
                    'Attempt to append a null element failed',
                    'Attempt to append an invalid element failed',
                    'Attempt to append a text element failed',
                    'Attempt to append a read-only element failed']

        self.do_perform_test(caplog, sample, expected)

    def test_testClipboardData(self, caplog):
        sample   = os.path.join(self.misc_path, "testClipboardData.html")
        expected = ['Test ClipboardData']
        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode.html")
        expected = ['<div id="cloned"><q>Can you copy <em>everything</em> I say?</q></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testCloneNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testCloneNode2.html")
        expected = ['[Window] Alert Text: [object HTMLButtonElement]',
                    '[Window] Alert Text: Clone node',
                    '[Window] Alert Text: None',
                    '[Window] Alert Text: [object Attr]',
                    '[Window] Alert Text: True']

        self.do_perform_test(caplog, sample, expected)

    def test_testCreateStyleSheet(self, caplog):
        sample   = os.path.join(self.misc_path, "testCreateStyleSheet.html")
        expected = ['[Window] Alert Text: style1.css',
                    '[Window] Alert Text: style2.css',
                    '[Window] Alert Text: style3.css',
                    '[Window] Alert Text: style4.css']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentAll(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentAll.html")
        expected = ["http://www.google.com"]
        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentWrite1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentWrite1.html")
        expected = ['Foobar',
                    "Google</a><script>alert('foobar');</script><script language=\"VBScript\">alert('Gnam');</script><script>alert('Aieeeeee');</script></body>"]
        self.do_perform_test(caplog, sample, expected)

    def test_testInnerHTML(self, caplog):
        sample   = os.path.join(self.misc_path, "testInnerHTML.html")
        expected = ['dude', 'Fred Flinstone']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertBefore(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertBefore.html")
        expected = ["<div>Just a sample</div><div>I'm your reference!</div></body></html>",
                    "[ERROR] Attempting to insert null element",
                    "[ERROR] Attempting to insert an invalid element",
                    "[ERROR] Attempting to insert using an invalid reference element",
                    "[ERROR] Attempting to insert a text node using an invalid reference element"]

        self.do_perform_test(caplog, sample, expected)

    def test_testPlugins(self, caplog):
        sample   = os.path.join(self.misc_path, "testPlugins.html")
        expected = ["Shockwave Flash 10.0.64.0",
                    "Windows Media Player 7",
                    "Adobe Acrobat"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation1(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation1.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation2(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation2.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation3(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation3.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation4(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation4.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation5(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation5.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testLocation6(self, caplog):
        sample   = os.path.join(self.misc_path, "testLocation6.html")
        expected = ["[HREF Redirection (document.location)]",
                    "Content-Location: about:blank --> Location: https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleEdge(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleEdge.html")
        expected = ["[Window] Alert Text: 7"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleEmulateIE(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleEmulateIE.html")
        expected = ["[Window] Alert Text: 7"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMetaXUACompatibleIE(self, caplog):
        sample   = os.path.join(self.misc_path, "testMetaXUACompatibleIE.html")
        expected = ["[Window] Alert Text: 7"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode.html")
        expected = ["thelink",
                    "thediv"]
        self.do_perform_test(caplog, sample, expected)

    def test_testNode2(self, caplog):
        sample   = os.path.join(self.misc_path, "testNode2.html")
        expected = ["thelink",
                    "thediv2"]
        self.do_perform_test(caplog, sample, expected)

    def test_testScope(self, caplog):
        sample   = os.path.join(self.misc_path, "testScope.html")
        expected = ["foobar",
                    "foo",
                    "bar",
                    "True",
                    "3",
                    "2012-10-07 11:13:00",
                    "3.14159265359",
                    "/foo/i"]
        self.do_perform_test(caplog, sample, expected)

    def test_testSetInterval(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetInterval.html")
        expected = ["[Window] Alert Text: Hello"]
        self.do_perform_test(caplog, sample, expected)

    def test_testText(self, caplog):
        sample   = os.path.join(self.misc_path, "testText.html")
        expected = ['<p id="p1">First line of paragraph.<br/> Some text added dynamically. </p>']
        self.do_perform_test(caplog, sample, expected)

    def test_testWindowOnload(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindowOnload.html")
        expected = ["[Window] Alert Text: Fired"]
        self.do_perform_test(caplog, sample, expected)

    def test_test_click(self, caplog):
        sample   = os.path.join(self.misc_path, "test_click.html")
        expected = ["[window open redirection] about:blank -> https://buffer.github.io/thug/"]
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML1(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML1.html")
        expected = ['<div id="five">five</div><div id="one">one</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML2(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML2.html")
        expected = ['<div id="two"><div id="six">six</div>two</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML3(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML3.html")
        expected = ['<div id="three">three<div id="seven">seven</div></div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testInsertAdjacentHTML4(self, caplog):
        sample   = os.path.join(self.misc_path, "testInsertAdjacentHTML4.html")
        expected = ['<div id="four">four</div><div id="eight">eight</div>']
        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent1(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent1.html")
        expected = ["[Window] Alert Text: Request completed"]
        self.do_perform_test(caplog, sample, expected)

    def test_testMicrosoftXMLHTTPEvent2(self, caplog):
        sample   = os.path.join(self.misc_path, "testMicrosoftXMLHTTPEvent2.html")
        expected = ["[Window] Alert Text: Request completed"]
        self.do_perform_test(caplog, sample, expected)

    def test_testCurrentScript(self, caplog):
        sample   = os.path.join(self.misc_path, "testCurrentScript.html")
        expected = ["[Window] Alert Text: This page has scripts",
                    "[Window] Alert Text: text/javascript",
                    "[Window] Alert Text: Just a useless script"]
        self.do_perform_test(caplog, sample, expected)

    def test_testCCInterpreter(self, caplog):
        sample   = os.path.join(self.misc_path, "testCCInterpreter.html")
        expected = ['JavaScript version: 5.7',
                    'Running on the 32-bit version of Windows']
        self.do_perform_test(caplog, sample, expected)

    def test_testTextNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testTextNode.html")
        expected = ['nodeName: #text',
                    'nodeType: 3',
                    'Object: [object Text]',
                    'nodeValue: Hello World',
                    'Length: 11',
                    'Substring(2,5): llo W',
                    'New nodeValue (replace): HelloAWorld',
                    'New nodeValue (delete 1): HelloWorld',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): Hello',
                    'New nodeValue (append): Hello Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): Hello New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testCommentNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testCommentNode.html")
        expected = ['nodeName: #comment',
                    'nodeType: 8',
                    'Object: [object Comment]',
                    'nodeValue: <!--Hello World-->',
                    'Length: 18',
                    'Substring(2,5): --Hel',
                    'New nodeValue (replace): <!--HAllo World-->',
                    'New nodeValue (delete 1): <!--Hllo World-->',
                    'Index error (delete 2)',
                    'New nodeValue (delete 3): <!--H',
                    'New nodeValue (append): <!--H Test',
                    'Index error (insert 1)',
                    'New nodeValue (insert 2): <!--H New Test',
                    'New nodeValue (reset): Reset']

        self.do_perform_test(caplog, sample, expected)

    def test_testDOMImplementation(self, caplog):
        sample   = os.path.join(self.misc_path, "testDOMImplementation.html")
        expected = ["hasFeature('core'): true", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testAttrNode(self, caplog):
        sample   = os.path.join(self.misc_path, "testAttrNode.html")
        expected = ['Object: [object Attr]',
                    'nodeName: test',
                    'nodeType: 2',
                    'nodeValue: foo',
                    'Length: undefined',
                    'New nodeValue: test2',
                    'Parent: null',
                    'Owner: null',
                    'Name: test',
                    'Specified: true',
                    'childNodes length: 0']

        self.do_perform_test(caplog, sample, expected)

    def test_testReplaceChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testReplaceChild.html")
        expected = ['firstChild: Old child',
                    'lastChild: Old child',
                    'innerText: Old child',
                    '[ERROR] Attempting to replace with a null element',
                    '[ERROR] Attempting to replace a null element',
                    '[ERROR] Attempting to replace with an invalid element',
                    '[ERROR] Attempting to replace an invalid element',
                    '[ERROR] Attempting to replace on a read-only element failed',
                    'Alert Text: New child',
                    '<div id="foobar"><!--Just a comment--></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testCookie(self, caplog):
        sample   = os.path.join(self.misc_path, "testCookie.html")
        expected = ["Alert Text: favorite_food=tripe; name=oeschger", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment1(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment1.html")
        expected = ["<div><p>Test</p></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentFragment2(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentFragment2.html")
        expected = ["<div id=\"foobar\"><b>This is B</b></div>", ]

        self.do_perform_test(caplog, sample, expected)

    def test_testClassList1(self, caplog):
        sample   = os.path.join(self.misc_path, "testClassList1.html")
        expected = ['[Initial value] <div class="foo"></div>',
                    '[After remove and add] <div class="anotherclass"></div>',
                    '[Item] anotherclass',
                    '[Empty item] null',
                    '[Toggle visible] true',
                    '[After toggle] <div class="anotherclass"></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testClassList4(self, caplog):
        sample   = os.path.join(self.misc_path, "testClassList4.html")
        expected = ['[After remove and add] <div class="anotherclass"></div>', ]

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentType(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentType.html")
        expected = ['Doctype: [object DocumentType]',
                    'Doctype name: html',
                    'Doctype nodeName: html',
                    'Doctype nodeType: 10',
                    'Doctype nodeValue: null',
                    'Doctype publicId: ',
                    'Doctype systemId: ',
                    'Doctype textContent: null']

        self.do_perform_test(caplog, sample, expected)

    def test_testRemoveChild(self, caplog):
        sample   = os.path.join(self.misc_path, "testRemoveChild.html")
        expected = ['<div>Don\'t care about me</div>',
                    '[ERROR] Attempting to remove null element',
                    '[ERROR] Attempting to remove an invalid element',
                    '[ERROR] Attempting to remove a read-only element',
                    '[ERROR] Attempting to remove an element not in the tree',
                    '[ERROR] Attempting to remove from a read-only element']

        self.do_perform_test(caplog, sample, expected)

    def test_testNamedNodeMap(self, caplog):
        sample   = os.path.join(self.misc_path, "testNamedNodeMap.html")
        expected = ['hasAttributes (before removal): true',
                    'hasAttribute(\'id\'): true',
                    'First test: id->p1',
                    'Second test: id->p1',
                    'Third test: id->p1',
                    'Fourth test: id->p1',
                    'Fifth test failed',
                    'Not existing: null',
                    'hasAttributes (after removal): false',
                    'Sixth test: foo->bar',
                    'Seventh test: foo->bar2',
                    'Final attributes length: 1']

        self.do_perform_test(caplog, sample, expected)

    def test_testEntityReference(self, caplog):
        sample   = os.path.join(self.misc_path, "testEntityReference.html")
        expected = ['node: [object EntityReference]',
                    'name: &',
                    'nodeName: &',
                    'nodeType: 5',
                    'nodeValue: null']

        self.do_perform_test(caplog, sample, expected)

    def test_getElementsByTagName(self, caplog):
        sample   = os.path.join(self.misc_path, "testGetElementsByTagName.html")
        expected = ['[object HTMLHtmlElement]',
                    '[object HTMLHeadElement]',
                    '[object HTMLBodyElement]',
                    '[object HTMLParagraphElement]',
                    '[object HTMLScriptElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_createElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testCreateElement.html")
        expected = ['[object HTMLParagraphElement]']

        self.do_perform_test(caplog, sample, expected)

    def test_testDocumentElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testDocumentElement.html")
        expected = ['<a href="http://www.google.com">Google</a>']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute1(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute1.html")
        expected = ['Attribute: bar',
                    'Attribute (after removal): null']

        self.do_perform_test(caplog, sample, expected)

    def test_testSetAttribute3(self, caplog):
        sample   = os.path.join(self.misc_path, "testSetAttribute3.html")
        expected = ['Alert Text: foo',
                    'Alert Text: bar',
                    'Alert Text: test',
                    'Alert Text: foobar']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLCollection(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLCollection.html")
        expected = ['<div id="odiv1">Page one</div>',
                    '<div name="odiv2">Page two</div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testApplyElement(self, caplog):
        sample   = os.path.join(self.misc_path, "testApplyElement.html")
        expected = ['<div id="outer"><div id="test"><div>Just a sample</div></div></div>',
                    '<div id="outer"><div>Just a div<div id="test"><div>Just a sample</div></div></div></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testWindow(self, caplog):
        sample   = os.path.join(self.misc_path, "testWindow.html")
        expected = ['window: [object Window]',
                    'self: [object Window]',
                    'top: [object Window]',
                    'length: 0',
                    'history: [object History]',
                    'pageXOffset: 0',
                    'pageYOffset: 0',
                    'screen: [object Screen]',
                    'screenLeft: 0',
                    'screenX: 0',
                    'confirm: true']

        self.do_perform_test(caplog, sample, expected)

    def test_testObject1(self, caplog):
        sample   = os.path.join(self.misc_path, "testObject1.html")
        expected = ['[object data redirection] about:blank -> https://github.com/buffer/thug/raw/master/tests/test_files/sample.swf']

        self.do_perform_test(caplog, sample, expected)

    def test_testReplaceChild2(self, caplog):
        sample   = os.path.join(self.misc_path, "testReplaceChild2.html")
        expected = ['<div id="foobar"><div id="test"></div></div>']

        self.do_perform_test(caplog, sample, expected)

    def test_testNavigator(self, caplog):
        sample   = os.path.join(self.misc_path, "testNavigator.html")
        expected = ['window: [object Window]',
                    'appCodeName: Mozilla',
                    'appName: Microsoft Internet Explorer',
                    'appVersion: 4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
                    'cookieEnabled: true',
                    'onLine: true',
                    'platform: Win32']

        self.do_perform_test(caplog, sample, expected)

    def test_testAdodbStream(self, caplog):
        sample   = os.path.join(self.misc_path, "testAdodbStream.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Adodb.Stream)',
                    '[Window] Alert Text: Stream content: Test',
                    '[Window] Alert Text: Stream content (first 2 chars): Te',
                    '[Window] Alert Text: Stream size: 4',
                    '[Adodb.Stream ActiveX] SaveToFile(test.txt, 2)',
                    '[Adodb.Stream ActiveX] LoadFromFile(test1234.txt)',
                    '[Window] Alert Text: Attempting to load from a not existing file',
                    '[Adodb.Stream ActiveX] LoadFromFile(test.txt)',
                    '[Window] Alert Text: ReadText: Test',
                    '[Window] Alert Text: ReadText(3): Tes',
                    '[Window] Alert Text: ReadText(10): Test',
                    '[Adodb.Stream ActiveX] Changed position in fileobject to: (2)',
                    '[Window] Alert Text: stTest2',
                    '[Adodb.Stream ActiveX] Close']

        self.do_perform_test(caplog, sample, expected)

    def test_testScriptingFileSystemObject(self, caplog):
        sample   = os.path.join(self.misc_path, "testScriptingFileSystemObject.html")
        expected = ['[Microsoft MDAC RDS.Dataspace ActiveX] CreateObject (Scripting.FileSystemObject)',
                    '[Script.FileSystemObject ActiveX] Returning C:\\WINDOWS for GetSpecialFolder("0")',
                    '[Script.FileSystemObject ActiveX] Returning C:\\WINDOWS\\system32 for GetSpecialFolder("1")',
                    '[WScript.Shell ActiveX] Expanding environment string "%TEMP%"',
                    '[Window] Alert Text: FolderExists(\'C:\\Windows\\System32\'): true',
                    '[Window] Alert Text: FileExists(\'\'): true',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\drivers\\etc\\hosts\'): true',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\test.txt\'): true',
                    '[Window] Alert Text: GetExtensionName("C:\\Windows\\System32\\test.txt"): .txt',
                    '[Window] Alert Text: FileExists(\'C:\\Windows\\System32\\test.txt\'): true',
                    '[Window] Alert Text: [After CopyFile] FileExists(\'C:\\Windows\\System32\\test2.txt\'): true',
                    '[Window] Alert Text: [After MoveFile] FileExists(\'C:\\Windows\\System32\\test2.txt\'): false',
                    '[Window] Alert Text: [After MoveFile] FileExists(\'C:\\Windows\\System32\\test3.txt\'): true']

        self.do_perform_test(caplog, sample, expected)

    def test_testHTMLOptionsCollection(self, caplog):
        sample   = os.path.join(self.misc_path, "testHTMLOptionsCollection.html")
        expected = ['length: 4',
                    'item(0): Volvo',
                    'namedItem(\'audi\'): Audi',
                    'namedItem(\'mercedes\').value: mercedes',
                    '[After remove] item(0): Saab',
                    '[After first add] length: 4',
                    '[After first add] item(3): foobar',
                    '[After second add] length: 5',
                    '[After second add] item(3): test1234',
                    'Not found error']

        self.do_perform_test(caplog, sample, expected)
