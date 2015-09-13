import atomac
import time

atomac.launchAppByBundleId('us.zoom.ringcentral')
time.sleep(1)
automator = atomac.getAppRefByBundleId('us.zoom.ringcentral')
window = automator.windows()[0]
print window.AXTitle
all=window.findAll()
all_in_group=all[0].findAll()
sign_in_button=all_in_group[2]
sign_in_button.Press()
time.sleep(10)
window = automator.windows()[0]
all=window.findAll()
print len(all)
#all[3].Press() #3 is close
#all[4].Press() #4 is max
#all[5].Press() #5 is min
web_area=all[0].findAll()[0]
web_all=web_area.findAll()
for i in range(len(web_all)):
    group_all=web_all[i].findAll()
    for j in range(0,len(group_all)):
        print '=================='+str(j)+'================'
        print group_all[j]
        print group_all[j].getActions()


