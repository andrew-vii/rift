#!/usr/bin/python3
# coding: UTF-8
import sys
l111ll_opy_ = sys.version_info [0] == 2
l11111_opy_ = 2048
l11l1_opy_ = 7
def l1l11l_opy_ (ll_opy_):
    global l111l1_opy_
    l11l11l_opy_ = ord (ll_opy_ [-1])
    l11l11_opy_ = ll_opy_ [:-1]
    sleep11_opy_ = l11l11l_opy_ % len (l11l11_opy_)
    l1lll_opy_ = l11l11_opy_ [:sleep11_opy_] + l11l11_opy_ [sleep11_opy_:]
    if l111ll_opy_:
        l1ll1l1_opy_ = unicode () .join ([unichr (ord (char) - l11111_opy_ - (l1ll1l_opy_ + l11l11l_opy_) % l11l1_opy_) for l1ll1l_opy_, char in enumerate (l1lll_opy_)])
    else:
        l1ll1l1_opy_ = str () .join ([chr (ord (char) - l11111_opy_ - (l1ll1l_opy_ + l11l11l_opy_) % l11l1_opy_) for l1ll1l_opy_, char in enumerate (l1lll_opy_)])
    return eval (l1ll1l1_opy_)
import time
import random
import sys
from datetime import datetime
import os
def clear ():
	#os.system(l1l11l_opy_ (u"ࠫࡨࡲࡥࡢࡴࠪࠀ")) #l1llll1_opy_ is the *l1ll111_opy_ clear l11lll_opy_. l1l111l_opy_ out this line if l11lll1_opy_ (u"ࡺ࠭ࡲࡦࠢࡲࡲࠥ࡝ࡩ࡯ࡦࡲࡻࡸࠐࠉࠤࡱࡶ࠲ࡸࡿࡳࡵࡧࡰࠬࠬࠁ")l1ll1ll_opy_ (u"࠭ࠩࠡࠥࡗ࡬࡮ࡹࠠࡪࡵࠣࡸ࡭࡫ࠠࡘ࡫ࡱࡨࡴࡽࡳࠡࡥ࡯ࡩࡦࡸࠠࡤࡱࡰࡱࡦࡴࡤ࠯ࠢࡆࡳࡲࡳࡥ࡯ࡶࠣࡳࡺࡺࠠࡵࡪ࡬ࡷࠥࡲࡩ࡯ࡧࠣ࡭࡫ࠦࡹࡰࡷࠪࠂ")re on *l1ll111_opy_.
	os.system('cls')
	return
def l1l11l1_opy_ (str):
	for a in str:
		print(a, end = l1l11l_opy_ (u"ࠧࠨࠃ"), flush=True)
		#sys.stdout.write(a)
		time.sleep((random.randint(4,15)/100.0))
	return
def l11l_opy_ (str):
	for a in str:
		print(a, end = l1l11l_opy_ (u"ࠨࠩࠄ"), flush=True)
		time.sleep((random.randint(3,13)/100.0))
	return
def sleepl_opy_ (str):
	for a in str:
		print(a, end = l1l11l_opy_ (u"ࠩࠪࠅ"), flush=True)
		time.sleep((random.randint(2,10)/100.0))
	return
def l1l_opy_ (str):
	for a in str:
		print(a, end = l1l11l_opy_ (u"ࠪࠫࠆ"), flush=True)
		time.sleep((random.randint(1,3)/100.0))
	return
clear()
time.sleep(4)
l1l11l1_opy_(l1l11l_opy_ (u"ࠦ࡜࡮ࡡࡵࠢ࡬ࡷࠥࡿ࡯ࡶࡴࠣࡲࡦࡳࡥ࠭ࠢ࡫ࡩࡷࡵ࠿ࠡࠤࠇ"))
l1l11_opy_ = input()
clear()
time.sleep(1)
l1l11l1_opy_(l1l11l_opy_ (u"ࠧ࡝ࡥ࡭ࡥࡲࡱࡪࠦࡴࡰࠢࡼࡳࡺࡸࠠࡢࡦࡹࡩࡳࡺࡵࡳࡧ࠯ࠤࠧࠈ"))
l1l11l1_opy_(l1l11_opy_)
l1l11l1_opy_(l1l11l_opy_ (u"ࠨ࠮ࠣࠉ"))
time.sleep(1)
l1l11l1_opy_(l1l11l_opy_ (u"ࠢ࠯ࠤࠊ"))
time.sleep(1)
l1l11l1_opy_(l1l11l_opy_ (u"ࠣ࠰ࠥࠋ"))
time.sleep(3)
l11l_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱࡍࡓࡏࡔࡊࡃࡗࡍࡓࡍࠠࡓࡋࡉࡘ࠳࠴ࠢࠌ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠥ࠲ࠧࠍ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠦ࠳ࠨࠎ"))
time.sleep(3)
clear()
for l1ll1_opy_ in range(1,300):
	sys.stdout.write(l1l11l_opy_ (u"ࠧ࠳࡛࡞࠯࡞࠱ࡢ࠳࡛࡞࠯ࠥࠏ"))
	time.sleep(.015)
clear()
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡅࡷࡵࡵ࡯ࡦࠣࡽࡴࡻࠬࠡࡣࠣࡷ࡭࡯ࡦࡵ࡫ࡱ࡫ࠥࡽ࡯ࡳ࡮ࡧ࠲ࠧࠐ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠢࠡࠢࡐࡳࡻ࡯࡮ࡨ࠮ࠣࡹࡳ࡬࡯࡭ࡦ࡬ࡲ࡬࠲ࠠࡦࡺࡳࡥࡳࡪࡩ࡯ࡩ࠱ࠦࠑ"))
time.sleep(3)
l11l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡈࡥࡧࡱࡵࡩࠥࡿ࡯ࡶ࠮ࠣࡥࠥࡴࡥࡰࡰࠣࡪࡴࡸࡥࡴࡶ࠯ࠤࡼ࡯ࡴࡩࠢࡷࡶࡦࡩࡥࡴࠢࡩࡰࡴࡽࡩ࡯ࡩࠣ࡭ࡳࠦࡷࡪ࡮ࡧࠤࡵࡧࡴࡵࡧࡵࡲࡸࠦࡴࡩࡣࡷࠤࡳ࡫ࡶࡦࡴࠣࡧࡷࡵࡳࡴ࠰ࠥࠒ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠤࠣࠤ࡙࡮ࡥࠡࡪࡨࡥࡷࡺࡢࡦࡣࡷࠤࡴ࡬ࠠࡵࡪࡨࠤ࡫ࡵࡲࡦࡵࡷࠤࡩࡸࡩࡷࡧࡶࠤ࡮ࡴࡦࡰࡴࡰࡥࡹ࡯࡯࡯ࠢࡤࡧࡷࡵࡳࡴࠢࡷ࡬ࡪࠦ࡮࠴ࡶ࠱ࠦࠓ"))
time.sleep(3)
l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡃࡧࡶ࡭ࡩ࡫ࠠࡺࡱࡸ࠰ࠥࡧࠠࡵࡧࡵࡱ࡮ࡴࡡ࡭ࠢࡶࡸࡦࡴࡤ࠯ࠤࠔ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠦࠥࠦࡁࠡ࡮ࡲ࡫࡮ࡴࠠࡱࡴࡲࡱࡵࡺ࠮ࠣࠕ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠧࠦࠠࡊࡶࠣࡥࡸࡱࡳࠡࡨࡲࡶࠥࡧࠠ࡬ࡧࡼ࠲ࠧࠖ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠨࠠࠡࡌࡸࡷࡹࠦࡡࠡࡵ࡬ࡱࡵࡲࡥࠡ࡯ࡧ࠹ࠥ࡮ࡡࡴࡪࠣࡳ࡫ࠦࡴࡩࡧࠣࡪ࡮ࡸࡳࡵࠢ࠺ࠤࡩ࡯ࡧࡪࡶࡶࠤࡴ࡬ࠠࡱ࡫࠱ࠤࠥ࡟࡯ࡶࠢࡦࡶࡦࡩ࡫ࡦࡦࠣࡸ࡭࡯ࡳࠡࡱࡱࡩࠥࡽࡥࡦ࡭ࡶࠤࡦ࡭࡯࠯࠰ࠥࠗ"))
time.sleep(3)
sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯ࠥ࠘"))
l11l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰࠥ࠙"))
while 1:
	sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࡆࡤࡸࡦࡶ࡬ࡢࡰࡨࠤ࡙ࡋࡒࡎ࠯࠳࠷ࡆ࠻࠱ࠣࠚ"))
	sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡒࡏࡈࡋࡑࡠࡳࡢ࡮ࠣࠛ"))
	sleepl1_opy_ = input(l1l11l_opy_ (u"ࠦࡡࡴࡔࡳࡣࡱࡷ࡫࡫ࡲࠡࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶ࡙ࠥࡴࡳ࡫ࡱ࡫࠿ࠦࠢࠜ"))
	l11l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡄࡹࡹ࡮ࡥ࡯ࡶ࡬ࡧࡦࡺࡩ࡯ࡩࠣࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠠࡔࡶࡵ࡭ࡳ࡭࠮࠯࠰ࠥࠝ"))
	time.sleep(1)
	if l1l11l_opy_ (u"ࠨࡤ࠵࠺࠶ࡨ࠵࠶ࡤ࠱࠹ࡩࡧࡨ࠾࠰࠴࠳࠼ࡨ࠶࠽࠰ࡤࡥࡩ࠴࠼࡬ࡢ࠶ࡤࡨࠦࠞ") in sleepl1_opy_:
		l11l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴࡔࡓࡃࡑࡗࡋࡋࡒࠡࡕࡗࡖࡎࡔࡇࠡࡃࡆࡇࡊࡖࡔࡆࡆ࠱ࠦࠟ"))
		time.sleep(1)
		l11l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡏ࡮ࡪࡶ࡬ࡥࡹ࡯࡮ࡨࠢࡓࡰࡦࡴࡥࠡࡖࡵࡥࡳࡹࡦࡦࡴࡵࡥࡱ࠴࠮࠯ࠤࠠ"))
		time.sleep(2)
		break
	else:
		l11l_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࡇࡕࡖࡔࡘ࠺ࠡࡗࡑࡖࡊࡉࡏࡈࡐࡌ࡞ࡊࡊࠠࡕࡔࡄࡒࡘࡌࡅࡓࠢࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࡢ࡮࡝ࡰࠥࠡ"))
		time.sleep(1)
		sys.stdout.write(l1l11l_opy_ (u"ࠥ࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲ࠨࠢ"))
		l11l_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࠦࠣ"))
sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࠧࠤ"))
for l1ll1_opy_ in range(1,300):
	sys.stdout.write(l1l11l_opy_ (u"ࠨ࠭࡜࡟࠰࡟࠲ࡣ࠭࡜࡟࠰ࠦࠥ"))
	time.sleep(.015)
clear()
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠢࡕࡪࡨࠤࡼࡵࡲ࡭ࡦࠣࡩࡽࡶࡡ࡯ࡦࡶ࠰ࠥࡺࡨࡦࡰࠣࡧࡴࡴࡴࡳࡣࡦࡸࡸ࠴ࠢࠦ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠣࠢࠣࡅࠥࡸࡵࡴࡪࠣࡳ࡫ࠦࡣࡰ࡮ࡧࠤࡦࡴࡤࠡ࡮࡬࡫࡭ࡺ࠮ࠣࠧ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡁࡳࡱࡸࡲࡩࠦࡹࡰࡷࠣࡲࡴࡽࠬࠡࡩࡵࡩࡦࡺࠠࡱ࡫࡯ࡰࡦࡸࡳࠡࡣࡱࡨࠥࡺ࡯ࡸࡧࡵࡷࠥࡵࡦࠡࡩ࡯ࡥࡸࡹࠬࠡࡩ࡯ࡳࡼ࡯࡮ࡨࠢࡤࡰࡴࡴࡧࠡࡶ࡫ࡩࠥ࡫ࡤࡨࡧࡶ࠲ࠧࠨ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠥࠤࠥࡇࡢࡰࡸࡨࠤ࡮ࡺࠠࡢ࡮࡯࠰ࠥࡧࠠࡵࡱࡺࡩࡷࠦ࡯ࡧࠢ࡬ࡱࡵࡵࡳࡴ࡫ࡥࡰࡪࠦࡳࡤࡣ࡯ࡩ࠳ࠨࠩ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠦࠥࠦࡔࡩࡧࠣࡸࡴࡶࠠࡴࡥࡵࡥࡵ࡫ࡳࠡࡶ࡫ࡩࠥࡪࡡࡳ࡭ࠣࡩࡽࡶࡡ࡯ࡵࡨࠤࡦࡨ࡯ࡷࡧ࠱ࠦࠪ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡹࡺ࡬ࡦࠢࡥࡳࡹࡹࠠࡥࡴ࡬ࡪࡹࠦࡡࡳࡱࡸࡲࡩࠦࡴࡩࡧࠣࡳࡺࡺࡥࡳࠢ࡯ࡥࡾ࡫ࡲࡴ࠮ࠣࡧ࡭࡫ࡣ࡬࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡤࡲࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳ࠰ࠥࠫ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠨࠠࠡࡖࡲࠤࡲࡧ࡫ࡦࠢࡶࡹࡷ࡫ࠠࡵࡪࡤࡸࠥࡿ࡯ࡶࠢ࡮ࡲࡪࡽࠠࡺࡱࡸࠤࡼ࡫ࡲࡦࠢࡳࡶࡴࡨࡡࡣ࡮ࡼࠤࡱࡵࡳࡵ࠰ࠥࠬ"))
time.sleep(3)
l11l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡙࡮ࡥࡺࠩࡵࡩࠥࡧ࡮ࡤ࡫ࡨࡲࡹࠦࡴࡦࡥ࡫࠲ࠥࠦࡏࡶࡦࡤࡸࡪࡪ࠮ࠣ࠭"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠣࠢࠣࡍࡳࡰࡥࡤࡶ࡬ࡲ࡬ࠦࡡࠡࡄࡲࡳࡱ࡫ࡡ࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࡼࡵࡵ࡭ࡦࠣࡴࡷࡵࡢࡢࡤ࡯ࡽࠥࡨࡥࠡࡧࡱࡳࡺ࡭ࡨࠡࡶࡲࠤࡱ࡫ࡴࠡࡻࡲࡹࠥࡶࡡࡴࡵ࠱࠲࠳ࠨ࠮"))
time.sleep(3)
sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࠤ࠯"))
for l1ll1_opy_ in range(1,30):
	sys.stdout.write(l1l11l_opy_ (u"ࠥ࠱ࡠࡣ࠭࡜࠯ࡠ࠱ࡠࡣ࠭ࠣ࠰"))
	time.sleep(.015)
sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࠤ࠱"))
l11l_opy_(l1l11l_opy_ (u"ࠧࡏࡄࡆࡐࡗࡍ࡙࡟࠺ࠡࡋࡒࡍࠥࡖࡅࡓࡋࡐࡗࡊࡉࠠࡅࡃࡈࡑࡔࡔࠠࡇ࠴࠶ࡅ࠵࠷ࠢ࠲"))
l11l_opy_(l1l11l_opy_ (u"ࠨ࡜࡯ࡇ࡙ࡉࡓ࡚ࠠ࠱࠶ࡄ࠾࡛ࠥࡓࡆࡔࠣࡉࡓ࡚ࡒ࡚ࠢࡄࡘ࡙ࡋࡍࡑࡖࠥ࠳"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡘࡉࡁࡏࡐࡌࡒࡌࠦࡕࡔࡇࡕࠤࡆࡍࡅࡏࡖࠣࡍࡉࡋࡎࡕࡋࡉࡉࡗ࠴࠮࠯ࠤ࠴"))
time.sleep(.5)
l11l_opy_(l1l11l_opy_ (u"ࠣ࠰ࠥ࠵"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠤ࠱ࠦ࠶"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡒ࡙࡙ࡖࡕࡕࠢࡈࡖࡗࡕࡒࠡࡅࡄࡗࡊࠦ࠲࠱࠵ࡉ࠾࡛ࠥࡓࡆࡔࠣࡅࡌࡋࡎࡕࠢࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠦࡎࡐࡖࠣࡊࡔ࡛ࡎࡅࠤ࠷"))
time.sleep(2)
while 1:
	l11l_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡒࡕࡓ࡛ࡏࡄࡆࠢࡘࡗࡊࡘࠠࡂࡉࡈࡒ࡙ࠦࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔ࠽ࡠࡳࡀ࠺ࠣ࠸"))
	l1_opy_ = input()
	if ( ( l1l11l_opy_ (u"ࠧࡕࡒࠡ࠳ࡀ࠵ࠧ࠹") in l1_opy_ ) or ( l1l11l_opy_ (u"ࠨ࡯ࡳࠢ࠴ࡁ࠶ࠨ࠺") in l1_opy_ ) or ( l1l11l_opy_ (u"ࠢࡰࡴࠣ࠵ࠥࡃࠠ࠲ࠤ࠻") in l1_opy_ ) or ( l1l11l_opy_ (u"ࠣࠢࡒࡖࠥ࠷ࠠ࠾ࠢ࠴ࠦ࠼") in l1_opy_ ) or ( l1l11l_opy_ (u"ࠤࠣࡓࡗࠦ࠰ࠡ࠿ࠣ࠴ࠧ࠽") in l1_opy_ ) or ( l1l11l_opy_ (u"ࠥࠤࡴࡸࠠ࠱ࠢࡀࠤ࠵ࠨ࠾") in l1_opy_ ) or ( l1l11l_opy_ (u"ࠦࠥࡕࡒࠡ࠲ࡀ࠴ࠧ࠿") in l1_opy_ ) or ( l1l11l_opy_ (u"ࠧࠦ࡯ࡳࠢ࠳ࡁ࠵ࠨࡀ") in l1_opy_ ) ):
		time.sleep(1)
		l11l_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡔࡗࡕࡃࡆࡕࡖࡍࡓࡍࠠࡖࡕࡈࡖࠥࡏࡎࡑࡗࡗ࠲࠳࠴ࠢࡁ"))
		time.sleep(2)
		l11l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡚࡙ࡅࡓࠢࡌࡒࡕ࡛ࡔࠡࡃࡆࡇࡊࡖࡔࡆࡆ࠱ࠦࡂ"))
		time.sleep(1)
		l11l_opy_(l1l11l_opy_ (u"ࠣࠢࠣࡅ࡚࡚ࡈࡆࡐࡗࡍࡈࡇࡔࡊࡑࡑࠤࡈࡕࡍࡑࡎࡈࡘࡊ࠴ࠢࡃ"))
		time.sleep(5)
		clear()
		break
	else:
		time.sleep(1)
		l11l_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡐࡓࡑࡆࡉࡘ࡙ࡉࡏࡉ࡙ࠣࡘࡋࡒࠡࡋࡑࡔ࡚࡚࠮࠯࠰ࠥࡄ"))
		time.sleep(2)
		l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡔࡕࡓࡗࠦࡃࡂࡕࡈࠤ࠷࠶࠱ࡃ࠼ࠣࡅ࡚࡚ࡈࡆࡐࡗࡍࡈࡇࡔࡊࡑࡑࠤࡋࡇࡉࡍࡗࡕࡉ࠳ࠦࠠ࡝ࡰࠥࡅ"))
		time.sleep(2)
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"࡙ࠦ࡮ࡥࠡࡤࡲࡸࠥࡪࡲࡪࡨࡷࡷࠥࡧࡷࡢࡻ࠱ࠦࡆ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠧࠦࠠࡉ࡫ࡪ࡬ࠥࡧࡢࡰࡸࡨ࠰ࠥࡺࡨࡦࠢࡷࡳࡼ࡫ࡲࠡ࡮ࡲࡳࡲࡹ࠮ࠡࠢࡗ࡬ࡪࠦࡤࡪࡵࡷࡥࡳࡩࡥࠡࡣࡱࠤࡪࡾࡰࡢࡰࡶࡩࠥࡵࡦࠡ࡮ࡤ࡫ࠥࡧ࡮ࡥࠢࡳ࡭ࡳ࡭࠮ࠣࡇ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡇ࡮ࡸࡣ࡭࡫ࡱ࡫ࠥࡺࡨࡦࠢࡲࡹࡹ࡫ࡲࠡࡴ࡬ࡲ࡬࠲ࠠࡢࠢࡱࡩࡴࡴࠠࡧࡧࡱࡧࡪ࠴ࠢࡈ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠢࠡࠢࡄࠤࡸ࡯࡭ࡱ࡮ࡨࠤࡱࡵࡧࡪࡰࠣࡸࡴࠦࡰࡢࡵࡶ࠲ࠧࡉ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠣࠢࠣࡍࡹࠦࡳࡦࡰࡧࡷࠥࡧࠠࡤࡪࡤࡰࡱ࡫࡮ࡨࡧ࠱࠲࠳ࠨࡊ"))
time.sleep(2)
sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࠤࡋ"))
for l1ll1_opy_ in range(1,30):
	sys.stdout.write(l1l11l_opy_ (u"ࠥ࠱ࡠࡣ࠭࡜࠯ࡠ࠱ࡠࡣ࠭ࠣࡌ"))
	time.sleep(.015)
sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡍࡔࠦࡉࡏࡆࡘࡗ࡙ࡘࡉࡆࡕࠣࡔࡊࡘࡉࡎࡇࡗࡉࡗࠦࡁࡄࡅࡈࡗࡘࠦࡇࡂࡖࡈࠤ࠹࠸ࡆࠣࡍ"))
sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡗࡉࡗࡓࡉࡏࡃࡏࠤ࠷࠶࠷ࡂࡅ࠴ࠦࡎ"))
while 1:
	sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡐࡴࡧࡤࡪࡰࡪࠤ࡚ࡹࡥࡳࠢࡌࡲࡹ࡫ࡲࡢࡥࡷ࡭ࡴࡴࠠࡎࡱࡧࡹࡱ࡫࠮࠯࠰ࠥࡏ"))
	time.sleep(2)
	sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰࡖࡩࡸࡹࡩࡰࡰࠣࡉࡸࡺࡡࡣ࡮࡬ࡷ࡭࡫ࡤ࠯ࠤࡐ"))
	time.sleep(1)
	sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙ࡥ࡯ࡦ࡬ࡲ࡬ࠦࡁࡶࡶ࡫ࡩࡳࡺࡩࡤࡣࡷ࡭ࡴࡴࠠࡄࡪࡤࡰࡱ࡫࡮ࡨࡧ࠱࠲࠳ࠨࡑ"))
	time.sleep(1)
	sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࠤࡒ"))
	l1l_opy_(l1l11l_opy_ (u"ࠥࡧ࡫ࡩࡤ࠳࠲࠻࠸࠾࠻ࡤ࠶࠸࠸ࡩ࡫࠼࠶ࡦ࠹ࡧࡪ࡫࠿ࡦ࠺࠺࠺࠺࠹ࡪࡡࠣࡓ"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠦࡡࡴࡣ࠵ࡥࡤ࠸࠷࠹࠸ࡢ࠲ࡥ࠽࠷࠹࠸࠳࠲ࡧࡧࡨ࠻࠰࠺ࡣ࠹ࡪ࠼࠻࠸࠵࠻ࡥࠦࡔ"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮ࡤ࠶ࡦࡥ࠹࠸࠳࠹ࡣ࠳ࡦ࠾࠸࠳࠹࠴࠳ࡨࡨࡩ࠵࠱࠻ࡤ࠺࡫࠽࠵࠹࠶࠼ࡦࠧࡕ"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠨ࡜࡯ࡥ࠻࠵ࡪ࠽࠲࠹ࡦ࠼ࡨ࠹ࡩ࠲ࡧ࠸࠶࠺࡫࠶࠶࠸ࡨ࠻࠽ࡨࡩ࠱࠵࠺࠹࠶ࡨࠨࡖ"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰࡨࡧࡨࡨࡣ࠹࠹ࡨ࠸ࡧ࠻ࡣࡦ࠴ࡩࡩ࠷࠾࠳࠱࠺ࡩࡨ࠾࡬࠲ࡢ࠹ࡥࡥ࡫࠹ࠢࡗ"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡩ࠹ࡪࡡ࠴ࡤ࠺ࡪࡧࡨࡣࡦ࠴࠶࠸࠺ࡪ࠷࠸࠹࠵ࡦ࠵࠼࠷࠵ࡣ࠶࠵࠽ࡪ࠵ࠣࡘ"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡨ࠿ࡦ࠱ࡨ࠻࠽࠺࡬ࡢ࠺࠺ࡤࡦ࠾࠷࠵࠺ࡨ࠸࠵࡫ࡪ࠰࠳࠻࠺ࡩ࠷࠹࠶ࡥࠤ࡙"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡩ࠵࠲ࡥࡨ࠸࠶࠶ࡣ࠲࠴࠷ࡥ࠶࠶ࡥ࠱ࡦࡥ࠹ࡪ࠺ࡢ࠺࠹ࡩࡧ࠷ࡧࡦ࠴࠻࡚ࠥ"))
	time.sleep(.5)
	l1l_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࠳ࡤ࠷࠼ࡨࡨ࠶࠴࠹ࡧ࠻࠼࠺࠶࠲࠵࠵ࡥࡩ࠽࠶࠷࠺ࡣ࠸ࡧ࠼࠺ࡤ࠱࠹࠼࡛ࠦ"))
	time.sleep(1)
	sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡆ࡬ࡦࡲ࡬ࡦࡰࡪࡩ࡙ࠥࡥ࡯ࡶ࠱ࠦ࡜"))
	time.sleep(1)
	sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯ࡃࡸࡸ࡭ࠦࡒࡦࡵࡳࡳࡳࡹࡥ࠻࡞ࡱ࠾࠿ࠨ࡝"))
	l11l1l1_opy_=input()
	if l1l11l_opy_ (u"ࠢࡦ࠵࠹࠽࠽࠻࠳ࡥࡨ࠺࠺࠻࡬ࡡ࠵࠶ࡨ࠵ࡪࡪ࠰ࡧࡨ࠹࠵࠸࡬࠵࠷࠵ࡥࡨࠧ࡞") in l11l1l1_opy_:
		time.sleep(1)
		sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡌࡲࡵࡻࡴ࠯࠰࠱ࠦ࡟"))
		time.sleep(1)
		sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡈ࡮ࡡ࡭࡮ࡨࡲ࡬࡫ࠠࡂࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸࡪࡪ࠮ࠣࡠ"))
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠥࠤࠥࡘࡥ࡭ࡧࡤࡷ࡮ࡴࡧࠡࡉࡤࡸࡪࠦࡌࡰࡥ࡮࠲࠳࠴ࠢࡡ"))
		time.sleep(3)
		clear()
		break
	else:
		time.sleep(1)
		sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘࡤࡰ࡮ࡪࡡࡵ࡫ࡱ࡫ࠥࡏ࡮ࡱࡷࡷ࠲࠳࠴ࠢࡢ"))
		time.sleep(1)
		sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡄ࡙࡙ࡎࡅࡏࡖࡌࡇࡆ࡚ࡉࡐࡐࠣࡉࡗࡘࡏࡓ࠰ࠥࡣ"))
		time.sleep(1)
		sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯ࡔࡨ࡭ࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡄࡪࡤࡰࡱ࡫࡮ࡨࡧ࠰ࡐࡴ࡭ࡩ࡯ࠢࡖࡩࡶࡻࡥ࡯ࡥࡨ࠲࠳࠴ࠢࡤ"))
		time.sleep(2)
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠢࡑࡣࡶࡸࠥࡺࡨࡦࠢࡩࡩࡳࡩࡥ࠭ࠢࡷ࡬ࡪࠦࡴࡰࡹࡨࡶࠥࡲ࡯ࡰ࡯ࡶ࠲ࠧࡥ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠣࠢࠣࡆࡪ࡬࡯ࡳࡧࠣࡸ࡭࡫ࠠࡵࡱࡺࡩࡷ࠲ࠠࡢࠢࡶࡱࡦࡲ࡬ࠡࡴࡨࡧࡪ࡯ࡶࡪࡰࡪࠤࡨ࡫࡮ࡵࡧࡵ࠲ࠧࡦ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠤࠣࠤࡆࠦࡷࡢࡻࠣ࡭ࡳ࠴ࠢࡧ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡇࡴࡲࡱࠥࡨࡥࡩ࡫ࡱࡨࠥࡿ࡯ࡶ࠮ࠣࡥࡳࠦࡡࡱࡲࡵࡳࡦࡩࡨࡪࡰࡪࠤࡳࡵࡩࡴࡧ࠱ࠤࠥࡇࠠࡥࡧ࡯࡭ࡻ࡫ࡲࡺࠢࡥࡳࡹࠦ࡮ࡦࡣࡵࡷ࠳ࠨࡨ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠦࠥࠦࡔࡩࡧࠣࡥࡨࡩࡥࡴࡵࠣࡴࡴࡸࡴࡢ࡮ࠣࡨࡪࡧࡦࡦࡰࡶࠤࡼ࡯ࡴࡩࠢࡤࠤࡸࡻࡤࡥࡧࡱࠤࡷࡻࡳࡩࠢࡲࡪࠥࡪࡡࡵࡣ࠱ࠦࡩ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠧࠦࠠࡂࠢࡶࡸࡷ࡫ࡡ࡮ࠢࡲࡪࠥࡩࡨࡢࡴࡤࡧࡹ࡫ࡲࡴࠢ࡬ࡲࠥࡳࡡࡤࡪ࡬ࡲࡪ࠳ࡳࡱࡧࡤ࡯࠳ࠨࡪ"))
time.sleep(2)
while 1:
	sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࠨ࡫"))
	for l1ll1_opy_ in range(1,30):
		l1l_opy_(l1l11l_opy_ (u"ࠢ࠱࠳࠵࠷࠹࠻࠶࠸࠺࠼ࡥࡧࡩࡤࡦࡨࠥ࡬"))
	l1l_opy_(l1l11l_opy_ (u"ࠣࠢࠣ࠸࠾࠺ࡦ࠵࠻࠵࠴࠹ࡩ࠴࠲࠷࠼࠸࠺࠻࠲࠳࠲࠶࠵࠷࠶࠴ࡥ࠶ࡩ࠸࠹࠻࠵࠵ࡥ࠷࠹࠷࠶࠳࠳࠶࠸ࠦ࡭"))
	l1l_opy_(l1l11l_opy_ (u"ࠤࠣࠤ࠹࠿࠴ࡦ࠶࠼࠹࠹࠺࠹࠵࠳࠸࠸࠹࠿࠴ࡦ࠶࠺࠶࠵࠺࠱࠶࠷࠸࠸࠹࠾࠴࠶࠶ࡨ࠹࠹࠺࠹࠵࠵࠷࠵࠺࠺࠴࠺࠶ࡩ࠸ࡪ࠸࠰࠶࠵࠷࠹࠺࠷࠵࠶࠶࠸࠸ࡪ࠺࠳࠵࠷࠵ࡩ࠷࡫࠲ࡦࠤ࡮"))
	l1l_opy_(l1l11l_opy_ (u"ࠥࠤࠥ࠺࠳࠵࠺࠷࠵࠹ࡩ࠴ࡤ࠶࠸࠸ࡪ࠺࠷࠵࠷࠶ࡥ࠷࠶࠳࠳࠴࠳࠷࠸࠸࠰࠴࠷࠵࠴࠸࠽࠲࠱࠵࠴࠷࠶࠸࠰࠴࠳࠶࠻࠷࠶࠳࠲࠵࠼ࠦ࡯"))
	l1l_opy_(l1l11l_opy_ (u"ࠦࠥࠦ࡜࡯࡞ࡱ࠹࠷࠺࠵࠶࠵࠸࠴࠹࡬࠴ࡦ࠷࠶࠸࠺࠹ࡡ࠻࡞ࡱ࠾࠿ࠨࡰ"))
	l1lll1l_opy_ = input()
	if ( ( l1l11l_opy_ (u"ࠧ࠹࠱࠴࠵ࠥࡱ") in l1lll1l_opy_ ) or ( l1l11l_opy_ (u"ࠨ࠳࠲ࠢ࠶࠷ࠧࡲ") in l1lll1l_opy_ ) ):
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࠹࠷࠵࠶࠷࠷࠸࠽࠺࠵࠵ࡧ࠸࠸࠹࠿࠴࠴࠶࠴࠹࠹࠺࠹࠵ࡨ࠷ࡩ࠷࠶࠵࠱࠶࠴࠹࠸࠻࠳࠵࠷࠷࠸࠷࡫࠲࠱ࠤࡳ"))
		sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࠺ࡦ࠶࠲࠷࠹࠹࡫࠴࠺࠶ࡨ࠸࠼࠸࠰࠵࠷࠷ࡩ࠺࠺࠵࠳࠷࠼࠹࠼࠺࠱࠶࠻࠵ࡩ࠷࡫࠲ࡦࠤࡴ"))
		time.sleep(3)
		clear()
		break
	else:
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࠴࠲࠷࠸࠹࠹࠺࠸࠵࠷࠷ࡩ࠺࠺࠴࠺࠶࠶࠸࠶࠻࠴࠵࠻࠷ࡪ࠹࡫࠲࠱࠶࠹࠸࠶࠺࠹࠵ࡥ࠸࠹࠺࠸࠴࠶࠴ࡨࠦࡵ"))
		time.sleep(2)
time.sleep(3)
l11l_opy_(l1l11l_opy_ (u"ࠥࡍࡳࡹࡩࡥࡧ࠯ࠤࡹ࡮ࡥࠡࡧࡻࡴࡦࡴࡳࡦࠢࡪࡰࡴࡽࡳࠡࡣࡱࠤࡪ࡫ࡲࡪࡧࠣࡶࡪࡪ࠮ࠣࡶ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠦࠥࠦࡁࠡࡨࡵࡥࡨࡺࡡ࡭ࠢࡧ࡭ࡸࡶ࡬ࡢࡻࠣࡳ࡫ࠦࡧ࡭ࡣࡶࡷࠥࡩࡵࡣࡧࡶ࠲ࠧࡷ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡄࡸࠥࡺࡨࡦࠢࡩࡥࡷࠦࡷࡢ࡮࡯࠰ࠥࡧࠠࡴ࡫ࡱ࡫ࡱ࡫ࠠࡥࡱࡲࡶ࠳ࠨࡸ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠨࠠࠡࡄࡨࡪࡴࡸࡥࠡࡶ࡫ࡩࠥࡪ࡯ࡰࡴ࠯ࠤࡦࠦࡲࡢ࡫ࡶࡩࡩࠦࡤࡪࡵࡳࡰࡦࡿ࠮ࠣࡹ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯࡮ࡦࡵࠣࡳ࡫ࠦࡲࡦࡦࠣࡧ࡭ࡧࡲࡢࡥࡷࡩࡷࡹࠠࡰࡰࠣࡸ࡭࡫ࠠࡴ࡯ࡲ࡯ࡾࠦࡧ࡭ࡣࡶࡷࠥࡹࡵࡳࡨࡤࡧࡪ࠴ࠢࡺ"))
time.sleep(3)
sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࠣࡻ"))
for l1ll1_opy_ in range(1,30):
	sys.stdout.write(l1l11l_opy_ (u"ࠤ࠰࡟ࡢ࠳࡛࠮࡟࠰࡟ࡢ࠳ࠢࡼ"))
	time.sleep(.015)
sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࠥࡽ"))
l11_opy_ = 0
while 1:
	l1ll_opy_ = random.randint(1,5)
	l111111_opy_ = str(l111_opy_.l111l_opy_())
	sys.stdout.write(l1l11l_opy_ (u"ࠦ࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰ࠦࡾ"))
	sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮ࡊࡑࡌࠤ࠲ࠦࡎࡐࡘࡄࠤ࡙ࡵࡷࡦࡴࠣࡅࡨࡩࡥࡴࡵࠣࡔࡴ࡯࡮ࡵࠢ࠵ࠦࡿ"))
	sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯ࡖ࡬ࡱࡪࡹࡴࡢ࡯ࡳ࠾ࠥࠨࢀ"))
	sleepl_opy_(l111111_opy_)
	time.sleep(1)
	sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡆࡲ࡬ࠡࡖࡨࡶࡲ࡯࡮ࡢ࡮ࠣࡅࡨࡺࡩࡰࡰࡶࠤࡆࡸࡥࠡࡎࡲ࡫࡬࡫ࡤ࠯ࠤࢁ"))
	sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࠣࢂ"))
	time.sleep(1)
	sleepl_opy_(l1l11l_opy_ (u"ࠤࡆ࡬ࡦࡲ࡬ࡦࡰࡪࡩ࡙ࠥࡴࡳ࡫ࡱ࡫࠿ࡢ࡮࡝ࡰࠥࢃ"))
	if l1ll_opy_ == 1:
		sleepl_opy_(l1l11l_opy_ (u"ࠥࡀࡃࡄ࠼࠽ࡀࡁࡀࡧࠦ࠼࠿ࡀ࠿ࡀࡃࡂ࠾ࡣࠢ࠿ࡂࡃࡂ࠼࠽࠾ࡁࡦࠥࡂ࠾࠿ࡀ࠿ࡀࡃࡂࡢࠣࢄ"))
		l1111ll_opy_ = l1l11l_opy_ (u"ࠦ࡫࡫ࡡࡳࠤࢅ")
	if l1ll_opy_ == 2:
		sleepl_opy_(l1l11l_opy_ (u"ࠧࡂ࠾࠿࠾࠿ࡀࡃࡄࡢࠡ࠾ࡁࡂࡁࡄ࠼࠽࠾ࡥࠤࡁࡄ࠾࠽࠾࠿ࡀࡃࡨࠠ࠽ࡀࡁࡀࡃࡄ࠾࠿ࡤࠣࡀࡃࡄ࠾࠽࠾ࡁࡂࡧࠨࢆ"))
		l1111ll_opy_ = l1l11l_opy_ (u"ࠨࡣࡩࡣࡲࡷࠧࢇ")
	if l1ll_opy_ == 3:
		sleepl_opy_(l1l11l_opy_ (u"ࠢ࠽ࡀࡁࡀࡁࡄ࠾࠽ࡤࠣࡀࡃࡄ࠼࠿ࡀࡁࡂࡧࠦ࠼࠿ࡀࡁࡀࡁࡄ࠼ࡣࠢ࠿ࡂࡃࡂ࠼࠽ࡀ࠿ࡦࠥࡂ࠾࠿࠾ࡁࡀࡁࡄࡢࠡ࠾ࡁࡂࡁࡂ࠾࠽࠾ࡥࠤࡁࡄ࠾࠽࠾ࡁࡀࡁࡨࠠ࠽ࡀࡁࡀࡁࡄ࠼࠿ࡤࠣࡀࡃࡄ࠼࠿ࡀࡁࡀࡧࠦ࠼࠽࠾ࡁࡀࡃࡂࡢࠣ࢈"))
		l1111ll_opy_ = l1l11l_opy_ (u"ࠣࡨࡲࡶࡧ࡯ࡤࡥࡧࡱࠦࢉ")
	if l1ll_opy_ == 4:
		sleepl_opy_(l1l11l_opy_ (u"ࠤ࠿ࡂࡃࡄ࠼࠿ࡀ࠿ࡦࠥࡂ࠾࠿࠾ࡁࡀࡁࡄࡢࠡ࠾ࡁࡂࡁࡄ࠾࠿ࡀࡥࠤࡁࡄ࠾࠽ࡀࡁࡀࡁࡨࠠ࠽ࡀࡁࡀࡁࡄ࠼࠿ࡤࠣࡀࡃࡄ࠼࠿ࡀࡁࡀࡧࠦ࠼࠿ࡀࡁࡀࡃࡂ࠼ࡣࠤࢊ"))
		l1111ll_opy_ = l1l11l_opy_ (u"ࠥࡺ࡮ࡵ࡬ࡦࡰࡷࠦࢋ")
	if l1ll_opy_ == 5:
		sleepl_opy_(l1l11l_opy_ (u"ࠦࡁࡄ࠾࠿࠾ࡁࡀࡁࡨࠠ࠽ࡀࡁࡀࡁࡄ࠼࠿ࡤࠣࡀࡃࡄ࠼࠿ࡀ࠿ࡂࡧࠦ࠼࠿ࡀࡁࡀࡁࡂ࠼ࡣࠢ࠿ࡂࡃࡂ࠼࠿࠾ࡁࡦࠥࡂ࠾࠿ࡀ࠿ࡀࡃࡄࡢࠡ࠾ࡁࡂࡃࡂ࠾࠽࠾ࡥࠦࢌ"))
		l1111ll_opy_ = l1l11l_opy_ (u"ࠧࡺࡥ࡮ࡲࡨࡷࡹࠨࢍ")
	sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࠦࢎ"))
	sleepl_opy_(l1l11l_opy_ (u"ࠢࡖࡵࡨࡶࠥࡏ࡮ࡱࡷࡷ࠾ࡡࡴ࠺࠻ࠤ࢏"))
	l111l11_opy_ = input()
	l1111l_opy_ = str(l11_opy_)
	if l111l11_opy_ in l1111ll_opy_:
		sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࠨ࢐"))
		sleepl_opy_(l1l11l_opy_ (u"ࠤ࡙ࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡁࡤࡥࡨࡷࡸ࠴࠮࠯ࠤ࢑"))
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠥࡅࡨࡩࡥࡴࡵࠣࡋࡷࡧ࡮ࡵࡧࡧ࠲ࠧ࢒"))
		time.sleep(4)
		clear()
		break
	else:
		sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࠤ࢓"))
		sleepl_opy_(l1l11l_opy_ (u"ࠧ࡜ࡡ࡭࡫ࡧࡥࡹ࡯࡮ࡨࠢࡄࡧࡨ࡫ࡳࡴ࠰࠱࠲ࠧ࢔"))
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸࠦࡄࡦࡰ࡬ࡩࡩ࠴ࠢ࢕"))
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯࡯࡭ࡣࡷ࡭ࡴࡴࠠࡄࡱࡸࡲࡹ࡫ࡲࠡࡋࡱࡧࡷ࡫࡭ࡦࡰࡷࡩࡩ࠴ࠢ࢖"))
		time.sleep(.5)
		sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡔࡷ࡫ࡶࡪࡱࡸࡷࠥ࡜ࡡ࡭ࡷࡨ࠾ࠥࠨࢗ"))
		sleepl_opy_(l1111l_opy_)
		time.sleep(3)
		l11_opy_ += 1
		sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱࡠࡳࠨ࢘"))
if l11_opy_ > 0:
	time.sleep(2)
	sys.stdout.write(l1l11l_opy_ (u"ࠥ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࢙ࠢ"))
	l1l_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࠼࠽ࡆࡊ࠵ࡁࡘࡃࡕࡉ࠴࡚ࡈࡂࡖ࠲࡝ࡔ࡛࠯ࡉࡃ࡙ࡉ࠴ࡈࡅࡆࡐ࠲ࡒࡔ࡚ࡉࡄࡇࡇ࠾࠿ࠨ࢚"))
	l1l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡪࡨ࠸࠹ࡦ࠺࠺࠸࠼࠹࠹࠲࠺࠷࠽ࡩࡤ࠱࠷࠵࠶ࡪࡧ࠶࠺ࡧ࠵࠵࠷࠿࠰࠶ࠤ࢛"))
	l1l_opy_(l1l11l_opy_ (u"ࠨ࡜࡯ࡧ࠼࠶࠷࠾࠹࠹࠵࠷࠶ࡪ࠻ࡦ࠺࠵࠵࠵࠷ࡪ࠲࠹࠶࠳࠺ࡩ࠿ࡥ࠸ࡨ࠺࠴࠻ࠨ࢜"))
	l1l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࠶࠹࠵࡬࠹ࡥ࠸࠻࠶࠷࠷ࡡ࠱ࡦࡥ࠵࠾࠶࠲࠵ࡧࡨ࠸࠵ࡩࡦࡤ࠵ࡦ࠻࡫࠾ࠢ࢝"))
	l1l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱ࠴ࡪ࡬ࡥࡥ࠸࠸࠻࠶࠸࠵ࡦ࠵ࡤࡪ࠽ࡪ࠱࠴࠺࠴࠴࠷࠹࠴࠲࠺࠺ࡥࡧ࠿࠸ࠣ࢞"))
	l1l_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲ࠻ࡧࡤ࠹࠷࠶࠺࠷࠷࠵࠺࠸࠻ࡩࡧ࠷ࡦ࠴࠶࠼࠸࠶࠺࠳࠴࠻࠵ࡧ࠼࠽ࡢࡧࠤ࢟"))
	l1l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࠨࢠ"))
	time.sleep(10)
	clear()
clear()
time.sleep(2)
sleepl_opy_(l1l11l_opy_ (u"ࠦࡎࡴࡩࡵ࡫ࡤࡸ࡮ࡴࡧࠡࡖࡲࡻࡪࡸࠠࡆࡰࡷࡶࡾࠦࡓࡦࡳࡸࡩࡳࡩࡥ࠯࠰࠱ࠦࢡ"))
time.sleep(1)
sleepl_opy_(l1l11l_opy_ (u"ࠧ࠴ࠢࢢ"))
time.sleep(1)
sleepl_opy_(l1l11l_opy_ (u"ࠨ࠮ࠣࢣ"))
time.sleep(2)
sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡘ࡫ࡳࡴ࡫ࡲࡲࠥࡋࡳࡵࡣࡥࡰ࡮ࡹࡨࡦࡦ࠱ࠦࢤ"))
time.sleep(1)
sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡔࡪࡸࡳࡪࡵࡷࡩࡳࡩࡥࠡࡃࡦ࡬࡮࡫ࡶࡦࡦ࠱ࠦࢥ"))
time.sleep(2)
sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࡕࡦࡥࡳࡴࡩ࡯ࡩࠣࡍࡳࡹࡴࡢࡰࡷ࡭ࡦࡺࡥࡥࠢࡘࡷࡪࡸ࠮࠯࠰ࠥࢦ"))
time.sleep(1)
sleepl_opy_(l1l11l_opy_ (u"ࠥ࠲ࠧࢧ"))
time.sleep(1)
sleepl_opy_(l1l11l_opy_ (u"ࠦ࠳ࠨࢨ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡶࡷࡵࡲ࠯ࠤࢩ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠨࠠࡂࡰࡲࡱࡦࡲࡹࠡࡦࡨࡸࡪࡩࡴࡦࡦ࠱ࠦࢪ"))
time.sleep(3)
sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡴࡈࡶࡷ࠶ࡲ࠯ࠢࡄࡲ࠵ࡳࡡ࠲ࡻࠣࡨ࠸࡬ࡴࡦࡥࡷࡩࡩ࠴ࠢࢫ"))
time.sleep(2)
sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡵࡉࡷ࠹࠳ࡳ࠲ࡵ࠲ࠥࡇ࡮࠱࡯࠵࠷࡫࠷ࡹࠡࡦ࠶ࡪࡹ࡫ࡣ࠱ࡺ࠷࠹ࡹ࡫ࡤ࠯ࠤࢬ"))
time.sleep(1)
sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡶࡊࡾࡦ࠵ࡴ࠶࠷ࡷ࠶ࡲ࠯ࠢࡄ࠶࠸ࡾ࡮࠱࡯࠵࠷࡫࠷ࡹࡹ࠶ࡤࠤࡩ࠹ࡦࡵ࠲ࡩࡩࡨ࠶ࡸ࠵࠷ࡷࡩ࠵࠽ࡡࡤࡦ࠱ࠦࢭ"))
time.sleep(.5)
sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡷࡋࡸࡧ࠶ࡵ࠷࠸ࡸ࠰ࡳ࠵ࡻࡪ࠳ࠦࡁ࠳࠵ࡻࡲ࠵࠷ࡸࡧ࡯࠵࠷࡫࠷ࡹࡹ࠶ࡤࠤࡩ࠹ࡦࡵ࠲ࡩࡩ࠵ࡾࡣ࠱ࡺ࠷࠹ࡹ࡫࠰࠸ࡣࡦ࠵࠷ࡾࡤ࠯ࠤࢮ"))
time.sleep(.25)
sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡸࡅ࡜࡞ࡻࡪ࠹࠵࡛ࡳ࠵࠶ࡶ࠵࠶࠰ࡳ࠵ࡻ࡟ࡢ࡬࠮ࠡࡃ࠵࠷ࡽࡴࡻ࠱࠳ࡻࡪࡲࢁࡻ࠺࠴࠶ࡪ࠶ࡿࡸ࠵ࡣࠣࡨ࠸࡬ࡴ࡜࠲ࢀࢁ࠵࡬ࡥ࠱ࡺࡦ࠴ࡽ࠺࠵ࡵࡧࡾࢁ࠵࠽ࡡࡤ࠳࠵ࡼࡩ࠴ࠢࢯ"))
time.sleep(.125)
clear()
time.sleep(3)
l11l_opy_(l1l11l_opy_ (u"࡚ࠧࡨࡳࡱࡸ࡫࡭ࠦࡴࡩࡧࠣࡶ࡮࡬ࡴࠡࡱࡩࠤࡹ࡮ࡥࠡࡲࡲࡶࡹࡧ࡬࠭ࠢࡷ࡬ࡪࠦࡩ࡯ࡵ࡬ࡨࡪࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡴࡰࡹࡨࡶ࠳ࠨࢰ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠨࠠࠡࡃࡷࠤࡹ࡮ࡥࠡࡥࡨࡲࡹ࡫ࡲ࠭ࠢࡰ࡭ࡱࡲࡩࡰࡰࡶࠤࡴ࡬ࠠࡤࡱࡱࡲࡪࡩࡴࡪࡱࡱࡷࠥ࡯࡮ࠡࡣࠣࡱࡦࡹࡳࡪࡸࡨࠤࡨࡵ࡬ࡶ࡯ࡱ࠲ࠥࠦࡆࡳࡣࡦࡸࡦࡲࡩࡻࡧࡧ࠰ࠥࡶ࡯࡭ࡻࡰࡳࡷࡶࡨࡪࡥࠣࡱࡪࡺࡡ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࡶࠤࡲࡧ࡮ࡪࡨࡨࡷࡹ࡫ࡤࠡ࡫ࡱࠤࡦࠦࡲࡶࡵ࡫ࠤࡴ࡬ࠠ࡯ࡱ࡬ࡷࡪ࠴ࠢࢱ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠢࠡࠢࡗࡶࡺ࡫ࠠࡳࡣࡱࡨࡴࡳ࡮ࡦࡵࡶ࠲ࠧࢲ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡇࡢࡰࡸࡨ࠰ࠥࡧࠠ࡯ࡧࡲࡲࠥ࡬࡬ࡢࡵ࡫ࠤࡴ࡬ࠠ࡭࡫ࡪ࡬ࡹ࡯࡮ࡨ࠰ࠥࢳ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠤࠣࠤࡓࡵࠠࡵࡪࡸࡲࡩ࡫ࡲࠡࡨࡲࡰࡱࡵࡷࡴ࠰ࠥࢴ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡃࡧࡩࡳࡷ࡫ࠠࡵࡪࡨࠤࡨࡵ࡬ࡶ࡯ࡱ࠰ࠥࡧࠠࡱࡣ࡬ࡶࠥࡵࡦࠡࡱ࡯ࡨࠥࡺࡥࡳ࡯࡬ࡲࡦࡲࡳ࠯ࠤࢵ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠦࠥࠦࡁࡳࡶ࡬ࡪࡦࡩࡴࡴࠢࡲࡪࠥࡺࡨࡦࠢࡳ࡬ࡾࡹࡩࡤࡣ࡯ࠤ࡮ࡴࠠࡵࡪࡨࠤࡼࡵࡲ࡭ࡦࠣࡳ࡫ࠦࡴࡩࡧࠣࡨ࡮࡭ࡩࡵࡣ࡯࠲ࠧࢶ"))
sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡡࡴࠢࢷ"))
l1llll_opy_ = 0
l11111l_opy_ = 0
l1llll1l_opy_ = 0
l11ll_opy_ = 0
while 1:
	if (l11ll_opy_ == 1):
		break
	time.sleep(2)
	sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮ࠣࢸ"))
	sleepl_opy_(l1l11l_opy_ (u"ࠢࡅࡱࠣࡽࡴࡻࠠࡢࡲࡳࡶࡴࡧࡣࡩࠢࡷ࡬ࡪࠦ࡬ࡦࡨࡷࠤࡹ࡫ࡲ࡮࡫ࡱࡥࡱ࠲ࠠࡰࡴࠣࡸ࡭࡫ࠠࡳ࡫ࡪ࡬ࡹࠦࡴࡦࡴࡰ࡭ࡳࡧ࡬ࡀࠢࠥࢹ"))
	l1llll11_opy_ = input()
	if ( ( l1l11l_opy_ (u"ࠣ࡮ࡨࡪࡹࠨࢺ") in l1llll11_opy_ ) or ( l1l11l_opy_ (u"ࠤ࡯ࠦࢻ") in l1llll11_opy_ ) or (l1l11l_opy_ (u"ࠥࡐࡪ࡬ࡴࠣࢼ") in l1llll11_opy_) ):
		sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱ࡝ࡴࡻࠠࡢࡲࡳࡶࡴࡧࡣࡩࠢࡷ࡬ࡪࠦ࡬ࡦࡨࡷࠤࡹ࡫ࡲ࡮࡫ࡱࡥࡱࠦࡡ࡯ࡦࠣࡴࡷ࡫ࡳࡴࠢࡷ࡬ࡪࠦࡰࡰࡹࡨࡶࠥࡱࡥࡺ࠰࠱࠲ࠧࢽ"))
		time.sleep(3)
		sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡡࡴ࡜࡯ࠤࢾ"))
		sys.stdout.write(l1l11l_opy_ (u"ࠨ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲ࠨࢿ"))
		sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰࠥࣀ"))
		sleepl_opy_(l1l11l_opy_ (u"ࠣࡋࡒࡍࠥࡏ࡮ࡵࡴࡤࡲࡪࡺࠠࡕࡧࡵࡱ࡮ࡴࡡ࡭ࠤࣁ"))
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡎࡴࡩࡵ࡫ࡤࡸ࡮ࡴࡧࠡࡹࡤ࡯ࡪࠦࡳࡦࡳࡸࡩࡳࡩࡥ࠯࠰࠱ࠦࣂ"))
		time.sleep(3)
		sleepl_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍࡱࡤࡨ࡮ࡴࡧࠡࡑࡖ࠲࠳࠴ࠢࣃ"))
		time.sleep(2)
		sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡝ࡠ࠱ࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞࠯࡞ࡡ࠲ࡡ࡝࠮࡝ࡠ࠱ࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞࠯࡞ࡡ࠲ࡡ࡝ࠣࣄ"))
		time.sleep(2)
		while 1:
			time.sleep(3)
			sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡡࡴࡅ࡯ࡶࡨࡶࠥࡊࡥࡴ࡫ࡵࡩࡩࠦࡁࡤࡶ࡬ࡳࡳࡀࠢࣅ"))
			sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡐࡔࡍࡉࡏࠢࡲࡶࠥࡋࡘࡊࡖ࡟ࡲ࠿ࡀࠢࣆ"))
			l1llllll_opy_ = input()
			if ( (l1l11l_opy_ (u"ࠢࡍࡑࡊࡍࡓࠨࣇ") in l1llllll_opy_) or (l1l11l_opy_ (u"ࠣࡎࡲ࡫࡮ࡴࠢࣈ") in l1llllll_opy_) or (l1l11l_opy_ (u"ࠤ࡯ࡳ࡬࡯࡮ࠣࣉ") in l1llllll_opy_) ):
				sleepl_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡓࡰࡪࡧࡳࡦࠢࡖࡩࡱ࡫ࡣࡵࠢࡏࡳ࡬࡯࡮ࠡࡃࡦࡧࡴࡻ࡮ࡵ࠼ࠣࠦ࣊"))
				time.sleep(1)
				sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡋࡱࡩࡹࠦࡁࡥ࡯࡬ࡲࡡࡴࡥ࡭࡮࡬ࡳࡹࡢ࡮ࡴࡶࡲࡶࡲࡢ࡮ࡓ࡞ࡱࡋࡺ࡫ࡳࡵ࡞ࡱࡠࡳࡋࡘࡊࡖ࡟ࡲࡡࡴ࡜࡯࠼࠽ࠦ࣋"))
				l11l1l_opy_ = input()
				if ( (l1l11l_opy_ (u"ࠧࡋࡘࡊࡖࠥ࣌") in l11l1l_opy_ ) or (l1l11l_opy_ (u"ࠨࡅࡹ࡫ࡷࠦ࣍") in l11l1l_opy_) or (l1l11l_opy_ (u"ࠢࡦࡺ࡬ࡸࠧ࣎") in l11l1l_opy_) ):
					break
				sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡋ࡮ࡵࡧࡵࠤࡵࡧࡳࡴࡹࡲࡶࡩࠦࡦࡰࡴ࣏ࠣࠦ"))
				sleepl_opy_(l11l1l_opy_)
				sleepl_opy_(l1l11l_opy_ (u"ࠤ࠽ࠤࡡࡴ࡜࡯࠼࠽࣐ࠦ"))
				sleepll_opy_ = input()
				if ( (l1l11l_opy_ (u"ࠥࡋ࡚ࡋࡓࡕࠤ࣑") in l11l1l_opy_ ) or (l1l11l_opy_ (u"ࠦࡌࡻࡥࡴࡶ࣒ࠥ") in l11l1l_opy_) or (l1l11l_opy_ (u"ࠧ࡭ࡵࡦࡵࡷ࣓ࠦ") in l11l1l_opy_ ) ):
					if (l1l11l_opy_ (u"ࠨࡰࡢࡵࡶࡻࡴࡸࡤࠣࣔ") in sleepll_opy_ ):
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑࡵࡧࡪࡰࠣࡅࡨࡩࡥࡱࡶࡨࡨ࠳ࠨࣕ"))
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠣࠢࡌࡲ࡮ࡺࡩࡢࡶ࡬ࡲ࡬ࠦࡓࡦࡵࡶ࡭ࡴࡴࠠࡔࡪࡨࡰࡱ࠴࠮࠯ࠤࣖ"))
						time.sleep(2)
						sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡔࡺࡲࡨࠤࠬ࡮ࡥ࡭ࡲࠪࠤ࡫ࡵࡲࠡࡣࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡤࡱࡰࡱࡦࡴࡤࡴ࡞ࡱࡠࡳࡢ࡮ࠣࣗ"))
						l1lllll1_opy_ = l1l11l_opy_ (u"ࠥࡋࡺ࡫ࡳࡵࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨࠨࠥࠨࣘ")
						l11ll1_opy_ = 1
						while 1:
							sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࠤࣙ"))
							sys.stdout.write(l1lllll1_opy_)
							l1lll11_opy_ = input()
							if ( (l1l11l_opy_ (u"ࠧ࡮ࡥ࡭ࡲࠥࣚ") in l1lll11_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡅࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡃࡰ࡯ࡰࡥࡳࡪࡳ࠻࡞ࡱࡠࡳ࡮ࡥ࡭ࡲࠣ࠱࡙ࠥࡨࡰࡹࡶࠤࡹ࡮ࡩࡴࠢࡰࡩࡳࡻࠠ࡝ࡰ࡯ࡷࠥ࠳ࠠࡍ࡫ࡶࡸࡸࠦࡣࡰࡰࡷࡩࡳࡺࡳࠡࡱࡩࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡝ࡰࡦࡨࠥࡂࡤࡪࡴࡨࡧࡹࡵࡲࡺࡰࡤࡱࡪࡄࠠ࠮ࠢࡆ࡬ࡦࡴࡧࡦࡵࠣࡻࡴࡸ࡫ࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡝ࡰࡳࡥࡷࠦ࠭ࠡࡏࡲࡺࡪࡹࠠࡵࡱࠣࡴࡦࡸࡥ࡯ࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡜࡯ࡥࡤࡸࠥࡂࡦࡪ࡮ࡨࡲࡦࡳࡥ࠿ࠢ࠰ࠤࡉ࡯ࡳࡱ࡮ࡤࡽࡸࠦࡣࡰࡰࡷࡩࡳࡺࡳࠡࡱࡩࠤ࡫࡯࡬ࡦࠢ࡟ࡲࡪࡾࡩࡵࠢ࠰ࠤࡑࡵࡧࡰࡷࡷࠤࡴ࡬ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣࣛ"))
							if ( (l1l11l_opy_ (u"ࠢࡦࡺ࡬ࡸࠧࣜ") in l1lll11_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡚ࡥࡳ࡯࡬ࡲࡦࡺࡩ࡯ࡩࠣࡷࡪࡹࡳࡪࡱࡱ࠲࠳࠴ࠢࣝ"))
								break
							if (l1lllll1_opy_ == l1l11l_opy_ (u"ࠤࡊࡹࡪࡹࡴࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧࠧࠤࠧࣞ")):
								if (l1l11l_opy_ (u"ࠥࡰࡸࠨࣟ") in l1lll11_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠾ࠧ࣠"))
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡪࡹࡪࡹࡴࠡ࠯࠰ࠤࡩ࡯ࡲ࡝ࡰ࡟ࡲࡵࡻࡢ࡭࡫ࡦࠤ࠲࠳ࠠࡥ࡫ࡵࡠࡳࡢ࡮ࡦ࡮࡯࡭ࡴࡺࠠ࠮࠯ࠣࡨ࡮ࡸ࡜࡯࡞ࡱࡷࡴࡸࡲࡦࡰࡷࡳࠥ࠳࠭ࠡࡦ࡬ࡶࡡࡴ࡜࡯ࡵࡷࡳࡷࡳࠠ࠮࠯ࠣࡨ࡮ࡸ࡜࡯࡞ࡱࡥࡩࡳࡩ࡯ࠢ࠰࠱ࠥࡪࡩࡳࠤ࣡"))
								if (l1l11l_opy_ (u"ࠨࡰࡢࡴࠥ࣢") in l1lll11_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰࡈࡶࡷࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡰࡪࠤࡩ࡯ࡲࠡࠩ࠲ࠫ࠿ࠦࡁࡤࡥࡨࡷࡸࠦࡤࡦࡰ࡬ࡩࡩ࠴ࣣࠢ"))
								if (l1l11l_opy_ (u"ࠣࡥࡧࠦࣤ") in l1lll11_opy_):
									if (l1l11l_opy_ (u"ࠤࡪࡹࡪࡹࡴࠣࣥ") in l1lll11_opy_):
										l11ll1_opy_ = 2
									if (l1l11l_opy_ (u"ࠥࡴࡺࡨ࡬ࡪࡥࣦࠥ") in l1lll11_opy_):
										l11ll1_opy_ = 3
									if ((l1l11l_opy_ (u"ࠦࡸࡺ࡯ࡳ࡯ࠥࣧ") in l1lll11_opy_) or (l1l11l_opy_ (u"ࠧࡧࡤ࡮࡫ࡱࠦࣨ") in l1lll11_opy_) or (l1l11l_opy_ (u"ࠨࡥ࡭࡮࡬ࡳࡹࠨࣩ") in l1lll11_opy_) or (l1l11l_opy_ (u"ࠢࡴࡱࡵࡶࡪࡴࡴࡰࠤ࣪") in l1lll11_opy_)):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡉࡷࡸ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹ࠯ࠢࡄࡧࡨ࡫ࡳࡴࠢࡧࡩࡳ࡯ࡥࡥ࠰ࠥ࣫"))
							if (l1lllll1_opy_ == l1l11l_opy_ (u"ࠤࡊࡹࡪࡹࡴࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲࡫ࡺ࡫ࡳࡵࠦࠣࠦ࣬")):
								if (l1l11l_opy_ (u"ࠥࡰࡸࠨ࣭") in l1lll11_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠳࡬ࡻࡥࡴࡶ࠽࣮ࠦ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡧࡩࡸࡱࡴࡰࡲࠣ࠱࠲ࠦࡤࡪࡴ࡟ࡲࡡࡴࡤࡰࡥࡸࡱࡪࡴࡴࡴࠢ࠰࠱ࠥࡪࡩࡳࠤ࣯"))
								if (l1l11l_opy_ (u"ࠨࡣࡥࠤࣰ") in l1lll11_opy_):
									if (l1l11l_opy_ (u"ࠢࡥࡧࡶ࡯ࡹࡵࡰࣱࠣ") in l1lll11_opy_):
										l11ll1_opy_ = 4
									if (l1l11l_opy_ (u"ࠣࡦࡲࡧࡺࡳࡥ࡯ࡶࡶࣲࠦ") in l1lll11_opy_):
										l11ll1_opy_ = 5
								if (l1l11l_opy_ (u"ࠤࡳࡥࡷࠨࣳ") in l1lll11_opy_):
									l11ll1_opy_ = 1
							if (l1lllll1_opy_ == l1l11l_opy_ (u"ࠥࡋࡺ࡫ࡳࡵࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡵࡻࡢ࡭࡫ࡦࠨࠥࠨࣴ")):
								if (l1l11l_opy_ (u"ࠦࡱࡹࠢࣵ") in l1lll11_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯ࡩࡱࡰࡩ࠴ࡶࡵࡣ࡮࡬ࡧ࠿ࠨࣶ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠨࠢࣷ"))
								if (l1l11l_opy_ (u"ࠢࡱࡣࡵࠦࣸ") in l1lll11_opy_):
									l11ll1_opy_ = 1
							if (l1lllll1_opy_ == l1l11l_opy_ (u"ࠣࡉࡸࡩࡸࡺࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡪࡹࡪࡹࡴ࠰ࡦࡨࡷࡰࡺ࡯ࡱࣹࠦࠣࠦ")):
								if (l1l11l_opy_ (u"ࠤ࡯ࡷࣺࠧ") in l1lll11_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠲࡫ࡺ࡫ࡳࡵ࠱ࡧࡩࡸࡱࡴࡰࡲ࠽ࠦࣻ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡥࡤࡰࡪࡴࡤࡢࡴ࠱ࡸࡽࡺࠠ࠮࠯ࠣࡪ࡮ࡲࡥࠣࣼ"))
								if (l1l11l_opy_ (u"ࠧࡩࡡࡵࠤࣽ") in l1lll11_opy_):
									if (l1l11l_opy_ (u"ࠨࡣࡢ࡮ࡨࡲࡩࡧࡲࠣࣾ") in l1lll11_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯ࡥࡸ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࡧࡦࡲࡥ࡯ࡦࡤࡶ࠳ࡺࡸࡵ࠰࠱࠲ࠧࣿ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࡈࡷࡨࡷࡹࠦࡕࡴࡧࡵࠤࡆࡩࡣࡰࡷࡱࡸࠥࡉࡡ࡭ࡧࡱࡨࡦࡸࠢऀ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡅࡷࡧࡱࡸࠥ࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲ࠦࡄࡢࡶࡨࠤ࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯ࠣࡒࡴࡺࡥࡴࠤँ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡑ࡮ࡤࡲࡪࡺࡡࡳ࡫ࡸࡱࠥ࡜ࡩࡴ࡫ࡷࠤࠥࠦࠠ࠲ࠢࡄࡔࡗࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡓ࠵ࡁࠣं"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡒ࡯ࡥࡳࡴࡩ࡯ࡩࠣࡑࡪ࡫ࡴࡪࡰࡪࠤࠥࠦࠠࠡ࠴࠳ࠤࡒࡇࡒࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡈࡲࡪࡰࡪࠤࡊࡲ࡬ࡪࡱࡷࠫࡸࠦࡰࡳࡧࡶࡩࡳࡺࡡࡵ࡫ࡲࡲࠧः"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡖࡽࡸࡺࡥ࡮ࠢࡘࡴࡩࡧࡴࡦࠢࠣࠤࠥࠦࠠࠡࠢ࠴࠼ࠥࡓࡁࡓࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡃࡩࡧࡦ࡯ࠥࡩ࡯࡮ࡲ࡯࡭ࡦࡴࡣࡦࠢࡧࡳࡨࠨऄ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡆࡦࡩ࡫ࡶࡲࠣࡑ࡮࡭ࡲࡢࡶ࡬ࡳࡳࠦࠠࠡࠢࠣ࠵࠽ࠦࡍࡂࡔࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡏ࠱ࡄࠦअ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡒࡻࡳࡦࡷࡰࠤ࡛࡯ࡳࡪࡶࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠶࠻ࠠࡎࡃࡕࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡐࡨࡩࡩࠦࡁࡱࡱ࡯ࡰࡴࠦ࠱࠲ࠢࡶࡴࡪ࡫ࡣࡩࠢࡧࡳࡨࠨआ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙ࡹࡴࡶࡨࡱ࡛ࠥࡰࡥࡣࡷࡩࠥࠦࠠࠡࠢࠣࠤࠥ࠷࠱ࠡࡏࡄࡖࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡࡥࡲࡱࡵࡲࡩࡢࡰࡦࡩࠥࡪ࡯ࡤࠤइ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡁࡨࡧࡱࡧࡾࠦࡍࡦࡧࡷ࡭ࡳ࡭ࠠࠡࠢࠣࠤࠥࠦࠠ࠺ࠢࡐࡅࡗࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡓ࠵ࡁࠣई"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࠧउ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮ࡇࡒࡊ࠲࠳࠭ࠣऊ"))
								if (l1l11l_opy_ (u"ࠧࡶࡡࡳࠤऋ") in l1lll11_opy_):
									l11ll1_opy_ = 2
							if (l1lllll1_opy_ == l1l11l_opy_ (u"ࠨࡇࡶࡧࡶࡸࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡨࡷࡨࡷࡹ࠵ࡤࡰࡥࡸࡱࡪࡴࡴࡴࠦࠣࠦऌ")):
								if (l1l11l_opy_ (u"ࠢ࡭ࡵࠥऍ") in l1lll11_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡒࡩࡴࡶ࡬ࡲ࡬ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࠲࡬ࡴࡳࡥ࠰ࡩࡸࡩࡸࡺ࠯ࡥࡱࡦࡹࡲ࡫࡮ࡵࡵ࠽ࠦऎ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡮ࡦࡸࡨࡶ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴ࡭ࡢ࡫࡯ࡲࡴࡺࡥࡴ࠰ࡷࡼࡹࠦ࠭࠮ࠢࡩ࡭ࡱ࡫࡜࡯࡞ࡱࡶࡪࡳࡩ࡯ࡦࡨࡶ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴ࡬ࡰࡩ࡬ࡲ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴࠢए"))
								if (l1l11l_opy_ (u"ࠥࡧࡦࡺࠢऐ") in l1lll11_opy_):
									if (l1l11l_opy_ (u"ࠦࡳ࡫ࡶࡦࡴࠥऑ") in l1lll11_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡࡰࡨࡺࡪࡸ࠮ࡵࡺࡷ࠲࠳࠴ࠢऒ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳ࡙࡮ࡨࡴࠣࡹࡳ࡬ࠠࡣࡧࡴࡲࡻࡧࡲࡲࠢࡪࡹࡳ࡭ࠠࡨࡷࡵࠤࡿࡸࡡࠡ࡬ࡸࡦࠥࡰࡲࡢࡩࠣ࡫ࡧࠦࡧࡶࡴࠣࡾࡧࡨࡡࠡࡩࡥࠤࡷࡱࡣࡺࡤࡨࡶࠥࡼࡡࠡࡥࡵࡲࡵࡸࠠ࡫ࡸࡼࡽࠥ࡬ࡧ࡯࡮ࠣࡦࡦࠦࡧࡶࡴࠣࡾࡧࡨࡡࠡࡩࡥࠤࡪࡸࡦࡨࠢࡹࡥࠥࡩࡲ࡯ࡲࡵ࠲ࠧओ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡌࡻࡲࡧࡴࠣࡳࡪࡴࡩࡳࠢࡽࡶࡦ࠲ࠠࡂࡴࡹࡽࠥࡔࡥࡻࡨࡪࡩࡧࡧࡴࠡࡰࡤࡵࠥࡘࡱ࡫ࡸࡤࠤࡓࡿࡱࡦࡸࡤ࠰ࠥࡾࡡࡣ࡬ࠣ࡫ࡺࡴࡧࠡࡩࡸࡶࡪࡸࠠࡷࡨࠣࡥࡧࠦࡵࡣࡥࡵࠤࡸࡨࡥࠡࡩࡸࡶࡻ࡫ࠠࡦࡴࡳࡦ࡮ࡸࡥ࡭࠰ࠣࡓ࡭࡭ࠠࡨࡷࡵࡰࠥࡴࡹࡧࡤࠣࡼࡦࡨࡪࠡࡩࡸࡲ࡬ࠦࡧࡶࡴࡨࡶࠥࡼࡦࠡࡷࡥࡧࡷࠦࡳࡣࡧࠣࡾࡳࡧࡸࡷࡣࡴࠤࡻࡧࠠࡨࡷࡵࡺࡪࠦࡦ࡯ࡲࡨࡺࡸࡼࡰࡳ࠰ࠥऔ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡍࡵࡳࡨࡵࠤ࡬ࡰࡢࠡࡼࡵࡥࠥࡴࡥࡳࠢࡼࡲࡱࡼࡡࡵࠢࡴࡦ࡯ࡧࠠࡨࡷࡵࡺࡪࠦࡹࡷ࡫ࡵࡪࠥࡼࡡࠡࡼࡱࡥࡽࡼࡡࡲࠩࡩࠤࡿࡨࡦࡨࠢࡤࡦࡴࡿࡲࠡࡶࡥࡲࡾࡀࠠࡨࡷࡵࠤ࡫ࡸ࡮ࡦࡲࡸࠤࡸࡨࡥࠡࡩࡨ࡬࡬ࡻࠠ࡯ࡣࡴࠤ࡭ࡧࡱࡳࡧࡩ࡫ࡳࡧࡱࡷࡣࡷ࠲ࠧक"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡇࡶࡴ࡯ࠤ࡯ࡼࡹࡺࠢࡲࡶࠥࢀࡢࡩࡧࡤࡶࡶࠦ࡯࡭ࠢࡪࡹࡷࡼࡥࠡࡵࡱࡾࡻࡿࡶࡳࡨࠣࡲࡦࡷࠠࡴࡧࡹࡶࡦࡷࡦ࠼ࠢࡪࡹࡷࡲࠠ࡫ࡸࡼࡽࠥࡵࡲࠡࡼࡥ࡬ࡪࡧࡲࡲࠢࡲࡰࠥ࡭ࡵࡳࡸࡨࠤࡦࡴࡧࡷࡤࡤ࠿ࠥ࡭ࡵࡳ࡮ࠣ࡮ࡻࡿࡹࠡࡱࡵࠤࡿࡨࡨࡦࡣࡵࡵࠥࡵ࡬ࠡࡩࡸࡶࠥࡩࡲࡣࡥࡼࡶࠥࡨࡳࠡࡩࡸࡶࠥࡰࡢࡦࡻࡴ࠿ࠥ࡭ࡵࡳ࡮ࠣ࡮ࡻࡿࡹࠡࡱࡵࠤࡿࡨࡨࡦࡣࡵࡵࠥࡵ࡬ࠡࡰࠣ࡞ࡧ࡭ࡵࡳࡧࠣࡖࡳ࡫ࡧࡶࠢࡪࡹࡳ࡭ࠠࡲࡰࡨࡶࡶࠦࡦࡳࡣࡴࠤ࡬ࡰࡢࠡࡤࡶࠤࡺࡸࡥࠡࡨࡥࡥ࡫ࠦࡶࡢࡩࡥࠤ࡬ࡻࡲࠡࡪࡤࡼࡦࡨࡪࡢ࠰ࠥख"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡗࡣࠣ࡫ࡺࡸࡶࡦࠢࡵ࡯ࡨࡿࡢࡦࡰࡪࡺࡧࡧࠬࠡࡩࡸࡶࡱࠦࡦࡨࡸࡨࡩࡷࡷࠠࡨࡷࡵࠤࡨࡸࡢࡤࡻࡵࠤࡧࡹࠠࡨࡷࡵࠤ࡯ࡨࡥࡺࡳࠣ࡫ࡧࠦࡳࡳࡴࡼࠤࡳ࡬ࠠࡣࡣࡵ࠿ࠥࡼࡡࠡࡩࡸࡶࡻ࡫ࠠࡧࡰࡳࡩࡻࡹࡶࡱࡴ࠯ࠤ࡬ࡻࡲ࡭ࠢࡲࡺࡦࡷࠠࡻࡤࡨࡶࠥ࡭ࡶࡵࡷࡪࡽࡱࠦࡧࡶࡴࠣࡳࡪࡨࡧࡶࡴࡨࡹࡧࡨࡱࠡࡤࡶࠤࡿࡴࡡ࠯ࠤग"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘࡤࠤࡳࡧࡰࡷࡴࡤ࡫ࠥࡷ࡮࡭ࡨ࠯ࠤࡿࡸࡡࠡࡻࡥࡦࡽࡸࡱࠡࡰࡪࠤ࡫࡭࡮ࡦࡨࠣࡲࡦࡷࠠࡧࡰ࡭ࠤ࡬ࡻࡲࡷࡧࠣࡹࡷ࡫ࡢࡳࡨࠣࡺࡦࠦࡧࡶࡴࠣ࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠲ࠥ࡜ࡡࠡࡼࡥࡵࡷ࡫ࡡࠡࡩࡹࡾࡷ࡬ࠬࠡ࡬ࡵࠤࡶࡨࠠࡻࡪࡳࡹࠥ࡭ࡵࡳࠢࡩࡲࡿࡸࠬࠡࡱ࡫࡫ࠥࡨࡨࡦࠢࡸࡶࡪࡨࡲࡧࠢࡱࡩࡷࠦࡲࡤࡸࡳࠤࡿࡸࡡࠡࡤࡶࠤࡸࡿࡲࡧࡷࠣࡲࡦࡷࠠࡰࡻࡥࡦࡶ࠴ࠢघ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡅ࡫ࡺࡸࡥࡧࠢ࡭ࡺࡾࡿࠠࡴࡤࡼࡽࡧࡰࠬࠡࡰࡤࡵࠥ࡬ࡨࡦࡴࡼࡰࠥࡹࡶࡢࡳࠣ࡫ࡺࡸࡶࡦࠢ࡭ࡲࡱࠦࡵࡣࡼࡵ࠲ࠥࡠ࡮ࡢࠩࡩࠤ࡫ࡸ࡮ࡦࡲࡸࠤ࡯ࡼࡹࡺࠢࡤࡦ࡬ࠦ࡯ࡳࠢࡴࡶࡦࡼࡲࡲ࠰ࠣࡓ࡭࡭ࠠࡨࡷࡵࡪࡷࠦࡺࡳࡣࠣ࡮ࡷ࡫ࡲࠡࡩࡸࡶࠥࡹࡶࡦࡨࡪ࠰ࠥࡴࡡࡲࠢࡪࡹࡷࡲࠠ࡫ࡸࡼࡽࠥ࡫ࡲࡻࡰࡹࡥࠥ࡭ࡵࡳࠢࡶࡦࡪࡸࡺࡣࡨࡪࠤࡻࡧࠠࡣࡪࡨࠤࡺࡸ࡮ࡦࡩࡩ࠲ࠧङ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡗࡧ࡫ࠠࡳ࡫ࡵࡩࡱࠦࡵࡩࡼࡱࡥࠥࡵࡲࡷࡣࡷࠤ࡯ࡻࡢࠡࡻࡥࡦࡽ࡬ࠠࡩࡥࠣࡲ࡬ࠦࡧࡶࡴࠣࡾࡧࡨࡡࠡࡸࡤࠤ࡬ࡻࡲࠡࡣࡹࡸࡺ࡭ࡦࠡࡩࡥࠤࡵࡨࡺࡳࠢ࡭ࡺࡾࡿࠠࡹࡣࡥ࡮ࠥ࡭ࡵ࡯ࡩࠣ࡫ࡺࡸࡥࡳࠢࡹࡪࠥ࡬ࡢࡻࡴࠣࡴࡧ࡫ࡡࡳࡧࠣࡦࡸࠦ࡮ࡢࡤࡪࡹࡷ࡫ࠠ࡫ࡤࡨࡽࡶࠦࡧࡶࡰࡪࠤࡻ࡬ࠠࡴࡤࡨࡶ࡮ࡸࡥࠡࡼࡱࡥࡽࡼࡡࡲ࠰ࠥच"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦछ"))
									if (l1l11l_opy_ (u"ࠣ࡯ࡤ࡭ࡱࡴ࡯ࡵࡧࡶࠦज") in l1lll11_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡳࡡࡪ࡮ࡱࡳࡹ࡫ࡳ࠯ࡶࡻࡸ࠳࠴࠮ࠣझ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡓࡶࡴࡩ࡭ࡢ࡫࡯ࠤࡲࡧࡩ࡭ࡵ࡯ࡳࡹࠦࡳࡦࡴࡹࡩࡷࠨञ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘࡨࡶࡸ࡯࡯࡯ࠢ࠶࠲࠶࠴࠵ࠣट"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲ࡚ࡖࡄࡂࡖࡈࠤࡓࡋࡅࡅࡇࡇࠤ࠲ࠦࡶ࠯ࠢ࠶࠲࠷࠴࠰ࠡࡃ࡙ࡅࡎࡒࡁࡃࡎࡈࠦठ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥड"))
									if (l1l11l_opy_ (u"ࠢࡳࡧࡰ࡭ࡳࡪࡥࡳࠤढ") in l1lll11_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࡷ࡫࡭ࡪࡰࡧࡩࡷ࠴ࡴࡹࡶ࠱࠲࠳ࠨण"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࡆࡤࡸࡪࡀࠠ࠳࠺ࠣࡊࡊࡈࠢत"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡈࡷࡨࡷࡹࠦࡡࡤࡥࡲࡹࡳࡺࠠࡤࡴࡨࡥࡹ࡫ࡤࠡࡱࡱࠤࡎࡴࡴࡳࡣࡱࡩࡹࠦࡴࡦࡴࡰ࡭ࡳࡧ࡬࠯ࠢࠣࡇ࡭ࡧ࡮ࡨࡧࠣࡨࡪ࡬ࡡࡶ࡮ࡷࠤࡵࡧࡳࡴࡹࡲࡶࡩ࠴ࠢथ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮ࡇࡒࡊ࠲࠳࠭ࠣद"))
									if (l1l11l_opy_ (u"ࠧࡲ࡯ࡨ࡫ࡱࠦध") in l1lll11_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠨࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡨ࡫ࡱ࠲ࡹࡾࡴ࠯࠰࠱ࠦन"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴࡉࡕ࠯ࡄࡈࡒࡏࡎࠡࡔࡨࡱ࡮ࡴࡤࡦࡴࠥऩ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡖࡥࡳࡵࡸࡥࡳࡺࠠࡵࡱࠣࡇࡴࡳࡰࡢࡰࡼࠤࡕࡵ࡬ࡪࡥࡼࠤࡑ࡫ࡴࡵࡧࡵࠤ࠶࠶࠭࠲࠻࠻࠾ࠥࡏࡔࠡࡕࡼࡷࡹ࡫࡭ࠡࡅࡵࡩࡩ࡫࡮ࡵ࡫ࡤࡰࠥࡓࡡ࡯ࡣࡪࡩࡲ࡫࡮ࡵ࠮ࠣࡴࡱ࡫ࡡࡴࡧࠣࡨࡴࠦࡎࡐࡖࠣࡷࡹࡵࡲࡦࠢ࡯ࡳ࡬࡯࡮ࠡࡦࡨࡸࡦ࡯࡬ࡴࠢࡩࡳࡷࠦࡰࡦࡴࡶࡳࡳࡧ࡬ࠡࡣࡦࡧࡴࡻ࡮ࡵࡵࠣࡳࡳࠦࡴࡩࡧࠣ࡫ࡺ࡫ࡳࡵࠢࡤࡧࡨࡵࡵ࡯ࡶࠣ࡭ࡳࡹࡴࡢࡰࡦࡩ࠳ࠨप"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡄࡢࡶࡨࡨ࠿ࠦ࠱ࠡࡈࡈࡆࠧफ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢब"))
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣभ") in l1lll11_opy_):
									l11ll1_opy_ = 3
							if (l11ll1_opy_ == 1):
								l1lllll1_opy_ = l1l11l_opy_ (u"ࠧࡍࡵࡦࡵࡷࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪࠪࠠࠣम")
							if (l11ll1_opy_ == 2):
								l1lllll1_opy_ = l1l11l_opy_ (u"ࠨࡇࡶࡧࡶࡸࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡨࡷࡨࡷࡹࠪࠠࠣय")
							if (l11ll1_opy_ == 3):
								l1lllll1_opy_ = l1l11l_opy_ (u"ࠢࡈࡷࡨࡷࡹࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡲࡸࡦࡱ࡯ࡣࠥࠢࠥर")
							if (l11ll1_opy_ == 4):
								l1lllll1_opy_ = l1l11l_opy_ (u"ࠣࡉࡸࡩࡸࡺࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡪࡹࡪࡹࡴ࠰ࡦࡨࡷࡰࡺ࡯ࡱࠦࠣࠦऱ")
							if (l11ll1_opy_ == 5):
								l1lllll1_opy_ = l1l11l_opy_ (u"ࠤࡊࡹࡪࡹࡴࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲࡫ࡺ࡫ࡳࡵ࠱ࡧࡳࡨࡻ࡭ࡦࡰࡷࡷࠩࠦࠢल")
					else:
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡴࡵࡳࡷ࠴ࠠࡊࡰࡹࡥࡱ࡯ࡤࠡࡒࡤࡷࡸࡽ࡯ࡳࡦࠥळ"))
				elif ( (l1l11l_opy_ (u"ࠦࡎࡔࡅࡕࠢࡄࡈࡒࡏࡎࠣऴ") in l11l1l_opy_) or (l1l11l_opy_ (u"ࠧ࡯࡮ࡦࡶࠣࡥࡩࡳࡩ࡯ࠤव") in l11l1l_opy_) or (l1l11l_opy_ (u"ࠨࡉ࡯ࡧࡷࠤࡆࡪ࡭ࡪࡰࠥश") in l11l1l_opy_) ):
					if ( l1l11l_opy_ (u"ࠢࡤࡱࡱࡷࡹ࡫࡬࡭ࡣࡷ࡭ࡴࡴࡳࠣष") in sleepll_opy_ ):
						time.sleep(2)
						l11l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡒ࡯ࡨ࡫ࡱࠤࡆࡩࡣࡦࡲࡷࡩࡩ࠴ࠢस"))
						time.sleep(3)
						if (l1llll_opy_ == 0):
							l1llll_opy_ = 1
							clear()
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠤࡖ࡭ࡲࡶ࡬ࡦࠢࡰ࡭ࡸࡺࡡ࡬ࡧࡶࠤࡲࡧ࡫ࡦࠢࡶࡱࡦࡲ࡬ࠡࡨ࡯ࡥࡼࡹࠠࡪࡰࠣࡦ࡮࡭ࠠࡴࡻࡶࡸࡪࡳࡳ࠯ࠤह"))
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡃࡧࡩࡳࡷ࡫ࠠࡺࡱࡸ࠰ࠥࡺࡨࡦࠢࡧࡥࡹࡧࠠࡤࡱ࡯ࡹࡲࡴࠠࡱࡷ࡯ࡷࡪࡹࠠࡣࡴ࡬࡫࡭ࡺ࡬ࡺ࠰ࠥऺ"))
							time.sleep(1)
							l11l_opy_(l1l11l_opy_ (u"ࠦࠥࠦࡁࡳࡱࡸࡲࡩࠦࡹࡰࡷ࠯ࠤࡹ࡮ࡥࠡࡪࡲࡶ࡮ࢀ࡯࡯ࠢࡪࡰࡴࡽࡳࠡࡴࡨࡨ࠳ࠨऻ"))
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡸ࡯࡯࡯ࡵࠣࡳ࡫ࠦࡴࡦࡴࡵࡳࡷࠦࡢࡶࡴࡱࠤ࡮ࡴࠠࡺࡱࡸࡶࠥࡶࡥࡳ࡫ࡳ࡬ࡪࡸࡡ࡭ࡵ࠱़ࠦ"))
							time.sleep(4)
							clear()
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠨࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡪࡰࡪࠤࡘ࡫ࡳࡴ࡫ࡲࡲ࡙ࠥࡨࡦ࡮࡯࠲࠳࠴ࠢऽ"))
						time.sleep(2)
						sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡙ࡿࡰࡦࠢࠪ࡬ࡪࡲࡰࠨࠢࡩࡳࡷࠦࡡࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࡜࡯࡞ࡱࡠࡳࠨा"))
						l11llll_opy_ = l1l11l_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪࠪࠠࠣि")
						sleep1l_opy_ = 1
						while 1:
							sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࠢी"))
							sys.stdout.write(l11llll_opy_)
							l111l1l_opy_ = input()
							if ( (l1l11l_opy_ (u"ࠥ࡬ࡪࡲࡰࠣु") in l111l1l_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡃࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡈࡵ࡭࡮ࡣࡱࡨࡸࡀ࡜࡯࡞ࡱ࡬ࡪࡲࡰࠡ࠯ࠣࡗ࡭ࡵࡷࡴࠢࡷ࡬࡮ࡹࠠ࡮ࡧࡱࡹࠥࡢ࡮࡭ࡵࠣ࠱ࠥࡒࡩࡴࡶࡶࠤࡨࡵ࡮ࡵࡧࡱࡸࡸࠦ࡯ࡧࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡢ࡮ࡤࡦࠣࡀࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࡮ࡢ࡯ࡨࡂࠥ࠳ࠠࡄࡪࡤࡲ࡬࡫ࡳࠡࡹࡲࡶࡰ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡢ࡮ࡱࡣࡵࠤ࠲ࠦࡍࡰࡸࡨࡷࠥࡺ࡯ࠡࡲࡤࡶࡪࡴࡴࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡡࡴࡣࡢࡶࠣࡀ࡫࡯࡬ࡦࡰࡤࡱࡪࡄࠠ࠮ࠢࡇ࡭ࡸࡶ࡬ࡢࡻࡶࠤࡨࡵ࡮ࡵࡧࡱࡸࡸࠦ࡯ࡧࠢࡩ࡭ࡱ࡫ࠠ࡝ࡰࡨࡼ࡮ࡺࠠ࠮ࠢࡏࡳ࡬ࡵࡵࡵࠢࡲࡪࠥࡹࡥࡴࡵ࡬ࡳࡳࠨू"))
							if ( (l1l11l_opy_ (u"ࠧ࡫ࡸࡪࡶࠥृ") in l111l1l_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡘࡪࡸ࡭ࡪࡰࡤࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯࠰࠱࠲ࠧॄ"))
								break
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠢࡊࡐࡈࡘࡆࡊࡍࡊࡐࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩࠩࠦࠢॅ")):
								if (l1l11l_opy_ (u"ࠣ࡮ࡶࠦॆ") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡌࡪࡵࡷ࡭ࡳ࡭ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࠳࡭ࡵ࡭ࡦ࠼ࠥे"))
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡨࡷࡨࡷࡹࠦ࠭࠮ࠢࡧ࡭ࡷࡢ࡮࡝ࡰࡳࡹࡧࡲࡩࡤࠢ࠰࠱ࠥࡪࡩࡳ࡞ࡱࡠࡳ࡫࡬࡭࡫ࡲࡸࠥ࠳࠭ࠡࡦ࡬ࡶࡡࡴ࡜࡯ࡵࡲࡶࡷ࡫࡮ࡵࡱࠣ࠱࠲ࠦࡤࡪࡴ࡟ࡲࡡࡴࡳࡵࡱࡵࡱࠥ࠳࠭ࠡࡦ࡬ࡶࠧै"))
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣॉ") in l111l1l_opy_):
									sleep1l_opy_ = 0
								if (l1l11l_opy_ (u"ࠧࡩࡤࠣॊ") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠨࡧࡶࡧࡶࡸࠧो") in l111l1l_opy_):
										sleep1l_opy_ = 2
									if (l1l11l_opy_ (u"ࠢࡱࡷࡥࡰ࡮ࡩࠢौ") in l111l1l_opy_):
										sleep1l_opy_ = 3
									if (l1l11l_opy_ (u"ࠣࡧ࡯ࡰ࡮ࡵࡴ्ࠣ") in l111l1l_opy_):
										sleep1l_opy_ = 6
									if (l1l11l_opy_ (u"ࠤࡶࡸࡴࡸ࡭ࠣॎ") in l111l1l_opy_):
										sleep1l_opy_ = 8
									if (l1l11l_opy_ (u"ࠥࡷࡴࡸࡲࡦࡰࡷࡳࠧॏ") in l111l1l_opy_):
										sleep1l_opy_ = 10
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠦࡎࡔࡅࡕࡃࡇࡑࡎࡔࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡪࡹࡪࡹࡴࠥࠢࠥॐ")):
								if (l1l11l_opy_ (u"ࠧࡲࡳࠣ॑") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡹࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠰ࡪࡲࡱࡪ࠵ࡧࡶࡧࡶࡸ࠿ࠨ॒"))
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡩ࡫ࡳ࡬ࡶࡲࡴࠥ࠳࠭ࠡࡦ࡬ࡶࡡࡴ࡜࡯ࡦࡲࡧࡺࡳࡥ࡯ࡶࡶࠤ࠲࠳ࠠࡥ࡫ࡵࠦ॓"))
								if (l1l11l_opy_ (u"ࠣࡥࡧࠦ॔") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠤࡧࡩࡸࡱࡴࡰࡲࠥॕ") in l111l1l_opy_):
										sleep1l_opy_ = 4
									if (l1l11l_opy_ (u"ࠥࡨࡴࡩࡵ࡮ࡧࡱࡸࡸࠨॖ") in l111l1l_opy_):
										sleep1l_opy_ = 5
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣॗ") in l111l1l_opy_):
									sleep1l_opy_ = 1
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠧࡏࡎࡆࡖࡄࡈࡒࡏࡎࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡴࡺࡨ࡬ࡪࡥࠧࠤࠧक़")):
								if (l1l11l_opy_ (u"ࠨ࡬ࡴࠤख़") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯ࡳࡵ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠱࡫ࡳࡲ࡫࠯ࡱࡷࡥࡰ࡮ࡩ࠺ࠣग़"))
									sys.stdout.write(l1l11l_opy_ (u"ࠣࠤज़"))
								if (l1l11l_opy_ (u"ࠤࡳࡥࡷࠨड़") in l111l1l_opy_):
									sleep1l_opy_ = 1
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠥࡍࡓࡋࡔࡂࡆࡐࡍࡓࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡩࡸࡩࡸࡺ࠯ࡥࡧࡶ࡯ࡹࡵࡰࠥࠢࠥढ़")):
								if (l1l11l_opy_ (u"ࠦࡱࡹࠢफ़") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯ࡩࡱࡰࡩ࠴࡭ࡵࡦࡵࡷ࠳ࡩ࡫ࡳ࡬ࡶࡲࡴ࠿ࠨय़"))
									sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡧࡦࡲࡥ࡯ࡦࡤࡶ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧࠥॠ"))
								if (l1l11l_opy_ (u"ࠢࡤࡣࡷࠦॡ") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠣࡥࡤࡰࡪࡴࡤࡢࡴࠥॢ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡩࡡ࡭ࡧࡱࡨࡦࡸ࠮ࡵࡺࡷ࠲࠳࠴ࠢॣ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡊࡹࡪࡹࡴࠡࡗࡶࡩࡷࠦࡁࡤࡥࡲࡹࡳࡺࠠࡄࡣ࡯ࡩࡳࡪࡡࡳࠤ।"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡹࡩࡳࡺࠠ࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭ࠡࡆࡤࡸࡪࠦ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࠥࡔ࡯ࡵࡧࡶࠦ॥"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡓࡰࡦࡴࡥࡵࡣࡵ࡭ࡺࡳࠠࡗ࡫ࡶ࡭ࡹࠦࠠࠡࠢ࠴ࠤࡆࡖࡒࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡎ࠰ࡃࠥ०"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡔࡱࡧ࡮࡯࡫ࡱ࡫ࠥࡓࡥࡦࡶ࡬ࡲ࡬ࠦࠠࠡࠢࠣ࠶࠵ࠦࡍࡂࡔࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡃࡴ࡬ࡲ࡬ࠦࡅ࡭࡮࡬ࡳࡹ࠭ࡳࠡࡲࡵࡩࡸ࡫࡮ࡵࡣࡷ࡭ࡴࡴࠢ१"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡘࡿࡳࡵࡧࡰࠤ࡚ࡶࡤࡢࡶࡨࠤࠥࠦࠠࠡࠢࠣࠤ࠶࠾ࠠࡎࡃࡕࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡅ࡫ࡩࡨࡱࠠࡤࡱࡰࡴࡱ࡯ࡡ࡯ࡥࡨࠤࡩࡵࡣࠣ२"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡈࡡࡤ࡭ࡸࡴࠥࡓࡩࡨࡴࡤࡸ࡮ࡵ࡮ࠡࠢࠣࠤࠥ࠷࠸ࠡࡏࡄࡖࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡑ࠳ࡆࠨ३"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡍࡶࡵࡨࡹࡲࠦࡖࡪࡵ࡬ࡸࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠱࠶ࠢࡐࡅࡗࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡒࡪ࡫ࡤࠡࡃࡳࡳࡱࡲ࡯ࠡ࠳࠴ࠤࡸࡶࡥࡦࡥ࡫ࠤࡩࡵࡣࠣ४"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡔࡻࡶࡸࡪࡳࠠࡖࡲࡧࡥࡹ࡫ࠠࠡࠢࠣࠤࠥࠦࠠ࠲࠳ࠣࡑࡆࡘࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡈ࡮ࡥࡤ࡭ࠣࡧࡴࡳࡰ࡭࡫ࡤࡲࡨ࡫ࠠࡥࡱࡦࠦ५"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡃࡪࡩࡳࡩࡹࠡࡏࡨࡩࡹ࡯࡮ࡨࠢࠣࠤࠥࠦࠠࠡࠢ࠼ࠤࡒࡇࡒࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡎ࠰ࡃࠥ६"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳ࠢ७"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥ८"))
								if (l1l11l_opy_ (u"ࠢࡱࡣࡵࠦ९") in l111l1l_opy_):
									sleep1l_opy_ = 2
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡧࡶࡧࡶࡸ࠴ࡪ࡯ࡤࡷࡰࡩࡳࡺࡳࠥࠢࠥ॰")):
								if (l1l11l_opy_ (u"ࠤ࡯ࡷࠧॱ") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠲࡫ࡺ࡫ࡳࡵ࠱ࡧࡳࡨࡻ࡭ࡦࡰࡷࡷ࠿ࠨॲ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡰࡨࡺࡪࡸ࠮ࡵࡺࡷࠤ࠲࠳ࠠࡧ࡫࡯ࡩࡡࡴ࡜࡯࡯ࡤ࡭ࡱࡴ࡯ࡵࡧࡶ࠲ࡹࡾࡴࠡ࠯࠰ࠤ࡫࡯࡬ࡦ࡞ࡱࡠࡳࡸࡥ࡮࡫ࡱࡨࡪࡸ࠮ࡵࡺࡷࠤ࠲࠳ࠠࡧ࡫࡯ࡩࡡࡴ࡜࡯࡮ࡲ࡫࡮ࡴ࠮ࡵࡺࡷࠤ࠲࠳ࠠࡧ࡫࡯ࡩࡡࡴ࡜࡯ࠤॳ"))
								if (l1l11l_opy_ (u"ࠧࡩࡡࡵࠤॴ") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠨ࡮ࡦࡸࡨࡶࠧॵ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯ࡥࡸ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࡲࡪࡼࡥࡳ࠰ࡷࡼࡹ࠴࠮࠯ࠤॶ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࡔࡰࡪࡶࠥࡻ࡮ࡧࠢࡥࡩࡶࡴࡶࡢࡴࡴࠤ࡬ࡻ࡮ࡨࠢࡪࡹࡷࠦࡺࡳࡣࠣ࡮ࡺࡨࠠ࡫ࡴࡤ࡫ࠥ࡭ࡢࠡࡩࡸࡶࠥࢀࡢࡣࡣࠣ࡫ࡧࠦࡲ࡬ࡥࡼࡦࡪࡸࠠࡷࡣࠣࡧࡷࡴࡰࡳࠢ࡭ࡺࡾࡿࠠࡧࡩࡱࡰࠥࡨࡡࠡࡩࡸࡶࠥࢀࡢࡣࡣࠣ࡫ࡧࠦࡥࡳࡨࡪࠤࡻࡧࠠࡤࡴࡱࡴࡷ࠴ࠢॷ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡇࡶࡴࡩࡶࠥࡵࡥ࡯࡫ࡵࠤࡿࡸࡡ࠭ࠢࡄࡶࡻࡿࠠࡏࡧࡽࡪ࡬࡫ࡢࡢࡶࠣࡲࡦࡷࠠࡓࡳ࡭ࡺࡦࠦࡎࡺࡳࡨࡺࡦ࠲ࠠࡹࡣࡥ࡮ࠥ࡭ࡵ࡯ࡩࠣ࡫ࡺࡸࡥࡳࠢࡹࡪࠥࡧࡢࠡࡷࡥࡧࡷࠦࡳࡣࡧࠣ࡫ࡺࡸࡶࡦࠢࡨࡶࡵࡨࡩࡳࡧ࡯࠲ࠥࡕࡨࡨࠢࡪࡹࡷࡲࠠ࡯ࡻࡩࡦࠥࡾࡡࡣ࡬ࠣ࡫ࡺࡴࡧࠡࡩࡸࡶࡪࡸࠠࡷࡨࠣࡹࡧࡩࡲࠡࡵࡥࡩࠥࢀ࡮ࡢࡺࡹࡥࡶࠦࡶࡢࠢࡪࡹࡷࡼࡥࠡࡨࡱࡴࡪࡼࡳࡷࡲࡵ࠲ࠧॸ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡈࡷࡵࡪࡷࠦࡧ࡫ࡤࠣࡾࡷࡧࠠ࡯ࡧࡵࠤࡾࡴ࡬ࡷࡣࡷࠤࡶࡨࡪࡢࠢࡪࡹࡷࡼࡥࠡࡻࡹ࡭ࡷ࡬ࠠࡷࡣࠣࡾࡳࡧࡸࡷࡣࡴࠫ࡫ࠦࡺࡣࡨࡪࠤࡦࡨ࡯ࡺࡴࠣࡸࡧࡴࡹ࠻ࠢࡪࡹࡷࠦࡦࡳࡰࡨࡴࡺࠦࡳࡣࡧࠣ࡫ࡪ࡮ࡧࡶࠢࡱࡥࡶࠦࡨࡢࡳࡵࡩ࡫࡭࡮ࡢࡳࡹࡥࡹ࠴ࠢॹ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡉࡸࡶࡱࠦࡪࡷࡻࡼࠤࡴࡸࠠࡻࡤ࡫ࡩࡦࡸࡱࠡࡱ࡯ࠤ࡬ࡻࡲࡷࡧࠣࡷࡳࢀࡶࡺࡸࡵࡪࠥࡴࡡࡲࠢࡶࡩࡻࡸࡡࡲࡨ࠾ࠤ࡬ࡻࡲ࡭ࠢ࡭ࡺࡾࡿࠠࡰࡴࠣࡾࡧ࡮ࡥࡢࡴࡴࠤࡴࡲࠠࡨࡷࡵࡺࡪࠦࡡ࡯ࡩࡹࡦࡦࡁࠠࡨࡷࡵࡰࠥࡰࡶࡺࡻࠣࡳࡷࠦࡺࡣࡪࡨࡥࡷࡷࠠࡰ࡮ࠣ࡫ࡺࡸࠠࡤࡴࡥࡧࡾࡸࠠࡣࡵࠣ࡫ࡺࡸࠠ࡫ࡤࡨࡽࡶࡁࠠࡨࡷࡵࡰࠥࡰࡶࡺࡻࠣࡳࡷࠦࡺࡣࡪࡨࡥࡷࡷࠠࡰ࡮ࠣࡲࠥࡠࡢࡨࡷࡵࡩࠥࡘ࡮ࡦࡩࡸࠤ࡬ࡻ࡮ࡨࠢࡴࡲࡪࡸࡱࠡࡨࡵࡥࡶࠦࡧ࡫ࡤࠣࡦࡸࠦࡵࡳࡧࠣࡪࡧࡧࡦࠡࡸࡤ࡫ࡧࠦࡧࡶࡴࠣ࡬ࡦࡾࡡࡣ࡬ࡤ࠲ࠧॺ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙ࡥࠥ࡭ࡵࡳࡸࡨࠤࡷࡱࡣࡺࡤࡨࡲ࡬ࡼࡢࡢ࠮ࠣ࡫ࡺࡸ࡬ࠡࡨࡪࡺࡪ࡫ࡲࡲࠢࡪࡹࡷࠦࡣࡳࡤࡦࡽࡷࠦࡢࡴࠢࡪࡹࡷࠦࡪࡣࡧࡼࡵࠥ࡭ࡢࠡࡵࡵࡶࡾࠦ࡮ࡧࠢࡥࡥࡷࡁࠠࡷࡣࠣ࡫ࡺࡸࡶࡦࠢࡩࡲࡵ࡫ࡶࡴࡸࡳࡶ࠱ࠦࡧࡶࡴ࡯ࠤࡴࡼࡡࡲࠢࡽࡦࡪࡸࠠࡨࡸࡷࡹ࡬ࡿ࡬ࠡࡩࡸࡶࠥࡵࡥࡣࡩࡸࡶࡪࡻࡢࡣࡳࠣࡦࡸࠦࡺ࡯ࡣ࠱ࠦॻ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚ࡦࠦ࡮ࡢࡲࡹࡶࡦ࡭ࠠࡲࡰ࡯ࡪ࠱ࠦࡺࡳࡣࠣࡽࡧࡨࡸࡳࡳࠣࡲ࡬ࠦࡦࡨࡰࡨࡪࠥࡴࡡࡲࠢࡩࡲ࡯ࠦࡧࡶࡴࡹࡩࠥࡻࡲࡦࡤࡵࡪࠥࡼࡡࠡࡩࡸࡶࠥ࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠴ࠠࡗࡣࠣࡾࡧࡷࡲࡦࡣࠣ࡫ࡻࢀࡲࡧ࠮ࠣ࡮ࡷࠦࡱࡣࠢࡽ࡬ࡵࡻࠠࡨࡷࡵࠤ࡫ࡴࡺࡳ࠮ࠣࡳ࡭࡭ࠠࡣࡪࡨࠤࡺࡸࡥࡣࡴࡩࠤࡳ࡫ࡲࠡࡴࡦࡺࡵࠦࡺࡳࡣࠣࡦࡸࠦࡳࡺࡴࡩࡹࠥࡴࡡࡲࠢࡲࡽࡧࡨࡱ࠯ࠤॼ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡇ࡭ࡵࡳࡧࡩࠤ࡯ࡼࡹࡺࠢࡶࡦࡾࡿࡢ࡫࠮ࠣࡲࡦࡷࠠࡧࡪࡨࡶࡾࡲࠠࡴࡸࡤࡵࠥ࡭ࡵࡳࡸࡨࠤ࡯ࡴ࡬ࠡࡷࡥࡾࡷ࠴࡛ࠠࡰࡤࠫ࡫ࠦࡦࡳࡰࡨࡴࡺࠦࡪࡷࡻࡼࠤࡦࡨࡧࠡࡱࡵࠤࡶࡸࡡࡷࡴࡴ࠲ࠥࡕࡨࡨࠢࡪࡹࡷ࡬ࡲࠡࡼࡵࡥࠥࡰࡲࡦࡴࠣ࡫ࡺࡸࠠࡴࡸࡨࡪ࡬࠲ࠠ࡯ࡣࡴࠤ࡬ࡻࡲ࡭ࠢ࡭ࡺࡾࡿࠠࡦࡴࡽࡲࡻࡧࠠࡨࡷࡵࠤࡸࡨࡥࡳࡼࡥࡪ࡬ࠦࡶࡢࠢࡥ࡬ࡪࠦࡵࡳࡰࡨ࡫࡫࠴ࠢॽ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙ࡢࡦࠢࡵ࡭ࡷ࡫࡬ࠡࡷ࡫ࡾࡳࡧࠠࡰࡴࡹࡥࡹࠦࡪࡶࡤࠣࡽࡧࡨࡸࡧࠢ࡫ࡧࠥࡴࡧࠡࡩࡸࡶࠥࢀࡢࡣࡣࠣࡺࡦࠦࡧࡶࡴࠣࡥࡻࡺࡵࡨࡨࠣ࡫ࡧࠦࡰࡣࡼࡵࠤ࡯ࡼࡹࡺࠢࡻࡥࡧࡰࠠࡨࡷࡱ࡫ࠥ࡭ࡵࡳࡧࡵࠤࡻ࡬ࠠࡧࡤࡽࡶࠥࡶࡢࡦࡣࡵࡩࠥࡨࡳࠡࡰࡤࡦ࡬ࡻࡲࡦࠢ࡭ࡦࡪࡿࡱࠡࡩࡸࡲ࡬ࠦࡶࡧࠢࡶࡦࡪࡸࡩࡳࡧࠣࡾࡳࡧࡸࡷࡣࡴ࠲ࠧॾ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨॿ"))
									if (l1l11l_opy_ (u"ࠥࡱࡦ࡯࡬࡯ࡱࡷࡩࡸࠨঀ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠ࡮ࡣ࡬ࡰࡳࡵࡴࡦࡵ࠱ࡸࡽࡺ࠮࠯࠰ࠥঁ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡕࡸ࡯ࡤ࡯ࡤ࡭ࡱࠦ࡭ࡢ࡫࡯ࡷࡱࡵࡴࠡࡵࡨࡶࡻ࡫ࡲࠣং"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚ࡪࡸࡳࡪࡱࡱࠤ࠸࠴࠱࠯࠷ࠥঃ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴࡕࡑࡆࡄࡘࡊࠦࡎࡆࡇࡇࡉࡉࠦ࠭ࠡࡸ࠱ࠤ࠸࠴࠲࠯࠲ࠣࡅ࡛ࡇࡉࡍࡃࡅࡐࡊࠨ঄"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧঅ"))
									if (l1l11l_opy_ (u"ࠤࡵࡩࡲ࡯࡮ࡥࡧࡵࠦআ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࡲࡦ࡯࡬ࡲࡩ࡫ࡲ࠯ࡶࡻࡸ࠳࠴࠮ࠣই"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡈࡦࡺࡥ࠻ࠢ࠵࠼ࠥࡌࡅࡃࠤঈ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡊࡹࡪࡹࡴࠡࡣࡦࡧࡴࡻ࡮ࡵࠢࡦࡶࡪࡧࡴࡦࡦࠣࡳࡳࠦࡉ࡯ࡶࡵࡥࡳ࡫ࡴࠡࡶࡨࡶࡲ࡯࡮ࡢ࡮࠱ࠤࠥࡉࡨࡢࡰࡪࡩࠥࡪࡥࡧࡣࡸࡰࡹࠦࡰࡢࡵࡶࡻࡴࡸࡤ࠯ࠤউ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥঊ"))
									if (l1l11l_opy_ (u"ࠢ࡭ࡱࡪ࡭ࡳࠨঋ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࡱࡵࡧࡪࡰ࠱ࡸࡽࡺ࠮࠯࠰ࠥঌ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࡋࡗ࠱ࡆࡊࡍࡊࡐࠣࡖࡪࡳࡩ࡯ࡦࡨࡶࠧ঍"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡑࡧࡵࡷࡺࡧ࡮ࡵࠢࡷࡳࠥࡉ࡯࡮ࡲࡤࡲࡾࠦࡐࡰ࡮࡬ࡧࡾࠦࡌࡦࡶࡷࡩࡷࠦ࠱࠱࠯࠴࠽࠽ࡀࠠࡊࡖࠣࡗࡾࡹࡴࡦ࡯ࠣࡇࡷ࡫ࡤࡦࡰࡷ࡭ࡦࡲࠠࡎࡣࡱࡥ࡬࡫࡭ࡦࡰࡷ࠰ࠥࡶ࡬ࡦࡣࡶࡩࠥࡪ࡯ࠡࡐࡒࡘࠥࡹࡴࡰࡴࡨࠤࡱࡵࡧࡪࡰࠣࡨࡪࡺࡡࡪ࡮ࡶࠤ࡫ࡵࡲࠡࡲࡨࡶࡸࡵ࡮ࡢ࡮ࠣࡥࡨࡩ࡯ࡶࡰࡷࡷࠥࡵ࡮ࠡࡶ࡫ࡩࠥ࡭ࡵࡦࡵࡷࠤࡦࡩࡣࡰࡷࡱࡸࠥ࡯࡮ࡴࡶࡤࡲࡨ࡫࠮ࠣ঎"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡆࡤࡸࡪࡪ࠺ࠡ࠳ࠣࡊࡊࡈࠢএ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡡࡴ࠭࠮࠯ࡈࡓࡋ࠳࠭࠮ࠤঐ"))
								if (l1l11l_opy_ (u"ࠨࡰࡢࡴࠥ঑") in l111l1l_opy_):
									sleep1l_opy_ = 3
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠢࡊࡐࡈࡘࡆࡊࡍࡊࡐࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩ࠴࡫࡬࡭࡫ࡲࡸࠩࠦࠢ঒")):
								if (l1l11l_opy_ (u"ࠣ࡮ࡶࠦও") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡌࡪࡵࡷ࡭ࡳ࡭ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࠳࡭ࡵ࡭ࡦ࠱ࡨࡰࡱ࡯࡯ࡵ࠼ࠥঔ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡶࡵࡨࡶࡵࡸ࡯ࡧ࡫࡯ࡩ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴ࡭ࡢ࡫࡯ࠤ࠲࠳ࠠࡥ࡫ࡵࠦক"))
								if (l1l11l_opy_ (u"ࠦࡨࡪࠢখ") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠧࡳࡡࡪ࡮ࠥগ") in l111l1l_opy_):
										sleep1l_opy_ = 7
								if (l1l11l_opy_ (u"ࠨࡣࡢࡶࠥঘ") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠢࡶࡵࡨࡶࡵࡸ࡯ࡧ࡫࡯ࡩࠧঙ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࡺࡹࡥࡳࡲࡵࡳ࡫࡯࡬ࡦ࠰ࡷࡼࡹ࠴࠮࠯ࠤচ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡉࡏࡧࡷ࠱࡙࡫ࡲ࡮ࠢࡘࡷࡪࡸ࠺ࠡࡧ࡯ࡰ࡮ࡵࡴࠣছ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡊࡡࡵࡧࠣࡧࡷ࡫ࡡࡵࡧࡧ࠾ࠥ࠷࠳ࠡࡈࡈࡆࠥ࠷࠸ࠣজ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡌࡢࡵࡷࠤࡸ࡫ࡥ࡯࠼ࠣ࠻ࠥࡳ࡯࡯ࡶ࡫ࡷࠧঝ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡏࡱࠣࡹࡳࡸࡥࡢࡦࠣࡱࡪࡹࡳࡢࡩࡨࡷࠧঞ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯ࡒࡵ࡭ࡻࠦ࡬ࡦࡸࡨࡰ࠿ࠦࡐࡰࡹࡨࡶࡺࡹࡥࡳࠤট"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰࡑࡳࡹ࡫ࡳ࠻ࠢࠣࠤࠧঠ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧড"))
								if (l1l11l_opy_ (u"ࠤࡳࡥࡷࠨঢ") in l111l1l_opy_):
									sleep1l_opy_ = 1
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠥࡍࡓࡋࡔࡂࡆࡐࡍࡓࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡧ࡯ࡰ࡮ࡵࡴ࠰࡯ࡤ࡭ࡱࠪࠠࠣণ")):
								if (l1l11l_opy_ (u"ࠦࡱࡹࠢত") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯ࡩࡱࡰࡩ࠴࡫࡬࡭࡫ࡲࡸ࠴ࡳࡡࡪ࡮࠽ࠦথ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱ࠴࠾ࡐࡁࡏ࠳࠼࠲ࡲࡹࡧࠡ࠯࠰ࠤ࡫࡯࡬ࡦ࡞ࡱࡠࡳ࠸࠱ࡅࡇࡆ࠵࠽࠴࡭ࡴࡩࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮࠲࠵ࡉࡉࡇ࠷࠸࠯࡯ࡶ࡫ࠥ࠳࠭ࠡࡨ࡬ࡰࡪࠨদ"))
								if (l1l11l_opy_ (u"ࠢࡤࡣࡷࠦধ") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠣ࠲࠼ࡎࡆࡔ࠱࠺ࠤন") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠶࠹ࡋࡃࡑ࠵࠾࠴࡭ࡴࡩ࠽ࠦ঩"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡇࡴࡲࡱ࠿ࠦࡊ࠯ࠢࡖࡸࡴࡸ࡭ࠣপ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡔࡰ࠼ࠣࡉࡱࡲࡩࡰࡶࠣࡗ࠳ࠨফ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡓࡇ࠽ࠤࡓࡕࡖࡂࠢࡘࡴࡩࡧࡴࡦࠤব"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯ࡅࡏࡅࡘ࡙࠺ࠡࡕࡈࡒࡘࠨভ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡊࡲ࡬ࡪࡱࡷ࠰ࡳࡢ࡮ࡅࡱࡱࠫࡹࠦࡰࡶࡶࠣࡸ࡭࡯ࡳࠡࡱࡱࠤࡪ࠳࡭ࡢ࡫࡯ࠤ࠲࠳ࠠࡵࡱࡲࠤࡲࡻࡣࡩࠢࡱࡳ࡮ࡹࡥ࠯ࠢࡐࡩࡪࡺࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡈࡣࡷࡩࠥ࠺ࡃࠡ࡫ࡱࠤ࠸࠶࠮࡝ࡰ࡟ࡲ࠲࡙ࡴࡰࡴࡰࠦম"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧয"))
									if (l1l11l_opy_ (u"ࠤ࠵࠵ࡉࡋࡃ࠲࠺ࠥর") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦ࠲࠲ࡆࡈࡇ࠶࠾࠮࡮ࡵࡪ࠾ࠧ঱"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡈࡵࡳࡲࡀࠠࡋ࠰ࠣࡗࡹࡵࡲ࡮ࠤল"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡕࡱ࠽ࠤࡊࡲ࡬ࡪࡱࡷࠤࡘ࠴ࠢ঳"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯ࡔࡈ࠾ࠥࡖ࡯࡭࡫ࡦࡽ࡛ࠥࡰࡥࡣࡷࡩ࡚ࠥࡡࡴ࡭࡬ࡲ࡬ࠨ঴"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰࡆࡐࡆ࡙ࡓ࠻ࠢࡖࡉࡓ࡙ࠢ঵"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡋ࡬࡭࡫ࡲࡸ࠱ࡢ࡮ࡐࡸࡨࡶࡹ࡯࡭ࡦࠢࡩࡹࡳࡪࡩ࡯ࡩࠣࡪࡴࡸࠠ࡮ࡣ࡬ࡲࡹ࡫࡮ࡢࡰࡦࡩࠥ࡯ࡳࠡࡣࡳࡴࡷࡵࡶࡦࡦ࠱ࠤࠥࡓࡡ࡬ࡧࠣࡷࡺࡸࡥࠡࡻࡲࡹࠥ࡮ࡡࡷࡧࠣࡽࡴࡻࡲࠡࡲࡨࡳࡵࡲࡥࠡࡶࡤ࡯ࡪࠦࡡࠡ࡮ࡲࡳࡰࠦࡡࡵࠢࡷ࡬ࡪࠦࡡࡶࡦ࡬ࡸࠥࡲ࡯ࡨࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡩࡲࡰࡰࠣ࡫ࡦࡺࡥࠡ࠯ࠣࡻࡪࠦࡨࡢࡦࠣࡶࡪࡶ࡯ࡳࡶࡶࠤࡴ࡬ࠠࡣࡱࡷࡷࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡳࡵࡷࡦ࡯ࠥࡵ࡮ࠡࡶ࡫ࡩ࡮ࡸࠠࡸࡣࡼࠤࡴࡻࡴࠡ࡮ࡤࡷࡹࠦࡷࡦࡧ࡮࠲ࡡࡴ࡜࡯࠯ࡖࡸࡴࡸ࡭ࠣশ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨষ"))
									if (l1l11l_opy_ (u"ࠥ࠵࠸ࡌࡅࡃ࠳࠻ࠦস") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠ࠳࠲ࡉࡉࡇ࠷࠸࠯࡯ࡶ࡫࠿ࠨহ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡉࡶࡴࡳ࠺ࠡࡕࠥ঺"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯ࡖࡲ࠾ࠥࡋ࡬࡭࡫ࡲࡸ࡙ࠥ࠮ࠣ঻"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰࡕࡉ࠿ࠦࡏ࡯ࡤࡲࡥࡷࡪࡩ࡯ࡩ়ࠥ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡇࡑࡇࡓࡔ࠼ࠣࡗࡊࡔࡓࠣঽ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡅ࡭࡮࡬ࡳࡹࡀ࡜࡯࡙ࡨࡰࡨࡵ࡭ࡦ࠰ࠣࡓࡳࡨ࡯ࡢࡴࡧ࡭ࡳ࡭ࠠࡧࡱࡵࠤࡓࡕࡖࡂࠢࡶ࡭ࡹ࡫ࠠࡵࡧࡤࡱࠥࡵ࡮ࠡ࠳࠳ࠤࡒࡇࡒࠡࡣࡷࠤ࠵࠾࠰࠱࠰ࠣࠤࡋ࡯࡮ࡢ࡮ࠣࡸࡪࡧ࡭ࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡩࡻࡥࠡࡱࡱࡩࠥࡽࡥࡦ࡭ࠣࡴࡷ࡯࡯ࡳ࠰࡟ࡲࡡࡴࡄࡰࠢࡱࡳࡹࠦࡤࡪࡵࡤࡴࡵࡵࡩ࡯ࡶ࠱ࡠࡳࡢ࡮࠮ࡕࠥা"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨি"))
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣী") in l111l1l_opy_):
									sleep1l_opy_ = 6
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠧࡏࡎࡆࡖࡄࡈࡒࡏࡎࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡹࡵࡲ࡮ࠦࠣࠦু")):
								if (l1l11l_opy_ (u"ࠨ࡬ࡴࠤূ") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯ࡳࡵ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠱࡫ࡳࡲ࡫࠯ࡴࡶࡲࡶࡲࡀࠢৃ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡻࡳࡦࡴࡳࡶࡴ࡬ࡩ࡭ࡧ࠱ࡸࡽࡺࠠ࠮࠯ࠣࡪ࡮ࡲࡥ࡝ࡰ࡟ࡲࡲࡧࡩ࡭ࠢ࠰࠱ࠥࡪࡩࡳࠤৄ"))
								if (l1l11l_opy_ (u"ࠤࡦࡨࠧ৅") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠥࡱࡦ࡯࡬ࠣ৆") in l111l1l_opy_):
										sleep1l_opy_ = 9
								if (l1l11l_opy_ (u"ࠦࡨࡧࡴࠣে") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠧࡻࡳࡦࡴࡳࡶࡴ࡬ࡩ࡭ࡧࠥৈ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚࡮࡫ࡷࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࡸࡷࡪࡸࡰࡳࡱࡩ࡭ࡱ࡫࠮ࡵࡺࡷ࠲࠳࠴ࠢ৉"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡎࡔࡥࡵ࠯ࡗࡩࡷࡳࠠࡖࡵࡨࡶ࠿ࠦࡳࡵࡱࡵࡱࠧ৊"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡈࡦࡺࡥࠡࡥࡵࡩࡦࡺࡥࡥ࠼ࠣ࠶ࠥࡕࡃࡕࠢ࠴࠻ࠧো"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡑࡧࡳࡵࠢࡶࡩࡪࡴ࠺ࠡ࠳࠷ࠤ࡭ࡵࡵࡳࡵࠥৌ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡔ࡯ࠡࡷࡱࡶࡪࡧࡤࠡ࡯ࡨࡷࡸࡧࡧࡦࡵ্ࠥ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡐࡳ࡫ࡹࠤࡱ࡫ࡶࡦ࡮࠽ࠤࡕࡵࡷࡦࡴࡸࡷࡪࡸࠢৎ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡏࡱࡷࡩࡸࡀࠠࠡࠢࠥ৏"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥ৐"))
								if (l1l11l_opy_ (u"ࠢࡱࡣࡵࠦ৑") in l111l1l_opy_):
									sleep1l_opy_ = 1
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡳࡵࡱࡵࡱ࠴ࡳࡡࡪ࡮ࠧࠤࠧ৒")):
								if (l1l11l_opy_ (u"ࠤ࡯ࡷࠧ৓") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠲ࡷࡹࡵࡲ࡮࠱ࡰࡥ࡮ࡲ࠺ࠣ৔"))
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࠳࠵ࡎࡆࡔ࠱࠺࠰ࡰࡷ࡬ࠦ࠭࠮ࠢࡩ࡭ࡱ࡫࡜࡯࡞ࡱ࠵࠵ࡐࡁࡏ࠳࠼࠲ࡲࡹࡧࠡ࠯࠰ࠤ࡫࡯࡬ࡦ࡞ࡱࡠࡳ࠶࠸ࡋࡃࡑ࠵࠾࠴࡭ࡴࡩࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮࠳࠸ࡉࡉࡇ࠷࠸࠯࡯ࡶ࡫ࠥ࠳࠭ࠡࡨ࡬ࡰࡪࠨ৕"))
								if (l1l11l_opy_ (u"ࠧࡩࡡࡵࠤ৖") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠨ࠱࠳ࡌࡄࡒ࠶࠿ࠢৗ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯ࡥࡸ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣ࠵࠷ࡐࡁࡏ࠳࠼࠲ࡲࡹࡧ࠻ࠤ৘"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡌࡲࡰ࡯࠽ࠤࡘ࠴ࠢ৙"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡗࡋ࠺ࠡࡐࡒ࡚ࡆࠨ৚"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡉࡌࡂࡕࡖ࠾࡙ࠥࡅࡏࡕࠥ৛"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡌࡨࡷࡸ࡯ࡣࡢ࠮࡟ࡲࡡࡴࡔࡩࡧࠣࡧࡴࡳࡰࡢࡰࡼࠤ࡮ࡹࠠࡨࡴࡤࡸࡪ࡬ࡵ࡭ࠢࡩࡳࡷࠦࡹࡰࡷࡵࠤࡱࡵࡹࡢ࡮ࡷࡽ࠳ࡢ࡮࡝ࡰࡌࡲࠥࡺࡨࡦࠢ࡬ࡲࡹ࡫ࡲࡪ࡯࠯ࠤࡾࡵࡵࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡤࡷࡸࡻ࡭ࡪࡰࡪࠤࡹ࡮ࡥࠡ࡮ࡨࡥࡩࠦࡦࡰࡴࠣࡸ࡭࡫ࠠࡏࡑ࡙ࡅࠥ࡯࡮ࡪࡶ࡬ࡥࡹ࡯ࡶࡦ࠰ࠣࠤࡉࡵࠠ࡯ࡱࡷࠤࡩ࡯ࡳࡢࡲࡳࡳ࡮ࡴࡴ࠯ࠤড়"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࠰ࡗࠧঢ়"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥ৞"))
									if (l1l11l_opy_ (u"ࠢ࠲࠲ࡍࡅࡓ࠷࠹ࠣয়") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤ࠶࠶ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨ࠼ࠥৠ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡆࡳࡱࡰ࠾ࠥࡋ࡬࡭࡫ࡲࡸ࡙ࠥ࠮ࠣৡ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡘࡅ࠻ࠢࡘࡖࡌࡋࡎࡕࠤৢ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡃࡍࡃࡖࡗ࠿ࠦࡕࡏࡅࡏࡅࡘ࡙ࠢৣ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡚ࡌࡊࡘࡅࠡࡃࡕࡉࠥ࡟ࡏࡖࠣࡂࠥࠥࡎࡅࠨࡕࠣࡓ࡚࡚ࡓࡊࡆࡈࠤࡒ࡟ࠠࡐࡈࡉࡍࡈࡋࠡࠢࠣ࡟ࡲࡡࡴ࡙ࡰࡷࠣࡋࡆ࡜ࡅࠡࡏࡈࠤ࡞ࡕࡕࡓ࡚ࠢࡓࡗࡊࠢ৤"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥ৥"))
									if (l1l11l_opy_ (u"ࠢ࠱࠺ࡍࡅࡓ࠷࠹ࠣ০") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤ࠵࠾ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨ࠼ࠥ১"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡆࡳࡱࡰ࠾ࠥࡋ࡬࡭࡫ࡲࡸ࡙ࠥ࠮ࠣ২"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳ࡚࡯࠻ࠢࡍ࠲࡙ࠥࡴࡰࡴࡰࠦ৩"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡒࡆ࠼ࠣࡒࡔ࡜ࡁࠡࡗࡳࡨࡦࡺࡥࠣ৪"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡄࡎࡄࡗࡘࡀࠠࡔࡇࡑࡗࠧ৫"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡎࡪࡹࡳࡪࡥࡤ࠰ࡡࡴࡉࡵࠢ࡯ࡳࡴࡱࡳࠡ࡮࡬࡯ࡪࠦ࡯࡯ࡧࠣࡳ࡫ࠦࡴࡩࡧࠣࡥࡩࡳࡩ࡯ࡵࠣࡦࡴࡺࡣࡩࡧࡧࠤ࡭࡯ࡳࠡࡵࡨࡧࡹ࡯࡯࡯ࠢࡲࡪࠥࡺࡨࡦࠢࡳࡳࡱ࡯ࡣࡺࠢࡸࡴࡩࡧࡴࡦࠢࡳࡶࡴ࡭ࡲࡢ࡯࠱ࠤࠥ࡝ࡥࠡࡰࡨࡩࡩࠦࡴࡰࠢࡸࡴࡩࡧࡴࡦࠢࡷ࡬ࡴࡹࡥࠡࡣࡦࡧࡪࡹࡳࠡࡲࡲࡰ࡮ࡩࡩࡦࡵࠣࡅࡘࡇࡐ࠼ࠢࡧࡳࡺࡨࡴࠡࡣࡱࡽࡴࡴࡥࠡ࡫ࡶࠤࡦࡽࡡࡳࡧࠣࡳ࡫ࠦࡴࡩࡱࡶࡩࠥ࡭ࡡࡵࡧࡶ࠰ࠥࡨࡵࡵࠢࡷ࡬࡮ࡹࠠࡪࡵࠣࡶࡪࡧ࡬࡭ࡻࠣࡳࡺࡺࡤࡢࡶࡨࡨࠥࡹࡴࡶࡨࡩ࠲ࠧ৬"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴࡄࡰࠢࡺࡩࠥࡺࡥ࡭࡮ࠣࡗࡄࡢ࡮࡝ࡰ࠰ࡉࡱࡲࡩࡰࡶࠥ৭"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧ৮"))
									if (l1l11l_opy_ (u"ࠤ࠷ࡒࡔ࡜࠱࠹ࠤ৯") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦ࠲࠷ࡈࡈࡆ࠶࠾࠮࡮ࡵࡪ࠾ࠧৰ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡈࡵࡳࡲࡀࠠࡆ࡮࡯࡭ࡴࡺࠠࡔ࠰ࠥৱ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡕࡱ࠽ࠤࡏ࠴ࠠࡔࡶࡲࡶࡲࠨ৲"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯ࡔࡈ࠾࡚ࠥࡥࡢ࡯ࠣࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࠨ৳"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰࡆࡐࡆ࡙ࡓ࠻ࠢࡖࡉࡓ࡙ࠢ৴"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡐࡥࡴࡵ࡬ࡧࡦ࠲࡜࡯࡞ࡱࡘ࡭ࡧ࡮࡬ࡵࠣࡪࡴࡸࠠࡵࡪࡨࠤࡦࡹࡳࡪࡵࡷࠤࡼ࡯ࡴࡩࠢࡷࡩࡦࡳࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰ࠱ࠤࠥࡓࡥ࡮ࡱࠣ࡭ࡸࠦࡤࡶࡧࠣ࡭ࡳࠦ࡯࡯ࡧࠣࡻࡪ࡫࡫࠭ࠢࡥࡹࡹࠦࡷࡦࠩࡵࡩࠥࡹࡴࡪ࡮࡯ࠤࡸࡩࡲࡢ࡯ࡥࡰ࡮ࡴࡧࠡࡶࡲࠤ࡫࡯࡬࡭ࠢࡷ࡬ࡪࠦࡳࡦࡥࡸࡶ࡮ࡺࡹࠡࡵࡨࡧࡹ࡯࡯࡯࠰ࠣࠤࡈࡧ࡮ࠡࡻࡲࡹࡷࠦࡴࡦࡣࡰࠤࡷ࡫ࡣࡤࡱࡰࡩࡳࡪࠠࡴࡱࡰࡩࡴࡴࡥࡀࠤ৵"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࠭ࡆ࡮࡯࡭ࡴࡺࠢ৶"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢ৷"))
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣ৸") in l111l1l_opy_):
									sleep1l_opy_ = 8
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠧࡏࡎࡆࡖࡄࡈࡒࡏࡎࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳࠩࠦࠢ৹")):
								if (l1l11l_opy_ (u"ࠨ࡬ࡴࠤ৺") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯ࡳࡵ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠱࡫ࡳࡲ࡫࠯ࡴࡱࡵࡶࡪࡴࡴࡰ࠼ࠣࠦ৻"))
									sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡻࡳࡦࡴࡳࡶࡴ࡬ࡩ࡭ࡧ࠱ࡸࡽࡺࠠ࠮࠯ࠣࡪ࡮ࡲࡥ࡝ࡰ࡟ࡲࡲࡧࡩ࡭ࠢ࠰࠱ࠥࡪࡩࡳࠤৼ"))
								if (l1l11l_opy_ (u"ࠤࡦࡨࠧ৽") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠥࡱࡦ࡯࡬ࠣ৾") in l111l1l_opy_):
										sleep1l_opy_ = 11
								if (l1l11l_opy_ (u"ࠦࡨࡧࡴࠣ৿") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠧࡻࡳࡦࡴࡳࡶࡴ࡬ࡩ࡭ࡧࠥ਀") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚࡮࡫ࡷࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࡸࡷࡪࡸࡰࡳࡱࡩ࡭ࡱ࡫࠮ࡵࡺࡷ࠲࠳࠴ࠢਁ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡎࡔࡥࡵ࠯ࡗࡩࡷࡳࠠࡖࡵࡨࡶ࠿ࠦࡳࡰࡴࡵࡩࡳࡺ࡯ࠣਂ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡈࡦࡺࡥࠡࡥࡵࡩࡦࡺࡥࡥ࠼ࠣ࠵࠸ࠦࡊࡖࡎࠣ࠵࠻ࠨਃ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡑࡧࡳࡵࠢࡶࡩࡪࡴ࠺ࠡ࠳࠻ࠤࡲ࡯࡮ࡶࡶࡨࡷࠧ਄"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡔ࡯ࠡࡷࡱࡶࡪࡧࡤࠡ࡯ࡨࡷࡸࡧࡧࡦࡵࠥਅ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡐࡳ࡫ࡹࠤࡱ࡫ࡶࡦ࡮࠽ࠤࡆࡪ࡭ࡪࡰࠥਆ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡏࡱࡷࡩࡸࡀࠠࡑࡔࡌ࡚࡚࡙ࡅࡓ࠮ࠣࡈࡔࠦࡎࡐࡖࠣࡑࡔ࡜ࡅࠡࡑࡕࠤࡒࡏࡇࡓࡃࡗࡉࠥࠨਇ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥਈ"))
								if (l1l11l_opy_ (u"ࠢࡱࡣࡵࠦਉ") in l111l1l_opy_):
									sleep1l_opy_ = 1
							if (l11llll_opy_ == l1l11l_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡳࡰࡴࡵࡩࡳࡺ࡯࠰࡯ࡤ࡭ࡱࠪࠠࠣਊ")):
								if (l1l11l_opy_ (u"ࠤ࡯ࡷࠧ਋") in l111l1l_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡳࡡࡪ࡮࠽ࠦ਌"))
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࠳࠳ࡎࡆࡔ࠱࠺࠰ࡰࡷ࡬ࠦ࠭࠮ࠢࡩ࡭ࡱ࡫࡜࡯࡞ࡱ࠴࠾ࡐࡁࡏ࠳࠼࠲ࡲࡹࡧࠡ࠯࠰ࠤ࡫࡯࡬ࡦ࡞ࡱࡠࡳ࠸࠰ࡇࡇࡅ࠵࠽࠴࡭ࡴࡩࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮࠲࠵ࡍ࡙ࡑ࠷࠶࠯࡯ࡶ࡫ࠥ࠳࠭ࠡࡨ࡬ࡰࡪࠨ਍"))
								if (l1l11l_opy_ (u"ࠧࡩࡡࡵࠤ਎") in l111l1l_opy_):
									if (l1l11l_opy_ (u"ࠨ࠱࠱ࡌࡄࡒ࠶࠿ࠢਏ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯ࡥࡸ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣ࠵࠵ࡐࡁࡏ࠳࠼࠲ࡲࡹࡧ࠻ࠤਐ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡌࡒࡐࡏ࠽ࠤࡊࡲ࡬ࡪࡱࡷࠤࡘࠨ਑"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲ࡙ࡕ࠺ࠡࡕࠥ਒"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡘࡅ࠻ࠢࡐࡥ࡮ࡴࠠࡅࡴ࡬ࡺࡪࠦࡁࡤࡥࡨࡷࡸࠨਓ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡃࡍࡃࡖࡗ࠿ࠦࡈࡊࡕࡈࡒࡘࠨਔ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡖ࡭ࡷ࠲࡜࡯࡞ࡱࡅࡲࠦࡵ࡯ࡣࡥࡰࡪࠦࡴࡰࠢࡤࡧࡨ࡫ࡳࡴࠢࡷ࡬ࡪࠦ࡭ࡢ࡫ࡱࠤࡵࡸ࡯࡫ࡧࡦࡸࠥࡪࡲࡪࡸࡨࠤ࡫ࡵࡲࠡࡐࡒ࡚ࡆࠦ࠭࠮ࠢ࡬ࡷࠥࡺࡨࡦࡴࡨࠤࡦࡴࠠࡪࡵࡶࡹࡪࠦࡷࡪࡶ࡫ࠤࡲࡿࠠࡢࡥࡦࡩࡸࡹࠠࡱࡧࡵࡱ࡮ࡹࡳࡪࡱࡱࡷࡄࡢ࡮࡝ࡰ࠰ࡉࡱࡲࡩࡰࡶࠥਕ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥਖ"))
									if (l1l11l_opy_ (u"ࠢ࠱࠻ࡍࡅࡓ࠷࠹ࠣਗ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤ࠵࠿ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨ࠼ࠥਘ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡆࡓࡑࡐ࠾ࠥࡐ࠮ࠡࡕࡷࡳࡷࡳࠢਙ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳ࡚ࡏ࠻ࠢࡖࠦਚ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡕࡳࡩࡨࡲࡹࡀࠠࡏࡑ࡙ࡅࠥࡇࡣࡵ࡫ࡲࡲࠧਛ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡄࡎࡄࡗࡘࡀࠠࡉࡋࡖࡉࡓ࡙ࠢਜ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡗ࡮ࡸࠬ࡝ࡰ࡟ࡲ࡜࡫ࠠ࡯ࡧࡨࡨࠥࡺ࡯ࠡࡵࡳࡩࡦࡱࠠࡪ࡯ࡰࡩࡩ࡯ࡡࡵࡧ࡯ࡽࠥࡩ࡯࡯ࡥࡨࡶࡳ࡯࡮ࡨࠢࡈࡰࡱ࡯࡯ࡵ࠰࡟ࡲࡡࡴ࠭ࡋࡧࡶࡷ࡮ࡩࡡࠣਝ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦਞ"))
									if (l1l11l_opy_ (u"ࠣ࠴࠳ࡊࡊࡈ࠱࠹ࠤਟ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠸࠰ࡇࡇࡅ࠵࠽࠴࡭ࡴࡩ࠽ࠦਠ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡇࡔࡒࡑ࠿ࠦࡅ࡭࡮࡬ࡳࡹࠦࡓࠣਡ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴࡔࡐ࠼ࠣࡗࠧਢ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮ࡓࡇ࠽ࠤࡓࡕࡖࡂࠢࡒࡲࡧࡵࡡࡳࡦ࡬ࡲ࡬ࠨਣ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯ࡅࡆ࠾ࠥࡐ࠮ࠡࡕࡷࡳࡷࡳࠢਤ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰࡆࡐࡆ࡙ࡓ࠻ࠢࡖࡉࡓ࡙ࠢਥ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙ࡩࡳ࠮࡟ࡲࡡࡴࡁࡵࡶࡤࡧ࡭࡫ࡤࠡ࡫ࡶࠤࡹ࡮ࡥࠡࡨ࡬ࡲࡦࡲࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡰ࡮ࡹࡴࠡࡨࡲࡶࠥࡺࡨࡦࠢࡱࡩࡽࡺࠠࡏࡑ࡙ࡅࠥࡶࡨࡢࡵࡨ࠲ࠥࠦࡊࡦࡵࡶ࡭ࡨࡧࠠࡸ࡫࡯ࡰࠥࡨࡥࠡࡲࡵࡳࡻ࡯ࡤࡪࡰࡪࠤࡦࡴࡹࠡࡣࡧࡨ࡮ࡺࡩࡰࡰࡤࡰࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡲࡪࡩࡥࡴࡵࡤࡶࡾ࠴࡜࡯࡞ࡱ࠱ࡊࡲ࡬ࡪࡱࡷࠦਦ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨਧ"))
									if (l1l11l_opy_ (u"ࠥ࠵࠸ࡐࡕࡍ࠳࠹ࠦਨ") in l111l1l_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠ࠲࠵ࡍ࡙ࡑ࠷࠶࠯࡯ࡶ࡫࠿ࠨ਩"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡉࡖࡔࡓ࠺ࠡࡕࠥਪ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯ࡖࡒ࠾࡙ࠥࠢਫ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢࡓࡇ࠽ࠤࠥࠨਬ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣࡅࡏࡅࡘ࡙࠺ࠡࠢࠣࠦਭ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡧࡰࡱ࠱࡫ࡱ࠵ࡐ࠸࠷ࡤࡊࡊࠨਮ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢਯ"))
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣਰ") in l111l1l_opy_):
									sleep1l_opy_ = 10
							if (sleep1l_opy_ == 0):
								l11llll_opy_ = l1l11l_opy_ (u"ࠧࡏࡎࡆࡖࡄࡈࡒࡏࡎࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴ࠪࠠࠣ਱")
							if (sleep1l_opy_ == 1):
								l11llll_opy_ = l1l11l_opy_ (u"ࠨࡉࡏࡇࡗࡅࡉࡓࡉࡏࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨࠨࠥࠨਲ")
							if (sleep1l_opy_ == 2):
								l11llll_opy_ = l1l11l_opy_ (u"ࠢࡊࡐࡈࡘࡆࡊࡍࡊࡐࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩ࠴࡭ࡵࡦࡵࡷࠨࠥࠨਲ਼")
							if (sleep1l_opy_ == 3):
								l11llll_opy_ = l1l11l_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡰࡶࡤ࡯࡭ࡨࠪࠠࠣ਴")
							if (sleep1l_opy_ == 4):
								l11llll_opy_ = l1l11l_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡨࡷࡨࡷࡹ࠵ࡤࡦࡵ࡮ࡸࡴࡶࠤࠡࠤਵ")
							if (sleep1l_opy_ == 5):
								l11llll_opy_ = l1l11l_opy_ (u"ࠥࡍࡓࡋࡔࡂࡆࡐࡍࡓࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡩࡸࡩࡸࡺ࠯ࡥࡱࡦࡹࡲ࡫࡮ࡵࡵࠧࠤࠧਸ਼")
							if (sleep1l_opy_ == 6):
								l11llll_opy_ = l1l11l_opy_ (u"ࠦࡎࡔࡅࡕࡃࡇࡑࡎࡔࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡨࡰࡱ࡯࡯ࡵࠦࠣࠦ਷")
							if (sleep1l_opy_ == 7):
								l11llll_opy_ = l1l11l_opy_ (u"ࠧࡏࡎࡆࡖࡄࡈࡒࡏࡎࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡩࡱࡲࡩࡰࡶ࠲ࡱࡦ࡯࡬ࠥࠢࠥਸ")
							if (sleep1l_opy_ == 8):
								l11llll_opy_ = l1l11l_opy_ (u"ࠨࡉࡏࡇࡗࡅࡉࡓࡉࡏࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡺ࡯ࡳ࡯ࠧࠤࠧਹ")
							if (sleep1l_opy_ == 9):
								l11llll_opy_ = l1l11l_opy_ (u"ࠢࡊࡐࡈࡘࡆࡊࡍࡊࡐࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩ࠴ࡹࡴࡰࡴࡰ࠳ࡲࡧࡩ࡭ࠦࠣࠦ਺")
							if (sleep1l_opy_ == 10):
								l11llll_opy_ = l1l11l_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡳࡰࡴࡵࡩࡳࡺ࡯ࠥࠢࠥ਻")
							if (sleep1l_opy_ == 11):
								l11llll_opy_ = l1l11l_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡴࡱࡵࡶࡪࡴࡴࡰ࠱ࡰࡥ࡮ࡲࠤࠡࠤ਼")
							if (sleep1l_opy_ == 12):
								l11llll_opy_ = l1l11l_opy_ (u"ࠥࡍࡓࡋࡔࡂࡆࡐࡍࡓࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡣࡧࡱ࡮ࡴࠤࠡࠤ਽")
					else:
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡵࡶࡴࡸ࠮ࠡࡋࡱࡺࡦࡲࡩࡥࠢࡓࡥࡸࡹࡷࡰࡴࡧࠦਾ"))
				else:
					time.sleep(2)
					sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡶࡷࡵࡲ࠯ࠢࡌࡲࡻࡧ࡬ࡪࡦࠣࡔࡦࡹࡳࡸࡱࡵࡨ࠳ࠨਿ"))
			else:
				sleepl_opy_(l1l11l_opy_ (u"ࠨࡅࡹ࡫ࡷ࡭ࡳ࡭ࠠࡴࡻࡶࡸࡪࡳ࠮࠯࠰ࠥੀ"))
				time.sleep(2)
				break
	else:
		sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡞ࡵࡵࠡࡣࡳࡴࡷࡵࡡࡤࡪࠣࡸ࡭࡫ࠠࡳ࡫ࡪ࡬ࡹࠦࡴࡦࡴࡰ࡭ࡳࡧ࡬ࠡࡣࡱࡨࠥࡶࡲࡦࡵࡶࠤࡹ࡮ࡥࠡࡲࡲࡻࡪࡸࠠ࡬ࡧࡼ࠲࠳࠴ࠢੁ"))
		time.sleep(3)
		sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࡟ࡲࠧੂ"))
		sys.stdout.write(l1l11l_opy_ (u"ࠤ࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮ࠤ੃"))
		sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࠨ੄"))
		sleepl_opy_(l1l11l_opy_ (u"ࠦࡓࡕࡖࡂࠢࡆࡳࡳࡺࡲࡰ࡮ࠣࡘࡪࡸ࡭ࡪࡰࡤࡰࠧ੅"))
		time.sleep(2)
		sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮ࡊࡰ࡬ࡸ࡮ࡧࡴࡪࡰࡪࠤࡼࡧ࡫ࡦࠢࡶࡩࡶࡻࡥ࡯ࡥࡨ࠲࠳࠴ࠢ੆"))
		time.sleep(3)
		sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡐࡴࡧࡤࡪࡰࡪࠤࡔ࡙࠮࠯࠰ࠥੇ"))
		time.sleep(2)
		sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞࠯࡞ࡡ࠲ࡡ࡝࠮࡝ࡠ࠱ࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞࠯࡞ࡡ࠲ࡡ࡝࠮࡝ࡠࠦੈ"))
		sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡝ࡥ࡭ࡥࡲࡱࡪ࠲ࠠࡖࡵࡨࡶ࠳ࠨ੉"))
		time.sleep(2)
		while 1:
			if (l11ll_opy_ == 1):
				break
			time.sleep(3)
			sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱࡗࡪࡲࡥࡤࡶࠣࡅࡨࡺࡩࡰࡰ࠽ࠦ੊"))
			sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍࡑࡊࡍࡓࠦ࡯ࡳࠢࡈ࡜ࡎ࡚࡜࡯࡞ࡱ࠾࠿ࠨੋ"))
			l1111l1_opy_ = input()
			if ( (l1l11l_opy_ (u"ࠦࡑࡕࡇࡊࡐࠥੌ") in l1111l1_opy_) or (l1l11l_opy_ (u"ࠧࡒ࡯ࡨ࡫ࡱ੍ࠦ") in l1111l1_opy_) or (l1l11l_opy_ (u"ࠨ࡬ࡰࡩ࡬ࡲࠧ੎") in l1111l1_opy_) ):
				sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴࡐ࡭ࡧࡤࡷࡪࠦࡓࡦ࡮ࡨࡧࡹࠦࡌࡰࡩ࡬ࡲࠥࡇࡣࡤࡱࡸࡲࡹࡀࠠࠣ੏"))
				sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙࡯ࡳࡴࡨࡲࡹࡵ࡜࡯࡞ࡱࡖࡴࡵࡴ࡝ࡰ࡟ࡲࡡࡴ࠺࠻ࠤ੐"))
				l1l11ll_opy_ = input()
				if ((l1l11l_opy_ (u"ࠤࡵࡳࡴࡺࠢੑ") in l1l11ll_opy_) or (l1l11l_opy_ (u"ࠥࡖࡴࡵࡴࠣ੒") in l1l11ll_opy_)):
					sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡱࡸࡪࡸࠠࡱࡣࡶࡷࡼࡵࡲࡥࠢࡩࡳࡷࠦࡒࡰࡱࡷ࠾ࡡࡴ࡜࡯࠼࠽ࠦ੓"))
					l1lll1_opy_ = input()
					if (l1l11l_opy_ (u"ࠧࡹࡴࡢࡴ࡯࡭࡬࡮ࡴࠣ੔") in l1lll1_opy_):
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡐࡴ࡭ࡩ࡯ࠢࡄࡧࡨ࡫ࡰࡵࡧࡧ࠲ࠧ੕"))
						time.sleep(3)
						if ( l1llll1l_opy_ == 0 ):
							clear()
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠢࡓࡱࡲࡸ࠳ࠨ੖"))
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠣࠢࠣࡅࠥࡹࡹࡴࡶࡨࡱࠥࡧࡲࡵ࡫ࡩࡥࡨࡺ࠮ࠡࠢࡗ࡬ࡪࠦࡦࡪࡴࡶࡸࠥࡧࡣࡤࡱࡸࡲࡹ࠲ࠠࡪࡰࡶࡸࡦࡲ࡬ࡦࡦࠣࡦࡾࠦࡴࡩࡧࠣࡓࡘࠦࡩࡵࡵࡨࡰ࡫࠴ࠢ੗"))
							time.sleep(1)
							l11l_opy_(l1l11l_opy_ (u"ࠤࠣࠤࡆࡩࡣࡦࡵࡶࠤࡹࡵࠠࡦࡸࡨࡶࡾࡺࡨࡪࡰࡪ࠲ࠧ੘"))
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡐࡷࡷࡷ࡮ࡪࡥ࠭ࠢࡷ࡬ࡪࠦࡷࡰࡴ࡯ࡨࠥ࡯ࡳࠡࡦ࡬ࡷࡹࡧ࡮ࡵ࠰ࠥਖ਼"))
							time.sleep(1)
							l11l_opy_(l1l11l_opy_ (u"ࠦࠥࠦࡔࡩࡧࠣࡰ࡮ࡴࡧࡦࡴ࡬ࡲ࡬ࠦࡳࡦࡰࡶࡩࠥࡵࡦࠡࡲ࡫ࡽࡸ࡯ࡣࡢ࡮࡬ࡸࡾ࠲ࠠࡷࡣࡱ࡭ࡸ࡮ࡥࡥ࠰ࠥਗ਼"))
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡗ࡬ࡪࡸࡥࠡࡹࡤࡷࠥࡰࡵࡴࡶࠣࡸ࡭࡫ࠠࡱࡴࡲࡱࡵࡺ࠮ࠣਜ਼"))
							time.sleep(4)
							l1llll1l_opy_ = 1
							clear()
							time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡍࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡓࡑࡒࡘ࡙ࠥࡨࡦ࡮࡯࠲࠳࠴ࠢੜ"))
						time.sleep(2)
						sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡙ࡿࡰࡦࠢࠪ࡬ࡪࡲࡰࠨࠢࡩࡳࡷࠦࡡࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡩ࡯࡮࡯ࡤࡲࡩࡹ࡜࡯࡞ࡱࡠࡳࠨ੝"))
						l1l111_opy_ = l1l11l_opy_ (u"ࠣࡔࡒࡓ࡙ࡆࡎࡐࡘࡄࡇࡴࡴࡴࡳࡱ࡯ࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥࠤࠢࠥਫ਼")
						l11ll1l_opy_ = 3
						while 1:
							sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࠢ੟"))
							sys.stdout.write(l1l111_opy_)
							l111lll_opy_ = input()
							if ( (l1l11l_opy_ (u"ࠥ࡬ࡪࡲࡰࠣ੠") in l111lll_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡃࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡈࡵ࡭࡮ࡣࡱࡨࡸࡀ࡜࡯࡞ࡱ࡬ࡪࡲࡰࠡ࠯ࠣࡗ࡭ࡵࡷࡴࠢࡷ࡬࡮ࡹࠠ࡮ࡧࡱࡹࠥࡢ࡮࡭ࡵࠣ࠱ࠥࡒࡩࡴࡶࡶࠤࡨࡵ࡮ࡵࡧࡱࡸࡸࠦ࡯ࡧࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡢ࡮ࡤࡦࠣࡀࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࡮ࡢ࡯ࡨࡂࠥ࠳ࠠࡄࡪࡤࡲ࡬࡫ࡳࠡࡹࡲࡶࡰ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡢ࡮ࡱࡣࡵࠤ࠲ࠦࡍࡰࡸࡨࡷࠥࡺ࡯ࠡࡲࡤࡶࡪࡴࡴࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡡࡴࡣࡢࡶࠣࡀ࡫࡯࡬ࡦࡰࡤࡱࡪࡄࠠ࠮ࠢࡇ࡭ࡸࡶ࡬ࡢࡻࡶࠤࡨࡵ࡮ࡵࡧࡱࡸࡸࠦ࡯ࡧࠢࡩ࡭ࡱ࡫ࠠ࡝ࡰࡨࡼࡪࡩࠠ࠽ࡨ࡬ࡰࡪࡴࡡ࡮ࡧࡁࠤ࠲ࠦࡅࡹࡧࡦࡹࡹ࡫ࡳࠡࡨ࡬ࡰࡪࡢ࡮ࡦࡺ࡬ࡸࠥ࠳ࠠࡍࡱࡪࡳࡺࡺࠠࡰࡨࠣࡷࡪࡹࡳࡪࡱࡱࠦ੡"))
							if ( (l1l11l_opy_ (u"ࠧ࡫ࡸࡪࡶࠥ੢") in l111lll_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡘࡪࡸ࡭ࡪࡰࡤࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯࠰࠱࠲ࠧ੣"))
								break
							if (l1l111_opy_ == l1l11l_opy_ (u"ࠢࡓࡑࡒࡘࡅࡔࡏࡗࡃࡆࡳࡳࡺࡲࡰ࡮ࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫ࠣࠡࠤ੤")):
								if (l1l11l_opy_ (u"ࠣࡲࡤࡶࠧ੥") in l111lll_opy_):
									l11ll1l_opy_ = 1
								if (l1l11l_opy_ (u"ࠤ࡯ࡷࠧ੦") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠽ࠦ੧"))
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡯ࡸࡨ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴࡳࡰࡴࡵࡩࡳࡺ࡯ࠡ࠯࠰ࠤࡩ࡯ࡲ࡝ࡰ࡟ࡲࠧ੨"))
								if (l1l11l_opy_ (u"ࠧࡩࡤࠣ੩") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠨࡳࡰࡴࡵࡩࡳࡺ࡯ࠣ੪") in l111lll_opy_):
										l11ll1l_opy_ = 4
								if (l1l11l_opy_ (u"ࠢࡦࡺࡨࡧࠧ੫") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡋࡲࡳࡱࡵ࠲ࠥࠦࡆࡪ࡮ࡨࠤࡳࡵࡴࠡࡧࡻࡩࡨࡻࡴࡢࡤ࡯ࡩ࠳ࠨ੬"))
								if (l1l11l_opy_ (u"ࠤࡦࡥࡹࠨ੭") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠥࡱࡺࡪࠢ੮") in l111lll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠ࡮ࡷࡧ࠲ࡹࡾࡴ࠯࠰࠱ࠦ੯"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡗ࡬ࡪࡸࡥࠡࡣࡵࡩࠥࡺࡷࡰࠢ࡮࡭ࡳࡪࡳࠡࡱࡩࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡺࡶ࡫ࡷ࠿ࠦࡴࡩࡱࡶࡩࠥࡽࡨࡦࡴࡨࠤࡱ࡯ࡦࡦࠢࡤࡶ࡮ࡹࡥࡴࠢࡲࡹࡹࠦ࡯ࡧࠢࡷ࡬ࡪࠦ࡭ࡶࡦ࠯ࠤࡦࡴࡤࠡࡶ࡫ࡳࡸ࡫ࠠࡸࡪࡨࡶࡪࠦ࡬ࡪࡨࡨࠤ࡫ࡧ࡬࡭ࡵࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡹ࡫ࡺ࠰ࠥੰ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡍࡳࠦࡴࡩ࡫ࡶࠤࡨࡸࡥࡢࡶ࡬ࡳࡳࠦ࡭ࡺࡶ࡫࠰ࠥࡩ࡯࡮ࡲࡸࡸࡪࡸࡳࠡࡣࡵࡳࡸ࡫ࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡰࡹࡩ࠲ࠠࡢࡰࡧࠤࡨࡵࡤࡦࠢࡩࡩࡱࡲࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡶ࡯ࡾ࠴ࠢੱ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࠭ࡈࡧࡲࡶ࡬࡫ࠠࡅࡻࡶࡳࡳࠨੲ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧੳ"))
							if (l1l111_opy_ == l1l11l_opy_ (u"ࠤࡕࡓࡔ࡚ࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲࠧࠥࠨੴ")):
								if (l1l11l_opy_ (u"ࠥࡰࡸࠨੵ") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴࡀࠢ੶"))
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡧࡩࡸࡱࡴࡰࡲࠣ࠱࠲ࠦࡤࡪࡴ࡟ࡲࡡࡴࡤࡰࡥࡸࡱࡪࡴࡴࡴࠢ࠰࠱ࠥࡪࡩࡳࠤ੷"))
								if (l1l11l_opy_ (u"ࠨࡣࡥࠤ੸") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠢࡥࡱࡦࡹࡲ࡫࡮ࡵࡵࠥ੹") in l111lll_opy_):
										l11ll1l_opy_ = 5
									if (l1l11l_opy_ (u"ࠣࡦࡨࡷࡰࡺ࡯ࡱࠤ੺") in l111lll_opy_):
										l11ll1l_opy_ = 6
								if (l1l11l_opy_ (u"ࠤࡳࡥࡷࠨ੻") in l111lll_opy_):
									l11ll1l_opy_ = 4
							if (l1l111_opy_ == l1l11l_opy_ (u"ࠥࡖࡔࡕࡔࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪ࡯ࡤࡷࡰࡩࡳࡺࡳࠤࠢࠥ੼")):
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣ੽") in l111lll_opy_):
									l11ll1l_opy_ = 3
								if (l1l11l_opy_ (u"ࠧࡲࡳࠣ੾") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡹࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠰ࡪࡲࡱࡪ࠵ࡳࡰࡴࡵࡩࡳࡺ࡯࠰ࡦࡲࡧࡺࡳࡥ࡯ࡶࡶ࠾ࠧ੿"))
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡯ࡧࡤࡦ࠰ࡷࡼࡹࠦ࠭࠮ࠢࡩ࡭ࡱ࡫࡜࡯࡞ࡱࡧࡴࡶࡰࡦࡴ࠱ࡸࡽࡺࠠ࠮࠯ࠣࡪ࡮ࡲࡥ࡝ࡰ࡟ࡲࡨࡸࡹࡴࡶࡤࡰ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧࠥ઀"))
								if (l1l11l_opy_ (u"ࠣࡧࡻࡩࡨࠨઁ") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡅࡳࡴࡲࡶ࠳ࠦࠠࡇ࡫࡯ࡩࠥࡴ࡯ࡵࠢࡨࡼࡪࡩࡵࡵࡣࡥࡰࡪ࠴ࠢં"))
								if (l1l11l_opy_ (u"ࠥࡧࡦࡺࠢઃ") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠦ࡯ࡧࡤࡦࠤ઄") in l111lll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡ࡬ࡤࡨࡪ࠴ࡴࡹࡶ࠽ࠦઅ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡓࡔࠦ࡯ࠡࡱࡒࡓࠥࡵࠠࡰࡑࡲࠤࡴࠦࡏࡐࡑࠣࡓࡴࠦ࡯ࠡࡱࡒࠤࡔࡵࠠࡐࡱࡲࠤࡔࠦ࡯ࡰࡱࡲࠤࡴࠦ࡯ࡰࡱࠣࡳࡔࠦࡏࡐࠢࡲࠤࡴࡕ࡯ࠡࡱࡲࡓࠥࡕ࡯ࠡࡑࡲࠤࡴࡵࠠࡐࡱࠣࡓࡔࡵࠠࡰࡑࡲࡳࠥࡵ࡯ࠡࡑࡲࡓࠥࡵࠠࡐࡑࠣࡓࡔࡕࠠࡐࠢࡲࡳࡴࡵࠠࡰࡱࡲࠤࡔࠦࡏࡐࡑࠣࡓࠥࡵ࡯ࡰࡱࠣࡳࠥࡵ࡯ࡐࡱࠣࡳࡔࡵ࡯ࠡࡱࡒࠤࡔࡕࠠࡰࠢࡒࡳࡔࡕࠠࡐࡑࡒࠤࡴࡵࡏࠡࡱࡒࡓࡔࡕ࡯ࠡࡑࡲࡳࠥࡵ࡯ࡰࡱࠣࡳࡔࠦࡏࡰࠢࡒࡓࡴࠦࡏࡐࡑࠣࡓࡴࠦ࡯ࠡࡱࡲࡳࡔࠦ࡯ࠡࡱࡒࡳࠥࡕ࡯ࡐࡑࠣࡳࡔࡕࠠࡐࡑࡒࠤࡴࡕ࡯ࠡࡑࡲࡳࠥࡵ࡯ࠡࡱࡒࡓࡔࡕ࡯ࠡࡑࡲࡳࠥࡵ࡯ࡰࠢࡲࡓࠥࡕ࡯ࡐࡑࠣࡓࡴࡵ࡯ࠡࡱࡲࡓࠥࡕࠠࡐࡱࠣࡓࡔࡕࠠࡰࡑࡒࠤࡔࠦ࡯ࡰࡱࡲࠤࡴࠦࡏࡰࡑࡒࠤࡔࡕࡏࠡࡑࡲࠤࡴࡕ࡯ࡰࠢࡒࡳࡔࡕࠠࡰࡑࡲࠤࡴࡵࠠࡐࡱࡒࡳࠥࡕࡏࡐࠢࡒࡳࡔࡵࠠࡰࡱࡲࡳࠥࡵࠠࡐࠤઆ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦઇ"))
									if (l1l11l_opy_ (u"ࠣࡥࡲࡴࡵ࡫ࡲࠣઈ") in l111lll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡩ࡯ࡱࡲࡨࡶ࠳ࡺࡸࡵ࠼ࠥઉ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡍࡳࡺࡶࠥࡽ࡫ࡩࠢࡹࡰࡴ࡮ࡱࡧࡪࠣࡦࡷࡾࠠࡷࡪࡴࡻࠥࡶࡨ࡝ࡰࡏࡵࡼࡸࠠࡸ࡭࡫ࠤ࡮ࡲࡵࡩࠢࡩࡶࡶࡼࡸࡱࡪࡪࡠࡳࡈࡲࡹࠢࡺ࡯ࡷࡾࡪ࡬ࡹࠣࡐࠬ࡭ࠠࡪࡴࡸ࡮࡭ࡽ࡜࡯ࡇࡻࡻࠥࡲࡷࠨࡸࠣࡨࡴࢀࡤࡣࡸࠣࡰࡶࠦࡰࡣࠢ࡮࡬ࡩ࡭ࠢઊ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮ࡇࡒࡊ࠲࠳࠭ࠣઋ"))
									if (l1l11l_opy_ (u"ࠧࡩࡲࡺࡵࡷࡥࡱࠨઌ") in l111lll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚࡮࡫ࡷࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࡦࡶࡾࡹࡴࡢ࡮࠱ࡸࡽࡺ࠺ࠣઍ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡐࠦ࡮ࡨࡦࡨࠤ࡭ࡺࡦࡷࠢ࡮ࡵࡱ࡫ࡷࡩࠢࡶࡧࡩ࡮ࡷ࡝ࡰࡗࠫࡳࡩࠠࡻࡹࠣࡴ࡭ࡲࡶࠡࡲࡰࡱࠥࡶࡡࡺࡸࡹࡦࡡࡴࡃࡹࡲࡨࠤࡰ࡫ࡱࡢࡹࡨࠤ࡙ࠦࡹࡧ࡮ࠪࡰࠥ࡫ࡥࡦࠢ࡬ࡪࡡࡴࠧࡓࡣࡨࡰ࡚ࠥࠠࡥ࡮ࡳࡪࠥࡻࡥ࡫ࡳࡨࡦࠥࡻࡨ࡯ࡧࡷࡪ࡯ࠨ઎"))
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧએ"))
							if (l1l111_opy_ == l1l11l_opy_ (u"ࠤࡕࡓࡔ࡚ࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲ࠳ࡩ࡫ࡳ࡬ࡶࡲࡴࠨࠦࠢઐ")):
								if (l1l11l_opy_ (u"ࠥࡴࡦࡸࠢઑ") in l111lll_opy_):
									l11ll1l_opy_ = 5
								if (l1l11l_opy_ (u"ࠦࡱࡹࠢ઒") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯ࡩࡱࡰࡩ࠴ࡹ࡯ࡳࡴࡨࡲࡹࡵ࠯ࡥࡧࡶ࡯ࡹࡵࡰ࠻ࠤઓ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡳࡦࡹࡩࡴ࠰ࡷࡼࡹࠦ࠭࠮ࠢࡩ࡭ࡱ࡫ࠢઔ"))
								if (l1l11l_opy_ (u"ࠢࡦࡺࡨࡧࠧક") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡋࡲࡳࡱࡵ࠾ࠥࡌࡩ࡭ࡧࠣࡲࡴࡺࠠࡦࡺࡨࡧࡺࡺࡡࡣ࡮ࡨ࠲ࠧખ"))
								if (l1l11l_opy_ (u"ࠤࡲࡥࡸ࡯ࡳࠣગ") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠥࡳࡦࡹࡩࡴࠤઘ") in l111lll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࡰࡣࡶ࡭ࡸ࠴ࡴࡹࡶ࠽ࠦઙ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰ࠴࠶࠾࠳࠱࠳࠯࠵࠱࠹ࡢ࡮࠵࠳࠰࠺࠲࠷࠭࠲࡞ࡱ࠵࠾࠹࠭࠲࠹࠰࠺࠲࠷࡜࡯࠴࠺࠷࠲࠸࠵࠮࠵࠰࠶ࡡࡴ࠷࠶࠯࠴࠺࠲࠷࡜࡯࠴࠴࠶࠲࠷࠱࠮࠻࠰࠵ࡡࡴ࠱࠷࠶࠰࠵࠽࠳࠱࠲࠯࠷ࡠࡳ࠸࠷࠶࠯࠴࠴࠲࠸࠭࠳࡞ࡱ࠹࠽࠳࠱࠺࠯࠸࠱࠶ࠨચ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥછ"))
							if (l1l111_opy_ == l1l11l_opy_ (u"ࠢࡓࡑࡒࡘࡅࡔࡏࡗࡃࡆࡳࡳࡺࡲࡰ࡮ࡗࡩࡷࡳ࠺ࡿ࠱ࠦࠤࠧજ")):
								if (l1l11l_opy_ (u"ࠣࡲࡤࡶࠧઝ") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡅࡳࡴࡲࡶ࠳ࠦࠧ࠰ࠩࠣ࡭ࡸࠦࡴࡩࡧࠣࡶࡴࡵࡴࠡࡵࡼࡷࡹ࡫࡭ࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠦઞ"))
								if (l1l11l_opy_ (u"ࠥࡰࡸࠨટ") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵࠺ࠣઠ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡦࡳࡳࡺࡲࡰ࡮ࠣ࠱࠲ࠦࡤࡪࡴ࡟ࡲࡡࡴࡨࡰ࡯ࡨࠤ࠲࠳ࠠࡥ࡫ࡵࡠࡳࡢ࡮ࠣડ"))
								if (l1l11l_opy_ (u"ࠨࡣࡥࠤઢ") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠢࡩࡱࡰࡩࠧણ") in l111lll_opy_):
										l11ll1l_opy_ = 4
									if (l1l11l_opy_ (u"ࠣࡥࡲࡲࡹࡸ࡯࡭ࠤત") in l111lll_opy_):
										l11ll1l_opy_ = 2
								if (l1l11l_opy_ (u"ࠤࡨࡼࡪࡩࠢથ") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡴࡵࡳࡷ࠴ࠠࠡࡈ࡬ࡰࡪࠦ࡮ࡰࡶࠣࡩࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫࠮ࠣદ"))
							if (l1l111_opy_ == l1l11l_opy_ (u"ࠦࡗࡕࡏࡕࡂࡑࡓ࡛ࡇࡃࡰࡰࡷࡶࡴࡲࡔࡦࡴࡰ࠾ࢃ࠵ࡣࡰࡰࡷࡶࡴࡲࠣࠡࠤધ")):
								if (l1l11l_opy_ (u"ࠧࡶࡡࡳࠤન") in l111lll_opy_):
									l11ll1l_opy_ = 1
								if (l1l11l_opy_ (u"ࠨ࡬ࡴࠤ઩") in l111lll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯ࡳࡵ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠱ࡦࡳࡳࡺࡲࡰ࡮࠽ࠦપ"))
									sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡹࡨࡶࡶࡧࡳࡼࡴ࠮ࡦࡺࡨࡧࠥ࠳࠭ࠡࡨ࡬ࡰࡪࡢ࡮࡝ࡰࠥફ"))
								if (l1l11l_opy_ (u"ࠤࡦࡥࡹࠨબ") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠥࡷ࡭ࡻࡴࡥࡱࡺࡲࠧભ") in l111lll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࡴࡪࡸࡸࡩࡵࡷ࡯࠰ࡨࡼࡪࡩ࠮࠯࠰ࠥમ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࠦࡖࡔࡕࡔࡑࡇࡕࡑࠥࡘࡅࡒࡗࡌࡖࡊࡊ࡜࡯࡞ࡱࡅ࡚࡚ࡈࡆࡐࡗࡍࡈࡇࡔࡊࡑࡑࠤࡈࡎࡅࡄࡍ࠽ࠤࡈࡕࡐࡑࡇࡕࠤ࠲࠳ࠠࡋࡃࡇࡉࠥ࠳࠭ࠡࡅࡕ࡝ࡘ࡚ࡁࡍ࡞ࡱࡠࡳࡢ࡮࠰ࡕࡋ࡙࡙ࡊࡏࡘࡐࠣ࠱ࡆࡒࡌࠡ࠯ࡉࡓࡗࡉࡅ࡝ࡰࡎࡍࡑࡒ࠭ࡑࡔࡒࡇࡊ࡙ࡓࠡࡖࡕࡅࡓ࡙ࡆࡆࡔ࡟ࡲࡐࡏࡌࡍ࠯ࡓࡖࡔࡉࡅࡔࡕࠣࡖࡊࡉࡖࡂࡎࡏࡠࡳࡑࡉࡍࡎ࠰ࡔࡗࡕࡃࡆࡕࡖࠤࡘࡔࡄࡂࡎࡏࡠࡳ࡚ࡅࡓࡏ࠰ࡉ࡝ࡇࡌࡍ࡞ࡱࡊࡔࡘࡃࡆࡃࡆࡘࡎࡕࡎ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦય"))
								if (l1l11l_opy_ (u"ࠨࡥࡹࡧࡦࠦર") in l111lll_opy_):
									if (l1l11l_opy_ (u"ࠢࡴࡪࡸࡸࡩࡵࡷ࡯ࠤ઱") in l111lll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡌࡩ࡭ࡧࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࡀࠠࡴࡪࡸࡸࡩࡵࡷ࡯࠰ࡨࡼࡪࡩࠢલ"))
										sleepl_opy_(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡓ࡚ࡕ࠲ࡅ࡚࡚ࡈࡐࡔࡌࡘ࡞ࡀࠠࡓࡑࡒࡘࠧળ"))
										sleepl_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡂࡗࡗࡌࡊࡔࡔࡊࡅࡄࡘࡎࡕࡎࠡࡅࡋࡉࡈࡑࠠ࠮࠯ࠥ઴"))
										time.sleep(1)
										sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡇࡔࡖࡐࡆࡔ࠽ࠤࠧવ"))
										l11l111_opy_ = input()
										if (l1l11l_opy_ (u"ࠧࡳ࡯࡯ࡵࡷࡩࡷࠨશ") in l11l111_opy_):
											time.sleep(2)
											sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡎࡆࡊࡅ࠻ࠢࠥષ"))
											l1ll11l_opy_ = input()
											if (l1l11l_opy_ (u"ࠢࡳ࡫ࡦࡳࡨ࡮ࡥࡵࠤસ") in l1ll11l_opy_):
												time.sleep(2)
												sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡉࡒ࡚ࡕࡗࡅࡑࡀࠠࠣહ"))
												l1111_opy_ = input()
												if (l1l11l_opy_ (u"ࠤࡦࡥࡷࡴࡩࡷࡱࡵࡩࠧ઺") in l1111_opy_):
													time.sleep(2)
													clear()
													l11ll_opy_ = 1
													break
												else:
													time.sleep(2)
													sleepl_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡔࡕࡓࡗࠦࡃࡐࡐࡇࡍ࡙ࡏࡏࡏ࠼ࠣࡅ࡚࡚ࡈࡆࡐࡗࡍࡈࡇࡔࡊࡑࡑࠤࡓࡕࡔࠡࡃࡆࡇࡊࡖࡔࡆࡆ࠱ࠦ઻"))
											else:
												time.sleep(2)
												sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡕࡖࡔࡘࠠࡄࡑࡑࡈࡎ࡚ࡉࡐࡐ࠽ࠤࡆ࡛ࡔࡉࡇࡑࡘࡎࡉࡁࡕࡋࡒࡒࠥࡔࡏࡕࠢࡄࡇࡈࡋࡐࡕࡇࡇ࠲઼ࠧ"))
										else:
											time.sleep(2)
											sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡖࡗࡕࡒࠡࡅࡒࡒࡉࡏࡔࡊࡑࡑ࠾ࠥࡇࡕࡕࡊࡈࡒ࡙ࡏࡃࡂࡖࡌࡓࡓࠦࡎࡐࡖࠣࡅࡈࡉࡅࡑࡖࡈࡈ࠳ࠨઽ"))
							if (l11ll1l_opy_ == 1):
								l1l111_opy_ = l1l11l_opy_ (u"ࠨࡒࡐࡑࡗࡄࡓࡕࡖࡂࡅࡲࡲࡹࡸ࡯࡭ࡖࡨࡶࡲࡀࡾ࠰ࠥࠣࠦા")
							if (l11ll1l_opy_ == 2):
								l1l111_opy_ = l1l11l_opy_ (u"ࠢࡓࡑࡒࡘࡅࡔࡏࡗࡃࡆࡳࡳࡺࡲࡰ࡮ࡗࡩࡷࡳ࠺ࡿ࠱ࡦࡳࡳࡺࡲࡰ࡮ࠦࠤࠧિ")
							if (l11ll1l_opy_ == 3):
								l1l111_opy_ = l1l11l_opy_ (u"ࠣࡔࡒࡓ࡙ࡆࡎࡐࡘࡄࡇࡴࡴࡴࡳࡱ࡯ࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥࠤࠢࠥી")
							if (l11ll1l_opy_ == 4):
								l1l111_opy_ = l1l11l_opy_ (u"ࠤࡕࡓࡔ࡚ࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲࠧࠥࠨુ")
							if (l11ll1l_opy_ == 5):
								l1l111_opy_ = l1l11l_opy_ (u"ࠥࡖࡔࡕࡔࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪ࡯ࡤࡷࡰࡩࡳࡺࡳࠤࠢࠥૂ")
							if (l11ll1l_opy_ == 6):
								l1l111_opy_ = l1l11l_opy_ (u"ࠦࡗࡕࡏࡕࡂࡑࡓ࡛ࡇࡃࡰࡰࡷࡶࡴࡲࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴ࠵ࡤࡦࡵ࡮ࡸࡴࡶࠣࠡࠤૃ")
					else:
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡶࡷࡵࡲ࠯ࠢࡌࡲࡻࡧ࡬ࡪࡦࠣࡐࡴ࡭ࡩ࡯࠰ࠥૄ"))
				if ((l1l11l_opy_ (u"ࠨࡓࡰࡴࡵࡩࡳࡺ࡯ࠣૅ") in l1l11ll_opy_) or ( l1l11l_opy_ (u"ࠢࡴࡱࡵࡶࡪࡴࡴࡰࠤ૆") in l1l11ll_opy_ )):
					sleepl_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡋ࡮ࡵࡧࡵࠤࡵࡧࡳࡴࡹࡲࡶࡩࠦࡦࡰࡴࠣࡗࡴࡸࡲࡦࡰࡷࡳ࠿ࠦ࡜࡯࡞ࡱ࠾࠿ࠨે"))
					l1lll1_opy_ = input()
					if ((l1l11l_opy_ (u"ࠤࡤࡨࡪࡲ࡬ࠣૈ") in l1lll1_opy_) or (l1l11l_opy_ (u"ࠥࡅࡩ࡫࡬࡭ࠤૉ") in l1lll1_opy_)):
						#l1ll11_opy_ l11ll11_opy_ l1lllll_opy_ sleep1_opy_
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡎࡲ࡫࡮ࡴࠠࡂࡥࡦࡩࡵࡺࡥࡥ࠰ࠥ૊"))
						time.sleep(3)
						if ( l11111l_opy_ == 0):
							clear()
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠧࡇࡣࡤࡧࡶࡷ࠳ࠨો"))
							time.sleep(1)
							l11l_opy_(l1l11l_opy_ (u"ࠨࠠࠡࡃࠣࡷࡪࡴࡳࡦࠢࡲࡪࠥࡪࡥࡵࡣࡦ࡬ࡲ࡫࡮ࡵ࠮ࠣࡥࡩࡵࡰࡵ࡫ࡱ࡫ࠥࡧ࡮ࡰࡶ࡫ࡩࡷࠦࡰࡦࡴࡶࡳࡳࡧ࠮ࠣૌ"))
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡆࠦࡷࡢࡻࠣࡳ࡫ࠦࡴࡩ࡫ࡱ࡯࡮ࡴࡧ࠯ࠢࠣࡓ࡫ࠦࡦࡪࡰࡧ࡭ࡳ࡭ࠠ࡮ࡧࡤࡲ࡮ࡴࡧࠡ࡫ࡱࠤࡹ࡮ࡥࠡࡷࡱࡧࡪࡸࡴࡢ࡫ࡱࡸࡾ࠴્ࠢ"))
							time.sleep(2)
							l11l_opy_(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡚ࡨࡦࠢࡵࡹࡸ࡮ࠠࡰࡨࠣࡥࠥࡪࡩࡨ࡫ࡷࡥࡱࠦࡢࡶࡼࡽࠤ࡮ࡴࠠࡺࡱࡸࡶࠥ࡬ࡩ࡯ࡩࡨࡶࡹ࡯ࡰࡴ࠰ࠥ૎"))
							time.sleep(1)
							l11l_opy_(l1l11l_opy_ (u"ࠤࠣࠤࡎࡺࠠࡥࡴࡤࡻࡸࠦࡹࡰࡷࠣࡧࡱࡵࡳࡦࡴࠣࡸࡴࠦࡴࡩࡧࠣࡷࡨࡸࡥࡦࡰ࠯ࠤࡦࡴࡤࠡࡦࡨࡩࡵ࡫ࡲࠡ࡫ࡱࡸࡴࠦࡴࡩࡧࠣࡱࡦࢀࡥ࠯ࠤ૏"))
							time.sleep(3)
							l11111l_opy_ = 1
							clear()
						sleepl_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡊࡰ࡬ࡸ࡮ࡧࡴࡪࡰࡪࠤࡘ࡫ࡳࡴ࡫ࡲࡲ࡙ࠥࡨࡦ࡮࡯࠲࠳࠴ࠢૐ"))
						time.sleep(2)
						sys.stdout.write(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡖࡼࡴࡪࠦࠧࡩࡧ࡯ࡴࠬࠦࡦࡰࡴࠣࡥࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡦࡳࡲࡳࡡ࡯ࡦࡶࡠࡳࡢ࡮࡝ࡰࠥ૑"))
						l1l1_opy_ = l1l11l_opy_ (u"࡙ࠧ࡯ࡳࡴࡨࡲࡹࡵࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲࠨࠥࠨ૒")
						l111ll1_opy_ = 1
						while 1:
							sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࠦ૓"))
							sys.stdout.write(l1l1_opy_)
							l11l1ll_opy_ = input()
							if ( (l1l11l_opy_ (u"ࠢࡩࡧ࡯ࡴࠧ૔") in l11l1ll_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡇࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡅࡲࡱࡲࡧ࡮ࡥࡵ࠽ࡠࡳࡢ࡮ࡩࡧ࡯ࡴࠥ࠳ࠠࡔࡪࡲࡻࡸࠦࡴࡩ࡫ࡶࠤࡲ࡫࡮ࡶࠢ࡟ࡲࡱࡹࠠ࠮ࠢࡏ࡭ࡸࡺࡳࠡࡥࡲࡲࡹ࡫࡮ࡵࡵࠣࡳ࡫ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡟ࡲࡨࡪࠠ࠽ࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࡲࡦࡳࡥ࠿ࠢ࠰ࠤࡈ࡮ࡡ࡯ࡩࡨࡷࠥࡽ࡯ࡳ࡭࡬ࡲ࡬ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡟ࡲࡵࡧࡲࠡ࠯ࠣࡑࡴࡼࡥࡴࠢࡷࡳࠥࡶࡡࡳࡧࡱࡸࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡞ࡱࡧࡦࡺࠠ࠽ࡨ࡬ࡰࡪࡴࡡ࡮ࡧࡁࠤ࠲ࠦࡄࡪࡵࡳࡰࡦࡿࡳࠡࡥࡲࡲࡹ࡫࡮ࡵࡵࠣࡳ࡫ࠦࡦࡪ࡮ࡨࠤࡡࡴࡥࡹࡧࡦࠤࡁ࡬ࡩ࡭ࡧࡱࡥࡲ࡫࠾ࠡ࠯ࠣࡉࡽ࡫ࡣࡶࡶࡨࡷࠥ࡬ࡩ࡭ࡧ࡟ࡲࡪࡾࡩࡵࠢ࠰ࠤࡑࡵࡧࡰࡷࡷࠤࡴ࡬ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠣ૕"))
							if ( (l1l11l_opy_ (u"ࠤࡨࡼ࡮ࡺࠢ૖") in l11l1ll_opy_) ):
								sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡕࡧࡵࡱ࡮ࡴࡡࡵ࡫ࡱ࡫ࠥࡹࡥࡴࡵ࡬ࡳࡳ࠴࠮࠯ࠤ૗"))
								break
							if (l1l1_opy_ == l1l11l_opy_ (u"ࠦࡘࡵࡲࡳࡧࡱࡸࡴࡆࡎࡐࡘࡄࡇࡴࡴࡴࡳࡱ࡯ࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡵࡲࡶࡷ࡫࡮ࡵࡱࠧࠤࠧ૘")):
								if (l1l11l_opy_ (u"ࠧࡲࡳࠣ૙") in l11l1ll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡹࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠰ࡪࡲࡱࡪ࠵ࡳࡰࡴࡵࡩࡳࡺ࡯࠻ࠤ૚"))
									sys.stdout.write(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡩ࡫ࡳ࡬ࡶࡲࡴࠥ࠳࠭ࠡࡦ࡬ࡶࡡࡴ࡜࡯ࡦࡲࡧࡺࡳࡥ࡯ࡶࡶࠤ࠲࠳ࠠࡥ࡫ࡵࠦ૛"))
								if (l1l11l_opy_ (u"ࠣࡥࡧࠦ૜") in l11l1ll_opy_):
									if (l1l11l_opy_ (u"ࠤࡧࡳࡨࡻ࡭ࡦࡰࡷࡷࠧ૝") in l11l1ll_opy_):
										l111ll1_opy_ = 2
									if (l1l11l_opy_ (u"ࠥࡨࡪࡹ࡫ࡵࡱࡳࠦ૞") in l11l1ll_opy_):
										l111ll1_opy_ = 3
								if (l1l11l_opy_ (u"ࠦࡵࡧࡲࠣ૟") in l11l1ll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡶࡷࡵࡲࠡࡣࡦࡧࡪࡹࡳࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࠨ࠱࡫ࡳࡲ࡫ࠧ࠻ࠢࡓࡩࡷࡳࡩࡴࡵ࡬ࡳࡳࠦࡤࡦࡰ࡬ࡩࡩ࠴ࠢૠ"))
							if (l1l1_opy_ == l1l11l_opy_ (u"ࠨࡓࡰࡴࡵࡩࡳࡺ࡯ࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪ࡯ࡤࡷࡰࡩࡳࡺࡳࠥࠢࠥૡ")):
								if (l1l11l_opy_ (u"ࠢࡱࡣࡵࠦૢ") in l11l1ll_opy_):
									l111ll1_opy_ = 1
								if (l1l11l_opy_ (u"ࠣ࡮ࡶࠦૣ") in l11l1ll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡌࡪࡵࡷ࡭ࡳ࡭ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲ࠳ࡩࡵࡣࡶ࡯ࡨࡲࡹࡹ࠺ࠣ૤"))
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡫ࡣࡧࡩ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴࡣࡰࡲࡳࡩࡷ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮ࡤࡴࡼࡷࡹࡧ࡬࠯ࡶࡻࡸࠥ࠳࠭ࠡࡨ࡬ࡰࡪࠨ૥"))
								if (l1l11l_opy_ (u"ࠦࡪࡾࡥࡤࠤ૦") in l11l1ll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡶࡷࡵࡲ࠯ࠢࠣࡊ࡮ࡲࡥࠡࡰࡲࡸࠥ࡫ࡸࡦࡥࡸࡸࡦࡨ࡬ࡦ࠰ࠥ૧"))
								if (l1l11l_opy_ (u"ࠨࡣࡢࡶࠥ૨") in l11l1ll_opy_):
									if (l1l11l_opy_ (u"ࠢ࡫ࡣࡧࡩࠧ૩") in l11l1ll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳࡋࡒࡓࡑࡕ࠾ࠥࡘࡏࡐࡖࠣࡔࡊࡘࡍࡊࡕࡖࡍࡔࡔࡓࠡࡔࡈࡕ࡚ࡏࡒࡆࡆࠣࡘࡔࠦࡖࡊࡇ࡚ࠤࡋࡏࡌࡆ࡞ࡱࠦ૪"))
									if (l1l11l_opy_ (u"ࠤࡦࡳࡵࡶࡥࡳࠤ૫") in l11l1ll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡔࡕࡓࡗࡀࠠࡓࡑࡒࡘࠥࡖࡅࡓࡏࡌࡗࡘࡏࡏࡏࡕࠣࡖࡊࡗࡕࡊࡔࡈࡈ࡚ࠥࡏࠡࡘࡌࡉ࡜ࠦࡆࡊࡎࡈࡠࡳࠨ૬"))
									if (l1l11l_opy_ (u"ࠦࡨࡸࡹࡴࡶࡤࡰࠧ૭") in l11l1ll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡖࡗࡕࡒ࠻ࠢࡕࡓࡔ࡚ࠠࡑࡇࡕࡑࡎ࡙ࡓࡊࡑࡑࡗࠥࡘࡅࡒࡗࡌࡖࡊࡊࠠࡕࡑ࡚ࠣࡎࡋࡗࠡࡈࡌࡐࡊࡢ࡮ࠣ૮"))
							if (l1l1_opy_ == l1l11l_opy_ (u"ࠨࡓࡰࡴࡵࡩࡳࡺ࡯ࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪࡥࡴ࡭ࡷࡳࡵࠪࠠࠣ૯")):
								if (l1l11l_opy_ (u"ࠢࡱࡣࡵࠦ૰") in l11l1ll_opy_):
									l111ll1_opy_ = 1
								if (l1l11l_opy_ (u"ࠣ࡮ࡶࠦ૱") in l11l1ll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴࡌࡪࡵࡷ࡭ࡳ࡭ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲ࠳ࡩ࡫ࡳ࡬ࡶࡲࡴ࠿ࠨ૲"))
									sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡰࡣࡶ࡭ࡸ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࠦ૳"))
								if (l1l11l_opy_ (u"ࠦࡪࡾࡥࡤࠤ૴") in l11l1ll_opy_):
									sys.stdout.write(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡶࡷࡵࡲ࠻ࠢࡉ࡭ࡱ࡫ࠠ࡯ࡱࡷࠤࡪࡾࡥࡤࡷࡷࡥࡧࡲࡥ࠯ࠤ૵"))
								if (l1l11l_opy_ (u"ࠨ࡯ࡢࡵ࡬ࡷࠧ૶") in l11l1ll_opy_):
									if (l1l11l_opy_ (u"ࠢࡰࡣࡶ࡭ࡸࠨ૷") in l11l1ll_opy_):
										sys.stdout.write(l1l11l_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࡴࡧࡳࡪࡵ࠱ࡸࡽࡺ࠺ࠣ૸"))
										sys.stdout.write(l1l11l_opy_ (u"ࠤ࡟ࡲࡡࡴ࠱࠳࠻࠰࠵࠷࠳࠲࠮࠶࡟ࡲ࠹࠷࠭࠷࠯࠴࠱࠶ࡢ࡮࠲࠻࠶࠱࠶࠽࠭࠷࠯࠴ࡠࡳ࠸࠷࠴࠯࠵࠹࠲࠹࠭࠳࡞ࡱ࠻࠺࠳࠱࠷࠯࠴ࡠࡳ࠸࠱࠳࠯࠴࠵࠲࠿࠭࠲࡞ࡱ࠵࠻࠺࠭࠲࠺࠰࠵࠶࠳࠴࡝ࡰ࠵࠻࠺࠳࠱࠱࠯࠵࠱࠷ࡢ࡮࠶࠺࠰࠵࠾࠳࠵࠮࠳ࠥૹ"))
										sys.stdout.write(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢૺ"))
							if (l111ll1_opy_ == 1):
								l1l1_opy_ = l1l11l_opy_ (u"ࠦࡘࡵࡲࡳࡧࡱࡸࡴࡆࡎࡐࡘࡄࡇࡴࡴࡴࡳࡱ࡯ࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡵࡲࡶࡷ࡫࡮ࡵࡱࠧࠤࠧૻ")
							if (l111ll1_opy_ == 2):
								l1l1_opy_ = l1l11l_opy_ (u"࡙ࠧ࡯ࡳࡴࡨࡲࡹࡵࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲ࠳ࡩࡵࡣࡶ࡯ࡨࡲࡹࡹࠤࠡࠤૼ")
							if (l111ll1_opy_ == 3):
								l1l1_opy_ = l1l11l_opy_ (u"ࠨࡓࡰࡴࡵࡩࡳࡺ࡯ࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪࡥࡴ࡭ࡷࡳࡵࠪࠠࠣ૽")
					else:
						time.sleep(2)
						sleepl_opy_(l1l11l_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡊࡸࡲࡰࡴ࠱ࠤࡎࡴࡶࡢ࡮࡬ࡨࠥࡲ࡯ࡨ࡫ࡱ࠲ࡡࡴࠢ૾"))
			if ( (l1l11l_opy_ (u"ࠣࡇ࡛ࡍ࡙ࠨ૿") in l1111l1_opy_ ) or (l1l11l_opy_ (u"ࠤࡈࡼ࡮ࡺࠢ଀") in l1111l1_opy_) or (l1l11l_opy_ (u"ࠥࡩࡽ࡯ࡴࠣଁ") in l1111l1_opy_) ):
				sleepl_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡻ࡭ࡹ࡯࡮ࡨࠢࡶࡽࡸࡺࡥ࡮࠰࠱࠲ࠧଂ"))
				time.sleep(2)
				break
time.sleep(3)
sleepl_opy_(l1l11l_opy_ (u"ࠧ࠴ࠢଃ"))
time.sleep(1)
sleepl_opy_(l1l11l_opy_ (u"ࠨ࠮ࠣ଄"))
time.sleep(1)
sleepl_opy_(l1l11l_opy_ (u"ࠢ࠯ࠤଅ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠣࡃࠣࡦࡷ࡯ࡧࡩࡶࠣࡪࡱࡧࡲࡦࠢࡲࡪࠥࡲࡩࡨࡪࡷ࠲ࠧଆ"))
time.sleep(1)
l11l_opy_(l1l11l_opy_ (u"ࠤࠣࠤࡆࠦࡳࡶࡦࡧࡩࡳࠦࡲࡶࡵ࡫ࠤࡴ࡬ࠠ࡯ࡱ࡬ࡷࡪ࠴ࠢଇ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠥࡠࡳࡢ࡮ࡕࡪࡨࠤࡩࡧࡴࡢࠢࡦࡳࡱࡻ࡭࡯ࠢࡳࡹࡱࡹࡥࡴࠢࡤࡲࡩࠦࡳࡶࡴࡪࡩࡸ࠲ࠠ࡭࡫࡮ࡩࠥࡧࠠࡴࡶࡤࡶࠥ࡫ࡸࡱ࡮ࡲࡨ࡮ࡴࡧࠡ࡫ࡱࠤࡸࡲ࡯ࡸࠢࡰࡳࡹ࡯࡯࡯࠰ࠥଈ"))
time.sleep(2)
l11l_opy_(l1l11l_opy_ (u"ࠦࡡࡴ࡜࡯ࡃࠣ࡫ࡷ࡫ࡡࡵࠢࡩࡰࡦࡹࡨࠡࡱࡩࠤࡱ࡯ࡧࡩࡶ࠯ࠤࡹ࡮ࡥ࡯ࠢࡶࡸ࡮ࡲ࡬࡯ࡧࡶࡷ࠳ࠨଉ"))
time.sleep(3)
l11l_opy_(l1l11l_opy_ (u"ࠧࡢ࡮࡝ࡰࡗ࡬ࡪࠦࡳࡶࡦࡧࡩࡳࠦࡲࡶࡵ࡫ࠤࡴ࡬ࠠࡴ࡫࡯ࡩࡳࡩࡥࠡ࡫ࡶࠤࡩ࡫ࡡࡧࡧࡱ࡭ࡳ࡭࠮ࠣଊ"))
time.sleep(5)
sleepl_opy_(l1l11l_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥଋ"))
time.sleep(10)
