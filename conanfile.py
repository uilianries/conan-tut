import os
from conans import ConanFile, tools


class TutConan(ConanFile):
    name = "tut"
    version = "20161219"
    license = "MIT"
    homepage = "https://github.com/mrzechonek/tut-framework"
    description = "A template based header only unit testing library"
    topics = ("tut", "template", "testing")
    copy_source = False

    @property
    def _source_subfolder(self):
        return os.path.join(self.source_folder, "source_subfolder")

    @property
    def _date(self):
        return self.version[0:4] + "-" + self.version[4:6] + "-" + self.version[6:8]

    def source(self):
        tools.get("{}/archive/{}.tar.gz".format(self.homepage, self._date))
        extracted_folder = self.name + "-framework-" + self._date
        os.rename(extracted_folder, self._source_subfolder)

    def package(self):
        self.copy("LICENSE", dst="licenses", src=self._source_subfolder)
        self.copy("*.h", dst="include", src=os.path.join(self._source_subfolder, "include"))
        self.copy("*.hpp", dst="include", src=os.path.join(self._source_subfolder, "include"))

    def package_id(self):
        self.info.header_only()