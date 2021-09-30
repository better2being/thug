
import logging

from thug.ActiveX.modules import TextStream

log = logging.getLogger("Thug")


ATTRIBUTES = {
    'Normal'     : 0,      # Normal file. No attributes are set.
    'ReadOnly'   : 1,      # Read-only file. Attribute is read/write.
    'Hidden'     : 2,      # Hidden file. Attribute is read/write.
    'System'     : 4,      # System file. Attribute is read/write.
    'Volume'     : 8,      # Disk drive volume label. Attribute is read-only.
    'Directory'  : 16,     # Folder or directory. Attribute is read-only.
    'Archive'    : 32,     # File has changed since last backup. Attribute is read/write.
    'Alias'      : 1024,   # Link or shortcut. Attribute is read-only.
    'Compressed' : 2048,   # Compressed file. Attribute is read-only.
}


class File:
    def __init__(self, filespec):
        self.Path = filespec
        self._Attributes = ATTRIBUTES['Archive']
        log.ThugLogging.add_behavior_warn(f'[File ActiveX] Path = {self.Path}, Attributes = {self._Attributes}')

    def getAttributes(self):
        return self._Attributes

    def setAttributes(self, key):
        if key.lower() in ('volume', 'directory', 'alias', 'compressed', ):
            return

        self._Attributes = ATTRIBUTES[key]

    Attributes = property(getAttributes, setAttributes)

    @property
    def ShortPath(self):
        _shortPath = []

        for p in self.Path.split('\\'):
            sp = p.split('.')

            if len(sp) == 1:
                spfn = p if len(p) <= 8 else f"{p[:6]}~1"
            else:
                spfn = ".".join(sp[:-1])
                ext  = sp[-1]

                if len(spfn) > 8:
                    spfn = f"{spfn[:6]}~1"

                spfn = f"{spfn}.{ext}"

            _shortPath.append(spfn)

        return "\\\\".join(_shortPath)

    @property
    def ShortName(self):
        spath = self.Path.split('\\')
        name  = spath[-1]
        sp    = name.split('.')

        if len(sp) == 1:
            if len(name) <= 8:
                return name

            return f"{name[:6]}~1"

        spfn = ".".join(sp[:-1])
        ext = sp[-1]

        if len(spfn) > 8:
            spfn = f"{spfn[:6]}~1"

        return f"{spfn}.{ext}"

    @property
    def Drive(self):
        spath = self.Path.split('\\')
        if spath[0].endswith(':'):
            return spath[0]

        return 'C:'

    def Copy(self, destination, overwrite = True):
        log.ThugLogging.add_behavior_warn(f'[File ActiveX] Copy({destination}, {overwrite})')

    def Move(self, destination):
        log.ThugLogging.add_behavior_warn(f'[File ActiveX] Move({destination})')

    def Delete(self, force = False):
        log.ThugLogging.add_behavior_warn(f'[File ActiveX] Delete({force})')

    def OpenAsTextStream(self, iomode = 'ForReading', _format = 0):
        log.ThugLogging.add_behavior_warn(f'[File ActiveX] OpenAsTextStream({iomode}, {_format})')
        stream = TextStream.TextStream()
        stream._filename = self.Path  # pylint:disable=undefined-variable
        return stream
