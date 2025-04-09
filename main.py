import gi
gi.require_version("GLib", "2.0")
gi.require_version("Gtk", "4.0")
gi.require_version("Gio", "2.0")

import sys
from gi.repository import GLib, Gtk, Gio

class App(Gtk.Application):
  def __init__(self):
    super().__init__(application_id="io.github.akku1139.FastVideoCreator")
    GLib.set_application_name("FastVideoCreator")

    self.connect("startup", self.on_startup)
    self.connect("activate", self.on_activate)


  def on_startup(self, *_args):
    menubar: Gio.MenuModel = Gtk.Builder.new_from_file("./ui/menubar.ui").get_object("menu") # pyright: ignore[reportAssignmentType]
    self.set_menubar(menubar)

  def on_activate(self, *_args):
    window = Gtk.ApplicationWindow(application=self, title="FastVideoCreator")

    window.set_show_menubar(True)

    window.present()

def main():
  app = App()
  exit_status = app.run(sys.argv)
  sys.exit(exit_status)

if __name__ == "__main__":
  main()
