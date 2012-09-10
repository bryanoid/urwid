import urwid

def exit_on_cr(key):
    if key == 'enter':
        raise urwid.ExitMainLoop()

def on_ask_change(edit, new_edit_text):
    assert edit is ask # we are passed our edit widget
    reply.set_text(('I say',
        u"Nice to meet you, " + new_edit_text))

palette = [('I say', 'default,bold', 'default', 'bold'),]
ask = urwid.Edit(('I say', u"What is your name?\n"))
reply = urwid.Text(u"")
listbox = urwid.ListBox(urwid.SimpleFocusListWalker([ask, reply]))
urwid.connect_signal(ask, 'change', on_ask_change)

loop = urwid.MainLoop(listbox, palette, unhandled_input=exit_on_cr)
loop.run()
