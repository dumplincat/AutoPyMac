import atomac

atomac.launchAppByBundleId('us.zoom.ringcentral')
automator = atomac.getAppRefByBundleId('us.zoom.ringcentral')
window = automator.windows()[0]
print window.AXTitle
all=window.findAll()
print all
all_in_group=all[0].findAll()
sign_in_button=all_in_group[2]
sign_in_button.Press()

