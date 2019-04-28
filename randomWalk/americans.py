import pygal_maps_world.maps
wm = pygal_maps_world.maps.World()
wm.title = 'NOrth centrel'
# wl = pygal.maps
# wl.title = 'aaaa'
wm.add('north american',{'ca':5200,'us':895,'mx':88800})
wm.add('south',['ar','bo','br'])
wm.render_to_file('americnas.svg')