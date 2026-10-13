from kivy.utils import platform


def share_file(path):
    print("[SHARE] Opening share sheet:", path)

    if platform != "ios":
        print("[SHARE] Not running on iOS.")
        return

    from pyobjus import autoclass

    UIApplication = autoclass("UIApplication")
    NSURL = autoclass("NSURL")
    UIActivityViewController = autoclass(
        "UIActivityViewController"
    )

    application = UIApplication.sharedApplication()
    presenter = application.keyWindow.rootViewController()

    # Find the currently visible view controller.
    while presenter.presentedViewController():
        presenter = presenter.presentedViewController()

    file_url = NSURL.fileURLWithPath_(path)

    activity = (
        UIActivityViewController.alloc()
        .initWithActivityItems_applicationActivities_(
            [file_url],
            None,
        )
    )

    # Required for iPad popover presentation.
    popover = activity.popoverPresentationController()

    if popover:
        view = presenter.view()
        popover.setSourceView_(view)
        popover.setSourceRect_(view.bounds())

    presenter.presentViewController_animated_completion_(
        activity,
        True,
        None,
    )

    print("[SHARE] Share sheet presented.")


import os
import shutil

from kivy.app import App
from kivy.utils import platform
from kivy.clock import Clock


if platform == "ios":
    from pyobjus import autoclass, protocol

    UIApplication = autoclass("UIApplication")
    UIDocumentPickerViewController = autoclass(
        "UIDocumentPickerViewController"
    )


    class BackupFilePicker:

        def __init__(self):
            self.picker = None

        def open(self):
            app = UIApplication.sharedApplication()
            presenter = app.keyWindow.rootViewController()

            while presenter.presentedViewController():
                presenter = presenter.presentedViewController()

            # 0 = import mode
            self.picker = (
                UIDocumentPickerViewController.alloc()
                .initWithDocumentTypes_inMode_(
                    ["public.zip-archive"],
                    0,
                )
            )

            self.picker.setDelegate_(self)

            presenter.presentViewController_animated_completion_(
                self.picker,
                True,
                None,
            )
        ###protocol methods
        @protocol("UIDocumentPickerDelegate")
        def documentPicker_didPickDocumentsAtURLs_(self, controller, urls):
            try:
                if urls.count() == 0:
                    return

                url = urls.firstObject()

                path_obj = url.path
                source_path = path_obj.UTF8String()

                print("[IMPORT] Selected source:", source_path)

                app = App.get_running_app()

                import_dir = os.path.join(app.user_data_dir, "imports")
                os.makedirs(import_dir, exist_ok=True)

                destination = os.path.join(
                    import_dir,
                    "selected-backup.zip"
                )

                shutil.copy2(source_path, destination)

                print("[IMPORT] Backup copied to:", destination)

                Clock.schedule_once(
                    lambda dt: app.on_backup_file_picked(destination),
                    0
                )

            except Exception as exc:
                print("[IMPORT] File selection failed:", exc)




        @protocol("UIDocumentPickerDelegate")
        def documentPickerWasCancelled_(self, controller):
            print("[IMPORT] File selection cancelled")


    _backup_picker = BackupFilePicker()


def pick_backup_file():
    if platform != "ios":
        print("[IMPORT] Native Files picker is only available on iOS.")
        return

    _backup_picker.open()