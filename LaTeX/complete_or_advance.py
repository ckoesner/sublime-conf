import sublime
import sublime_plugin


# Attempt to trigger an exact completion (such as a snippet) and if no text was
# subsequently inserted, then advance to the next field instead. In order to
# only take precedence once already inside of a snippet, the key binding should
# appear as follows:
#   { "keys": ["tab"], "command": "complete_or_advance", "context":
#     [
#       { "key": "has_next_field", "operator": "equal", "operand": true }
#     ]
#   },


def build_context(view):
  w = 3
  return [view.substr(sublime.Region(r.begin() - w, r.end() + w)) for r in 
    view.sel()]


class CompleteOrAdvanceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    before = build_context(self.view)
    self.view.run_command("insert_best_completion", args = {"exact": True})
    after = build_context(self.view)
    if before == after:
      self.view.run_command("next_field")