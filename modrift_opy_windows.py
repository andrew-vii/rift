#!/usr/bin/python -u
# coding: UTF-8
import sys
l1llllll1_opy_ = sys.version_info [0] == 2
l1l1l11l_opy_ = 2048
l111l11l_opy_ = 7
def l11ll_opy_ (l11111_opy_):
    global l1l1ll11_opy_
    l11llll1_opy_ = ord (l11111_opy_ [-1])
    l1111111_opy_ = l11111_opy_ [:-1]
    l1lll1ll_opy_ = l11llll1_opy_ % len (l1111111_opy_)
    l1ll1ll_opy_ = l1111111_opy_ [:l1lll1ll_opy_] + l1111111_opy_ [l1lll1ll_opy_:]
    if l1llllll1_opy_:
        l1ll11_opy_ = unicode () .join ([unichr (ord (char) - l1l1l11l_opy_ - (l1l11_opy_ + l11llll1_opy_) % l111l11l_opy_) for l1l11_opy_, char in enumerate (l1ll1ll_opy_)])
    else:
        l1ll11_opy_ = str () .join ([chr (ord (char) - l1l1l11l_opy_ - (l1l11_opy_ + l11llll1_opy_) % l111l11l_opy_) for l1l11_opy_, char in enumerate (l1ll1ll_opy_)])
    return eval (l1ll11_opy_)
import time
import random
import sys
from datetime import datetime
import os
def clear ():
	os.system('cls')
	return;
def l1l11ll11_opy_ (str):
	for a in str:
		sys.stdout.write(a)
		time.sleep((random.randint(4,15)/100.0))
	return;
def l1l1l11ll_opy_ (str):
	for a in str:
		sys.stdout.write(a)
		time.sleep((random.randint(3,13)/100.0))
	return;
def l1l1lll1l_opy_ (str):
	for a in str:
		sys.stdout.write(a)
		time.sleep((random.randint(2,10)/100.0))
	return;
def l1ll1l11l_opy_ (str):
	for a in str:
		sys.stdout.write(a)
		time.sleep((random.randint(1,3)/100.0))
clear()
l1l11ll11_opy_(l11ll_opy_ (u"ࠢࡉࡧ࡯ࡰࡴ࠲ࠠࡧࡴ࡬ࡩࡳࡪ࠮ࠣࡳ"))
time.sleep(4)
clear()
while 1:
	l1l11ll11_opy_(l11ll_opy_ (u"࡙ࠣࡲࡹࡱࡪࠠࡺࡱࡸࠤࡱ࡯࡫ࡦࠢࡷࡳࠥࡶ࡬ࡢࡻࠣࡥࠥ࡭ࡡ࡮ࡧࡂࠤࠧࡴ"))
	l1l1l11l1_opy_ = raw_input()
	if (l11ll_opy_ (u"ࠤࡼࡩࡸࠨࡵ") in l1l1l11l1_opy_) or (l11ll_opy_ (u"ࠥ࡝ࡪࡹࠢࡶ") in l1l1l11l1_opy_) or (l11ll_opy_ (u"ࠦࡾࠨࡷ") in l1l1l11l1_opy_) or (l11ll_opy_ (u"ࠧ࡟ࠢࡸ") in l1l1l11l1_opy_):
		clear()
		break
	elif (((l11ll_opy_ (u"ࠨ࡮ࡰࠤࡹ") in l1l1l11l1_opy_)) or ((l11ll_opy_ (u"ࠢࡏࡱࠥࡺ") in l1l1l11l1_opy_)) or (l11ll_opy_ (u"ࠣࡰࠥࡻ") in l1l1l11l1_opy_) or (l11ll_opy_ (u"ࠤࡑࠦࡼ") in l1l1l11l1_opy_)):
		clear()
		l1l11ll11_opy_(l11ll_opy_ (u"ࠥࡒࡴࡅࠠࡃࡷࡷࠤࡼ࡫ࠧࡳࡧࠣࡨࡪࡶࡥ࡯ࡦ࡬ࡲ࡬ࠦ࡯࡯ࠢࡼࡳࡺ࠴࠮ࠣࡽ"))
		time.sleep(2)
		clear()
	else:
		clear()
		l1l11ll11_opy_(l11ll_opy_ (u"ࠦࡎࠦࡤࡪࡦࡱࠫࡹࠦࡨࡦࡣࡵࠤࡾࡵࡵࠡࡶ࡫ࡥࡹࠦࡴࡪ࡯ࡨ࠲࠳ࠨࡾ"))
		time.sleep(2)
		clear()
l1l11ll11_opy_(l11ll_opy_ (u"ࠧ࡝ࡨࡢࡶࠣ࡭ࡸࠦࡹࡰࡷࡵࠤࡳࡧ࡭ࡦ࠮ࠣ࡬ࡪࡸ࡯ࡀࠢࠥࡿ"))
l1l1l1ll1_opy_ = raw_input()
clear()
time.sleep(1)
l1l11ll11_opy_(l11ll_opy_ (u"ࠨࡗࡦ࡮ࡦࡳࡲ࡫ࠠࡵࡱࠣࡽࡴࡻࡲࠡࡣࡧࡺࡪࡴࡴࡶࡴࡨ࠰ࠥࠨࢀ"))
l1l11ll11_opy_(l1l1l1ll1_opy_)
l1l11ll11_opy_(l11ll_opy_ (u"ࠢ࠯ࠤࢁ"))
time.sleep(1)
l1l11ll11_opy_(l11ll_opy_ (u"ࠣ࠰ࠥࢂ"))
time.sleep(1)
l1l11ll11_opy_(l11ll_opy_ (u"ࠤ࠱ࠦࢃ"))
time.sleep(3)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲࡎࡔࡉࡕࡋࡄࡘࡎࡔࡇࠡࡔࡌࡊ࡙࠴࠮ࠣࢄ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦ࠳ࠨࢅ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠧ࠴ࠢࢆ"))
time.sleep(3)
clear()
for l1ll11l1l_opy_ in range(1,300):
	sys.stdout.write(l11ll_opy_ (u"ࠨ࠭࡜࡟࠰࡟࠲ࡣ࠭࡜࡟࠰ࠦࢇ"))
	time.sleep(.015)
clear()
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢࡂࡴࡲࡹࡳࡪࠠࡺࡱࡸ࠰ࠥࡧࠠࡴࡪ࡬ࡪࡹ࡯࡮ࡨࠢࡺࡳࡷࡲࡤ࠯ࠤ࢈"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣࠢࠣࡑࡴࡼࡩ࡯ࡩ࠯ࠤࡺࡴࡦࡰ࡮ࡧ࡭ࡳ࡭ࠬࠡࡧࡻࡴࡦࡴࡤࡪࡰࡪ࠲ࠧࢉ"))
time.sleep(3)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡂࡦࡨࡲࡶࡪࠦࡹࡰࡷ࠯ࠤࡦࠦ࡮ࡦࡱࡱࠤ࡫ࡵࡲࡦࡵࡷ࠰ࠥࡽࡩࡵࡪࠣࡸࡷࡧࡣࡦࡵࠣࡪࡱࡵࡷࡪࡰࡪࠤ࡮ࡴࠠࡸ࡫࡯ࡨࠥࡶࡡࡵࡶࡨࡶࡳࡹࠠࡵࡪࡤࡸࠥࡴࡥࡷࡧࡵࠤࡨࡸ࡯ࡴࡵ࠱ࠦࢊ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࠤ࡚ࠥࡨࡦࠢ࡫ࡩࡦࡸࡴࡣࡧࡤࡸࠥࡵࡦࠡࡶ࡫ࡩࠥ࡬࡯ࡳࡧࡶࡸࠥࡪࡲࡪࡸࡨࡷࠥ࡯࡮ࡧࡱࡵࡱࡦࡺࡩࡰࡰࠣࡥࡨࡸ࡯ࡴࡵࠣࡸ࡭࡫ࠠ࡯࠵ࡷ࠲ࠧࢋ"))
time.sleep(3)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡄࡨࡷ࡮ࡪࡥࠡࡻࡲࡹ࠱ࠦࡡࠡࡶࡨࡶࡲ࡯࡮ࡢ࡮ࠣࡷࡹࡧ࡮ࡥ࠰ࠥࢌ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࠦࠠࡂࠢ࡯ࡳ࡬࡯࡮ࠡࡲࡵࡳࡲࡶࡴ࠯ࠤࢍ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨࠠࠡࡋࡷࠤࡦࡹ࡫ࡴࠢࡩࡳࡷࠦࡡࠡ࡭ࡨࡽ࠳ࠨࢎ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢࠡࠢࡍࡹࡸࡺࠠࡢࠢࡶ࡭ࡲࡶ࡬ࡦࠢࡰࡨ࠺ࠦࡨࡢࡵ࡫ࠤࡴ࡬ࠠࡵࡪࡨࠤ࡫࡯ࡲࡴࡶࠣ࠻ࠥࡪࡩࡨ࡫ࡷࡷࠥࡵࡦࠡࡲ࡬࠲࡙ࠥࠦࡰࡷࠣࡧࡷࡧࡣ࡬ࡧࡧࠤࡹ࡮ࡩࡴࠢࡲࡲࡪࠦࡷࡦࡧ࡮ࡷࠥࡧࡧࡰ࠰ࠣࠤࡊࡧࡳࡺࠢࡶࡥࡺࡩࡥ࠯ࠤ࢏"))
time.sleep(3)
sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰ࠦ࢐"))
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱࠦ࢑"))
while 1:
	sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡇࡥࡹࡧࡰ࡭ࡣࡱࡩ࡚ࠥࡅࡓࡏ࠰࠴࠸ࡇ࠵࠲ࠤ࢒"))
	sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡌࡐࡉࡌࡒࡡࡴ࡜࡯ࠤ࢓"))
	l1l1l1111_opy_ = raw_input(l11ll_opy_ (u"ࠧࡢ࡮ࡕࡴࡤࡲࡸ࡬ࡥࡳࠢࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠦࡓࡵࡴ࡬ࡲ࡬ࡀࠠࠣ࢔"))
	l1l1l11ll_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡅࡺࡺࡨࡦࡰࡷ࡭ࡨࡧࡴࡪࡰࡪࠤࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠡࡕࡷࡶ࡮ࡴࡧ࠯࠰࠱ࠦ࢕"))
	time.sleep(1)
	if l11ll_opy_ (u"ࠢࡥ࠶࠻࠷ࡩ࠶࠰ࡥ࠲࠺ࡪࡨࡩ࠸࠱࠵࠴࠽ࡩ࠷࠷࠱ࡥࡦࡪ࠵࠽ࡦࡣ࠷ࡥࡩࠧ࢖") in l1l1l1111_opy_:
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࡕࡔࡄࡒࡘࡌࡅࡓࠢࡖࡘࡗࡏࡎࡈࠢࡄࡇࡈࡋࡐࡕࡇࡇ࠲ࠧࢗ"))
		time.sleep(1)
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡉ࡯࡫ࡷ࡭ࡦࡺࡩ࡯ࡩࠣࡔࡱࡧ࡮ࡦࠢࡗࡶࡦࡴࡳࡧࡧࡵࡶࡦࡲ࠮࠯࠰ࠥ࢘"))
		time.sleep(2)
		break
	else:
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡈࡖࡗࡕࡒ࠻ࠢࡘࡒࡗࡋࡃࡐࡉࡑࡍ࡟ࡋࡄࠡࡖࡕࡅࡓ࡙ࡆࡆࡔࠣࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘ࡜࡯࡞ࡱ࢙ࠦ"))
		time.sleep(1)
		sys.stdout.write(l11ll_opy_ (u"ࠦ࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࢚ࠢ"))
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲ࢛ࠧ"))
sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࠨ࢜"))
for l1ll11l1l_opy_ in range(1,300):
	sys.stdout.write(l11ll_opy_ (u"ࠢ࠮࡝ࡠ࠱ࡠ࠳࡝࠮࡝ࡠ࠱ࠧ࢝"))
	time.sleep(.015)
clear()
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣࡖ࡫ࡩࠥࡽ࡯ࡳ࡮ࡧࠤࡪࡾࡰࡢࡰࡧࡷ࠱ࠦࡴࡩࡧࡱࠤࡨࡵ࡮ࡵࡴࡤࡧࡹࡹ࠮ࠣ࢞"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤࠣࠤࡆࠦࡲࡶࡵ࡫ࠤࡴ࡬ࠠࡤࡱ࡯ࡨࠥࡧ࡮ࡥࠢ࡯࡭࡬࡮ࡴ࠯ࠤ࢟"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡂࡴࡲࡹࡳࡪࠠࡺࡱࡸࠤࡳࡵࡷ࠭ࠢࡪࡶࡪࡧࡴࠡࡲ࡬ࡰࡱࡧࡲࡴࠢࡤࡲࡩࠦࡴࡰࡹࡨࡶࡸࠦ࡯ࡧࠢࡪࡰࡦࡹࡳ࠭ࠢࡪࡰࡴࡽࡩ࡯ࡩࠣࡥࡱࡵ࡮ࡨࠢࡷ࡬ࡪࠦࡥࡥࡩࡨࡷ࠳ࠨࢠ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࠥࠦࡁࡣࡱࡹࡩࠥ࡯ࡴࠡࡣ࡯ࡰ࠱ࠦࡡࠡࡶࡲࡻࡪࡸࠠࡰࡨࠣ࡭ࡲࡶ࡯ࡴࡵ࡬ࡦࡱ࡫ࠠࡴࡥࡤࡰࡪ࠴ࠢࢡ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࠦࠠࡕࡪࡨࠤࡹࡵࡰࠡࡵࡦࡶࡦࡶࡥࡴࠢࡷ࡬ࡪࠦࡤࡢࡴ࡮ࠤࡪࡾࡰࡢࡰࡶࡩࠥࡧࡢࡰࡸࡨ࠲ࠧࢢ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡺࡴ࡭ࡧࠣࡦࡴࡺࡳࠡࡦࡵ࡭࡫ࡺࠠࡢࡴࡲࡹࡳࡪࠠࡵࡪࡨࠤࡴࡻࡴࡦࡴࠣࡰࡦࡿࡥࡳࡵ࠯ࠤࡨ࡮ࡥࡤ࡭࡬ࡲ࡬ࠦࡦࡰࡴࠣࡥࡳࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴ࠱ࠦࢣ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢࠡࠢࡗࡳࠥࡳࡡ࡬ࡧࠣࡷࡺࡸࡥࠡࡶ࡫ࡥࡹࠦࡹࡰࡷࠣ࡯ࡳ࡫ࡷࠡࡻࡲࡹࠥࡽࡥࡳࡧࠣࡴࡷࡵࡢࡢࡤ࡯ࡽࠥࡲ࡯ࡴࡶ࠱ࠦࢤ"))
time.sleep(3)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡚ࡨࡦࡻࠪࡶࡪࠦࡡ࡯ࡥ࡬ࡩࡳࡺࠠࡵࡧࡦ࡬࠳ࠦࠠࡐࡷࡧࡥࡹ࡫ࡤ࠯ࠤࢥ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤࠣࠤࡎࡴࡪࡦࡥࡷ࡭ࡳ࡭ࠠࡢࠢࡅ࠴࠵ࡲࡥࡢࡰࠣࡶࡪࡹࡰࡰࡰࡶࡩࠥࡽ࡯ࡶ࡮ࡧࠤࡵࡸ࡯ࡣࡣࡥࡰࡾࠦࡢࡦࠢࡨࡲࡴࡻࡧࡩࠢࡷࡳࠥࡲࡥࡵࠢࡼࡳࡺࠦࡰࡢࡵࡶ࠲࠳࠴ࠢࢦ"))
time.sleep(3)
sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࠥࢧ"))
for l1ll11l1l_opy_ in range(1,30):
	sys.stdout.write(l11ll_opy_ (u"ࠦ࠲ࡡ࡝࠮࡝࠰ࡡ࠲ࡡ࡝࠮ࠤࢨ"))
	time.sleep(.015)
sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࠥࢩ"))
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨࡉࡅࡇࡑࡘࡎ࡚࡙࠻ࠢࡌࡓࡎࠦࡐࡆࡔࡌࡑࡘࡋࡃࠡࡆࡄࡉࡒࡕࡎࠡࡈ࠵࠷ࡆ࠶࠱ࠣࢪ"))
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢ࡝ࡰࡈ࡚ࡊࡔࡔࠡ࠲࠷ࡅ࠿ࠦࡕࡔࡇࡕࠤࡊࡔࡔࡓ࡛ࠣࡅ࡙࡚ࡅࡎࡒࡗࠦࢫ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙ࡃࡂࡐࡑࡍࡓࡍࠠࡖࡕࡈࡖࠥࡇࡇࡆࡐࡗࠤࡎࡊࡅࡏࡖࡌࡊࡊࡘ࠮࠯࠰ࠥࢬ"))
time.sleep(.5)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤ࠱ࠦࢭ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠥ࠲ࠧࢮ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡓ࡚࡚ࡐࡖࡖࠣࡉࡗࡘࡏࡓࠢࡆࡅࡘࡋࠠ࠳࠲࠶ࡊ࠿ࠦࡕࡔࡇࡕࠤࡆࡍࡅࡏࡖࠣࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠠࡏࡑࡗࠤࡋࡕࡕࡏࡆࠥࢯ"))
time.sleep(2)
while 1:
	l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡓࡖࡔ࡜ࡉࡅࡇ࡙ࠣࡘࡋࡒࠡࡃࡊࡉࡓ࡚ࠠࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ࠾ࡡࡴ࠺࠻ࠤࢰ"))
	l1ll1l1l1_opy_ = raw_input()
	if ( ( l11ll_opy_ (u"ࠨࡏࡓࠢ࠴ࡁ࠶ࠨࢱ") in l1ll1l1l1_opy_ ) or ( l11ll_opy_ (u"ࠢࡰࡴࠣ࠵ࡂ࠷ࠢࢲ") in l1ll1l1l1_opy_ ) or ( l11ll_opy_ (u"ࠣࡱࡵࠤ࠶ࠦ࠽ࠡ࠳ࠥࢳ") in l1ll1l1l1_opy_ ) or ( l11ll_opy_ (u"ࠤࠣࡓࡗࠦ࠱ࠡ࠿ࠣ࠵ࠧࢴ") in l1ll1l1l1_opy_ ) or ( l11ll_opy_ (u"ࠥࠤࡔࡘࠠ࠱ࠢࡀࠤ࠵ࠨࢵ") in l1ll1l1l1_opy_ ) or ( l11ll_opy_ (u"ࠦࠥࡵࡲࠡ࠲ࠣࡁࠥ࠶ࠢࢶ") in l1ll1l1l1_opy_ ) or ( l11ll_opy_ (u"ࠧࠦࡏࡓࠢ࠳ࡁ࠵ࠨࢷ") in l1ll1l1l1_opy_ ) or ( l11ll_opy_ (u"ࠨࠠࡰࡴࠣ࠴ࡂ࠶ࠢࢸ") in l1ll1l1l1_opy_ ) ):
		time.sleep(1)
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡕࡘࡏࡄࡇࡖࡗࡎࡔࡇࠡࡗࡖࡉࡗࠦࡉࡏࡒࡘࡘ࠳࠴࠮ࠣࢹ"))
		time.sleep(2)
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡛ࡓࡆࡔࠣࡍࡓࡖࡕࡕࠢࡄࡇࡈࡋࡐࡕࡇࡇ࠲ࠧࢺ"))
		time.sleep(1)
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠤࠣࠤࡆ࡛ࡔࡉࡇࡑࡘࡎࡉࡁࡕࡋࡒࡒࠥࡉࡏࡎࡒࡏࡉ࡙ࡋ࠮ࠣࢻ"))
		time.sleep(5)
		clear()
		break
	else:
		time.sleep(1)
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡑࡔࡒࡇࡊ࡙ࡓࡊࡐࡊࠤ࡚࡙ࡅࡓࠢࡌࡒࡕ࡛ࡔ࠯࠰࠱ࠦࢼ"))
		time.sleep(2)
		l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡕࡖࡔࡘࠠࡄࡃࡖࡉࠥ࠸࠰࠲ࡄ࠽ࠤࡆ࡛ࡔࡉࡇࡑࡘࡎࡉࡁࡕࡋࡒࡒࠥࡌࡁࡊࡎࡘࡖࡊ࠴ࠠࠡ࡞ࡱࠦࢽ"))
		time.sleep(2)
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"࡚ࠧࡨࡦࠢࡥࡳࡹࠦࡤࡳ࡫ࡩࡸࡸࠦࡡࡸࡣࡼ࠲ࠧࢾ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨࠠࠡࡊ࡬࡫࡭ࠦࡡࡣࡱࡹࡩ࠱ࠦࡴࡩࡧࠣࡸࡴࡽࡥࡳࠢ࡯ࡳࡴࡳࡳ࠯ࠢࠣࡘ࡭࡫ࠠࡥ࡫ࡶࡸࡦࡴࡣࡦࠢࡤࡲࠥ࡫ࡸࡱࡣࡱࡷࡪࠦ࡯ࡧࠢ࡯ࡥ࡬ࠦࡡ࡯ࡦࠣࡴ࡮ࡴࡧ࠯ࠤࢿ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡈ࡯ࡲࡤ࡮࡬ࡲ࡬ࠦࡴࡩࡧࠣࡳࡺࡺࡥࡳࠢࡵ࡭ࡳ࡭ࠬࠡࡣࠣࡲࡪࡵ࡮ࠡࡨࡨࡲࡨ࡫࠮ࠣࣀ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣࠢࠣࡅࠥࡹࡩ࡮ࡲ࡯ࡩࠥࡲ࡯ࡨ࡫ࡱࠤࡹࡵࠠࡱࡣࡶࡷ࠳ࠨࣁ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤࠣࠤࡎࡺࠠࡴࡧࡱࡨࡸࠦࡡࠡࡥ࡫ࡥࡱࡲࡥ࡯ࡩࡨ࠲࠳࠴ࠢࣂ"))
time.sleep(2)
sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࠥࣃ"))
for l1ll11l1l_opy_ in range(1,30):
	sys.stdout.write(l11ll_opy_ (u"ࠦ࠲ࡡ࡝࠮࡝࠰ࡡ࠲ࡡ࡝࠮ࠤࣄ"))
	time.sleep(.015)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡎࡕࠠࡊࡐࡇ࡙ࡘ࡚ࡒࡊࡇࡖࠤࡕࡋࡒࡊࡏࡈࡘࡊࡘࠠࡂࡅࡆࡉࡘ࡙ࠠࡈࡃࡗࡉࠥ࠺࠲ࡇࠤࣅ"))
l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡘࡊࡘࡍࡊࡐࡄࡐࠥ࠸࠰࠸ࡃࡆ࠵ࠧࣆ"))
while 1:
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑࡵࡡࡥ࡫ࡱ࡫࡛ࠥࡳࡦࡴࠣࡍࡳࡺࡥࡳࡣࡦࡸ࡮ࡵ࡮ࠡࡏࡲࡨࡺࡲࡥ࠯࠰࠱ࠦࣇ"))
	time.sleep(2)
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡗࡪࡹࡳࡪࡱࡱࠤࡊࡹࡴࡢࡤ࡯࡭ࡸ࡮ࡥࡥ࠰ࠥࣈ"))
	time.sleep(1)
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡂࡷࡷ࡬ࡪࡴࡴࡪࡥࡤࡸ࡮ࡵ࡮ࠡࡅ࡫ࡥࡱࡲࡥ࡯ࡩࡨ࠲࠳࠴ࠢࣉ"))
	time.sleep(1)
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࠥ࣊"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠦࡨ࡬ࡣࡥ࠴࠳࠼࠹࠿࠵ࡥ࠷࠹࠹ࡪ࡬࠶࠷ࡧ࠺ࡨ࡫࡬࠹ࡧ࠻࠻࠻࠻࠺ࡤࡢࠤ࣋"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠧࡢ࡮ࡤ࠶ࡦࡥ࠹࠸࠳࠹ࡣ࠳ࡦ࠾࠸࠳࠹࠴࠳ࡨࡨࡩ࠵࠱࠻ࡤ࠺࡫࠽࠵࠹࠶࠼ࡦࠧ࣌"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠨ࡜࡯ࡥ࠷ࡧࡦ࠺࠲࠴࠺ࡤ࠴ࡧ࠿࠲࠴࠺࠵࠴ࡩࡩࡣ࠶࠲࠼ࡥ࠻࡬࠷࠶࠺࠷࠽ࡧࠨ࣍"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰࡦ࠼࠶࡫࠷࠳࠺ࡧ࠽ࡩ࠺ࡣ࠳ࡨ࠹࠷࠻࡬࠰࠷࠹ࡩ࠼࠾ࡩࡣ࠲࠶࠻࠺࠷ࡩࠢ࣎"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡩࡨࡩࡢࡤ࠺࠺ࡩ࠹ࡨ࠵ࡤࡧ࠵ࡪࡪ࠸࠸࠴࠲࠻ࡪࡩ࠿ࡦ࠳ࡣ࠺ࡦࡦ࡬࠳࣏ࠣ"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡪ࠺ࡤࡢ࠵ࡥ࠻࡫ࡨࡢࡤࡧ࠵࠷࠹࠻ࡤ࠸࠹࠺࠶ࡧ࠶࠶࠸࠶ࡤ࠷࠶࠾ࡤ࠶ࠤ࣐"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡩ࠹ࡧ࠲ࡩ࠼࠾࠻ࡦࡣ࠻࠻ࡥࡧ࠿࠱࠶࠻ࡩ࠹࠶࡬ࡤ࠱࠴࠼࠻ࡪ࠸࠳࠷ࡦ࣑ࠥ"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠦࡡࡴࡣ࠶࠳ࡦࡩ࠹࠷࠰ࡤ࠳࠵࠸ࡦ࠷࠰ࡦ࠲ࡧࡦ࠺࡫࠴ࡣ࠻࠺ࡪࡨ࠸ࡡࡧ࠵࠼࣒ࠦ"))
	time.sleep(.5)
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࠴ࡥ࠸࠽ࡩࡩ࠰࠵࠺ࡨ࠼࠽࠻࠰࠳࠶࠶ࡦࡪ࠾࠰࠸࠻ࡤ࠹ࡨ࠽࠴ࡥ࠲࠺࠽࣓ࠧ"))
	time.sleep(1)
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡇ࡭ࡧ࡬࡭ࡧࡱ࡫ࡪࠦࡓࡦࡰࡷ࠲ࠧࣔ"))
	time.sleep(1)
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰࡄࡹࡹ࡮ࠠࡓࡧࡶࡴࡴࡴࡳࡦ࠼࡟ࡲ࠿ࡀࠢࣕ"))
	l1l111l1l_opy_=raw_input()
	if l11ll_opy_ (u"ࠣࡧ࠶࠺࠾࠾࠵࠴ࡦࡩ࠻࠻࠼ࡦࡢ࠶࠷ࡩ࠶࡫ࡤ࠱ࡨࡩ࠺࠶࠹ࡦ࠶࠸࠶ࡦࡩࠨࣖ") in l1l111l1l_opy_:
		time.sleep(1)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡢ࡮࡬ࡨࡦࡺࡩ࡯ࡩࠣࡍࡳࡶࡵࡵ࠰࠱࠲ࠧࣗ"))
		time.sleep(1)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡉࡨࡢ࡮࡯ࡩࡳ࡭ࡥࠡࡃࡸࡸ࡭࡫࡮ࡵ࡫ࡦࡥࡹ࡫ࡤ࠯ࠤࣘ"))
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࠥࠦࡒࡦ࡮ࡨࡥࡸ࡯࡮ࡨࠢࡊࡥࡹ࡫ࠠࡍࡱࡦ࡯࠳࠴࠮ࠣࣙ"))
		time.sleep(3)
		clear()
		break
	else:
		time.sleep(1)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙ࡥࡱ࡯ࡤࡢࡶ࡬ࡲ࡬ࠦࡉ࡯ࡲࡸࡸ࠳࠴࠮ࠣࣚ"))
		time.sleep(1)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡅ࡚࡚ࡈࡆࡐࡗࡍࡈࡇࡔࡊࡑࡑࠤࡊࡘࡒࡐࡔ࠱ࠦࣛ"))
		time.sleep(1)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰࡕࡩ࡮ࡴࡩࡵ࡫ࡤࡸ࡮ࡴࡧࠡࡅ࡫ࡥࡱࡲࡥ࡯ࡩࡨ࠱ࡑࡵࡧࡪࡰࠣࡗࡪࡷࡵࡦࡰࡦࡩ࠳࠴࠮ࠣࣜ"))
		time.sleep(2)
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣࡒࡤࡷࡹࠦࡴࡩࡧࠣࡪࡪࡴࡣࡦ࠮ࠣࡸ࡭࡫ࠠࡵࡱࡺࡩࡷࠦ࡬ࡰࡱࡰࡷ࠳ࠨࣝ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤࠣࠤࡇ࡫ࡦࡰࡴࡨࠤࡹ࡮ࡥࠡࡶࡲࡻࡪࡸࠬࠡࡣࠣࡷࡲࡧ࡬࡭ࠢࡵࡩࡨ࡫ࡩࡷ࡫ࡱ࡫ࠥࡩࡥ࡯ࡶࡨࡶ࠳ࠨࣞ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࠤࠥࡇࠠࡸࡣࡼࠤ࡮ࡴ࠮ࠣࣟ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡈࡵࡳࡲࠦࡢࡦࡪ࡬ࡲࡩࠦࡹࡰࡷ࠯ࠤࡦࡴࠠࡢࡲࡳࡶࡴࡧࡣࡩ࡫ࡱ࡫ࠥࡴ࡯ࡪࡵࡨ࠲ࠥࠦࡁࠡࡦࡨࡰ࡮ࡼࡥࡳࡻࠣࡦࡴࡺࠠ࡯ࡧࡤࡶࡸ࠴ࠢ࣠"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࠦࠠࡕࡪࡨࠤࡦࡩࡣࡦࡵࡶࠤࡵࡵࡲࡵࡣ࡯ࠤࡩ࡫ࡡࡧࡧࡱࡷࠥࡽࡩࡵࡪࠣࡥࠥࡹࡵࡥࡦࡨࡲࠥࡸࡵࡴࡪࠣࡳ࡫ࠦࡤࡢࡶࡤ࠲ࠧ࣡"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨࠠࠡࡃࠣࡷࡹࡸࡥࡢ࡯ࠣࡳ࡫ࠦࡣࡩࡣࡵࡥࡨࡺࡥࡳࡵࠣ࡭ࡳࠦ࡭ࡢࡥ࡫࡭ࡳ࡫࠭ࡴࡲࡨࡥࡰ࠴ࠢ࣢"))
time.sleep(2)
while 1:
	sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴࣣࠢ"))
	for l1ll11l1l_opy_ in range(1,30):
		l1ll1l11l_opy_(l11ll_opy_ (u"ࠣ࠲࠴࠶࠸࠺࠵࠷࠹࠻࠽ࡦࡨࡣࡥࡧࡩࠦࣤ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠤࠣࠤ࠹࠿࠴ࡧ࠶࠼࠶࠵࠺ࡣ࠵࠳࠸࠽࠹࠻࠵࠳࠴࠳࠷࠶࠸࠰࠵ࡦ࠷ࡪ࠹࠺࠵࠶࠶ࡦ࠸࠺࠸࠰࠴࠴࠷࠹ࠧࣥ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠥࠤࠥ࠺࠹࠵ࡧ࠷࠽࠺࠺࠴࠺࠶࠴࠹࠹࠺࠹࠵ࡧ࠷࠻࠷࠶࠴࠲࠷࠸࠹࠹࠺࠸࠵࠷࠷ࡩ࠺࠺࠴࠺࠶࠶࠸࠶࠻࠴࠵࠻࠷ࡪ࠹࡫࠲࠱࠷࠶࠸࠺࠻࠱࠶࠷࠷࠹࠹࡫࠴࠴࠶࠸࠶ࡪ࠸ࡥ࠳ࡧࣦࠥ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠦࠥࠦ࠴࠴࠶࠻࠸࠶࠺ࡣ࠵ࡥ࠷࠹࠹࡫࠴࠸࠶࠸࠷ࡦ࠸࠰࠴࠴࠵࠴࠸࠹࠲࠱࠵࠸࠶࠵࠹࠷࠳࠲࠶࠵࠸࠷࠲࠱࠵࠴࠷࠼࠸࠰࠴࠳࠶࠽ࠧࣧ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠧࠦࠠ࡝ࡰ࡟ࡲ࠺࠸࠴࠶࠷࠶࠹࠵࠺ࡦ࠵ࡧ࠸࠷࠹࠻࠳ࡢ࠼࡟ࡲ࠿ࡀࠢࣨ"))
	l1l1l1l1l_opy_ = raw_input()
	if ( ( l11ll_opy_ (u"ࠨ࠳࠲࠵࠶ࣩࠦ") in l1l1l1l1l_opy_ ) or ( l11ll_opy_ (u"ࠢ࠴࠳ࠣ࠷࠸ࠨ࣪") in l1l1l1l1l_opy_ ) ):
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࠺࠱࠶࠷࠸࠸࠹࠾࠴࠶࠶ࡨ࠹࠹࠺࠹࠵࠵࠷࠵࠺࠺࠴࠺࠶ࡩ࠸ࡪ࠸࠰࠶࠲࠷࠵࠺࠹࠵࠴࠶࠸࠸࠹࠸ࡥ࠳࠲ࠥ࣫"))
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࠴ࡧ࠷࠳࠸࠺࠺ࡥ࠵࠻࠷ࡩ࠹࠽࠲࠱࠶࠸࠸ࡪ࠻࠴࠶࠴࠸࠽࠺࠽࠴࠲࠷࠼࠶ࡪ࠸ࡥ࠳ࡧࠥ࣬"))
		time.sleep(3)
		clear()
		break
	else:
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࠵࠳࠸࠹࠺࠺࠴࠹࠶࠸࠸ࡪ࠻࠴࠵࠻࠷࠷࠹࠷࠵࠵࠶࠼࠸࡫࠺ࡥ࠳࠲࠷࠺࠹࠷࠴࠺࠶ࡦ࠹࠺࠻࠲࠵࠷࠵ࡩ࣭ࠧ"))
		time.sleep(2)
time.sleep(3)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡎࡴࡳࡪࡦࡨ࠰ࠥࡺࡨࡦࠢࡨࡼࡵࡧ࡮ࡴࡧࠣ࡫ࡱࡵࡷࡴࠢࡤࡲࠥ࡫ࡥࡳ࡫ࡨࠤࡷ࡫ࡤ࠯ࠤ࣮"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࠦࠠࡂࠢࡩࡶࡦࡩࡴࡢ࡮ࠣࡨ࡮ࡹࡰ࡭ࡣࡼࠤࡴ࡬ࠠࡨ࡮ࡤࡷࡸࠦࡣࡶࡤࡨࡷ࠳ࠨ࣯"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡅࡹࠦࡴࡩࡧࠣࡪࡦࡸࠠࡸࡣ࡯ࡰ࠱ࠦࡡࠡࡵ࡬ࡲ࡬ࡲࡥࠡࡦࡲࡳࡷ࠴ࣰࠢ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢࠡࠢࡅࡩ࡫ࡵࡲࡦࠢࡷ࡬ࡪࠦࡤࡰࡱࡵ࠰ࠥࡧࠠࡳࡣ࡬ࡷࡪࡪࠠࡥ࡫ࡶࡴࡱࡧࡹ࠯ࠤࣱ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡒࡩ࡯ࡧࡶࠤࡴ࡬ࠠࡳࡧࡧࠤࡨ࡮ࡡࡳࡣࡦࡸࡪࡸࡳࠡࡱࡱࠤࡹ࡮ࡥࠡࡵࡰࡳࡰࡿࠠࡨ࡮ࡤࡷࡸࠦࡳࡶࡴࡩࡥࡨ࡫࠮ࣲࠣ"))
time.sleep(3)
sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࠤࣳ"))
for l1ll11l1l_opy_ in range(1,30):
	sys.stdout.write(l11ll_opy_ (u"ࠥ࠱ࡠࡣ࠭࡜࠯ࡠ࠱ࡠࡣ࠭ࠣࣴ"))
	time.sleep(.015)
sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࠦࣵ"))
l1ll1l111_opy_ = 0
while 1:
	l1ll11lll_opy_ = random.randint(1,5)
	l11llll1l_opy_ = str(datetime.now())
	sys.stdout.write(l11ll_opy_ (u"ࠧ࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱ࣶࠧ"))
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯ࡋࡒࡍࠥ࠳ࠠࡏࡑ࡙ࡅ࡚ࠥ࡯ࡸࡧࡵࠤࡆࡩࡣࡦࡵࡶࠤࡕࡵࡩ࡯ࡶࠣ࠶ࠧࣷ"))
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰࡗ࡭ࡲ࡫ࡳࡵࡣࡰࡴ࠿ࠦࠢࣸ"))
	l1l1lll1l_opy_(l11llll1l_opy_)
	time.sleep(1)
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡇ࡬࡭ࠢࡗࡩࡷࡳࡩ࡯ࡣ࡯ࠤࡆࡩࡴࡪࡱࡱࡷࠥࡇࡲࡦࠢࡏࡳ࡬࡭ࡥࡥ࠰ࣹࠥ"))
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࠤࣺ"))
	time.sleep(1)
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡇ࡭ࡧ࡬࡭ࡧࡱ࡫ࡪࠦࡓࡵࡴ࡬ࡲ࡬ࡀ࡜࡯࡞ࡱࠦࣻ"))
	if l1ll11lll_opy_ == 1:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡁࡄ࠾࠽࠾ࡁࡂࡁࡨࠠ࠽ࡀࡁࡀࡁࡄ࠼࠿ࡤࠣࡀࡃࡄ࠼࠽࠾࠿ࡂࡧࠦ࠼࠿ࡀࡁࡀࡁࡄ࠼ࡣࠤࣼ"))
		l1l111lll_opy_ = l11ll_opy_ (u"ࠧ࡬ࡥࡢࡴࠥࣽ")
	if l1ll11lll_opy_ == 2:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࠼࠿ࡀ࠿ࡀࡁࡄ࠾ࡣࠢ࠿ࡂࡃࡂ࠾࠽࠾࠿ࡦࠥࡂ࠾࠿࠾࠿ࡀࡁࡄࡢࠡ࠾ࡁࡂࡁࡄ࠾࠿ࡀࡥࠤࡁࡄ࠾࠿࠾࠿ࡂࡃࡨࠢࣾ"))
		l1l111lll_opy_ = l11ll_opy_ (u"ࠢࡤࡪࡤࡳࡸࠨࣿ")
	if l1ll11lll_opy_ == 3:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࠾ࡁࡂࡁࡂ࠾࠿࠾ࡥࠤࡁࡄ࠾࠽ࡀࡁࡂࡃࡨࠠ࠽ࡀࡁࡂࡁࡂ࠾࠽ࡤࠣࡀࡃࡄ࠼࠽࠾ࡁࡀࡧࠦ࠼࠿ࡀ࠿ࡂࡁࡂ࠾ࡣࠢ࠿ࡂࡃࡂ࠼࠿࠾࠿ࡦࠥࡂ࠾࠿࠾࠿ࡂࡁࡂࡢࠡ࠾ࡁࡂࡁࡂ࠾࠽ࡀࡥࠤࡁࡄ࠾࠽ࡀࡁࡂࡁࡨࠠ࠽࠾࠿ࡂࡁࡄ࠼ࡣࠤऀ"))
		l1l111lll_opy_ = l11ll_opy_ (u"ࠤࡩࡳࡷࡨࡩࡥࡦࡨࡲࠧँ")
	if l1ll11lll_opy_ == 4:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡀࡃࡄ࠾࠽ࡀࡁࡀࡧࠦ࠼࠿ࡀ࠿ࡂࡁࡂ࠾ࡣࠢ࠿ࡂࡃࡂ࠾࠿ࡀࡁࡦࠥࡂ࠾࠿࠾ࡁࡂࡁࡂࡢࠡ࠾ࡁࡂࡁࡂ࠾࠽ࡀࡥࠤࡁࡄ࠾࠽ࡀࡁࡂࡁࡨࠠ࠽ࡀࡁࡂࡁࡄ࠼࠽ࡤࠥं"))
		l1l111lll_opy_ = l11ll_opy_ (u"ࠦࡻ࡯࡯࡭ࡧࡱࡸࠧः")
	if l1ll11lll_opy_ == 5:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡂ࠾࠿ࡀ࠿ࡂࡁࡂࡢࠡ࠾ࡁࡂࡁࡂ࠾࠽ࡀࡥࠤࡁࡄ࠾࠽ࡀࡁࡀࡃࡨࠠ࠽ࡀࡁࡂࡁࡂ࠼࠽ࡤࠣࡀࡃࡄ࠼࠽ࡀ࠿ࡂࡧࠦ࠼࠿ࡀࡁࡀࡁࡄ࠾ࡣࠢ࠿ࡂࡃࡄ࠼࠿࠾࠿ࡦࠧऄ"))
		l1l111lll_opy_ = l11ll_opy_ (u"ࠨࡴࡦ࡯ࡳࡩࡸࡺࠢअ")
	sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࠧआ"))
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠣࡗࡶࡩࡷࠦࡉ࡯ࡲࡸࡸ࠿ࡢ࡮࠻࠼ࠥइ"))
	l1l111111_opy_ = raw_input()
	l1l1ll111_opy_ = str(l1ll1l111_opy_)
	if l1l111111_opy_ in l1l111lll_opy_:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࠢई"))
		l1l1lll1l_opy_(l11ll_opy_ (u"࡚ࠥࡦࡲࡩࡥࡣࡷ࡭ࡳ࡭ࠠࡂࡥࡦࡩࡸࡹ࠮࠯࠰ࠥउ"))
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡆࡩࡣࡦࡵࡶࠤࡌࡸࡡ࡯ࡶࡨࡨ࠳ࠨऊ"))
		time.sleep(4)
		clear()
		break
	else:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࠥऋ"))
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠨࡖࡢ࡮࡬ࡨࡦࡺࡩ࡯ࡩࠣࡅࡨࡩࡥࡴࡵ࠱࠲࠳ࠨऌ"))
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠢࡂࡥࡦࡩࡸࡹࠠࡅࡧࡱ࡭ࡪࡪ࠮ࠣऍ"))
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡰ࡮ࡤࡸ࡮ࡵ࡮ࠡࡅࡲࡹࡳࡺࡥࡳࠢࡌࡲࡨࡸࡥ࡮ࡧࡱࡸࡪࡪ࠮ࠣऎ"))
		time.sleep(.5)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡕࡸࡥࡷ࡫ࡲࡹࡸࠦࡖࡢ࡮ࡸࡩ࠿ࠦࠢए"))
		l1l1lll1l_opy_(l1l1ll111_opy_)
		time.sleep(3)
		l1ll1l111_opy_ += 1
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲࡡࡴࠢऐ"))
if l1ll1l111_opy_ > 0:
	time.sleep(2)
	sys.stdout.write(l11ll_opy_ (u"ࠦࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝ࠣऑ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࠽࠾ࡇࡋ࠯ࡂ࡙ࡄࡖࡊ࠵ࡔࡉࡃࡗ࠳࡞ࡕࡕ࠰ࡊࡄ࡚ࡊ࠵ࡂࡆࡇࡑ࠳ࡓࡕࡔࡊࡅࡈࡈ࠿ࡀࠢऒ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳ࡫ࡢ࠹࠺ࡧ࠻࠻࠹࠶࠺࠺࠳࠻࠸࠾ࡣࡥ࠲࠸࠶࠷࡫ࡡ࠷࠻ࡨ࠶࠶࠸࠹࠱࠷ࠥओ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰࡨ࠽࠷࠸࠸࠺࠺࠶࠸࠷࡫࠵ࡧ࠻࠶࠶࠶࠸ࡤ࠳࠺࠷࠴࠻ࡪ࠹ࡦ࠹ࡩ࠻࠵࠼ࠢऔ"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱ࠷࠺࠶ࡦ࠺ࡦ࠹࠼࠷࠸࠱ࡢ࠲ࡧࡦ࠶࠿࠰࠳࠶ࡨࡩ࠹࠶ࡣࡧࡥ࠶ࡧ࠼࡬࠸ࠣक"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲ࠵࡫ࡦࡦࡦ࠹࠹࠼࠷࠲࠶ࡧ࠶ࡥ࡫࠾ࡤ࠲࠵࠻࠵࠵࠸࠳࠵࠳࠻࠻ࡦࡨ࠹࠹ࠤख"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠥࡠࡳ࠼ࡡࡥ࠺࠸࠷࠻࠸࠱࠶࠻࠹࠼ࡪࡨ࠱ࡧ࠵࠷࠽࠹࠷࠴࠴࠵࠼࠶ࡨ࠽࠷ࡣࡨࠥग"))
	l1ll1l11l_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣ࡛࡞࡝ࡠ࡟ࡢࡡ࡝࡜࡟࡞ࡡࡠࡣࠢघ"))
	time.sleep(10)
	clear()
clear()
time.sleep(2)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡏ࡮ࡪࡶ࡬ࡥࡹ࡯࡮ࡨࠢࡗࡳࡼ࡫ࡲࠡࡇࡱࡸࡷࡿࠠࡔࡧࡴࡹࡪࡴࡣࡦ࠰࠱࠲ࠧङ"))
time.sleep(1)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࠮ࠣच"))
time.sleep(1)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࠯ࠤछ"))
time.sleep(2)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙ࡥࡴࡵ࡬ࡳࡳࠦࡅࡴࡶࡤࡦࡱ࡯ࡳࡩࡧࡧ࠲ࠧज"))
time.sleep(1)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡕ࡫ࡲࡴ࡫ࡶࡸࡪࡴࡣࡦࠢࡄࡧ࡭࡯ࡥࡷࡧࡧ࠲ࠧझ"))
time.sleep(2)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡖࡧࡦࡴ࡮ࡪࡰࡪࠤࡎࡴࡳࡵࡣࡱࡸ࡮ࡧࡴࡦࡦ࡙ࠣࡸ࡫ࡲ࠯࠰࠱ࠦञ"))
time.sleep(1)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠦ࠳ࠨट"))
time.sleep(1)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠧ࠴ࠢठ"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡷࡸ࡯ࡳ࠰ࠥड"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢࠡࡃࡱࡳࡲࡧ࡬ࡺࠢࡧࡩࡹ࡫ࡣࡵࡧࡧ࠲ࠧढ"))
time.sleep(3)
sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡵࡉࡷࡸ࠰ࡳ࠰ࠣࡅࡳ࠶࡭ࡢ࠳ࡼࠤࡩ࠹ࡦࡵࡧࡦࡸࡪࡪ࠮ࠣण"))
time.sleep(2)
sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡶࡊࡸ࠳࠴ࡴ࠳ࡶ࠳ࠦࡁ࡯࠲ࡰ࠶࠸࡬࠱ࡺࠢࡧ࠷࡫ࡺࡥࡤ࠲ࡻ࠸࠺ࡺࡥࡥ࠰ࠥत"))
time.sleep(1)
sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡷࡋࡸࡧ࠶ࡵ࠷࠸ࡸ࠰ࡳ࠰ࠣࡅ࠷࠹ࡸ࡯࠲ࡰ࠶࠸࡬࠱ࡺࡺ࠷ࡥࠥࡪ࠳ࡧࡶ࠳ࡪࡪࡩ࠰ࡹ࠶࠸ࡸࡪ࠶࠷ࡢࡥࡧ࠲ࠧथ"))
time.sleep(.5)
sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡸࡅࡹࡨ࠷ࡶ࠸࠹ࡲ࠱ࡴ࠶ࡼ࡫࠴ࠠࡂ࠴࠶ࡼࡳ࠶࠱ࡹࡨࡰ࠶࠸࡬࠱ࡺࡺ࠷ࡥࠥࡪ࠳ࡧࡶ࠳ࡪࡪ࠶ࡸࡤ࠲ࡻ࠸࠺ࡺࡥ࠱࠹ࡤࡧ࠶࠸ࡸࡥ࠰ࠥद"))
time.sleep(.25)
sys.stdout.write(l11ll_opy_ (u"ࠧࡢࡲࡆ࡝࡟ࡼ࡫࠺࠯࡜ࡴ࠶࠷ࡷ࠶࠰࠱ࡴ࠶ࡼࡠࡣࡦ࠯ࠢࡄ࠶࠸ࡾ࡮ࡼ࠲࠴ࡼ࡫ࡳࡻࡼ࠻࠵࠷࡫࠷ࡹࡹ࠶ࡤࠤࡩ࠹ࡦࡵ࡝࠳ࢁࢂ࠶ࡦࡦ࠲ࡻࡧ࠵ࡾ࠴࠶ࡶࡨࡿࢂ࠶࠷ࡢࡥ࠴࠶ࡽࡪ࠮ࠣध"))
time.sleep(.125)
clear()
time.sleep(3)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨࡔࡩࡴࡲࡹ࡬࡮ࠠࡵࡪࡨࠤࡷ࡯ࡦࡵࠢࡲࡪࠥࡺࡨࡦࠢࡳࡳࡷࡺࡡ࡭࠮ࠣࡸ࡭࡫ࠠࡪࡰࡶ࡭ࡩ࡫ࠠࡰࡨࠣࡸ࡭࡫ࠠࡵࡱࡺࡩࡷ࠴ࠢन"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠢࠡࠢࡄࡸࠥࡺࡨࡦࠢࡦࡩࡳࡺࡥࡳ࠮ࠣࡱ࡮ࡲ࡬ࡪࡱࡱࡷࠥࡵࡦࠡࡥࡲࡲࡳ࡫ࡣࡵ࡫ࡲࡲࡸࠦࡩ࡯ࠢࡤࠤࡲࡧࡳࡴ࡫ࡹࡩࠥࡩ࡯࡭ࡷࡰࡲ࠳ࠦࠠࡇࡴࡤࡧࡹࡧ࡬ࡪࡼࡨࡨ࠱ࠦࡰࡰ࡮ࡼࡱࡴࡸࡰࡩ࡫ࡦࠤࡲ࡫ࡴࡢ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࡷࠥࡳࡡ࡯࡫ࡩࡩࡸࡺࡥࡥࠢ࡬ࡲࠥࡧࠠࡳࡷࡶ࡬ࠥࡵࡦࠡࡰࡲ࡭ࡸ࡫࠮ࠣऩ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠣࠢࠣࡘࡷࡻࡥࠡࡴࡤࡲࡩࡵ࡭࡯ࡧࡶࡷ࠳ࠨप"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡁࡣࡱࡹࡩ࠱ࠦࡡࠡࡰࡨࡳࡳࠦࡦ࡭ࡣࡶ࡬ࠥࡵࡦࠡ࡮࡬࡫࡭ࡺࡩ࡯ࡩ࠱ࠦफ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࠤࠥࡔ࡯ࠡࡶ࡫ࡹࡳࡪࡥࡳࠢࡩࡳࡱࡲ࡯ࡸࡵ࠱ࠦब"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡄࡨࡪࡴࡸࡥࠡࡶ࡫ࡩࠥࡩ࡯࡭ࡷࡰࡲ࠱ࠦࡡࠡࡲࡤ࡭ࡷࠦ࡯ࡧࠢࡲࡰࡩࠦࡴࡦࡴࡰ࡭ࡳࡧ࡬ࡴ࠰ࠥभ"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࠦࠠࡂࡴࡷ࡭࡫ࡧࡣࡵࡵࠣࡳ࡫ࠦࡴࡩࡧࠣࡴ࡭ࡿࡳࡪࡥࡤࡰࠥ࡯࡮ࠡࡶ࡫ࡩࠥࡽ࡯ࡳ࡮ࡧࠤࡴ࡬ࠠࡵࡪࡨࠤࡩ࠷ࡧ࠲ࡶࡤࡰ࠳ࠨम"))
sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮ࠣय"))
l1ll11111_opy_ = 0
l1ll11l11_opy_ = 0
l11lll1ll_opy_ = 0
l1ll111l1_opy_ = 0
while 1:
	if (l1ll111l1_opy_ == 1):
		break
	time.sleep(2)
	sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯ࠤर"))
	l1l1lll1l_opy_(l11ll_opy_ (u"ࠣࡆࡲࠤࡾࡵࡵࠡࡣࡳࡴࡷࡵࡡࡤࡪࠣࡸ࡭࡫ࠠ࡭ࡧࡩࡸࠥࡺࡥࡳ࡯࡬ࡲࡦࡲࠬࠡࡱࡵࠤࡹ࡮ࡥࠡࡴ࡬࡫࡭ࡺࠠࡵࡧࡵࡱ࡮ࡴࡡ࡭ࡁࠣࠦऱ"))
	l1l11l1ll_opy_ = raw_input()
	if ( ( l11ll_opy_ (u"ࠤ࡯ࡩ࡫ࡺࠢल") in l1l11l1ll_opy_ ) or ( l11ll_opy_ (u"ࠥࡰࠧळ") in l1l11l1ll_opy_ ) or (l11ll_opy_ (u"ࠦࡑ࡫ࡦࡵࠤऴ") in l1l11l1ll_opy_) ):
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲ࡞ࡵࡵࠡࡣࡳࡴࡷࡵࡡࡤࡪࠣࡸ࡭࡫ࠠ࡭ࡧࡩࡸࠥࡺࡥࡳ࡯࡬ࡲࡦࡲࠠࡢࡰࡧࠤࡵࡸࡥࡴࡵࠣࡸ࡭࡫ࠠࡱࡱࡺࡩࡷࠦ࡫ࡦࡻ࠱࠲࠳ࠨव"))
		time.sleep(3)
		sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࡝ࡰࠥश"))
		sys.stdout.write(l11ll_opy_ (u"ࠢ࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳ࠢष"))
		sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࠦस"))
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠤࡌࡓࡎࠦࡉ࡯ࡶࡵࡥࡳ࡫ࡴࠡࡖࡨࡶࡲ࡯࡮ࡢ࡮ࠥह"))
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡏ࡮ࡪࡶ࡬ࡥࡹ࡯࡮ࡨࠢࡺࡥࡰ࡫ࠠࡴࡧࡴࡹࡪࡴࡣࡦ࠰࠱࠲ࠧऺ"))
		time.sleep(3)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎࡲࡥࡩ࡯࡮ࡨࠢࡒࡗ࠳࠴࠮ࠣऻ"))
		time.sleep(2)
		sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡞ࡡ࠲ࡡ࡝࠮࡝ࡠ࠱ࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞࠯࡞ࡡ࠲ࡡ࡝࠮࡝ࡠ࠱ࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞ࠤ़"))
		time.sleep(2)
		while 1:
			time.sleep(3)
			l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮ࡆࡰࡷࡩࡷࠦࡄࡦࡵ࡬ࡶࡪࡪࠠࡂࡥࡷ࡭ࡴࡴ࠺ࠣऽ"))
			sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑࡕࡇࡊࡐࠣࡳࡷࠦࡅ࡙ࡋࡗࡠࡳࡀ࠺ࠣा"))
			l1l1llll1_opy_ = raw_input()
			if ( (l11ll_opy_ (u"ࠣࡎࡒࡋࡎࡔࠢि") in l1l1llll1_opy_) or (l11ll_opy_ (u"ࠤࡏࡳ࡬࡯࡮ࠣी") in l1l1llll1_opy_) or (l11ll_opy_ (u"ࠥࡰࡴ࡭ࡩ࡯ࠤु") in l1l1llll1_opy_) ):
				l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡔࡱ࡫ࡡࡴࡧࠣࡗࡪࡲࡥࡤࡶࠣࡐࡴ࡭ࡩ࡯ࠢࡄࡧࡨࡵࡵ࡯ࡶ࠽ࠤࠧू"))
				time.sleep(1)
				sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡌࡲࡪࡺࠠࡂࡦࡰ࡭ࡳࡢ࡮ࡦ࡮࡯࡭ࡴࡺ࡜࡯ࡵࡷࡳࡷࡳ࡜࡯ࡔ࡟ࡲࡌࡻࡥࡴࡶ࡟ࡲࡡࡴࡅ࡙ࡋࡗࡠࡳࡢ࡮࡝ࡰ࠽࠾ࠧृ"))
				l1l1ll11l_opy_ = raw_input()
				if ( (l11ll_opy_ (u"ࠨࡅ࡙ࡋࡗࠦॄ") in l1l1ll11l_opy_ ) or (l11ll_opy_ (u"ࠢࡆࡺ࡬ࡸࠧॅ") in l1l1ll11l_opy_) or (l11ll_opy_ (u"ࠣࡧࡻ࡭ࡹࠨॆ") in l1l1ll11l_opy_) ):
					break
				l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡅ࡯ࡶࡨࡶࠥࡶࡡࡴࡵࡺࡳࡷࡪࠠࡧࡱࡵࠤࠧे"))
				l1l1lll1l_opy_(l1l1ll11l_opy_)
				l1l1lll1l_opy_(l11ll_opy_ (u"ࠥ࠾ࠥࡢ࡮࡝ࡰ࠽࠾ࠧै"))
				l1l11lll1_opy_ = raw_input()
				if ( (l11ll_opy_ (u"ࠦࡌ࡛ࡅࡔࡖࠥॉ") in l1l1ll11l_opy_ ) or (l11ll_opy_ (u"ࠧࡍࡵࡦࡵࡷࠦॊ") in l1l1ll11l_opy_) or (l11ll_opy_ (u"ࠨࡧࡶࡧࡶࡸࠧो") in l1l1ll11l_opy_ ) ):
					if (l11ll_opy_ (u"ࠢࡱࡣࡶࡷࡼࡵࡲࡥࠤौ") in l1l11lll1_opy_ ):
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡒ࡯ࡨ࡫ࡱࠤࡆࡩࡣࡦࡲࡷࡩࡩ࠴्ࠢ"))
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠤࠣࡍࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡔࡧࡶࡷ࡮ࡵ࡮ࠡࡕ࡫ࡩࡱࡲ࠮࠯࠰ࠥॎ"))
						time.sleep(2)
						sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡕࡻࡳࡩࠥ࠭ࡨࡦ࡮ࡳࠫࠥ࡬࡯ࡳࠢࡤࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡥࡲࡱࡲࡧ࡮ࡥࡵ࡟ࡲࡡࡴ࡜࡯ࠤॏ"))
						l1l111l11_opy_ = l11ll_opy_ (u"ࠦࡌࡻࡥࡴࡶࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩࠩࠦࠢॐ")
						l1l1ll1l1_opy_ = 1
						while 1:
							sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࠥ॑"))
							sys.stdout.write(l1l111l11_opy_)
							l1l1l1l11_opy_ = raw_input()
							if ( (l11ll_opy_ (u"ࠨࡨࡦ࡮ࡳ॒ࠦ") in l1l1l1l11_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡆࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡄࡱࡰࡱࡦࡴࡤࡴ࠼࡟ࡲࡡࡴࡨࡦ࡮ࡳࠤ࠲ࠦࡓࡩࡱࡺࡷࠥࡺࡨࡪࡵࠣࡱࡪࡴࡵࠡ࡞ࡱࡰࡸࠦ࠭ࠡࡎ࡬ࡷࡹࡹࠠࡤࡱࡱࡸࡪࡴࡴࡴࠢࡲࡪࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡞ࡱࡧࡩࠦ࠼ࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࡱࡥࡲ࡫࠾ࠡ࠯ࠣࡇ࡭ࡧ࡮ࡨࡧࡶࠤࡼࡵࡲ࡬࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࡞ࡱࡴࡦࡸࠠ࠮ࠢࡐࡳࡻ࡫ࡳࠡࡶࡲࠤࡵࡧࡲࡦࡰࡷࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࡝ࡰࡦࡥࡹࠦ࠼ࡧ࡫࡯ࡩࡳࡧ࡭ࡦࡀࠣ࠱ࠥࡊࡩࡴࡲ࡯ࡥࡾࡹࠠࡤࡱࡱࡸࡪࡴࡴࡴࠢࡲࡪࠥ࡬ࡩ࡭ࡧࠣࡠࡳ࡫ࡸࡪࡶࠣ࠱ࠥࡒ࡯ࡨࡱࡸࡸࠥࡵࡦࠡࡵࡨࡷࡸ࡯࡯࡯ࠤ॓"))
							if ( (l11ll_opy_ (u"ࠣࡧࡻ࡭ࡹࠨ॔") in l1l1l1l11_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡔࡦࡴࡰ࡭ࡳࡧࡴࡪࡰࡪࠤࡸ࡫ࡳࡴ࡫ࡲࡲ࠳࠴࠮ࠣॕ"))
								break
							if (l1l111l11_opy_ == l11ll_opy_ (u"ࠥࡋࡺ࡫ࡳࡵࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨࠨࠥࠨॖ")):
								if (l11ll_opy_ (u"ࠦࡱࡹࠢॗ") in l1l1l1l11_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯ࡩࡱࡰࡩ࠿ࠨक़"))
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࡫ࡺ࡫ࡳࡵࠢ࠰࠱ࠥࡪࡩࡳ࡞ࡱࡠࡳࡶࡵࡣ࡮࡬ࡧࠥ࠳࠭ࠡࡦ࡬ࡶࡡࡴ࡜࡯ࡧ࡯ࡰ࡮ࡵࡴࠡ࠯࠰ࠤࡩ࡯ࡲ࡝ࡰ࡟ࡲࡸࡵࡲࡳࡧࡱࡸࡴࠦ࠭࠮ࠢࡧ࡭ࡷࡢ࡮࡝ࡰࡶࡸࡴࡸ࡭ࠡ࠯࠰ࠤࡩ࡯ࡲ࡝ࡰ࡟ࡲࡦࡪ࡭ࡪࡰࠣ࠱࠲ࠦࡤࡪࡴࠥख़"))
								if (l11ll_opy_ (u"ࠢࡱࡣࡵࠦग़") in l1l1l1l11_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡉࡷࡸ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡪࡩࡳࠢࠪ࠳ࠬࡀࠠࡂࡥࡦࡩࡸࡹࠠࡥࡧࡱ࡭ࡪࡪ࠮ࠣज़"))
								if (l11ll_opy_ (u"ࠤࡦࡨࠧड़") in l1l1l1l11_opy_):
									if (l11ll_opy_ (u"ࠥ࡫ࡺ࡫ࡳࡵࠤढ़") in l1l1l1l11_opy_):
										l1l1ll1l1_opy_ = 2
									if (l11ll_opy_ (u"ࠦࡵࡻࡢ࡭࡫ࡦࠦफ़") in l1l1l1l11_opy_):
										l1l1ll1l1_opy_ = 3
									if ((l11ll_opy_ (u"ࠧࡹࡴࡰࡴࡰࠦय़") in l1l1l1l11_opy_) or (l11ll_opy_ (u"ࠨࡡࡥ࡯࡬ࡲࠧॠ") in l1l1l1l11_opy_) or (l11ll_opy_ (u"ࠢࡦ࡮࡯࡭ࡴࡺࠢॡ") in l1l1l1l11_opy_) or (l11ll_opy_ (u"ࠣࡵࡲࡶࡷ࡫࡮ࡵࡱࠥॢ") in l1l1l1l11_opy_)):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡊࡸࡲࡰࡴࠣࡥࡨࡩࡥࡴࡵ࡬ࡲ࡬ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺ࠰ࠣࡅࡨࡩࡥࡴࡵࠣࡨࡪࡴࡩࡦࡦ࠱ࠦॣ"))
							if (l1l111l11_opy_ == l11ll_opy_ (u"ࠥࡋࡺ࡫ࡳࡵࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳࡬ࡻࡥࡴࡶࠧࠤࠧ।")):
								if (l11ll_opy_ (u"ࠦࡱࡹࠢ॥") in l1l1l1l11_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯ࡩࡱࡰࡩ࠴࡭ࡵࡦࡵࡷ࠾ࠧ०"))
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡨࡪࡹ࡫ࡵࡱࡳࠤ࠲࠳ࠠࡥ࡫ࡵࡠࡳࡢ࡮ࡥࡱࡦࡹࡲ࡫࡮ࡵࡵࠣ࠱࠲ࠦࡤࡪࡴࠥ१"))
								if (l11ll_opy_ (u"ࠢࡤࡦࠥ२") in l1l1l1l11_opy_):
									if (l11ll_opy_ (u"ࠣࡦࡨࡷࡰࡺ࡯ࡱࠤ३") in l1l1l1l11_opy_):
										l1l1ll1l1_opy_ = 4
									if (l11ll_opy_ (u"ࠤࡧࡳࡨࡻ࡭ࡦࡰࡷࡷࠧ४") in l1l1l1l11_opy_):
										l1l1ll1l1_opy_ = 5
								if (l11ll_opy_ (u"ࠥࡴࡦࡸࠢ५") in l1l1l1l11_opy_):
									l1l1ll1l1_opy_ = 1
							if (l1l111l11_opy_ == l11ll_opy_ (u"ࠦࡌࡻࡥࡴࡶࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩ࠴ࡶࡵࡣ࡮࡬ࡧࠩࠦࠢ६")):
								if (l11ll_opy_ (u"ࠧࡲࡳࠣ७") in l1l1l1l11_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡹࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠰ࡪࡲࡱࡪ࠵ࡰࡶࡤ࡯࡭ࡨࡀࠢ८"))
									sys.stdout.write(l11ll_opy_ (u"ࠢࠣ९"))
								if (l11ll_opy_ (u"ࠣࡲࡤࡶࠧ॰") in l1l1l1l11_opy_):
									l1l1ll1l1_opy_ = 1
							if (l1l111l11_opy_ == l11ll_opy_ (u"ࠤࡊࡹࡪࡹࡴࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲࡫ࡺ࡫ࡳࡵ࠱ࡧࡩࡸࡱࡴࡰࡲࠧࠤࠧॱ")):
								if (l11ll_opy_ (u"ࠥࡰࡸࠨॲ") in l1l1l1l11_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠳࡬ࡻࡥࡴࡶ࠲ࡨࡪࡹ࡫ࡵࡱࡳ࠾ࠧॳ"))
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡦࡥࡱ࡫࡮ࡥࡣࡵ࠲ࡹࡾࡴࠡ࠯࠰ࠤ࡫࡯࡬ࡦࠤॴ"))
								if (l11ll_opy_ (u"ࠨࡣࡢࡶࠥॵ") in l1l1l1l11_opy_):
									if (l11ll_opy_ (u"ࠢࡤࡣ࡯ࡩࡳࡪࡡࡳࠤॶ") in l1l1l1l11_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࡨࡧ࡬ࡦࡰࡧࡥࡷ࠴ࡴࡹࡶ࠱࠲࠳ࠨॷ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࡉࡸࡩࡸࡺࠠࡖࡵࡨࡶࠥࡇࡣࡤࡱࡸࡲࡹࠦࡃࡢ࡮ࡨࡲࡩࡧࡲࠣॸ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡸࡨࡲࡹࠦ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳ࠠࡅࡣࡷࡩࠥ࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰ࠤࡓࡵࡴࡦࡵࠥॹ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡒ࡯ࡥࡳ࡫ࡴࡢࡴ࡬ࡹࡲࠦࡖࡪࡵ࡬ࡸࠥࠦࠠࠡ࠳ࠣࡅࡕࡘࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡔ࠯ࡂࠤॺ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡓࡰࡦࡴ࡮ࡪࡰࡪࠤࡒ࡫ࡥࡵ࡫ࡱ࡫ࠥࠦࠠࠡࠢ࠵࠴ࠥࡓࡁࡓࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡂࡳ࡫ࡱ࡫ࠥࡋ࡬࡭࡫ࡲࡸࠬࡹࠠࡱࡴࡨࡷࡪࡴࡴࡢࡶ࡬ࡳࡳࠨॻ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡗࡾࡹࡴࡦ࡯࡙ࠣࡵࡪࡡࡵࡧࠣࠤࠥࠦࠠࠡࠢࠣ࠵࠽ࠦࡍࡂࡔࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡣࡰ࡯ࡳࡰ࡮ࡧ࡮ࡤࡧࠣࡨࡴࡩࠢॼ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡇࡧࡣ࡬ࡷࡳࠤࡒ࡯ࡧࡳࡣࡷ࡭ࡴࡴࠠࠡࠢࠣࠤ࠶࠾ࠠࡎࡃࡕࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡐ࠲ࡅࠧॽ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡓࡵࡴࡧࡸࡱࠥ࡜ࡩࡴ࡫ࡷࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠷࠵ࠡࡏࡄࡖࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡑࡩࡪࡪࠠࡂࡲࡲࡰࡱࡵࠠ࠲࠳ࠣࡷࡵ࡫ࡥࡤࡪࠣࡨࡴࡩࠢॾ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡓࡺࡵࡷࡩࡲࠦࡕࡱࡦࡤࡸࡪࠦࠠࠡࠢࠣࠤࠥࠦ࠱࠲ࠢࡐࡅࡗࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡭࡫ࡣ࡬ࠢࡦࡳࡲࡶ࡬ࡪࡣࡱࡧࡪࠦࡤࡰࡥࠥॿ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡂࡩࡨࡲࡨࡿࠠࡎࡧࡨࡸ࡮ࡴࡧࠡࠢࠣࠤࠥࠦࠠࠡ࠻ࠣࡑࡆࡘࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡔ࠯ࡂࠤঀ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲ࠨঁ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡡࡴ࠭࠮࠯ࡈࡓࡋ࠳࠭࠮ࠤং"))
								if (l11ll_opy_ (u"ࠨࡰࡢࡴࠥঃ") in l1l1l1l11_opy_):
									l1l1ll1l1_opy_ = 2
							if (l1l111l11_opy_ == l11ll_opy_ (u"ࠢࡈࡷࡨࡷࡹࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡩࡸࡩࡸࡺ࠯ࡥࡱࡦࡹࡲ࡫࡮ࡵࡵࠧࠤࠧ঄")):
								if (l11ll_opy_ (u"ࠣ࡮ࡶࠦঅ") in l1l1l1l11_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡌࡪࡵࡷ࡭ࡳ࡭ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣ࠳࡭ࡵ࡭ࡦ࠱ࡪࡹࡪࡹࡴ࠰ࡦࡲࡧࡺࡳࡥ࡯ࡶࡶ࠾ࠧআ"))
									sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡯ࡧࡹࡩࡷ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮࡮ࡣ࡬ࡰࡳࡵࡴࡦࡵ࠱ࡸࡽࡺࠠ࠮࠯ࠣࡪ࡮ࡲࡥ࡝ࡰ࡟ࡲࡷ࡫࡭ࡪࡰࡧࡩࡷ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮࡭ࡱࡪ࡭ࡳ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮ࠣই"))
								if (l11ll_opy_ (u"ࠦࡨࡧࡴࠣঈ") in l1l1l1l11_opy_):
									if (l11ll_opy_ (u"ࠧࡴࡥࡷࡧࡵࠦউ") in l1l1l1l11_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚࡮࡫ࡷࡪࡰࡪࠤ࡫࡯࡬ࡦࠢࡱࡩࡻ࡫ࡲ࠯ࡶࡻࡸ࠳࠴࠮ࠣঊ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴࡓ࡯ࡩࡵࠤࡺࡴࡦࠡࡤࡨࡵࡳࡼࡡࡳࡳࠣ࡫ࡺࡴࡧࠡࡩࡸࡶࠥࢀࡲࡢࠢ࡭ࡹࡧࠦࡪࡳࡣࡪࠤ࡬ࡨࠠࡨࡷࡵࠤࡿࡨࡢࡢࠢࡪࡦࠥࡸ࡫ࡤࡻࡥࡩࡷࠦࡶࡢࠢࡦࡶࡳࡶࡲࠡ࡬ࡹࡽࡾࠦࡦࡨࡰ࡯ࠤࡧࡧࠠࡨࡷࡵࠤࡿࡨࡢࡢࠢࡪࡦࠥ࡫ࡲࡧࡩࠣࡺࡦࠦࡣࡳࡰࡳࡶ࠳ࠨঋ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡍࡵࡳࡨࡵࠤࡴ࡫࡮ࡪࡴࠣࡾࡷࡧࠬࠡࡃࡵࡺࡾࠦࡎࡦࡼࡩ࡫ࡪࡨࡡࡵࠢࡱࡥࡶࠦࡒࡲ࡬ࡹࡥࠥࡔࡹࡲࡧࡹࡥ࠱ࠦࡸࡢࡤ࡭ࠤ࡬ࡻ࡮ࡨࠢࡪࡹࡷ࡫ࡲࠡࡸࡩࠤࡦࡨࠠࡶࡤࡦࡶࠥࡹࡢࡦࠢࡪࡹࡷࡼࡥࠡࡧࡵࡴࡧ࡯ࡲࡦ࡮࠱ࠤࡔ࡮ࡧࠡࡩࡸࡶࡱࠦ࡮ࡺࡨࡥࠤࡽࡧࡢ࡫ࠢࡪࡹࡳ࡭ࠠࡨࡷࡵࡩࡷࠦࡶࡧࠢࡸࡦࡨࡸࠠࡴࡤࡨࠤࡿࡴࡡࡹࡸࡤࡵࠥࡼࡡࠡࡩࡸࡶࡻ࡫ࠠࡧࡰࡳࡩࡻࡹࡶࡱࡴ࠱ࠦঌ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡇࡶࡴࡩࡶࠥ࡭ࡪࡣࠢࡽࡶࡦࠦ࡮ࡦࡴࠣࡽࡳࡲࡶࡢࡶࠣࡵࡧࡰࡡࠡࡩࡸࡶࡻ࡫ࠠࡺࡸ࡬ࡶ࡫ࠦࡶࡢࠢࡽࡲࡦࡾࡶࡢࡳࠪࡪࠥࢀࡢࡧࡩࠣࡥࡧࡵࡹࡳࠢࡷࡦࡳࡿ࠺ࠡࡩࡸࡶࠥ࡬ࡲ࡯ࡧࡳࡹࠥࡹࡢࡦࠢࡪࡩ࡭࡭ࡵࠡࡰࡤࡵࠥ࡮ࡡࡲࡴࡨࡪ࡬ࡴࡡࡲࡸࡤࡸ࠳ࠨ঍"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡈࡷࡵࡰࠥࡰࡶࡺࡻࠣࡳࡷࠦࡺࡣࡪࡨࡥࡷࡷࠠࡰ࡮ࠣ࡫ࡺࡸࡶࡦࠢࡶࡲࡿࡼࡹࡷࡴࡩࠤࡳࡧࡱࠡࡵࡨࡺࡷࡧࡱࡧ࠽ࠣ࡫ࡺࡸ࡬ࠡ࡬ࡹࡽࡾࠦ࡯ࡳࠢࡽࡦ࡭࡫ࡡࡳࡳࠣࡳࡱࠦࡧࡶࡴࡹࡩࠥࡧ࡮ࡨࡸࡥࡥࡀࠦࡧࡶࡴ࡯ࠤ࡯ࡼࡹࡺࠢࡲࡶࠥࢀࡢࡩࡧࡤࡶࡶࠦ࡯࡭ࠢࡪࡹࡷࠦࡣࡳࡤࡦࡽࡷࠦࡢࡴࠢࡪࡹࡷࠦࡪࡣࡧࡼࡵࡀࠦࡧࡶࡴ࡯ࠤ࡯ࡼࡹࡺࠢࡲࡶࠥࢀࡢࡩࡧࡤࡶࡶࠦ࡯࡭ࠢࡱࠤ࡟ࡨࡧࡶࡴࡨࠤࡗࡴࡥࡨࡷࠣ࡫ࡺࡴࡧࠡࡳࡱࡩࡷࡷࠠࡧࡴࡤࡵࠥ࡭ࡪࡣࠢࡥࡷࠥࡻࡲࡦࠢࡩࡦࡦ࡬ࠠࡷࡣࡪࡦࠥ࡭ࡵࡳࠢ࡫ࡥࡽࡧࡢ࡫ࡣ࠱ࠦ঎"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡘࡤࠤ࡬ࡻࡲࡷࡧࠣࡶࡰࡩࡹࡣࡧࡱ࡫ࡻࡨࡡ࠭ࠢࡪࡹࡷࡲࠠࡧࡩࡹࡩࡪࡸࡱࠡࡩࡸࡶࠥࡩࡲࡣࡥࡼࡶࠥࡨࡳࠡࡩࡸࡶࠥࡰࡢࡦࡻࡴࠤ࡬ࡨࠠࡴࡴࡵࡽࠥࡴࡦࠡࡤࡤࡶࡀࠦࡶࡢࠢࡪࡹࡷࡼࡥࠡࡨࡱࡴࡪࡼࡳࡷࡲࡵ࠰ࠥ࡭ࡵࡳ࡮ࠣࡳࡻࡧࡱࠡࡼࡥࡩࡷࠦࡧࡷࡶࡸ࡫ࡾࡲࠠࡨࡷࡵࠤࡴ࡫ࡢࡨࡷࡵࡩࡺࡨࡢࡲࠢࡥࡷࠥࢀ࡮ࡢ࠰ࠥএ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙ࡥࠥࡴࡡࡱࡸࡵࡥ࡬ࠦࡱ࡯࡮ࡩ࠰ࠥࢀࡲࡢࠢࡼࡦࡧࡾࡲࡲࠢࡱ࡫ࠥ࡬ࡧ࡯ࡧࡩࠤࡳࡧࡱࠡࡨࡱ࡮ࠥ࡭ࡵࡳࡸࡨࠤࡺࡸࡥࡣࡴࡩࠤࡻࡧࠠࡨࡷࡵࠤ࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠳ࠦࡖࡢࠢࡽࡦࡶࡸࡥࡢࠢࡪࡺࡿࡸࡦ࠭ࠢ࡭ࡶࠥࡷࡢࠡࡼ࡫ࡴࡺࠦࡧࡶࡴࠣࡪࡳࢀࡲ࠭ࠢࡲ࡬࡬ࠦࡢࡩࡧࠣࡹࡷ࡫ࡢࡳࡨࠣࡲࡪࡸࠠࡳࡥࡹࡴࠥࢀࡲࡢࠢࡥࡷࠥࡹࡹࡳࡨࡸࠤࡳࡧࡱࠡࡱࡼࡦࡧࡷ࠮ࠣঐ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡆ࡬ࡻࡲࡦࡨࠣ࡮ࡻࡿࡹࠡࡵࡥࡽࡾࡨࡪ࠭ࠢࡱࡥࡶࠦࡦࡩࡧࡵࡽࡱࠦࡳࡷࡣࡴࠤ࡬ࡻࡲࡷࡧࠣ࡮ࡳࡲࠠࡶࡤࡽࡶ࠳࡚ࠦ࡯ࡣࠪࡪࠥ࡬ࡲ࡯ࡧࡳࡹࠥࡰࡶࡺࡻࠣࡥࡧ࡭ࠠࡰࡴࠣࡵࡷࡧࡶࡳࡳ࠱ࠤࡔ࡮ࡧࠡࡩࡸࡶ࡫ࡸࠠࡻࡴࡤࠤ࡯ࡸࡥࡳࠢࡪࡹࡷࠦࡳࡷࡧࡩ࡫࠱ࠦ࡮ࡢࡳࠣ࡫ࡺࡸ࡬ࠡ࡬ࡹࡽࡾࠦࡥࡳࡼࡱࡺࡦࠦࡧࡶࡴࠣࡷࡧ࡫ࡲࡻࡤࡩ࡫ࠥࡼࡡࠡࡤ࡫ࡩࠥࡻࡲ࡯ࡧࡪࡪ࠳ࠨ঑"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡘࡨࡥࠡࡴ࡬ࡶࡪࡲࠠࡶࡪࡽࡲࡦࠦ࡯ࡳࡸࡤࡸࠥࡰࡵࡣࠢࡼࡦࡧࡾࡦࠡࡪࡦࠤࡳ࡭ࠠࡨࡷࡵࠤࡿࡨࡢࡢࠢࡹࡥࠥ࡭ࡵࡳࠢࡤࡺࡹࡻࡧࡧࠢࡪࡦࠥࡶࡢࡻࡴࠣ࡮ࡻࡿࡹࠡࡺࡤࡦ࡯ࠦࡧࡶࡰࡪࠤ࡬ࡻࡲࡦࡴࠣࡺ࡫ࠦࡦࡣࡼࡵࠤࡵࡨࡥࡢࡴࡨࠤࡧࡹࠠ࡯ࡣࡥ࡫ࡺࡸࡥࠡ࡬ࡥࡩࡾࡷࠠࡨࡷࡱ࡫ࠥࡼࡦࠡࡵࡥࡩࡷ࡯ࡲࡦࠢࡽࡲࡦࡾࡶࡢࡳ࠱ࠦ঒"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧও"))
									if (l11ll_opy_ (u"ࠤࡰࡥ࡮ࡲ࡮ࡰࡶࡨࡷࠧঔ") in l1l1l1l11_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦ࡭ࡢ࡫࡯ࡲࡴࡺࡥࡴ࠰ࡷࡼࡹ࠴࠮࠯ࠤক"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡔࡷࡵࡣ࡮ࡣ࡬ࡰࠥࡳࡡࡪ࡮ࡶࡰࡴࡺࠠࡴࡧࡵࡺࡪࡸࠢখ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙ࡩࡷࡹࡩࡰࡰࠣ࠷࠳࠷࠮࠶ࠤগ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳ࡛ࡐࡅࡃࡗࡉࠥࡔࡅࡆࡆࡈࡈࠥ࠳ࠠࡷ࠰ࠣ࠷࠳࠸࠮࠱ࠢࡄ࡚ࡆࡏࡌࡂࡄࡏࡉࠧঘ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦঙ"))
									if (l11ll_opy_ (u"ࠣࡴࡨࡱ࡮ࡴࡤࡦࡴࠥচ") in l1l1l1l11_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡸࡥ࡮࡫ࡱࡨࡪࡸ࠮ࡵࡺࡷ࠲࠳࠴ࠢছ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡇࡥࡹ࡫࠺ࠡ࠴࠻ࠤࡋࡋࡂࠣজ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡉࡸࡩࡸࡺࠠࡢࡥࡦࡳࡺࡴࡴࠡࡥࡵࡩࡦࡺࡥࡥࠢࡲࡲࠥࡏ࡮ࡵࡴࡤࡲࡪࡺࠠࡵࡧࡵࡱ࡮ࡴࡡ࡭࠰ࠣࠤࡈ࡮ࡡ࡯ࡩࡨࠤࡩ࡫ࡦࡢࡷ࡯ࡸࠥࡶࡡࡴࡵࡺࡳࡷࡪ࠮ࠣঝ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡡࡴ࠭࠮࠯ࡈࡓࡋ࠳࠭࠮ࠤঞ"))
									if (l11ll_opy_ (u"ࠨ࡬ࡰࡩ࡬ࡲࠧট") in l1l1l1l11_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠢࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦ࡬ࡰࡩ࡬ࡲ࠳ࡺࡸࡵ࠰࠱࠲ࠧঠ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࡊࡖ࠰ࡅࡉࡓࡉࡏࠢࡕࡩࡲ࡯࡮ࡥࡧࡵࠦড"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡐࡦࡴࡶࡹࡦࡴࡴࠡࡶࡲࠤࡈࡵ࡭ࡱࡣࡱࡽࠥࡖ࡯࡭࡫ࡦࡽࠥࡒࡥࡵࡶࡨࡶࠥ࠷࠰࠮࠳࠼࠼࠿ࠦࡉࡕࠢࡖࡽࡸࡺࡥ࡮ࠢࡆࡶࡪࡪࡥ࡯ࡶ࡬ࡥࡱࠦࡍࡢࡰࡤ࡫ࡪࡳࡥ࡯ࡶ࠯ࠤࡵࡲࡥࡢࡵࡨࠤࡩࡵࠠࡏࡑࡗࠤࡸࡺ࡯ࡳࡧࠣࡰࡴ࡭ࡩ࡯ࠢࡧࡩࡹࡧࡩ࡭ࡵࠣࡪࡴࡸࠠࡱࡧࡵࡷࡴࡴࡡ࡭ࠢࡤࡧࡨࡵࡵ࡯ࡶࡶࠤࡴࡴࠠࡵࡪࡨࠤ࡬ࡻࡥࡴࡶࠣࡥࡨࡩ࡯ࡶࡰࡷࠤ࡮ࡴࡳࡵࡣࡱࡧࡪ࠴ࠢঢ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡅࡣࡷࡩࡩࡀࠠ࠲ࠢࡉࡉࡇࠨণ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮ࡇࡒࡊ࠲࠳࠭ࠣত"))
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤথ") in l1l1l1l11_opy_):
									l1l1ll1l1_opy_ = 3
							if (l1l1ll1l1_opy_ == 1):
								l1l111l11_opy_ = l11ll_opy_ (u"ࠨࡇࡶࡧࡶࡸࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫ࠤࠡࠤদ")
							if (l1l1ll1l1_opy_ == 2):
								l1l111l11_opy_ = l11ll_opy_ (u"ࠢࡈࡷࡨࡷࡹࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡩࡸࡩࡸࡺࠤࠡࠤধ")
							if (l1l1ll1l1_opy_ == 3):
								l1l111l11_opy_ = l11ll_opy_ (u"ࠣࡉࡸࡩࡸࡺࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡳࡹࡧࡲࡩࡤࠦࠣࠦন")
							if (l1l1ll1l1_opy_ == 4):
								l1l111l11_opy_ = l11ll_opy_ (u"ࠤࡊࡹࡪࡹࡴࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲࡫ࡺ࡫ࡳࡵ࠱ࡧࡩࡸࡱࡴࡰࡲࠧࠤࠧ঩")
							if (l1l1ll1l1_opy_ == 5):
								l1l111l11_opy_ = l11ll_opy_ (u"ࠥࡋࡺ࡫ࡳࡵࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳࡬ࡻࡥࡴࡶ࠲ࡨࡴࡩࡵ࡮ࡧࡱࡸࡸࠪࠠࠣপ")
					else:
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡵࡶࡴࡸ࠮ࠡࡋࡱࡺࡦࡲࡩࡥࠢࡓࡥࡸࡹࡷࡰࡴࡧࠦফ"))
				elif ( (l11ll_opy_ (u"ࠧࡏࡎࡆࡖࠣࡅࡉࡓࡉࡏࠤব") in l1l1ll11l_opy_) or (l11ll_opy_ (u"ࠨࡩ࡯ࡧࡷࠤࡦࡪ࡭ࡪࡰࠥভ") in l1l1ll11l_opy_) or (l11ll_opy_ (u"ࠢࡊࡰࡨࡸࠥࡇࡤ࡮࡫ࡱࠦম") in l1l1ll11l_opy_) ):
					if ( l11ll_opy_ (u"ࠣࡥࡲࡲࡸࡺࡥ࡭࡮ࡤࡸ࡮ࡵ࡮ࡴࠤয") in l1l11lll1_opy_ ):
						time.sleep(2)
						l1l1l11ll_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡌࡰࡩ࡬ࡲࠥࡇࡣࡤࡧࡳࡸࡪࡪ࠮ࠣর"))
						time.sleep(3)
						if (l1ll11111_opy_ == 0):
							l1ll11111_opy_ = 1
							clear()
		   					time.sleep(2)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࡗ࡮ࡳࡰ࡭ࡧࠣࡱ࡮ࡹࡴࡢ࡭ࡨࡷࠥࡳࡡ࡬ࡧࠣࡷࡲࡧ࡬࡭ࠢࡩࡰࡦࡽࡳࠡ࡫ࡱࠤࡧ࡯ࡧࠡࡵࡼࡷࡹ࡫࡭ࡴ࠰ࠥ঱"))
		   					time.sleep(2)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡄࡨࡪࡴࡸࡥࠡࡻࡲࡹ࠱ࠦࡴࡩࡧࠣࡨࡦࡺࡡࠡࡥࡲࡰࡺࡳ࡮ࠡࡲࡸࡰࡸ࡫ࡳࠡࡤࡵ࡭࡬࡮ࡴ࡭ࡻ࠱ࠦল"))
		   					time.sleep(1)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࠦࠠࡂࡴࡲࡹࡳࡪࠠࡺࡱࡸ࠰ࠥࡺࡨࡦࠢ࡫ࡳࡷ࡯ࡺࡰࡰࠣ࡫ࡱࡵࡷࡴࠢࡵࡩࡩ࠴ࠢ঳"))
		   					time.sleep(2)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚࡮ࡹࡩࡰࡰࡶࠤࡴ࡬ࠠࡵࡧࡵࡶࡴࡸࠠࡣࡷࡵࡲࠥ࡯࡮ࠡࡻࡲࡹࡷࠦࡰࡦࡴ࡬ࡴ࡭࡫ࡲࡢ࡮ࡶ࠲ࠧ঴"))
		   					time.sleep(4)
		   					clear()
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠢࠡࡋࡱ࡭ࡹ࡯ࡡࡵ࡫ࡱ࡫࡙ࠥࡥࡴࡵ࡬ࡳࡳࠦࡓࡩࡧ࡯ࡰ࠳࠴࠮ࠣ঵"))
						time.sleep(2)
						sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡚ࡹࡱࡧࠣࠫ࡭࡫࡬ࡱࠩࠣࡪࡴࡸࠠࡢࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࡝ࡰ࡟ࡲࡡࡴࠢশ"))
						l1l11l1l1_opy_ = l11ll_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫ࠤࠡࠤষ")
						l1l11llll_opy_ = 1
						while 1:
							sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࠣস"))
							sys.stdout.write(l1l11l1l1_opy_)
							l1l11111l_opy_ = raw_input()
							if ( (l11ll_opy_ (u"ࠦ࡭࡫࡬ࡱࠤহ") in l1l11111l_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡄࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡉ࡯࡮࡯ࡤࡲࡩࡹ࠺࡝ࡰ࡟ࡲ࡭࡫࡬ࡱࠢ࠰ࠤࡘ࡮࡯ࡸࡵࠣࡸ࡭࡯ࡳࠡ࡯ࡨࡲࡺࠦ࡜࡯࡮ࡶࠤ࠲ࠦࡌࡪࡵࡷࡷࠥࡩ࡯࡯ࡶࡨࡲࡹࡹࠠࡰࡨࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡜࡯ࡥࡧࠤࡁࡪࡩࡳࡧࡦࡸࡴࡸࡹ࡯ࡣࡰࡩࡃࠦ࠭ࠡࡅ࡫ࡥࡳ࡭ࡥࡴࠢࡺࡳࡷࡱࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡜࡯ࡲࡤࡶࠥ࠳ࠠࡎࡱࡹࡩࡸࠦࡴࡰࠢࡳࡥࡷ࡫࡮ࡵࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡢ࡮ࡤࡣࡷࠤࡁ࡬ࡩ࡭ࡧࡱࡥࡲ࡫࠾ࠡ࠯ࠣࡈ࡮ࡹࡰ࡭ࡣࡼࡷࠥࡩ࡯࡯ࡶࡨࡲࡹࡹࠠࡰࡨࠣࡪ࡮ࡲࡥࠡ࡞ࡱࡩࡽ࡯ࡴࠡ࠯ࠣࡐࡴ࡭࡯ࡶࡶࠣࡳ࡫ࠦࡳࡦࡵࡶ࡭ࡴࡴࠢ঺"))
							if ( (l11ll_opy_ (u"ࠨࡥࡹ࡫ࡷࠦ঻") in l1l11111l_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡙࡫ࡲ࡮࡫ࡱࡥࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰ࠱࠲࠳ࠨ়"))
								break
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪࠪࠠࠣঽ")):
								if (l11ll_opy_ (u"ࠤ࡯ࡷࠧা") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠽ࠦি"))
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡩࡸࡩࡸࡺࠠ࠮࠯ࠣࡨ࡮ࡸ࡜࡯࡞ࡱࡴࡺࡨ࡬ࡪࡥࠣ࠱࠲ࠦࡤࡪࡴ࡟ࡲࡡࡴࡥ࡭࡮࡬ࡳࡹࠦ࠭࠮ࠢࡧ࡭ࡷࡢ࡮࡝ࡰࡶࡳࡷࡸࡥ࡯ࡶࡲࠤ࠲࠳ࠠࡥ࡫ࡵࡠࡳࡢ࡮ࡴࡶࡲࡶࡲࠦ࠭࠮ࠢࡧ࡭ࡷࠨী"))
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤু") in l1l11111l_opy_):
									l1l11llll_opy_ = 0
								if (l11ll_opy_ (u"ࠨࡣࡥࠤূ") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠢࡨࡷࡨࡷࡹࠨৃ") in l1l11111l_opy_):
										l1l11llll_opy_ = 2
									if (l11ll_opy_ (u"ࠣࡲࡸࡦࡱ࡯ࡣࠣৄ") in l1l11111l_opy_):
										l1l11llll_opy_ = 3
									if (l11ll_opy_ (u"ࠤࡨࡰࡱ࡯࡯ࡵࠤ৅") in l1l11111l_opy_):
										l1l11llll_opy_ = 6
									if (l11ll_opy_ (u"ࠥࡷࡹࡵࡲ࡮ࠤ৆") in l1l11111l_opy_):
										l1l11llll_opy_ = 8
									if (l11ll_opy_ (u"ࠦࡸࡵࡲࡳࡧࡱࡸࡴࠨে") in l1l11111l_opy_):
										l1l11llll_opy_ = 10
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠧࡏࡎࡆࡖࡄࡈࡒࡏࡎࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲࡫ࡺ࡫ࡳࡵࠦࠣࠦৈ")):
								if (l11ll_opy_ (u"ࠨ࡬ࡴࠤ৉") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯ࡳࡵ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠱࡫ࡳࡲ࡫࠯ࡨࡷࡨࡷࡹࡀࠢ৊"))
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡪࡥࡴ࡭ࡷࡳࡵࠦ࠭࠮ࠢࡧ࡭ࡷࡢ࡮࡝ࡰࡧࡳࡨࡻ࡭ࡦࡰࡷࡷࠥ࠳࠭ࠡࡦ࡬ࡶࠧো"))
								if (l11ll_opy_ (u"ࠤࡦࡨࠧৌ") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠥࡨࡪࡹ࡫ࡵࡱࡳ্ࠦ") in l1l11111l_opy_):
										l1l11llll_opy_ = 4
									if (l11ll_opy_ (u"ࠦࡩࡵࡣࡶ࡯ࡨࡲࡹࡹࠢৎ") in l1l11111l_opy_):
										l1l11llll_opy_ = 5
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤ৏") in l1l11111l_opy_):
									l1l11llll_opy_ = 1
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠨࡉࡏࡇࡗࡅࡉࡓࡉࡏࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡵࡻࡢ࡭࡫ࡦࠨࠥࠨ৐")):
								if (l11ll_opy_ (u"ࠢ࡭ࡵࠥ৑") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡒࡩࡴࡶ࡬ࡲ࡬ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࠲࡬ࡴࡳࡥ࠰ࡲࡸࡦࡱ࡯ࡣ࠻ࠤ৒"))
									sys.stdout.write(l11ll_opy_ (u"ࠤࠥ৓"))
								if (l11ll_opy_ (u"ࠥࡴࡦࡸࠢ৔") in l1l11111l_opy_):
									l1l11llll_opy_ = 1
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠦࡎࡔࡅࡕࡃࡇࡑࡎࡔࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡪࡹࡪࡹࡴ࠰ࡦࡨࡷࡰࡺ࡯ࡱࠦࠣࠦ৕")):
								if (l11ll_opy_ (u"ࠧࡲࡳࠣ৖") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡹࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠰ࡪࡲࡱࡪ࠵ࡧࡶࡧࡶࡸ࠴ࡪࡥࡴ࡭ࡷࡳࡵࡀࠢৗ"))
									sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡨࡧ࡬ࡦࡰࡧࡥࡷ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࠦ৘"))
								if (l11ll_opy_ (u"ࠣࡥࡤࡸࠧ৙") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠤࡦࡥࡱ࡫࡮ࡥࡣࡵࠦ৚") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࡣࡢ࡮ࡨࡲࡩࡧࡲ࠯ࡶࡻࡸ࠳࠴࠮ࠣ৛"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡋࡺ࡫ࡳࡵࠢࡘࡷࡪࡸࠠࡂࡥࡦࡳࡺࡴࡴࠡࡅࡤࡰࡪࡴࡤࡢࡴࠥড়"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡺࡪࡴࡴࠡ࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮ࠢࡇࡥࡹ࡫ࠠ࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲ࠦࡎࡰࡶࡨࡷࠧঢ়"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡔࡱࡧ࡮ࡦࡶࡤࡶ࡮ࡻ࡭ࠡࡘ࡬ࡷ࡮ࡺࠠࠡࠢࠣ࠵ࠥࡇࡐࡓࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡏ࠱ࡄࠦ৞"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡕࡲࡡ࡯ࡰ࡬ࡲ࡬ࠦࡍࡦࡧࡷ࡭ࡳ࡭ࠠࠡࠢࠣࠤ࠷࠶ࠠࡎࡃࡕࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡄࡵ࡭ࡳ࡭ࠠࡆ࡮࡯࡭ࡴࡺࠧࡴࠢࡳࡶࡪࡹࡥ࡯ࡶࡤࡸ࡮ࡵ࡮ࠣয়"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡙ࡹࡴࡶࡨࡱ࡛ࠥࡰࡥࡣࡷࡩࠥࠦࠠࠡࠢࠣࠤࠥ࠷࠸ࠡࡏࡄࡖࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡࡥࡲࡱࡵࡲࡩࡢࡰࡦࡩࠥࡪ࡯ࡤࠤৠ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡂࡢࡥ࡮ࡹࡵࠦࡍࡪࡩࡵࡥࡹ࡯࡯࡯ࠢࠣࠤࠥࠦ࠱࠹ࠢࡐࡅࡗࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡒ࠴ࡇࠢৡ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡎࡷࡶࡩࡺࡳࠠࡗ࡫ࡶ࡭ࡹࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠲࠷ࠣࡑࡆࡘࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡓ࡫ࡥࡥࠢࡄࡴࡴࡲ࡬ࡰࠢ࠴࠵ࠥࡹࡰࡦࡧࡦ࡬ࠥࡪ࡯ࡤࠤৢ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡕࡼࡷࡹ࡫࡭ࠡࡗࡳࡨࡦࡺࡥࠡࠢࠣࠤࠥࠦࠠࠡ࠳࠴ࠤࡒࡇࡒࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤࡨࡵ࡭ࡱ࡮࡬ࡥࡳࡩࡥࠡࡦࡲࡧࠧৣ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡄ࡫ࡪࡴࡣࡺࠢࡐࡩࡪࡺࡩ࡯ࡩࠣࠤࠥࠦࠠࠡࠢࠣ࠽ࠥࡓࡁࡓࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡏ࠱ࡄࠦ৤"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭ࠣ৥"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦ০"))
								if (l11ll_opy_ (u"ࠣࡲࡤࡶࠧ১") in l1l11111l_opy_):
									l1l11llll_opy_ = 2
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡨࡷࡨࡷࡹ࠵ࡤࡰࡥࡸࡱࡪࡴࡴࡴࠦࠣࠦ২")):
								if (l11ll_opy_ (u"ࠥࡰࡸࠨ৩") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠳࡬ࡻࡥࡴࡶ࠲ࡨࡴࡩࡵ࡮ࡧࡱࡸࡸࡀࠢ৪"))
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡱࡩࡻ࡫ࡲ࠯ࡶࡻࡸࠥ࠳࠭ࠡࡨ࡬ࡰࡪࡢ࡮࡝ࡰࡰࡥ࡮ࡲ࡮ࡰࡶࡨࡷ࠳ࡺࡸࡵࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴࡲࡦ࡯࡬ࡲࡩ࡫ࡲ࠯ࡶࡻࡸࠥ࠳࠭ࠡࡨ࡬ࡰࡪࡢ࡮࡝ࡰ࡯ࡳ࡬࡯࡮࠯ࡶࡻࡸࠥ࠳࠭ࠡࡨ࡬ࡰࡪࡢ࡮࡝ࡰࠥ৫"))
								if (l11ll_opy_ (u"ࠨࡣࡢࡶࠥ৬") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠢ࡯ࡧࡹࡩࡷࠨ৭") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤࡳ࡫ࡶࡦࡴ࠱ࡸࡽࡺ࠮࠯࠰ࠥ৮"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯ࡕࡱ࡫ࡷࠦࡵ࡯ࡨࠣࡦࡪࡷ࡮ࡷࡣࡵࡵࠥ࡭ࡵ࡯ࡩࠣ࡫ࡺࡸࠠࡻࡴࡤࠤ࡯ࡻࡢࠡ࡬ࡵࡥ࡬ࠦࡧࡣࠢࡪࡹࡷࠦࡺࡣࡤࡤࠤ࡬ࡨࠠࡳ࡭ࡦࡽࡧ࡫ࡲࠡࡸࡤࠤࡨࡸ࡮ࡱࡴࠣ࡮ࡻࡿࡹࠡࡨࡪࡲࡱࠦࡢࡢࠢࡪࡹࡷࠦࡺࡣࡤࡤࠤ࡬ࡨࠠࡦࡴࡩ࡫ࠥࡼࡡࠡࡥࡵࡲࡵࡸ࠮ࠣ৯"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡈࡷࡵࡪࡷࠦ࡯ࡦࡰ࡬ࡶࠥࢀࡲࡢ࠮ࠣࡅࡷࡼࡹࠡࡐࡨࡾ࡫࡭ࡥࡣࡣࡷࠤࡳࡧࡱࠡࡔࡴ࡮ࡻࡧࠠࡏࡻࡴࡩࡻࡧࠬࠡࡺࡤࡦ࡯ࠦࡧࡶࡰࡪࠤ࡬ࡻࡲࡦࡴࠣࡺ࡫ࠦࡡࡣࠢࡸࡦࡨࡸࠠࡴࡤࡨࠤ࡬ࡻࡲࡷࡧࠣࡩࡷࡶࡢࡪࡴࡨࡰ࠳ࠦࡏࡩࡩࠣ࡫ࡺࡸ࡬ࠡࡰࡼࡪࡧࠦࡸࡢࡤ࡭ࠤ࡬ࡻ࡮ࡨࠢࡪࡹࡷ࡫ࡲࠡࡸࡩࠤࡺࡨࡣࡳࠢࡶࡦࡪࠦࡺ࡯ࡣࡻࡺࡦࡷࠠࡷࡣࠣ࡫ࡺࡸࡶࡦࠢࡩࡲࡵ࡫ࡶࡴࡸࡳࡶ࠳ࠨৰ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡉࡸࡶ࡫ࡸࠠࡨ࡬ࡥࠤࡿࡸࡡࠡࡰࡨࡶࠥࡿ࡮࡭ࡸࡤࡸࠥࡷࡢ࡫ࡣࠣ࡫ࡺࡸࡶࡦࠢࡼࡺ࡮ࡸࡦࠡࡸࡤࠤࡿࡴࡡࡹࡸࡤࡵࠬ࡬ࠠࡻࡤࡩ࡫ࠥࡧࡢࡰࡻࡵࠤࡹࡨ࡮ࡺ࠼ࠣ࡫ࡺࡸࠠࡧࡴࡱࡩࡵࡻࠠࡴࡤࡨࠤ࡬࡫ࡨࡨࡷࠣࡲࡦࡷࠠࡩࡣࡴࡶࡪ࡬ࡧ࡯ࡣࡴࡺࡦࡺ࠮ࠣৱ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡊࡹࡷࡲࠠ࡫ࡸࡼࡽࠥࡵࡲࠡࡼࡥ࡬ࡪࡧࡲࡲࠢࡲࡰࠥ࡭ࡵࡳࡸࡨࠤࡸࡴࡺࡷࡻࡹࡶ࡫ࠦ࡮ࡢࡳࠣࡷࡪࡼࡲࡢࡳࡩ࠿ࠥ࡭ࡵࡳ࡮ࠣ࡮ࡻࡿࡹࠡࡱࡵࠤࡿࡨࡨࡦࡣࡵࡵࠥࡵ࡬ࠡࡩࡸࡶࡻ࡫ࠠࡢࡰࡪࡺࡧࡧ࠻ࠡࡩࡸࡶࡱࠦࡪࡷࡻࡼࠤࡴࡸࠠࡻࡤ࡫ࡩࡦࡸࡱࠡࡱ࡯ࠤ࡬ࡻࡲࠡࡥࡵࡦࡨࡿࡲࠡࡤࡶࠤ࡬ࡻࡲࠡ࡬ࡥࡩࡾࡷ࠻ࠡࡩࡸࡶࡱࠦࡪࡷࡻࡼࠤࡴࡸࠠࡻࡤ࡫ࡩࡦࡸࡱࠡࡱ࡯ࠤࡳ࡚ࠦࡣࡩࡸࡶࡪࠦࡒ࡯ࡧࡪࡹࠥ࡭ࡵ࡯ࡩࠣࡵࡳ࡫ࡲࡲࠢࡩࡶࡦࡷࠠࡨ࡬ࡥࠤࡧࡹࠠࡶࡴࡨࠤ࡫ࡨࡡࡧࠢࡹࡥ࡬ࡨࠠࡨࡷࡵࠤ࡭ࡧࡸࡢࡤ࡭ࡥ࠳ࠨ৲"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚ࡦࠦࡧࡶࡴࡹࡩࠥࡸ࡫ࡤࡻࡥࡩࡳ࡭ࡶࡣࡣ࠯ࠤ࡬ࡻࡲ࡭ࠢࡩ࡫ࡻ࡫ࡥࡳࡳࠣ࡫ࡺࡸࠠࡤࡴࡥࡧࡾࡸࠠࡣࡵࠣ࡫ࡺࡸࠠ࡫ࡤࡨࡽࡶࠦࡧࡣࠢࡶࡶࡷࡿࠠ࡯ࡨࠣࡦࡦࡸ࠻ࠡࡸࡤࠤ࡬ࡻࡲࡷࡧࠣࡪࡳࡶࡥࡷࡵࡹࡴࡷ࠲ࠠࡨࡷࡵࡰࠥࡵࡶࡢࡳࠣࡾࡧ࡫ࡲࠡࡩࡹࡸࡺ࡭ࡹ࡭ࠢࡪࡹࡷࠦ࡯ࡦࡤࡪࡹࡷ࡫ࡵࡣࡤࡴࠤࡧࡹࠠࡻࡰࡤ࠲ࠧ৳"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛ࡧࠠ࡯ࡣࡳࡺࡷࡧࡧࠡࡳࡱࡰ࡫࠲ࠠࡻࡴࡤࠤࡾࡨࡢࡹࡴࡴࠤࡳ࡭ࠠࡧࡩࡱࡩ࡫ࠦ࡮ࡢࡳࠣࡪࡳࡰࠠࡨࡷࡵࡺࡪࠦࡵࡳࡧࡥࡶ࡫ࠦࡶࡢࠢࡪࡹࡷࠦ࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠮ࠡࡘࡤࠤࡿࡨࡱࡳࡧࡤࠤ࡬ࡼࡺࡳࡨ࠯ࠤ࡯ࡸࠠࡲࡤࠣࡾ࡭ࡶࡵࠡࡩࡸࡶࠥ࡬࡮ࡻࡴ࠯ࠤࡴ࡮ࡧࠡࡤ࡫ࡩࠥࡻࡲࡦࡤࡵࡪࠥࡴࡥࡳࠢࡵࡧࡻࡶࠠࡻࡴࡤࠤࡧࡹࠠࡴࡻࡵࡪࡺࠦ࡮ࡢࡳࠣࡳࡾࡨࡢࡲ࠰ࠥ৴"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡈࡧࡶࡴࡨࡪࠥࡰࡶࡺࡻࠣࡷࡧࡿࡹࡣ࡬࠯ࠤࡳࡧࡱࠡࡨ࡫ࡩࡷࡿ࡬ࠡࡵࡹࡥࡶࠦࡧࡶࡴࡹࡩࠥࡰ࡮࡭ࠢࡸࡦࡿࡸ࠮ࠡ࡜ࡱࡥࠬ࡬ࠠࡧࡴࡱࡩࡵࡻࠠ࡫ࡸࡼࡽࠥࡧࡢࡨࠢࡲࡶࠥࡷࡲࡢࡸࡵࡵ࠳ࠦࡏࡩࡩࠣ࡫ࡺࡸࡦࡳࠢࡽࡶࡦࠦࡪࡳࡧࡵࠤ࡬ࡻࡲࠡࡵࡹࡩ࡫࡭ࠬࠡࡰࡤࡵࠥ࡭ࡵࡳ࡮ࠣ࡮ࡻࡿࡹࠡࡧࡵࡾࡳࡼࡡࠡࡩࡸࡶࠥࡹࡢࡦࡴࡽࡦ࡫࡭ࠠࡷࡣࠣࡦ࡭࡫ࠠࡶࡴࡱࡩ࡬࡬࠮ࠣ৵"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡓࡣࡧࠣࡶ࡮ࡸࡥ࡭ࠢࡸ࡬ࡿࡴࡡࠡࡱࡵࡺࡦࡺࠠ࡫ࡷࡥࠤࡾࡨࡢࡹࡨࠣ࡬ࡨࠦ࡮ࡨࠢࡪࡹࡷࠦࡺࡣࡤࡤࠤࡻࡧࠠࡨࡷࡵࠤࡦࡼࡴࡶࡩࡩࠤ࡬ࡨࠠࡱࡤࡽࡶࠥࡰࡶࡺࡻࠣࡼࡦࡨࡪࠡࡩࡸࡲ࡬ࠦࡧࡶࡴࡨࡶࠥࡼࡦࠡࡨࡥࡾࡷࠦࡰࡣࡧࡤࡶࡪࠦࡢࡴࠢࡱࡥࡧ࡭ࡵࡳࡧࠣ࡮ࡧ࡫ࡹࡲࠢࡪࡹࡳ࡭ࠠࡷࡨࠣࡷࡧ࡫ࡲࡪࡴࡨࠤࡿࡴࡡࡹࡸࡤࡵ࠳ࠨ৶"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢ৷"))
									if (l11ll_opy_ (u"ࠦࡲࡧࡩ࡭ࡰࡲࡸࡪࡹࠢ৸") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡ࡯ࡤ࡭ࡱࡴ࡯ࡵࡧࡶ࠲ࡹࡾࡴ࠯࠰࠱ࠦ৹"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡖࡲࡰࡥࡰࡥ࡮ࡲࠠ࡮ࡣ࡬ࡰࡸࡲ࡯ࡵࠢࡶࡩࡷࡼࡥࡳࠤ৺"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡫ࡲࡴ࡫ࡲࡲࠥ࠹࠮࠲࠰࠸ࠦ৻"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࡖࡒࡇࡅ࡙ࡋࠠࡏࡇࡈࡈࡊࡊࠠ࠮ࠢࡹ࠲ࠥ࠹࠮࠳࠰࠳ࠤࡆ࡜ࡁࡊࡎࡄࡆࡑࡋࠢৼ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨ৽"))
									if (l11ll_opy_ (u"ࠥࡶࡪࡳࡩ࡯ࡦࡨࡶࠧ৾") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࡳࡧࡰ࡭ࡳࡪࡥࡳ࠰ࡷࡼࡹ࠴࠮࠯ࠤ৿"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡉࡧࡴࡦ࠼ࠣ࠶࠽ࠦࡆࡆࡄࠥ਀"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡋࡺ࡫ࡳࡵࠢࡤࡧࡨࡵࡵ࡯ࡶࠣࡧࡷ࡫ࡡࡵࡧࡧࠤࡴࡴࠠࡊࡰࡷࡶࡦࡴࡥࡵࠢࡷࡩࡷࡳࡩ࡯ࡣ࡯࠲ࠥࠦࡃࡩࡣࡱ࡫ࡪࠦࡤࡦࡨࡤࡹࡱࡺࠠࡱࡣࡶࡷࡼࡵࡲࡥ࠰ࠥਁ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦਂ"))
									if (l11ll_opy_ (u"ࠣ࡮ࡲ࡫࡮ࡴࠢਃ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡲ࡯ࡨ࡫ࡱ࠲ࡹࡾࡴ࠯࠰࠱ࠦ਄"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰࡌࡘ࠲ࡇࡄࡎࡋࡑࠤࡗ࡫࡭ࡪࡰࡧࡩࡷࠨਅ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡒࡨࡶࡸࡻࡡ࡯ࡶࠣࡸࡴࠦࡃࡰ࡯ࡳࡥࡳࡿࠠࡑࡱ࡯࡭ࡨࡿࠠࡍࡧࡷࡸࡪࡸࠠ࠲࠲࠰࠵࠾࠾࠺ࠡࡋࡗࠤࡘࡿࡳࡵࡧࡰࠤࡈࡸࡥࡥࡧࡱࡸ࡮ࡧ࡬ࠡࡏࡤࡲࡦ࡭ࡥ࡮ࡧࡱࡸ࠱ࠦࡰ࡭ࡧࡤࡷࡪࠦࡤࡰࠢࡑࡓ࡙ࠦࡳࡵࡱࡵࡩࠥࡲ࡯ࡨ࡫ࡱࠤࡩ࡫ࡴࡢ࡫࡯ࡷࠥ࡬࡯ࡳࠢࡳࡩࡷࡹ࡯࡯ࡣ࡯ࠤࡦࡩࡣࡰࡷࡱࡸࡸࠦ࡯࡯ࠢࡷ࡬ࡪࠦࡧࡶࡧࡶࡸࠥࡧࡣࡤࡱࡸࡲࡹࠦࡩ࡯ࡵࡷࡥࡳࡩࡥ࠯ࠤਆ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡇࡥࡹ࡫ࡤ࠻ࠢ࠴ࠤࡋࡋࡂࠣਇ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡠࡳࡢ࡮࠮࠯࠰ࡉࡔࡌ࠭࠮࠯ࠥਈ"))
								if (l11ll_opy_ (u"ࠢࡱࡣࡵࠦਉ") in l1l11111l_opy_):
									l1l11llll_opy_ = 3
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡥ࡭࡮࡬ࡳࡹࠪࠠࠣਊ")):
								if (l11ll_opy_ (u"ࠤ࡯ࡷࠧ਋") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠲ࡩࡱࡲࡩࡰࡶ࠽ࠦ਌"))
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡷࡶࡩࡷࡶࡲࡰࡨ࡬ࡰࡪ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮࡮ࡣ࡬ࡰࠥ࠳࠭ࠡࡦ࡬ࡶࠧ਍"))
								if (l11ll_opy_ (u"ࠧࡩࡤࠣ਎") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠨ࡭ࡢ࡫࡯ࠦਏ") in l1l11111l_opy_):
										l1l11llll_opy_ = 7
								if (l11ll_opy_ (u"ࠢࡤࡣࡷࠦਐ") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠣࡷࡶࡩࡷࡶࡲࡰࡨ࡬ࡰࡪࠨ਑") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡻࡳࡦࡴࡳࡶࡴ࡬ࡩ࡭ࡧ࠱ࡸࡽࡺ࠮࠯࠰ࠥ਒"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡊࡐࡨࡸ࠲࡚ࡥࡳ࡯࡙ࠣࡸ࡫ࡲ࠻ࠢࡨࡰࡱ࡯࡯ࡵࠤਓ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡄࡢࡶࡨࠤࡨࡸࡥࡢࡶࡨࡨ࠿ࠦ࠱࠴ࠢࡉࡉࡇࠦ࠱࠹ࠤਔ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡍࡣࡶࡸࠥࡹࡥࡦࡰ࠽ࠤ࠼ࠦ࡭ࡰࡰࡷ࡬ࡸࠨਕ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡐࡲࠤࡺࡴࡲࡦࡣࡧࠤࡲ࡫ࡳࡴࡣࡪࡩࡸࠨਖ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰࡓࡶ࡮ࡼࠠ࡭ࡧࡹࡩࡱࡀࠠࡑࡱࡺࡩࡷࡻࡳࡦࡴࠥਗ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡒࡴࡺࡥࡴ࠼ࠣࠤࠥࠨਘ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨਙ"))
								if (l11ll_opy_ (u"ࠥࡴࡦࡸࠢਚ") in l1l11111l_opy_):
									l1l11llll_opy_ = 1
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠦࡎࡔࡅࡕࡃࡇࡑࡎࡔࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡨࡰࡱ࡯࡯ࡵ࠱ࡰࡥ࡮ࡲࠤࠡࠤਛ")):
								if (l11ll_opy_ (u"ࠧࡲࡳࠣਜ") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡹࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠰ࡪࡲࡱࡪ࠵ࡥ࡭࡮࡬ࡳࡹ࠵࡭ࡢ࡫࡯࠾ࠧਝ"))
									sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࠵࠿ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴ࠲࠲ࡆࡈࡇ࠶࠾࠮࡮ࡵࡪࠤ࠲࠳ࠠࡧ࡫࡯ࡩࡡࡴ࡜࡯࠳࠶ࡊࡊࡈ࠱࠹࠰ࡰࡷ࡬ࠦ࠭࠮ࠢࡩ࡭ࡱ࡫ࠢਞ"))
								if (l11ll_opy_ (u"ࠣࡥࡤࡸࠧਟ") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠤ࠳࠽ࡏࡇࡎ࠲࠻ࠥਠ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦ࠰࠺ࡌࡄࡒ࠶࠿࠮࡮ࡵࡪ࠾ࠧਡ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡈࡵࡳࡲࡀࠠࡋ࠰ࠣࡗࡹࡵࡲ࡮ࠤਢ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡕࡱ࠽ࠤࡊࡲ࡬ࡪࡱࡷࠤࡘ࠴ࠢਣ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡔࡈ࠾ࠥࡔࡏࡗࡃ࡙ࠣࡵࡪࡡࡵࡧࠥਤ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰࡆࡐࡆ࡙ࡓ࠻ࠢࡖࡉࡓ࡙ࠢਥ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡋ࡬࡭࡫ࡲࡸ࠱ࡴ࡜࡯ࡆࡲࡲࠬࡺࠠࡱࡷࡷࠤࡹ࡮ࡩࡴࠢࡲࡲࠥ࡫࠭࡮ࡣ࡬ࡰࠥ࠳࠭ࠡࡶࡲࡳࠥࡳࡵࡤࡪࠣࡲࡴ࡯ࡳࡦ࠰ࠣࡑࡪ࡫ࡴࠡ࡫ࡱࡷ࡮ࡪࡥࠡࡉࡤࡸࡪࠦ࠴ࡄࠢ࡬ࡲࠥ࠹࠰࠯࡞ࡱࡠࡳ࠳ࡓࡵࡱࡵࡱࠧਦ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨਧ"))
									if (l11ll_opy_ (u"ࠥ࠶࠶ࡊࡅࡄ࠳࠻ࠦਨ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠ࠳࠳ࡇࡉࡈ࠷࠸࠯࡯ࡶ࡫࠿ࠨ਩"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡉࡶࡴࡳ࠺ࠡࡌ࠱ࠤࡘࡺ࡯ࡳ࡯ࠥਪ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡖࡲ࠾ࠥࡋ࡬࡭࡫ࡲࡸ࡙ࠥ࠮ࠣਫ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰࡕࡉ࠿ࠦࡐࡰ࡮࡬ࡧࡾࠦࡕࡱࡦࡤࡸࡪࠦࡔࡢࡵ࡮࡭ࡳ࡭ࠢਬ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡇࡑࡇࡓࡔ࠼ࠣࡗࡊࡔࡓࠣਭ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡅ࡭࡮࡬ࡳࡹ࠲࡜࡯ࡑࡹࡩࡷࡺࡩ࡮ࡧࠣࡪࡺࡴࡤࡪࡰࡪࠤ࡫ࡵࡲࠡ࡯ࡤ࡭ࡳࡺࡥ࡯ࡣࡱࡧࡪࠦࡩࡴࠢࡤࡴࡵࡸ࡯ࡷࡧࡧ࠲ࠥࠦࡍࡢ࡭ࡨࠤࡸࡻࡲࡦࠢࡼࡳࡺࠦࡨࡢࡸࡨࠤࡾࡵࡵࡳࠢࡳࡩࡴࡶ࡬ࡦࠢࡷࡥࡰ࡫ࠠࡢࠢ࡯ࡳࡴࡱࠠࡢࡶࠣࡸ࡭࡫ࠠࡢࡷࡧ࡭ࡹࠦ࡬ࡰࡩࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡣࡳࡱࡱࠤ࡬ࡧࡴࡦࠢ࠰ࠤࡼ࡫ࠠࡩࡣࡧࠤࡷ࡫ࡰࡰࡴࡷࡷࠥࡵࡦࠡࡤࡲࡸࡸࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡶࡸࡧࡰࠦ࡯࡯ࠢࡷ࡬ࡪ࡯ࡲࠡࡹࡤࡽࠥࡵࡵࡵࠢ࡯ࡥࡸࡺࠠࡸࡧࡨ࡯࠳ࡢ࡮࡝ࡰ࠰ࡗࡹࡵࡲ࡮ࠤਮ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢਯ"))
									if (l11ll_opy_ (u"ࠦ࠶࠹ࡆࡆࡄ࠴࠼ࠧਰ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡ࠴࠳ࡊࡊࡈ࠱࠹࠰ࡰࡷ࡬ࡀࠢ਱"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡊࡷࡵ࡭࠻ࠢࡖࠦਲ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰࡗࡳ࠿ࠦࡅ࡭࡮࡬ࡳࡹࠦࡓ࠯ࠤਲ਼"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡖࡊࡀࠠࡐࡰࡥࡳࡦࡸࡤࡪࡰࡪࠦ਴"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡈࡒࡁࡔࡕ࠽ࠤࡘࡋࡎࡔࠤਵ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡆ࡮࡯࡭ࡴࡺ࠺࡝ࡰ࡚ࡩࡱࡩ࡯࡮ࡧ࠱ࠤࡔࡴࡢࡰࡣࡵࡨ࡮ࡴࡧࠡࡨࡲࡶࠥࡔࡏࡗࡃࠣࡷ࡮ࡺࡥࠡࡶࡨࡥࡲࠦ࡯࡯ࠢ࠴࠴ࠥࡓࡁࡓࠢࡤࡸࠥ࠶࠸࠱࠲࠱ࠤࠥࡌࡩ࡯ࡣ࡯ࠤࡹ࡫ࡡ࡮ࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡪࡵࡦࠢࡲࡲࡪࠦࡷࡦࡧ࡮ࠤࡵࡸࡩࡰࡴ࠱ࡠࡳࡢ࡮ࡅࡱࠣࡲࡴࡺࠠࡥ࡫ࡶࡥࡵࡶ࡯ࡪࡰࡷ࠲ࡡࡴ࡜࡯࠯ࡖࠦਸ਼"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢ਷"))
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤਸ") in l1l11111l_opy_):
									l1l11llll_opy_ = 6
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠨࡉࡏࡇࡗࡅࡉࡓࡉࡏࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡺ࡯ࡳ࡯ࠧࠤࠧਹ")):
								if (l11ll_opy_ (u"ࠢ࡭ࡵࠥ਺") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡒࡩࡴࡶ࡬ࡲ࡬ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࠲࡬ࡴࡳࡥ࠰ࡵࡷࡳࡷࡳ࠺ࠣ਻"))
									sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡵࡴࡧࡵࡴࡷࡵࡦࡪ࡮ࡨ࠲ࡹࡾࡴࠡ࠯࠰ࠤ࡫࡯࡬ࡦ࡞ࡱࡠࡳࡳࡡࡪ࡮ࠣ࠱࠲ࠦࡤࡪࡴ਼ࠥ"))
								if (l11ll_opy_ (u"ࠥࡧࡩࠨ਽") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠦࡲࡧࡩ࡭ࠤਾ") in l1l11111l_opy_):
										l1l11llll_opy_ = 9
								if (l11ll_opy_ (u"ࠧࡩࡡࡵࠤਿ") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠨࡵࡴࡧࡵࡴࡷࡵࡦࡪ࡮ࡨࠦੀ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯ࡥࡸ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࡹࡸ࡫ࡲࡱࡴࡲࡪ࡮ࡲࡥ࠯ࡶࡻࡸ࠳࠴࠮ࠣੁ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡏࡎࡦࡶ࠰ࡘࡪࡸ࡭ࠡࡗࡶࡩࡷࡀࠠࡴࡶࡲࡶࡲࠨੂ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡉࡧࡴࡦࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤ࠷ࠦࡏࡄࡖࠣ࠵࠼ࠨ੃"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡒࡡࡴࡶࠣࡷࡪ࡫࡮࠻ࠢ࠴࠸ࠥ࡮࡯ࡶࡴࡶࠦ੄"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡎࡰࠢࡸࡲࡷ࡫ࡡࡥࠢࡰࡩࡸࡹࡡࡨࡧࡶࠦ੅"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡑࡴ࡬ࡺࠥࡲࡥࡷࡧ࡯࠾ࠥࡖ࡯ࡸࡧࡵࡹࡸ࡫ࡲࠣ੆"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡐࡲࡸࡪࡹ࠺ࠡࠢࠣࠦੇ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦੈ"))
								if (l11ll_opy_ (u"ࠣࡲࡤࡶࠧ੉") in l1l11111l_opy_):
									l1l11llll_opy_ = 1
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡴࡶࡲࡶࡲ࠵࡭ࡢ࡫࡯ࠨࠥࠨ੊")):
								if (l11ll_opy_ (u"ࠥࡰࡸࠨੋ") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠳ࡸࡺ࡯ࡳ࡯࠲ࡱࡦ࡯࡬࠻ࠤੌ"))
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࠴࠶ࡏࡇࡎ࠲࠻࠱ࡱࡸ࡭ࠠ࠮࠯ࠣࡪ࡮ࡲࡥ࡝ࡰ࡟ࡲ࠶࠶ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴ࠰࠹ࡌࡄࡒ࠶࠿࠮࡮ࡵࡪࠤ࠲࠳ࠠࡧ࡫࡯ࡩࡡࡴ࡜࡯࠴࠹ࡊࡊࡈ࠱࠹࠰ࡰࡷ࡬ࠦ࠭࠮ࠢࡩ࡭ࡱ࡫੍ࠢ"))
								if (l11ll_opy_ (u"ࠨࡣࡢࡶࠥ੎") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠢ࠲࠴ࡍࡅࡓ࠷࠹ࠣ੏") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤ࠶࠸ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨ࠼ࠥ੐"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡆࡳࡱࡰ࠾࡙ࠥ࠮ࠣੑ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡘࡅ࠻ࠢࡑࡓ࡛ࡇࠢ੒"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡃࡍࡃࡖࡗ࠿ࠦࡓࡆࡐࡖࠦ੓"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡍࡩࡸࡹࡩࡤࡣ࠯ࡠࡳࡢ࡮ࡕࡪࡨࠤࡨࡵ࡭ࡱࡣࡱࡽࠥ࡯ࡳࠡࡩࡵࡥࡹ࡫ࡦࡶ࡮ࠣࡪࡴࡸࠠࡺࡱࡸࡶࠥࡲ࡯ࡺࡣ࡯ࡸࡾ࠴࡜࡯࡞ࡱࡍࡳࠦࡴࡩࡧࠣ࡭ࡳࡺࡥࡳ࡫ࡰ࠰ࠥࡿ࡯ࡶࠢࡺ࡭ࡱࡲࠠࡣࡧࠣࡥࡸࡹࡵ࡮࡫ࡱ࡫ࠥࡺࡨࡦࠢ࡯ࡩࡦࡪࠠࡧࡱࡵࠤࡹ࡮ࡥࠡࡐࡒ࡚ࡆࠦࡩ࡯࡫ࡷ࡭ࡦࡺࡩࡷࡧ࠱ࠤࠥࡊ࡯ࠡࡰࡲࡸࠥࡪࡩࡴࡣࡳࡴࡴ࡯࡮ࡵ࠰ࠥ੔"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࠱ࡘࠨ੕"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦ੖"))
									if (l11ll_opy_ (u"ࠣ࠳࠳ࡎࡆࡔ࠱࠺ࠤ੗") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠷࠰ࡋࡃࡑ࠵࠾࠴࡭ࡴࡩ࠽ࠦ੘"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡇࡴࡲࡱ࠿ࠦࡅ࡭࡮࡬ࡳࡹࠦࡓ࠯ࠤਖ਼"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡒࡆ࠼࡙ࠣࡗࡍࡅࡏࡖࠥਗ਼"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡄࡎࡄࡗࡘࡀࠠࡖࡐࡆࡐࡆ࡙ࡓࠣਜ਼"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࡛ࡍࡋࡒࡆࠢࡄࡖࡊ࡙ࠦࡐࡗࠤࡃࠦࠦࡈࡆࠩࡖࠤࡔ࡛ࡔࡔࡋࡇࡉࠥࡓ࡙ࠡࡑࡉࡊࡎࡉࡅࠢࠣࠤࡠࡳࡢ࡮࡚ࡱࡸࠤࡌࡇࡖࡆࠢࡐࡉࠥ࡟ࡏࡖࡔ࡛ࠣࡔࡘࡄࠣੜ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦ੝"))
									if (l11ll_opy_ (u"ࠣ࠲࠻ࡎࡆࡔ࠱࠺ࠤਫ਼") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠶࠸ࡋࡃࡑ࠵࠾࠴࡭ࡴࡩ࠽ࠦ੟"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡇࡴࡲࡱ࠿ࠦࡅ࡭࡮࡬ࡳࡹࠦࡓ࠯ࠤ੠"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡔࡰ࠼ࠣࡎ࠳ࠦࡓࡵࡱࡵࡱࠧ੡"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡓࡇ࠽ࠤࡓࡕࡖࡂࠢࡘࡴࡩࡧࡴࡦࠤ੢"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡅࡏࡅࡘ࡙࠺ࠡࡕࡈࡒࡘࠨ੣"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡏ࡫ࡳࡴ࡫ࡦࡥ࠱ࡢ࡮ࡊࡶࠣࡰࡴࡵ࡫ࡴࠢ࡯࡭ࡰ࡫ࠠࡰࡰࡨࠤࡴ࡬ࠠࡵࡪࡨࠤࡦࡪ࡭ࡪࡰࡶࠤࡧࡵࡴࡤࡪࡨࡨࠥ࡮ࡩࡴࠢࡶࡩࡨࡺࡩࡰࡰࠣࡳ࡫ࠦࡴࡩࡧࠣࡴࡴࡲࡩࡤࡻࠣࡹࡵࡪࡡࡵࡧࠣࡴࡷࡵࡧࡳࡣࡰ࠲ࠥࠦࡗࡦࠢࡱࡩࡪࡪࠠࡵࡱࠣࡹࡵࡪࡡࡵࡧࠣࡸ࡭ࡵࡳࡦࠢࡤࡧࡨ࡫ࡳࡴࠢࡳࡳࡱ࡯ࡣࡪࡧࡶࠤࡆ࡙ࡁࡑ࠽ࠣࡨࡴࡻࡢࡵࠢࡤࡲࡾࡵ࡮ࡦࠢ࡬ࡷࠥࡧࡷࡢࡴࡨࠤࡴ࡬ࠠࡵࡪࡲࡷࡪࠦࡧࡢࡶࡨࡷ࠱ࠦࡢࡶࡶࠣࡸ࡭࡯ࡳࠡ࡫ࡶࠤࡷ࡫ࡡ࡭࡮ࡼࠤࡴࡻࡴࡥࡣࡷࡩࡩࠦࡳࡵࡷࡩࡪ࠳ࠨ੤"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࡅࡱࠣࡻࡪࠦࡴࡦ࡮࡯ࠤࡘࡅ࡜࡯࡞ࡱ࠱ࡊࡲ࡬ࡪࡱࡷࠦ੥"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨ੦"))
									if (l11ll_opy_ (u"ࠥ࠸ࡓࡕࡖ࠲࠺ࠥ੧") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡘ࡬ࡩࡼ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠ࠳࠸ࡉࡉࡇ࠷࠸࠯࡯ࡶ࡫࠿ࠨ੨"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡉࡶࡴࡳ࠺ࠡࡇ࡯ࡰ࡮ࡵࡴࠡࡕ࠱ࠦ੩"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡖࡲ࠾ࠥࡐ࠮ࠡࡕࡷࡳࡷࡳࠢ੪"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰࡕࡉ࠿ࠦࡔࡦࡣࡰࠤࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠢ੫"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡇࡑࡇࡓࡔ࠼ࠣࡗࡊࡔࡓࠣ੬"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡊࡦࡵࡶ࡭ࡨࡧࠬ࡝ࡰ࡟ࡲ࡙࡮ࡡ࡯࡭ࡶࠤ࡫ࡵࡲࠡࡶ࡫ࡩࠥࡧࡳࡴ࡫ࡶࡸࠥࡽࡩࡵࡪࠣࡸࡪࡧ࡭ࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱ࠲ࠥࠦࡍࡦ࡯ࡲࠤ࡮ࡹࠠࡥࡷࡨࠤ࡮ࡴࠠࡰࡰࡨࠤࡼ࡫ࡥ࡬࠮ࠣࡦࡺࡺࠠࡸࡧࠪࡶࡪࠦࡳࡵ࡫࡯ࡰࠥࡹࡣࡳࡣࡰࡦࡱ࡯࡮ࡨࠢࡷࡳࠥ࡬ࡩ࡭࡮ࠣࡸ࡭࡫ࠠࡴࡧࡦࡹࡷ࡯ࡴࡺࠢࡶࡩࡨࡺࡩࡰࡰ࠱ࠤࠥࡉࡡ࡯ࠢࡼࡳࡺࡸࠠࡵࡧࡤࡱࠥࡸࡥࡤࡥࡲࡱࡪࡴࡤࠡࡵࡲࡱࡪࡵ࡮ࡦࡁࠥ੭"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࠮ࡇ࡯ࡰ࡮ࡵࡴࠣ੮"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮ࡇࡒࡊ࠲࠳࠭ࠣ੯"))
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤੰ") in l1l11111l_opy_):
									l1l11llll_opy_ = 8
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠨࡉࡏࡇࡗࡅࡉࡓࡉࡏࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴࠪࠠࠣੱ")):
								if (l11ll_opy_ (u"ࠢ࡭ࡵࠥੲ") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡒࡩࡴࡶ࡬ࡲ࡬ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࠲࡬ࡴࡳࡥ࠰ࡵࡲࡶࡷ࡫࡮ࡵࡱ࠽ࠤࠧੳ"))
									sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡵࡴࡧࡵࡴࡷࡵࡦࡪ࡮ࡨ࠲ࡹࡾࡴࠡ࠯࠰ࠤ࡫࡯࡬ࡦ࡞ࡱࡠࡳࡳࡡࡪ࡮ࠣ࠱࠲ࠦࡤࡪࡴࠥੴ"))
								if (l11ll_opy_ (u"ࠥࡧࡩࠨੵ") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠦࡲࡧࡩ࡭ࠤ੶") in l1l11111l_opy_):
										l1l11llll_opy_ = 11
								if (l11ll_opy_ (u"ࠧࡩࡡࡵࠤ੷") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠨࡵࡴࡧࡵࡴࡷࡵࡦࡪ࡮ࡨࠦ੸") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯ࡥࡸ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࡹࡸ࡫ࡲࡱࡴࡲࡪ࡮ࡲࡥ࠯ࡶࡻࡸ࠳࠴࠮ࠣ੹"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡏࡎࡦࡶ࠰ࡘࡪࡸ࡭ࠡࡗࡶࡩࡷࡀࠠࡴࡱࡵࡶࡪࡴࡴࡰࠤ੺"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡉࡧࡴࡦࠢࡦࡶࡪࡧࡴࡦࡦ࠽ࠤ࠶࠹ࠠࡋࡗࡏࠤ࠶࠼ࠢ੻"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡒࡡࡴࡶࠣࡷࡪ࡫࡮࠻ࠢ࠴࠼ࠥࡳࡩ࡯ࡷࡷࡩࡸࠨ੼"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡎࡰࠢࡸࡲࡷ࡫ࡡࡥࠢࡰࡩࡸࡹࡡࡨࡧࡶࠦ੽"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡑࡴ࡬ࡺࠥࡲࡥࡷࡧ࡯࠾ࠥࡇࡤ࡮࡫ࡱࠦ੾"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡐࡲࡸࡪࡹ࠺ࠡࡒࡕࡍ࡛࡛ࡓࡆࡔ࠯ࠤࡉࡕࠠࡏࡑࡗࠤࡒࡕࡖࡆࠢࡒࡖࠥࡓࡉࡈࡔࡄࡘࡊࠦࠢ੿"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦ઀"))
								if (l11ll_opy_ (u"ࠣࡲࡤࡶࠧઁ") in l1l11111l_opy_):
									l1l11llll_opy_ = 1
							if (l1l11l1l1_opy_ == l11ll_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡴࡱࡵࡶࡪࡴࡴࡰ࠱ࡰࡥ࡮ࡲࠤࠡࠤં")):
								if (l11ll_opy_ (u"ࠥࡰࡸࠨઃ") in l1l11111l_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴ࠵࡭ࡢ࡫࡯࠾ࠧ઄"))
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࠴࠴ࡏࡇࡎ࠲࠻࠱ࡱࡸ࡭ࠠ࠮࠯ࠣࡪ࡮ࡲࡥ࡝ࡰ࡟ࡲ࠵࠿ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨࠢ࠰࠱ࠥ࡬ࡩ࡭ࡧ࡟ࡲࡡࡴ࠲࠱ࡈࡈࡆ࠶࠾࠮࡮ࡵࡪࠤ࠲࠳ࠠࡧ࡫࡯ࡩࡡࡴ࡜࡯࠳࠶ࡎ࡚ࡒ࠱࠷࠰ࡰࡷ࡬ࠦ࠭࠮ࠢࡩ࡭ࡱ࡫ࠢઅ"))
								if (l11ll_opy_ (u"ࠨࡣࡢࡶࠥઆ") in l1l11111l_opy_):
									if (l11ll_opy_ (u"ࠢ࠲࠲ࡍࡅࡓ࠷࠹ࠣઇ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡜ࡩࡦࡹ࡬ࡲ࡬ࠦࡦࡪ࡮ࡨࠤ࠶࠶ࡊࡂࡐ࠴࠽࠳ࡳࡳࡨ࠼ࠥઈ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡆࡓࡑࡐ࠾ࠥࡋ࡬࡭࡫ࡲࡸ࡙ࠥࠢઉ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳ࡚ࡏ࠻ࠢࡖࠦઊ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡒࡆ࠼ࠣࡑࡦ࡯࡮ࠡࡆࡵ࡭ࡻ࡫ࠠࡂࡥࡦࡩࡸࡹࠢઋ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡄࡎࡄࡗࡘࡀࠠࡉࡋࡖࡉࡓ࡙ࠢઌ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡗ࡮ࡸࠬ࡝ࡰ࡟ࡲࡆࡳࠠࡶࡰࡤࡦࡱ࡫ࠠࡵࡱࠣࡥࡨࡩࡥࡴࡵࠣࡸ࡭࡫ࠠ࡮ࡣ࡬ࡲࠥࡶࡲࡰ࡬ࡨࡧࡹࠦࡤࡳ࡫ࡹࡩࠥ࡬࡯ࡳࠢࡑࡓ࡛ࡇࠠ࠮࠯ࠣ࡭ࡸࠦࡴࡩࡧࡵࡩࠥࡧ࡮ࠡ࡫ࡶࡷࡺ࡫ࠠࡸ࡫ࡷ࡬ࠥࡳࡹࠡࡣࡦࡧࡪࡹࡳࠡࡲࡨࡶࡲ࡯ࡳࡴ࡫ࡲࡲࡸࡅ࡜࡯࡞ࡱ࠱ࡊࡲ࡬ࡪࡱࡷࠦઍ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦ઎"))
									if (l11ll_opy_ (u"ࠣ࠲࠼ࡎࡆࡔ࠱࠺ࠤએ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥ࠶࠹ࡋࡃࡑ࠵࠾࠴࡭ࡴࡩ࠽ࠦઐ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡇࡔࡒࡑ࠿ࠦࡊ࠯ࠢࡖࡸࡴࡸ࡭ࠣઑ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴࡔࡐ࠼ࠣࡗࠧ઒"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡖࡴࡪࡩࡳࡺ࠺ࠡࡐࡒ࡚ࡆࠦࡁࡤࡶ࡬ࡳࡳࠨઓ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡅࡏࡅࡘ࡙࠺ࠡࡊࡌࡗࡊࡔࡓࠣઔ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡘ࡯ࡲ࠭࡞ࡱࡠࡳ࡝ࡥࠡࡰࡨࡩࡩࠦࡴࡰࠢࡶࡴࡪࡧ࡫ࠡ࡫ࡰࡱࡪࡪࡩࡢࡶࡨࡰࡾࠦࡣࡰࡰࡦࡩࡷࡴࡩ࡯ࡩࠣࡉࡱࡲࡩࡰࡶ࠱ࡠࡳࡢ࡮࠮ࡌࡨࡷࡸ࡯ࡣࡢࠤક"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧખ"))
									if (l11ll_opy_ (u"ࠤ࠵࠴ࡋࡋࡂ࠲࠺ࠥગ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦ࠲࠱ࡈࡈࡆ࠶࠾࠮࡮ࡵࡪ࠾ࠧઘ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡈࡕࡓࡒࡀࠠࡆ࡮࡯࡭ࡴࡺࠠࡔࠤઙ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮ࡕࡑ࠽ࠤࡘࠨચ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯ࡔࡈ࠾ࠥࡔࡏࡗࡃࠣࡓࡳࡨ࡯ࡢࡴࡧ࡭ࡳ࡭ࠢછ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰࡆࡇ࠿ࠦࡊ࠯ࠢࡖࡸࡴࡸ࡭ࠣજ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡇࡑࡇࡓࡔ࠼ࠣࡗࡊࡔࡓࠣઝ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡓࡪࡴ࠯ࡠࡳࡢ࡮ࡂࡶࡷࡥࡨ࡮ࡥࡥࠢ࡬ࡷࠥࡺࡨࡦࠢࡩ࡭ࡳࡧ࡬ࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡱ࡯ࡳࡵࠢࡩࡳࡷࠦࡴࡩࡧࠣࡲࡪࡾࡴࠡࡐࡒ࡚ࡆࠦࡰࡩࡣࡶࡩ࠳ࠦࠠࡋࡧࡶࡷ࡮ࡩࡡࠡࡹ࡬ࡰࡱࠦࡢࡦࠢࡳࡶࡴࡼࡩࡥ࡫ࡱ࡫ࠥࡧ࡮ࡺࠢࡤࡨࡩ࡯ࡴࡪࡱࡱࡥࡱࠦࡩ࡯ࡨࡲࡶࡲࡧࡴࡪࡱࡱࠤࡳ࡫ࡣࡦࡵࡶࡥࡷࡿ࠮࡝ࡰ࡟ࡲ࠲ࡋ࡬࡭࡫ࡲࡸࠧઞ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲ࠲࠳࠭ࡆࡑࡉ࠱࠲࠳ࠢટ"))
									if (l11ll_opy_ (u"ࠦ࠶࠹ࡊࡖࡎ࠴࠺ࠧઠ") in l1l11111l_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡ࠳࠶ࡎ࡚ࡒ࠱࠷࠰ࡰࡷ࡬ࡀࠢડ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡊࡗࡕࡍ࠻ࠢࡖࠦઢ"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰࡗࡓ࠿ࠦࡓࠣણ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣࡔࡈ࠾ࠥࠦࠢત"))
										sys.stdout.write(l11ll_opy_ (u"ࠤࡆࡐࡆ࡙ࡓ࠻ࠢࠣࠤࠧથ"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡨࡱࡲ࠲࡬ࡲ࠯ࡑ࠹࠸ࡥࡋࡋࠢદ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮ࡇࡒࡊ࠲࠳࠭ࠣધ"))
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤન") in l1l11111l_opy_):
									l1l11llll_opy_ = 10
							if (l1l11llll_opy_ == 0):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠨࡉࡏࡇࡗࡅࡉࡓࡉࡏࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࠤࠡࠤ઩")
							if (l1l11llll_opy_ == 1):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠢࡊࡐࡈࡘࡆࡊࡍࡊࡐࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩࠩࠦࠢપ")
							if (l1l11llll_opy_ == 2):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡧࡶࡧࡶࡸࠩࠦࠢફ")
							if (l1l11llll_opy_ == 3):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡱࡷࡥࡰ࡮ࡩࠤࠡࠤબ")
							if (l1l11llll_opy_ == 4):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠥࡍࡓࡋࡔࡂࡆࡐࡍࡓࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡩࡸࡩࡸࡺ࠯ࡥࡧࡶ࡯ࡹࡵࡰࠥࠢࠥભ")
							if (l1l11llll_opy_ == 5):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠦࡎࡔࡅࡕࡃࡇࡑࡎࡔࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡪࡹࡪࡹࡴ࠰ࡦࡲࡧࡺࡳࡥ࡯ࡶࡶࠨࠥࠨમ")
							if (l1l11llll_opy_ == 6):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠧࡏࡎࡆࡖࡄࡈࡒࡏࡎࡁࡋࡱࡩࡹ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡩࡱࡲࡩࡰࡶࠧࠤࠧય")
							if (l1l11llll_opy_ == 7):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠨࡉࡏࡇࡗࡅࡉࡓࡉࡏࡂࡌࡲࡪࡺࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡪࡲ࡬ࡪࡱࡷ࠳ࡲࡧࡩ࡭ࠦࠣࠦર")
							if (l1l11llll_opy_ == 8):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠢࡊࡐࡈࡘࡆࡊࡍࡊࡐࡃࡍࡳ࡫ࡴࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩ࠴ࡹࡴࡰࡴࡰࠨࠥࠨ઱")
							if (l1l11llll_opy_ == 9):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠣࡋࡑࡉ࡙ࡇࡄࡎࡋࡑࡄࡎࡴࡥࡵࡖࡨࡶࡲࡀࡾ࠰ࡪࡲࡱࡪ࠵ࡳࡵࡱࡵࡱ࠴ࡳࡡࡪ࡮ࠧࠤࠧલ")
							if (l1l11llll_opy_ == 10):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠤࡌࡒࡊ࡚ࡁࡅࡏࡌࡒࡅࡏ࡮ࡦࡶࡗࡩࡷࡳ࠺ࡿ࠱࡫ࡳࡲ࡫࠯ࡴࡱࡵࡶࡪࡴࡴࡰࠦࠣࠦળ")
							if (l1l11llll_opy_ == 11):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠥࡍࡓࡋࡔࡂࡆࡐࡍࡓࡆࡉ࡯ࡧࡷࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥ࠰ࡵࡲࡶࡷ࡫࡮ࡵࡱ࠲ࡱࡦ࡯࡬ࠥࠢࠥ઴")
							if (l1l11llll_opy_ == 12):
								l1l11l1l1_opy_ = l11ll_opy_ (u"ࠦࡎࡔࡅࡕࡃࡇࡑࡎࡔࡀࡊࡰࡨࡸ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡤࡨࡲ࡯࡮ࠥࠢࠥવ")
					else:
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡶࡷࡵࡲ࠯ࠢࡌࡲࡻࡧ࡬ࡪࡦࠣࡔࡦࡹࡳࡸࡱࡵࡨࠧશ"))
				else:
					time.sleep(2)
					l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡷࡸ࡯ࡳ࠰ࠣࡍࡳࡼࡡ࡭࡫ࡧࠤࡕࡧࡳࡴࡹࡲࡶࡩ࠴ࠢષ"))
			else:
				l1l1lll1l_opy_(l11ll_opy_ (u"ࠢࡆࡺ࡬ࡸ࡮ࡴࡧࠡࡵࡼࡷࡹ࡫࡭࠯࠰࠱ࠦસ"))
				time.sleep(2)
				break
	else:
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡟࡯ࡶࠢࡤࡴࡵࡸ࡯ࡢࡥ࡫ࠤࡹ࡮ࡥࠡࡴ࡬࡫࡭ࡺࠠࡵࡧࡵࡱ࡮ࡴࡡ࡭ࠢࡤࡲࡩࠦࡰࡳࡧࡶࡷࠥࡺࡨࡦࠢࡳࡳࡼ࡫ࡲࠡ࡭ࡨࡽ࠳࠴࠮ࠣહ"))
		time.sleep(3)
		sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱࡠࡳࠨ઺"))
		sys.stdout.write(l11ll_opy_ (u"ࠥ࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯࠰࠱࠲࠳࠭࠮࠯ࠥ઻"))
		sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ઼ࠢ"))
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡔࡏࡗࡃࠣࡇࡴࡴࡴࡳࡱ࡯ࠤ࡙࡫ࡲ࡮࡫ࡱࡥࡱࠨઽ"))
		time.sleep(2)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯ࡋࡱ࡭ࡹ࡯ࡡࡵ࡫ࡱ࡫ࠥࡽࡡ࡬ࡧࠣࡷࡪࡷࡵࡦࡰࡦࡩ࠳࠴࠮ࠣા"))
		time.sleep(3)
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑࡵࡡࡥ࡫ࡱ࡫ࠥࡕࡓ࠯࠰࠱ࠦિ"))
		time.sleep(2)
		sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡡ࡝࠮࡝ࡠ࠱ࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞࠯࡞ࡡ࠲ࡡ࡝࠮࡝ࡠ࠱ࡠࡣ࠭࡜࡟࠰࡟ࡢ࠳࡛࡞࠯࡞ࡡࠧી"))
		l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡗࡦ࡮ࡦࡳࡲ࡫ࠬࠡࡗࡶࡩࡷ࠴ࠢુ"))
		time.sleep(2)
		while 1:
			if (l1ll111l1_opy_ == 1):
				break
			time.sleep(3)
			l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࡝ࡰ࡟ࡲࡘ࡫࡬ࡦࡥࡷࠤࡆࡩࡴࡪࡱࡱ࠾ࠧૂ"))
			sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎࡒࡋࡎࡔࠠࡰࡴࠣࡉ࡝ࡏࡔ࡝ࡰ࡟ࡲ࠿ࡀࠢૃ"))
			l11lllll1_opy_ = raw_input()
			if ( (l11ll_opy_ (u"ࠧࡒࡏࡈࡋࡑࠦૄ") in l11lllll1_opy_) or (l11ll_opy_ (u"ࠨࡌࡰࡩ࡬ࡲࠧૅ") in l11lllll1_opy_) or (l11ll_opy_ (u"ࠢ࡭ࡱࡪ࡭ࡳࠨ૆") in l11lllll1_opy_) ):
				l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮ࡑ࡮ࡨࡥࡸ࡫ࠠࡔࡧ࡯ࡩࡨࡺࠠࡍࡱࡪ࡭ࡳࠦࡁࡤࡥࡲࡹࡳࡺ࠺ࠡࠤે"))
				sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡓࡰࡴࡵࡩࡳࡺ࡯࡝ࡰ࡟ࡲࡗࡵ࡯ࡵ࡞ࡱࡠࡳࡢ࡮࠻࠼ࠥૈ"))
				l1l11ll1l_opy_ = raw_input()
				if ((l11ll_opy_ (u"ࠥࡶࡴࡵࡴࠣૉ") in l1l11ll1l_opy_) or (l11ll_opy_ (u"ࠦࡗࡵ࡯ࡵࠤ૊") in l1l11ll1l_opy_)):
					l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡲࡹ࡫ࡲࠡࡲࡤࡷࡸࡽ࡯ࡳࡦࠣࡪࡴࡸࠠࡓࡱࡲࡸ࠿ࡢ࡮࡝ࡰ࠽࠾ࠧો"))
					l1l1lllll_opy_ = raw_input()
					if (l11ll_opy_ (u"ࠨࡳࡵࡣࡵࡰ࡮࡭ࡨࡵࠤૌ") in l1l1lllll_opy_):
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑࡵࡧࡪࡰࠣࡅࡨࡩࡥࡱࡶࡨࡨ࠳ࠨ્"))
						time.sleep(3)
						if ( l11lll1ll_opy_ == 0 ):
							clear()
							time.sleep(2)
							l1l1l11ll_opy_(l11ll_opy_ (u"ࠣࡔࡲࡳࡹ࠴ࠢ૎"))
		   					time.sleep(2)
							l1l1l11ll_opy_(l11ll_opy_ (u"ࠤࠣࠤࡆࠦࡳࡺࡵࡷࡩࡲࠦࡡࡳࡶ࡬ࡪࡦࡩࡴ࠯ࠢࠣࡘ࡭࡫ࠠࡧ࡫ࡵࡷࡹࠦࡡࡤࡥࡲࡹࡳࡺࠬࠡ࡫ࡱࡷࡹࡧ࡬࡭ࡧࡧࠤࡧࡿࠠࡵࡪࡨࠤࡔ࡙ࠠࡪࡶࡶࡩࡱ࡬࠮ࠣ૏"))
		   					time.sleep(1)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࠤࠥࡇࡣࡤࡧࡶࡷࠥࡺ࡯ࠡࡧࡹࡩࡷࡿࡴࡩ࡫ࡱ࡫࠳ࠨૐ"))
							time.sleep(2)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡑࡸࡸࡸ࡯ࡤࡦ࠮ࠣࡸ࡭࡫ࠠࡸࡱࡵࡰࡩࠦࡩࡴࠢࡧ࡭ࡸࡺࡡ࡯ࡶ࠱ࠦ૑"))
		   					time.sleep(1)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࠦࠠࡕࡪࡨࠤࡱ࡯࡮ࡨࡧࡵ࡭ࡳ࡭ࠠࡴࡧࡱࡷࡪࠦ࡯ࡧࠢࡳ࡬ࡾࡹࡩࡤࡣ࡯࡭ࡹࡿࠬࠡࡸࡤࡲ࡮ࡹࡨࡦࡦ࠱ࠦ૒"))
		   					time.sleep(2)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡘ࡭࡫ࡲࡦࠢࡺࡥࡸࠦࡪࡶࡵࡷࠤࡹ࡮ࡥࠡࡲࡵࡳࡲࡶࡴ࠯ࠤ૓"))
		   					time.sleep(4)
		   					l11lll1ll_opy_ = 1
		   					clear()
		   					time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡎࡴࡩࡵ࡫ࡤࡸ࡮ࡴࡧࠡࡔࡒࡓ࡙ࠦࡓࡩࡧ࡯ࡰ࠳࠴࠮ࠣ૔"))
						time.sleep(2)
						sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳ࡚ࡹࡱࡧࠣࠫ࡭࡫࡬ࡱࠩࠣࡪࡴࡸࠠࡢࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡣࡰ࡯ࡰࡥࡳࡪࡳ࡝ࡰ࡟ࡲࡡࡴࠢ૕"))
						l1l1ll1ll_opy_ = l11ll_opy_ (u"ࠤࡕࡓࡔ࡚ࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦࠥࠣࠦ૖")
						l1l11l111_opy_ = 3
						while 1:
							sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࠣ૗"))
							sys.stdout.write(l1l1ll1ll_opy_)
							l1l1111l1_opy_ = raw_input()
							if ( (l11ll_opy_ (u"ࠦ࡭࡫࡬ࡱࠤ૘") in l1l1111l1_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡄࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡉ࡯࡮࡯ࡤࡲࡩࡹ࠺࡝ࡰ࡟ࡲ࡭࡫࡬ࡱࠢ࠰ࠤࡘ࡮࡯ࡸࡵࠣࡸ࡭࡯ࡳࠡ࡯ࡨࡲࡺࠦ࡜࡯࡮ࡶࠤ࠲ࠦࡌࡪࡵࡷࡷࠥࡩ࡯࡯ࡶࡨࡲࡹࡹࠠࡰࡨࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡜࡯ࡥࡧࠤࡁࡪࡩࡳࡧࡦࡸࡴࡸࡹ࡯ࡣࡰࡩࡃࠦ࠭ࠡࡅ࡫ࡥࡳ࡭ࡥࡴࠢࡺࡳࡷࡱࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࡜࡯ࡲࡤࡶࠥ࠳ࠠࡎࡱࡹࡩࡸࠦࡴࡰࠢࡳࡥࡷ࡫࡮ࡵࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥࡢ࡮ࡤࡣࡷࠤࡁ࡬ࡩ࡭ࡧࡱࡥࡲ࡫࠾ࠡ࠯ࠣࡈ࡮ࡹࡰ࡭ࡣࡼࡷࠥࡩ࡯࡯ࡶࡨࡲࡹࡹࠠࡰࡨࠣࡪ࡮ࡲࡥࠡ࡞ࡱࡩࡽ࡫ࡣࠡ࠾ࡩ࡭ࡱ࡫࡮ࡢ࡯ࡨࡂࠥ࠳ࠠࡆࡺࡨࡧࡺࡺࡥࡴࠢࡩ࡭ࡱ࡫࡜࡯ࡧࡻ࡭ࡹࠦ࠭ࠡࡎࡲ࡫ࡴࡻࡴࠡࡱࡩࠤࡸ࡫ࡳࡴ࡫ࡲࡲࠧ૙"))
							if ( (l11ll_opy_ (u"ࠨࡥࡹ࡫ࡷࠦ૚") in l1l1111l1_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡙࡫ࡲ࡮࡫ࡱࡥࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰ࠱࠲࠳ࠨ૛"))
								break
							if (l1l1ll1ll_opy_ == l11ll_opy_ (u"ࠣࡔࡒࡓ࡙ࡆࡎࡐࡘࡄࡇࡴࡴࡴࡳࡱ࡯ࡘࡪࡸ࡭࠻ࢀ࠲࡬ࡴࡳࡥࠤࠢࠥ૜")):
								if (l11ll_opy_ (u"ࠤࡳࡥࡷࠨ૝") in l1l1111l1_opy_):
									l1l11l111_opy_ = 1
								if (l11ll_opy_ (u"ࠥࡰࡸࠨ૞") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎ࡬ࡷࡹ࡯࡮ࡨࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠥ࠵ࡨࡰ࡯ࡨ࠾ࠧ૟"))
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡰࡹࡩ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮ࡴࡱࡵࡶࡪࡴࡴࡰࠢ࠰࠱ࠥࡪࡩࡳ࡞ࡱࡠࡳࠨૠ"))
								if (l11ll_opy_ (u"ࠨࡣࡥࠤૡ") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠢࡴࡱࡵࡶࡪࡴࡴࡰࠤૢ") in l1l1111l1_opy_):
										l1l11l111_opy_ = 4
								if (l11ll_opy_ (u"ࠣࡧࡻࡩࡨࠨૣ") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡅࡳࡴࡲࡶ࠳ࠦࠠࡇ࡫࡯ࡩࠥࡴ࡯ࡵࠢࡨࡼࡪࡩࡵࡵࡣࡥࡰࡪ࠴ࠢ૤"))
								if (l11ll_opy_ (u"ࠥࡧࡦࡺࠢ૥") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠦࡲࡻࡤࠣ૦") in l1l1111l1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡ࡯ࡸࡨ࠳ࡺࡸࡵ࠰࠱࠲ࠧ૧"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡘ࡭࡫ࡲࡦࠢࡤࡶࡪࠦࡴࡸࡱࠣ࡯࡮ࡴࡤࡴࠢࡲࡪࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠ࡮ࡻࡷ࡬ࡸࡀࠠࡵࡪࡲࡷࡪࠦࡷࡩࡧࡵࡩࠥࡲࡩࡧࡧࠣࡥࡷ࡯ࡳࡦࡵࠣࡳࡺࡺࠠࡰࡨࠣࡸ࡭࡫ࠠ࡮ࡷࡧ࠰ࠥࡧ࡮ࡥࠢࡷ࡬ࡴࡹࡥࠡࡹ࡫ࡩࡷ࡫ࠠ࡭࡫ࡩࡩࠥ࡬ࡡ࡭࡮ࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡳ࡬ࡻ࠱ࠦ૨"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡎࡴࠠࡵࡪ࡬ࡷࠥࡩࡲࡦࡣࡷ࡭ࡴࡴࠠ࡮ࡻࡷ࡬࠱ࠦࡣࡰ࡯ࡳࡹࡹ࡫ࡲࡴࠢࡤࡶࡴࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡱࡺࡪࠬࠡࡣࡱࡨࠥࡩ࡯ࡥࡧࠣࡪࡪࡲ࡬ࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡷࡰࡿ࠮ࠣ૩"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࠮ࡉࡨࡳࡷ࡭ࡥࠡࡆࡼࡷࡴࡴࠢ૪"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨ૫"))
							if (l1l1ll1ll_opy_ == l11ll_opy_ (u"ࠥࡖࡔࡕࡔࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳࠨࠦࠢ૬")):
								if (l11ll_opy_ (u"ࠦࡱࡹࠢ૭") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯ࡩࡱࡰࡩ࠴ࡹ࡯ࡳࡴࡨࡲࡹࡵ࠺ࠣ૮"))
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡨࡪࡹ࡫ࡵࡱࡳࠤ࠲࠳ࠠࡥ࡫ࡵࡠࡳࡢ࡮ࡥࡱࡦࡹࡲ࡫࡮ࡵࡵࠣ࠱࠲ࠦࡤࡪࡴࠥ૯"))
								if (l11ll_opy_ (u"ࠢࡤࡦࠥ૰") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠣࡦࡲࡧࡺࡳࡥ࡯ࡶࡶࠦ૱") in l1l1111l1_opy_):
										l1l11l111_opy_ = 5
									if (l11ll_opy_ (u"ࠤࡧࡩࡸࡱࡴࡰࡲࠥ૲") in l1l1111l1_opy_):
										l1l11l111_opy_ = 6
								if (l11ll_opy_ (u"ࠥࡴࡦࡸࠢ૳") in l1l1111l1_opy_):
									l1l11l111_opy_ = 4
							if (l1l1ll1ll_opy_ == l11ll_opy_ (u"ࠦࡗࡕࡏࡕࡂࡑࡓ࡛ࡇࡃࡰࡰࡷࡶࡴࡲࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴ࠵ࡤࡰࡥࡸࡱࡪࡴࡴࡴࠥࠣࠦ૴")):
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤ૵") in l1l1111l1_opy_):
									l1l11l111_opy_ = 3
								if (l11ll_opy_ (u"ࠨ࡬ࡴࠤ૶") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯ࡳࡵ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠱࡫ࡳࡲ࡫࠯ࡴࡱࡵࡶࡪࡴࡴࡰ࠱ࡧࡳࡨࡻ࡭ࡦࡰࡷࡷ࠿ࠨ૷"))
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡰࡡࡥࡧ࠱ࡸࡽࡺࠠ࠮࠯ࠣࡪ࡮ࡲࡥ࡝ࡰ࡟ࡲࡨࡵࡰࡱࡧࡵ࠲ࡹࡾࡴࠡ࠯࠰ࠤ࡫࡯࡬ࡦ࡞ࡱࡠࡳࡩࡲࡺࡵࡷࡥࡱ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࠦ૸"))
								if (l11ll_opy_ (u"ࠤࡨࡼࡪࡩࠢૹ") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡴࡵࡳࡷ࠴ࠠࠡࡈ࡬ࡰࡪࠦ࡮ࡰࡶࠣࡩࡽ࡫ࡣࡶࡶࡤࡦࡱ࡫࠮ࠣૺ"))
								if (l11ll_opy_ (u"ࠦࡨࡧࡴࠣૻ") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠧࡰࡡࡥࡧࠥૼ") in l1l1111l1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࡚࡮࡫ࡷࡪࡰࡪࠤ࡫࡯࡬ࡦࠢ࡭ࡥࡩ࡫࠮ࡵࡺࡷ࠾ࠧ૽"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡔࡕࠠࡰࠢࡲࡓࡔࠦ࡯ࠡࡱࡒࡳࠥࡵࠠࡐࡑࡒࠤࡔࡵࠠࡰࠢࡲࡓࠥࡕ࡯ࠡࡑࡲࡳࠥࡕࠠࡰࡱࡲࡳࠥࡵࠠࡰࡱࡲࠤࡴࡕࠠࡐࡑࠣࡳࠥࡵࡏࡰࠢࡲࡳࡔࠦࡏࡰࠢࡒࡳࠥࡵ࡯ࠡࡑࡲࠤࡔࡕ࡯ࠡࡱࡒࡳࡴࠦ࡯ࡰࠢࡒࡳࡔࠦ࡯ࠡࡑࡒࠤࡔࡕࡏࠡࡑࠣࡳࡴࡵ࡯ࠡࡱࡲࡳࠥࡕࠠࡐࡑࡒࠤࡔࠦ࡯ࡰࡱࡲࠤࡴࠦ࡯ࡰࡑࡲࠤࡴࡕ࡯ࡰࠢࡲࡓࠥࡕࡏࠡࡱࠣࡓࡴࡕࡏࠡࡑࡒࡓࠥࡵ࡯ࡐࠢࡲࡓࡔࡕࡏࡰࠢࡒࡳࡴࠦ࡯ࡰࡱࡲࠤࡴࡕࠠࡐࡱࠣࡓࡔࡵࠠࡐࡑࡒࠤࡔࡵࠠࡰࠢࡲࡳࡴࡕࠠࡰࠢࡲࡓࡴࠦࡏࡰࡑࡒࠤࡴࡕࡏࠡࡑࡒࡓࠥࡵࡏࡰࠢࡒࡳࡴࠦ࡯ࡰࠢࡲࡓࡔࡕࡏࡰࠢࡒࡳࡴࠦ࡯ࡰࡱࠣࡳࡔࠦࡏࡰࡑࡒࠤࡔࡵ࡯ࡰࠢࡲࡳࡔࠦࡏࠡࡑࡲࠤࡔࡕࡏࠡࡱࡒࡓࠥࡕࠠࡰࡱࡲࡳࠥࡵࠠࡐࡱࡒࡓࠥࡕࡏࡐࠢࡒࡳࠥࡵࡏࡰࡱࠣࡓࡴࡕࡏࠡࡱࡒࡳࠥࡵ࡯ࠡࡑࡲࡓࡴࠦࡏࡐࡑࠣࡓࡴࡕ࡯ࠡࡱࡲࡳࡴࠦ࡯ࠡࡑࠥ૾"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧ૿"))
									if (l11ll_opy_ (u"ࠤࡦࡳࡵࡶࡥࡳࠤ଀") in l1l1111l1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡗ࡫ࡨࡻ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࡣࡰࡲࡳࡩࡷ࠴ࡴࡹࡶ࠽ࠦଁ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡎࡴࡻࡷࠦࡷ࡬ࡪࠣࡺࡱࡵࡨࡲࡨ࡫ࠤࡧࡸࡸࠡࡸ࡫ࡵࡼࠦࡰࡩ࡞ࡱࡐࡶࡽࡲࠡࡹ࡮࡬ࠥ࡯࡬ࡶࡪࠣࡪࡷࡷࡶࡹࡲ࡫࡫ࡡࡴࡂࡳࡺࠣࡻࡰࡸࡸ࡫࡭ࡺࠤࡑ࠭ࡧࠡ࡫ࡵࡹ࡯࡮ࡷ࡝ࡰࡈࡼࡼࠦ࡬ࡸࠩࡹࠤࡩࡵࡺࡥࡤࡹࠤࡱࡷࠠࡱࡤࠣ࡯࡭ࡪࡧࠣଂ"))
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡡࡴ࠭࠮࠯ࡈࡓࡋ࠳࠭࠮ࠤଃ"))
									if (l11ll_opy_ (u"ࠨࡣࡳࡻࡶࡸࡦࡲࠢ଄") in l1l1111l1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲ࡛࡯ࡥࡸ࡫ࡱ࡫ࠥ࡬ࡩ࡭ࡧࠣࡧࡷࡿࡳࡵࡣ࡯࠲ࡹࡾࡴ࠻ࠤଅ"))
										sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡑࠠ࡯ࡩࡧࡩࠥ࡮ࡴࡧࡸࠣ࡯ࡶࡲࡥࡸࡪࠣࡷࡨࡪࡨࡸ࡞ࡱࡘࠬࡴࡣࠡࡼࡺࠤࡵ࡮࡬ࡷࠢࡳࡱࡲࠦࡰࡢࡻࡹࡺࡧࡢ࡮ࡄࡺࡳࡩࠥࡱࡥࡲࡣࡺࡩ࡚ࠥࠠࡺࡨ࡯ࠫࡱࠦࡥࡦࡧࠣ࡭࡫ࡢ࡮ࠨࡔࡤࡩࡱࠦࡔࠡࡦ࡯ࡴ࡫ࠦࡵࡦ࡬ࡴࡩࡧࠦࡵࡩࡰࡨࡸ࡫ࡰࠢଆ"))
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴ࡜࡯࡞ࡱ࠱࠲࠳ࡅࡐࡈ࠰࠱࠲ࠨଇ"))
							if (l1l1ll1ll_opy_ == l11ll_opy_ (u"ࠥࡖࡔࡕࡔࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪࡥࡴ࡭ࡷࡳࡵࠩࠠࠣଈ")):
								if (l11ll_opy_ (u"ࠦࡵࡧࡲࠣଉ") in l1l1111l1_opy_):
									l1l11l111_opy_ = 5
								if (l11ll_opy_ (u"ࠧࡲࡳࠣଊ") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡐ࡮ࡹࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠ࠰ࡪࡲࡱࡪ࠵ࡳࡰࡴࡵࡩࡳࡺ࡯࠰ࡦࡨࡷࡰࡺ࡯ࡱ࠼ࠥଋ"))
									sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡴࡧࡳࡪࡵ࠱ࡸࡽࡺࠠ࠮࠯ࠣࡪ࡮ࡲࡥࠣଌ"))
								if (l11ll_opy_ (u"ࠣࡧࡻࡩࡨࠨ଍") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡅࡳࡴࡲࡶ࠿ࠦࡆࡪ࡮ࡨࠤࡳࡵࡴࠡࡧࡻࡩࡨࡻࡴࡢࡤ࡯ࡩ࠳ࠨ଎"))
								if (l11ll_opy_ (u"ࠥࡳࡦࡹࡩࡴࠤଏ") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠦࡴࡧࡳࡪࡵࠥଐ") in l1l1111l1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡࡱࡤࡷ࡮ࡹ࠮ࡵࡺࡷ࠾ࠧ଑"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱ࠵࠷࠿࠭࠲࠴࠰࠶࠲࠺࡜࡯࠶࠴࠱࠻࠳࠱࠮࠳࡟ࡲ࠶࠿࠳࠮࠳࠺࠱࠻࠳࠱࡝ࡰ࠵࠻࠸࠳࠲࠶࠯࠶࠱࠷ࡢ࡮࠸࠷࠰࠵࠻࠳࠱࡝ࡰ࠵࠵࠷࠳࠱࠲࠯࠼࠱࠶ࡢ࡮࠲࠸࠷࠱࠶࠾࠭࠲࠳࠰࠸ࡡࡴ࠲࠸࠷࠰࠵࠵࠳࠲࠮࠴࡟ࡲ࠺࠾࠭࠲࠻࠰࠹࠲࠷ࠢ଒"))
										sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦଓ"))
							if (l1l1ll1ll_opy_ == l11ll_opy_ (u"ࠣࡔࡒࡓ࡙ࡆࡎࡐࡘࡄࡇࡴࡴࡴࡳࡱ࡯ࡘࡪࡸ࡭࠻ࢀ࠲ࠧࠥࠨଔ")):
								if (l11ll_opy_ (u"ࠤࡳࡥࡷࠨକ") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡆࡴࡵࡳࡷ࠴ࠠࠨ࠱ࠪࠤ࡮ࡹࠠࡵࡪࡨࠤࡷࡵ࡯ࡵࠢࡶࡽࡸࡺࡥ࡮ࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࠧଖ"))
								if (l11ll_opy_ (u"ࠦࡱࡹࠢଗ") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡏ࡭ࡸࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦ࠯࠻ࠤଘ"))
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡧࡴࡴࡴࡳࡱ࡯ࠤ࠲࠳ࠠࡥ࡫ࡵࡠࡳࡢ࡮ࡩࡱࡰࡩࠥ࠳࠭ࠡࡦ࡬ࡶࡡࡴ࡜࡯ࠤଙ"))
								if (l11ll_opy_ (u"ࠢࡤࡦࠥଚ") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠣࡪࡲࡱࡪࠨଛ") in l1l1111l1_opy_):
										l1l11l111_opy_ = 4
									if (l11ll_opy_ (u"ࠤࡦࡳࡳࡺࡲࡰ࡮ࠥଜ") in l1l1111l1_opy_):
										l1l11l111_opy_ = 2
								if (l11ll_opy_ (u"ࠥࡩࡽ࡫ࡣࠣଝ") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡵࡶࡴࡸ࠮ࠡࠢࡉ࡭ࡱ࡫ࠠ࡯ࡱࡷࠤࡪࡾࡥࡤࡷࡷࡥࡧࡲࡥ࠯ࠤଞ"))
							if (l1l1ll1ll_opy_ == l11ll_opy_ (u"ࠧࡘࡏࡐࡖࡃࡒࡔ࡜ࡁࡄࡱࡱࡸࡷࡵ࡬ࡕࡧࡵࡱ࠿ࢄ࠯ࡤࡱࡱࡸࡷࡵ࡬ࠤࠢࠥଟ")):
								if (l11ll_opy_ (u"ࠨࡰࡢࡴࠥଠ") in l1l1111l1_opy_):
									l1l11l111_opy_ = 1
								if (l11ll_opy_ (u"ࠢ࡭ࡵࠥଡ") in l1l1111l1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡒࡩࡴࡶ࡬ࡲ࡬ࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࠲ࡧࡴࡴࡴࡳࡱ࡯࠾ࠧଢ"))
									sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡳࡩࡷࡷࡨࡴࡽ࡮࠯ࡧࡻࡩࡨࠦ࠭࠮ࠢࡩ࡭ࡱ࡫࡜࡯࡞ࡱࠦଣ"))
								if (l11ll_opy_ (u"ࠥࡧࡦࡺࠢତ") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠦࡸ࡮ࡵࡵࡦࡲࡻࡳࠨଥ") in l1l1111l1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡙࡭ࡪࡽࡩ࡯ࡩࠣࡪ࡮ࡲࡥࠡࡵ࡫ࡹࡹࡪ࡯ࡸࡰ࠱ࡩࡽ࡫ࡣ࠯࠰࠱ࠦଦ"))
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࠧࡗࡕࡏࡕࡒࡈࡖࡒࠦࡒࡆࡓࡘࡍࡗࡋࡄ࡝ࡰ࡟ࡲࡆ࡛ࡔࡉࡇࡑࡘࡎࡉࡁࡕࡋࡒࡒࠥࡉࡈࡆࡅࡎ࠾ࠥࡉࡏࡑࡒࡈࡖࠥ࠳࠭ࠡࡌࡄࡈࡊࠦ࠭࠮ࠢࡆࡖ࡞࡙ࡔࡂࡎ࡟ࡲࡡࡴ࡜࡯࠱ࡖࡌ࡚࡚ࡄࡐ࡙ࡑࠤ࠲ࡇࡌࡍࠢ࠰ࡊࡔࡘࡃࡆ࡞ࡱࡏࡎࡒࡌ࠮ࡒࡕࡓࡈࡋࡓࡔࠢࡗࡖࡆࡔࡓࡇࡇࡕࡠࡳࡑࡉࡍࡎ࠰ࡔࡗࡕࡃࡆࡕࡖࠤࡗࡋࡃࡗࡃࡏࡐࡡࡴࡋࡊࡎࡏ࠱ࡕࡘࡏࡄࡇࡖࡗ࡙ࠥࡎࡅࡃࡏࡐࡡࡴࡔࡆࡔࡐ࠱ࡊ࡞ࡁࡍࡎ࡟ࡲࡋࡕࡒࡄࡇࡄࡇ࡙ࡏࡏࡏ࡞ࡱࡠࡳࡢ࡮࡝ࡰ࠰࠱࠲ࡋࡏࡇ࠯࠰࠱ࠧଧ"))
								if (l11ll_opy_ (u"ࠢࡦࡺࡨࡧࠧନ") in l1l1111l1_opy_):
									if (l11ll_opy_ (u"ࠣࡵ࡫ࡹࡹࡪ࡯ࡸࡰࠥ଩") in l1l1111l1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡆࡪ࡮ࡨࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴ࠺ࠡࡵ࡫ࡹࡹࡪ࡯ࡸࡰ࠱ࡩࡽ࡫ࡣࠣପ"))
										l1l1lll1l_opy_(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡔ࡛ࡖ࠳ࡆ࡛ࡔࡉࡑࡕࡍ࡙࡟࠺ࠡࡔࡒࡓ࡙ࠨଫ"))
										l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡃࡘࡘࡍࡋࡎࡕࡋࡆࡅ࡙ࡏࡏࡏࠢࡆࡌࡊࡉࡋࠡ࠯࠰ࠦବ"))
										time.sleep(1)
										sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰ࡟ࡲࡈࡕࡐࡑࡇࡕ࠾ࠥࠨଭ"))
										l1l1111ll_opy_ = raw_input()
										if (l11ll_opy_ (u"ࠨ࡭ࡰࡰࡶࡸࡪࡸࠢମ") in l1l1111ll_opy_):
											time.sleep(2)
											sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡏࡇࡄࡆ࠼ࠣࠦଯ"))
											l1l1l111l_opy_ = raw_input()
											if (l11ll_opy_ (u"ࠣࡴ࡬ࡧࡴࡩࡨࡦࡶࠥର") in l1l1l111l_opy_):
												time.sleep(2)
												sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡃࡓ࡛ࡖࡘࡆࡒ࠺ࠡࠤ଱"))
												l1ll1111l_opy_ = raw_input()
												if (l11ll_opy_ (u"ࠥࡧࡦࡸ࡮ࡪࡸࡲࡶࡪࠨଲ") in l1ll1111l_opy_):
													time.sleep(2)
													clear()
													l1ll111l1_opy_ = 1
													break
												else:
													time.sleep(2)
													l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡕࡖࡔࡘࠠࡄࡑࡑࡈࡎ࡚ࡉࡐࡐ࠽ࠤࡆ࡛ࡔࡉࡇࡑࡘࡎࡉࡁࡕࡋࡒࡒࠥࡔࡏࡕࠢࡄࡇࡈࡋࡐࡕࡇࡇ࠲ࠧଳ"))
											else:
												time.sleep(2)
												l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡖࡗࡕࡒࠡࡅࡒࡒࡉࡏࡔࡊࡑࡑ࠾ࠥࡇࡕࡕࡊࡈࡒ࡙ࡏࡃࡂࡖࡌࡓࡓࠦࡎࡐࡖࠣࡅࡈࡉࡅࡑࡖࡈࡈ࠳ࠨ଴"))
										else:
											time.sleep(2)
											l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡗࡘࡏࡓࠢࡆࡓࡓࡊࡉࡕࡋࡒࡒ࠿ࠦࡁࡖࡖࡋࡉࡓ࡚ࡉࡄࡃࡗࡍࡔࡔࠠࡏࡑࡗࠤࡆࡉࡃࡆࡒࡗࡉࡉ࠴ࠢଵ"))
							if (l1l11l111_opy_ == 1):
								l1l1ll1ll_opy_ = l11ll_opy_ (u"ࠢࡓࡑࡒࡘࡅࡔࡏࡗࡃࡆࡳࡳࡺࡲࡰ࡮ࡗࡩࡷࡳ࠺ࡿ࠱ࠦࠤࠧଶ")
							if (l1l11l111_opy_ == 2):
								l1l1ll1ll_opy_ = l11ll_opy_ (u"ࠣࡔࡒࡓ࡙ࡆࡎࡐࡘࡄࡇࡴࡴࡴࡳࡱ࡯ࡘࡪࡸ࡭࠻ࢀ࠲ࡧࡴࡴࡴࡳࡱ࡯ࠧࠥࠨଷ")
							if (l1l11l111_opy_ == 3):
								l1l1ll1ll_opy_ = l11ll_opy_ (u"ࠤࡕࡓࡔ࡚ࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦࠥࠣࠦସ")
							if (l1l11l111_opy_ == 4):
								l1l1ll1ll_opy_ = l11ll_opy_ (u"ࠥࡖࡔࡕࡔࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳࠨࠦࠢହ")
							if (l1l11l111_opy_ == 5):
								l1l1ll1ll_opy_ = l11ll_opy_ (u"ࠦࡗࡕࡏࡕࡂࡑࡓ࡛ࡇࡃࡰࡰࡷࡶࡴࡲࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴ࠵ࡤࡰࡥࡸࡱࡪࡴࡴࡴࠥࠣࠦ଺")
							if (l1l11l111_opy_ == 6):
								l1l1ll1ll_opy_ = l11ll_opy_ (u"ࠧࡘࡏࡐࡖࡃࡒࡔ࡜ࡁࡄࡱࡱࡸࡷࡵ࡬ࡕࡧࡵࡱ࠿ࢄ࠯ࡩࡱࡰࡩ࠴ࡹ࡯ࡳࡴࡨࡲࡹࡵ࠯ࡥࡧࡶ࡯ࡹࡵࡰࠤࠢࠥ଻")
					else:
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡷࡸ࡯ࡳ࠰ࠣࡍࡳࡼࡡ࡭࡫ࡧࠤࡑࡵࡧࡪࡰ࠱଼ࠦ"))
				if ((l11ll_opy_ (u"ࠢࡔࡱࡵࡶࡪࡴࡴࡰࠤଽ") in l1l11ll1l_opy_) or ( l11ll_opy_ (u"ࠣࡵࡲࡶࡷ࡫࡮ࡵࡱࠥା") in l1l11ll1l_opy_ )):
					l1l1lll1l_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡅ࡯ࡶࡨࡶࠥࡶࡡࡴࡵࡺࡳࡷࡪࠠࡧࡱࡵࠤࡘࡵࡲࡳࡧࡱࡸࡴࡀࠠ࡝ࡰ࡟ࡲ࠿ࡀࠢି"))
					l1l1lllll_opy_ = raw_input()
					if ((l11ll_opy_ (u"ࠥࡥࡩ࡫࡬࡭ࠤୀ") in l1l1lllll_opy_) or (l11ll_opy_ (u"ࠦࡆࡪࡥ࡭࡮ࠥୁ") in l1l1lllll_opy_)):
						#l1l11l11l_opy_ l11llllll_opy_ l1l1l1lll_opy_ l1l1lll11_opy_
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡏࡳ࡬࡯࡮ࠡࡃࡦࡧࡪࡶࡴࡦࡦ࠱ࠦୂ"))
						time.sleep(3)
						if ( l1ll11l11_opy_ == 0):
							clear()
							time.sleep(2)
							l1l1l11ll_opy_(l11ll_opy_ (u"ࠨࡁࡤࡥࡨࡷࡸ࠴ࠢୃ"))
		   					time.sleep(1)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠢࠡࠢࡄࠤࡸ࡫࡮ࡴࡧࠣࡳ࡫ࠦࡤࡦࡶࡤࡧ࡭ࡳࡥ࡯ࡶ࠯ࠤࡦࡪ࡯ࡱࡶ࡬ࡲ࡬ࠦࡡ࡯ࡱࡷ࡬ࡪࡸࠠࡱࡧࡵࡷࡴࡴࡡ࠯ࠤୄ"))
		   					time.sleep(2)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡇࠠࡸࡣࡼࠤࡴ࡬ࠠࡵࡪ࡬ࡲࡰ࡯࡮ࡨ࠰ࠣࠤࡔ࡬ࠠࡧ࡫ࡱࡨ࡮ࡴࡧࠡ࡯ࡨࡥࡳ࡯࡮ࡨࠢ࡬ࡲࠥࡺࡨࡦࠢࡸࡲࡨ࡫ࡲࡵࡣ࡬ࡲࡹࡿ࠮ࠣ୅"))
		   					time.sleep(2)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡔࡩࡧࠣࡶࡺࡹࡨࠡࡱࡩࠤࡦࠦࡤ࠲ࡩ࠴ࡸࡦࡲࠠࡣࡷࡽࡾࠥ࡯࡮ࠡࡻࡲࡹࡷࠦࡦࡪࡰࡪࡩࡷࡺࡩࡱࡵ࠱ࠦ୆"))
							time.sleep(1)
		   					l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࠤࠥࡏࡴࠡࡦࡵࡥࡼࡹࠠࡺࡱࡸࠤࡨࡲ࡯ࡴࡧࡵࠤࡹࡵࠠࡵࡪࡨࠤࡸࡩࡲࡦࡧࡱ࠰ࠥࡧ࡮ࡥࠢࡧࡩࡪࡶࡥࡳࠢ࡬ࡲࡹࡵࠠࡵࡪࡨࠤࡲࡧࡺࡦ࠰ࠥେ"))
		   					time.sleep(3)
							l1ll11l11_opy_ = 1
							clear()
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡋࡱ࡭ࡹ࡯ࡡࡵ࡫ࡱ࡫࡙ࠥࡥࡴࡵ࡬ࡳࡳࠦࡓࡩࡧ࡯ࡰ࠳࠴࠮ࠣୈ"))
						time.sleep(2)
						sys.stdout.write(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡗࡽࡵ࡫ࠠࠨࡪࡨࡰࡵ࠭ࠠࡧࡱࡵࠤࡦࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡧࡴࡳ࡭ࡢࡰࡧࡷࡡࡴ࡜࡯࡞ࡱࠦ୉"))
						l1ll11ll1_opy_ = l11ll_opy_ (u"ࠨࡓࡰࡴࡵࡩࡳࡺ࡯ࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳࠩࠦࠢ୊")
						l11llll11_opy_ = 1
						while 1:
							sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࠧୋ"))
							sys.stdout.write(l1ll11ll1_opy_)
							l1l111ll1_opy_ = raw_input()
							if ( (l11ll_opy_ (u"ࠣࡪࡨࡰࡵࠨୌ") in l1l111ll1_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡁࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡆࡳࡲࡳࡡ࡯ࡦࡶ࠾ࡡࡴ࡜࡯ࡪࡨࡰࡵࠦ࠭ࠡࡕ࡫ࡳࡼࡹࠠࡵࡪ࡬ࡷࠥࡳࡥ࡯ࡷࠣࡠࡳࡲࡳࠡ࠯ࠣࡐ࡮ࡹࡴࡴࠢࡦࡳࡳࡺࡥ࡯ࡶࡶࠤࡴ࡬ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡠࡳࡩࡤࠡ࠾ࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽࡳࡧ࡭ࡦࡀࠣ࠱ࠥࡉࡨࡢࡰࡪࡩࡸࠦࡷࡰࡴ࡮࡭ࡳ࡭ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡠࡳࡶࡡࡳࠢ࠰ࠤࡒࡵࡶࡦࡵࠣࡸࡴࠦࡰࡢࡴࡨࡲࡹࠦࡤࡪࡴࡨࡧࡹࡵࡲࡺࠢ࡟ࡲࡨࡧࡴࠡ࠾ࡩ࡭ࡱ࡫࡮ࡢ࡯ࡨࡂࠥ࠳ࠠࡅ࡫ࡶࡴࡱࡧࡹࡴࠢࡦࡳࡳࡺࡥ࡯ࡶࡶࠤࡴ࡬ࠠࡧ࡫࡯ࡩࠥࡢ࡮ࡦࡺࡨࡧࠥࡂࡦࡪ࡮ࡨࡲࡦࡳࡥ࠿ࠢ࠰ࠤࡊࡾࡥࡤࡷࡷࡩࡸࠦࡦࡪ࡮ࡨࡠࡳ࡫ࡸࡪࡶࠣ࠱ࠥࡒ࡯ࡨࡱࡸࡸࠥࡵࡦࠡࡵࡨࡷࡸ࡯࡯࡯ࠤ୍"))
							if ( (l11ll_opy_ (u"ࠥࡩࡽ࡯ࡴࠣ୎") in l1l111ll1_opy_) ):
								sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡖࡨࡶࡲ࡯࡮ࡢࡶ࡬ࡲ࡬ࠦࡳࡦࡵࡶ࡭ࡴࡴ࠮࠯࠰ࠥ୏"))
								break
							if (l1ll11ll1_opy_ == l11ll_opy_ (u"࡙ࠧ࡯ࡳࡴࡨࡲࡹࡵࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲࠨࠥࠨ୐")):
								if (l11ll_opy_ (u"ࠨ࡬ࡴࠤ୑") in l1l111ll1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡑ࡯ࡳࡵ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡ࠱࡫ࡳࡲ࡫࠯ࡴࡱࡵࡶࡪࡴࡴࡰ࠼ࠥ୒"))
									sys.stdout.write(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡪࡥࡴ࡭ࡷࡳࡵࠦ࠭࠮ࠢࡧ࡭ࡷࡢ࡮࡝ࡰࡧࡳࡨࡻ࡭ࡦࡰࡷࡷࠥ࠳࠭ࠡࡦ࡬ࡶࠧ୓"))
								if (l11ll_opy_ (u"ࠤࡦࡨࠧ୔") in l1l111ll1_opy_):
									if (l11ll_opy_ (u"ࠥࡨࡴࡩࡵ࡮ࡧࡱࡸࡸࠨ୕") in l1l111ll1_opy_):
										l11llll11_opy_ = 2
									if (l11ll_opy_ (u"ࠦࡩ࡫ࡳ࡬ࡶࡲࡴࠧୖ") in l1l111ll1_opy_):
										l11llll11_opy_ = 3
								if (l11ll_opy_ (u"ࠧࡶࡡࡳࠤୗ") in l1l111ll1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡷࡸ࡯ࡳࠢࡤࡧࡨ࡫ࡳࡴ࡫ࡱ࡫ࠥࡪࡩࡳࡧࡦࡸࡴࡸࡹࠡࠩ࠲࡬ࡴࡳࡥࠨ࠼ࠣࡔࡪࡸ࡭ࡪࡵࡶ࡭ࡴࡴࠠࡥࡧࡱ࡭ࡪࡪ࠮ࠣ୘"))
							if (l1ll11ll1_opy_ == l11ll_opy_ (u"ࠢࡔࡱࡵࡶࡪࡴࡴࡰࡂࡑࡓ࡛ࡇࡃࡰࡰࡷࡶࡴࡲࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴ࠵ࡤࡰࡥࡸࡱࡪࡴࡴࡴࠦࠣࠦ୙")):
								if (l11ll_opy_ (u"ࠣࡲࡤࡶࠧ୚") in l1l111ll1_opy_):
									l11llll11_opy_ = 1
								if (l11ll_opy_ (u"ࠤ࡯ࡷࠧ୛") in l1l111ll1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪ࡯ࡤࡷࡰࡩࡳࡺࡳ࠻ࠤଡ଼"))
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡬ࡤࡨࡪ࠴ࡴࡹࡶࠣ࠱࠲ࠦࡦࡪ࡮ࡨࡠࡳࡢ࡮ࡤࡱࡳࡴࡪࡸ࠮ࡵࡺࡷࠤ࠲࠳ࠠࡧ࡫࡯ࡩࡡࡴ࡜࡯ࡥࡵࡽࡸࡺࡡ࡭࠰ࡷࡼࡹࠦ࠭࠮ࠢࡩ࡭ࡱ࡫ࠢଢ଼"))
								if (l11ll_opy_ (u"ࠧ࡫ࡸࡦࡥࠥ୞") in l1l111ll1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡷࡸ࡯ࡳ࠰ࠣࠤࡋ࡯࡬ࡦࠢࡱࡳࡹࠦࡥࡹࡧࡦࡹࡹࡧࡢ࡭ࡧ࠱ࠦୟ"))
								if (l11ll_opy_ (u"ࠢࡤࡣࡷࠦୠ") in l1l111ll1_opy_):
									if (l11ll_opy_ (u"ࠣ࡬ࡤࡨࡪࠨୡ") in l1l111ll1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡅࡓࡔࡒࡖ࠿ࠦࡒࡐࡑࡗࠤࡕࡋࡒࡎࡋࡖࡗࡎࡕࡎࡔࠢࡕࡉࡖ࡛ࡉࡓࡇࡇࠤ࡙ࡕࠠࡗࡋࡈ࡛ࠥࡌࡉࡍࡇ࡟ࡲࠧୢ"))
									if (l11ll_opy_ (u"ࠥࡧࡴࡶࡰࡦࡴࠥୣ") in l1l111ll1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡇࡕࡖࡔࡘ࠺ࠡࡔࡒࡓ࡙ࠦࡐࡆࡔࡐࡍࡘ࡙ࡉࡐࡐࡖࠤࡗࡋࡑࡖࡋࡕࡉࡉࠦࡔࡐ࡙ࠢࡍࡊ࡝ࠠࡇࡋࡏࡉࡡࡴࠢ୤"))
									if (l11ll_opy_ (u"ࠧࡩࡲࡺࡵࡷࡥࡱࠨ୥") in l1l111ll1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡗࡘࡏࡓ࠼ࠣࡖࡔࡕࡔࠡࡒࡈࡖࡒࡏࡓࡔࡋࡒࡒࡘࠦࡒࡆࡓࡘࡍࡗࡋࡄࠡࡖࡒࠤ࡛ࡏࡅࡘࠢࡉࡍࡑࡋ࡜࡯ࠤ୦"))
							if (l1ll11ll1_opy_ == l11ll_opy_ (u"ࠢࡔࡱࡵࡶࡪࡴࡴࡰࡂࡑࡓ࡛ࡇࡃࡰࡰࡷࡶࡴࡲࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴ࠵ࡤࡦࡵ࡮ࡸࡴࡶࠤࠡࠤ୧")):
								if (l11ll_opy_ (u"ࠣࡲࡤࡶࠧ୨") in l1l111ll1_opy_):
									l11llll11_opy_ = 1
								if (l11ll_opy_ (u"ࠤ࡯ࡷࠧ୩") in l1l111ll1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮ࡍ࡫ࡶࡸ࡮ࡴࡧࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪࡥࡴ࡭ࡷࡳࡵࡀࠢ୪"))
									sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡱࡤࡷ࡮ࡹ࠮ࡵࡺࡷࠤ࠲࠳ࠠࡧ࡫࡯ࡩࠧ୫"))
								if (l11ll_opy_ (u"ࠧ࡫ࡸࡦࡥࠥ୬") in l1l111ll1_opy_):
									sys.stdout.write(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡉࡷࡸ࡯ࡳ࠼ࠣࡊ࡮ࡲࡥࠡࡰࡲࡸࠥ࡫ࡸࡦࡥࡸࡸࡦࡨ࡬ࡦ࠰ࠥ୭"))
								if (l11ll_opy_ (u"ࠢࡰࡣࡶ࡭ࡸࠨ୮") in l1l111ll1_opy_):
									if (l11ll_opy_ (u"ࠣࡱࡤࡷ࡮ࡹࠢ୯") in l1l111ll1_opy_):
										sys.stdout.write(l11ll_opy_ (u"ࠤ࡟ࡲࡡࡴࡖࡪࡧࡺ࡭ࡳ࡭ࠠࡧ࡫࡯ࡩࠥࡵࡡࡴ࡫ࡶ࠲ࡹࡾࡴ࠻ࠤ୰"))
										sys.stdout.write(l11ll_opy_ (u"ࠥࡠࡳࡢ࡮࠲࠴࠼࠱࠶࠸࠭࠳࠯࠷ࡠࡳ࠺࠱࠮࠸࠰࠵࠲࠷࡜࡯࠳࠼࠷࠲࠷࠷࠮࠸࠰࠵ࡡࡴ࠲࠸࠵࠰࠶࠺࠳࠳࠮࠴࡟ࡲ࠼࠻࠭࠲࠸࠰࠵ࡡࡴ࠲࠲࠴࠰࠵࠶࠳࠹࠮࠳࡟ࡲ࠶࠼࠴࠮࠳࠻࠱࠶࠷࠭࠵࡞ࡱ࠶࠼࠻࠭࠲࠲࠰࠶࠲࠸࡜࡯࠷࠻࠱࠶࠿࠭࠶࠯࠴ࠦୱ"))
										sys.stdout.write(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯࡞ࡱࡠࡳ࠳࠭࠮ࡇࡒࡊ࠲࠳࠭ࠣ୲"))
							if (l11llll11_opy_ == 1):
								l1ll11ll1_opy_ = l11ll_opy_ (u"࡙ࠧ࡯ࡳࡴࡨࡲࡹࡵࡀࡏࡑ࡙ࡅࡈࡵ࡮ࡵࡴࡲࡰ࡙࡫ࡲ࡮࠼ࢁ࠳࡭ࡵ࡭ࡦ࠱ࡶࡳࡷࡸࡥ࡯ࡶࡲࠨࠥࠨ୳")
							if (l11llll11_opy_ == 2):
								l1ll11ll1_opy_ = l11ll_opy_ (u"ࠨࡓࡰࡴࡵࡩࡳࡺ࡯ࡁࡐࡒ࡚ࡆࡉ࡯࡯ࡶࡵࡳࡱ࡚ࡥࡳ࡯࠽ࢂ࠴࡮࡯࡮ࡧ࠲ࡷࡴࡸࡲࡦࡰࡷࡳ࠴ࡪ࡯ࡤࡷࡰࡩࡳࡺࡳࠥࠢࠥ୴")
							if (l11llll11_opy_ == 3):
								l1ll11ll1_opy_ = l11ll_opy_ (u"ࠢࡔࡱࡵࡶࡪࡴࡴࡰࡂࡑࡓ࡛ࡇࡃࡰࡰࡷࡶࡴࡲࡔࡦࡴࡰ࠾ࢃ࠵ࡨࡰ࡯ࡨ࠳ࡸࡵࡲࡳࡧࡱࡸࡴ࠵ࡤࡦࡵ࡮ࡸࡴࡶࠤࠡࠤ୵")
					else:
						time.sleep(2)
						l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࡞ࡱࡠࡳࡋࡲࡳࡱࡵ࠲ࠥࡏ࡮ࡷࡣ࡯࡭ࡩࠦ࡬ࡰࡩ࡬ࡲ࠳ࡢ࡮ࠣ୶"))
			if ( (l11ll_opy_ (u"ࠤࡈ࡜ࡎ࡚ࠢ୷") in l11lllll1_opy_ ) or (l11ll_opy_ (u"ࠥࡉࡽ࡯ࡴࠣ୸") in l11lllll1_opy_) or (l11ll_opy_ (u"ࠦࡪࡾࡩࡵࠤ୹") in l11lllll1_opy_) ):
				l1l1lll1l_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡈࡼ࡮ࡺࡩ࡯ࡩࠣࡷࡾࡹࡴࡦ࡯࠱࠲࠳ࠨ୺"))
				time.sleep(2)
				break
time.sleep(3)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠨ࠮ࠣ୻"))
time.sleep(1)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࠯ࠤ୼"))
time.sleep(1)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠣ࠰ࠥ୽"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠤࡄࠤࡧࡸࡩࡨࡪࡷࠤ࡫ࡲࡡࡳࡧࠣࡳ࡫ࠦ࡬ࡪࡩ࡫ࡸ࠳ࠨ୾"))
time.sleep(1)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠥࠤࠥࡇࠠࡴࡷࡧࡨࡪࡴࠠࡳࡷࡶ࡬ࠥࡵࡦࠡࡰࡲ࡭ࡸ࡫࠮ࠣ୿"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠦࡡࡴ࡜࡯ࡖ࡫ࡩࠥࡪࡡࡵࡣࠣࡧࡴࡲࡵ࡮ࡰࠣࡴࡺࡲࡳࡦࡵࠣࡥࡳࡪࠠࡴࡷࡵ࡫ࡪࡹࠬࠡ࡮࡬࡯ࡪࠦࡡࠡࡵࡷࡥࡷࠦࡥࡹࡲ࡯ࡳࡩ࡯࡮ࡨࠢ࡬ࡲࠥࡹ࡬ࡰࡹࠣࡱࡴࡺࡩࡰࡰ࠱ࠦ஀"))
time.sleep(2)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠧࡢ࡮࡝ࡰࡄࠤ࡬ࡸࡥࡢࡶࠣࡪࡱࡧࡳࡩࠢࡲࡪࠥࡲࡩࡨࡪࡷ࠰ࠥࡺࡨࡦࡰࠣࡷࡹ࡯࡬࡭ࡰࡨࡷࡸ࠴ࠢ஁"))
time.sleep(3)
l1l1l11ll_opy_(l11ll_opy_ (u"ࠨ࡜࡯࡞ࡱࡘ࡭࡫ࠠࡴࡷࡧࡨࡪࡴࠠࡳࡷࡶ࡬ࠥࡵࡦࠡࡵ࡬ࡰࡪࡴࡣࡦࠢ࡬ࡷࠥࡪࡥࡢࡨࡨࡲ࡮ࡴࡧ࠯ࠤஂ"))
time.sleep(5)
l1l1lll1l_opy_(l11ll_opy_ (u"ࠢ࡝ࡰ࡟ࡲࡡࡴ࡜࡯࠯࠰࠱ࡊࡕࡆ࠮࠯࠰ࠦஃ"))
time.sleep(10)
