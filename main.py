import gi
gi.require_version("GLib", "2.0")
gi.require_version("Gtk", "4.0")

import sys
from gi.repository import GLib, Gtk

class MyApplication(Gtk.Application):
  def __init__(self):
    super().__init__(application_id="io.github.akku1139.FastVideoCreator")
    GLib.set_application_name("FastVideoCreator")
    self.connect("activate", self.on_activate)

  def on_activate(self, *_args):
    window = Gtk.ApplicationWindow(application=self, title="FastVideoCreator")
    window.present()

def main():
  app = MyApplication()
  exit_status = app.run(sys.argv)
  sys.exit(exit_status)

if __name__ == "__main__":
  main()
