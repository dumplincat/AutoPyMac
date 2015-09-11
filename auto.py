import atomac

atomac.launchAppByBundleId('us.zoom.ringcentral')
automator = atomac.getAppRefByBundleId('us.zoom.ringcentral')
window = automator.windows()[0]
print window.AXTitle
all=window.findAll()
print all
