#!/usr/bin/python

import matplotlib as mpl
mpl.use('Agg')
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os, datetime, sys
import numpy as np
import _imaging


def int2str(mm):
	if(mm == '01'): ms = 'January'
	if(mm == '02'): ms = 'February'
	if(mm == '03'): ms = 'March'
	if(mm == '04'): ms = 'April'
	if(mm == '05'): ms = 'May'
	if(mm == '06'): ms = 'June'
	if(mm == '07'): ms = 'July'
	if(mm == '08'): ms = 'August'
	if(mm == '09'): ms = 'September'
	if(mm == '10'): ms = 'October'
	if(mm == '11'): ms = 'November'
	if(mm == '12'): ms = 'December'
	return ms


fdate = sys.argv[1]   #(expects format like: 201301)
yyyy = fdate[0:4]
mm = fdate[4:]
ms = int2str(mm)
labeldate = ms+' '+yyyy


imgsize = sys.argv[2]   #(expects 620, 1000, DIY, HD, or HDSD)

figdpi = 72

cmd = "/usr/bin/python ./precipMap.py "+fdate+" "+imgsize
os.system(cmd)


cmd = "/usr/bin/python ./precipColorbar.py "+fdate+" "+imgsize
os.system(cmd)


if not os.path.isdir('../Images'):
	cmd = 'mkdir ../Images'
	os.system(cmd)
if not os.path.isdir('../Images/Precipitation/'+imgsize):
	cmd = 'mkdir ../Images/Precipitation/'+imgsize
	os.system(cmd)


if(imgsize == '620' or imgsize == '1000'):
	im1 = Image.open("temporary_map.png")
	im2 = Image.open("temporary_cbar.png")
	im3 = Image.new('RGBA', size = (im1.size[0], im1.size[1]+im2.size[1]))
	im3.paste(im2, (0,im1.size[1]))
	im3.paste(im1, (0,0))
	img_path = '../Images/Precipitation/'+imgsize+'/'
	imgw = str(im3.size[0])
	imgh = str(im3.size[1])
	img_name = 'clmdivprecip--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.png'
	pngfile = img_path+img_name
	print "Saving "+pngfile
	im3.save(pngfile)


if(imgsize == 'DIY'):
	im1 = "./temporary_map.png"
	imgs = Image.open(im1)
	imgw = str(imgs.size[0])
	imgh = str(imgs.size[1])
	img_path = '../Images/Precipitation/'+imgsize+'/'
	img_name = 'clmdivprecip--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.png'
	cmd = 'mv '+im1+' '+img_name
	os.system(cmd)
	im2 = "./temporary_cbar.eps"
	cbar_name = 'clmdivprecip--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00_colorbar.eps'
	cmd = 'mv '+im2+' '+cbar_name
	os.system(cmd)	
	cmd1 = 'zip clmdivprecip--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.zip '+img_name+' '+cbar_name+' noaa_logo.eps '
	os.system(cmd1)
	cmd2 = 'mv clmdivprecip--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.zip '+img_path
	os.system(cmd2)
	cmd3 = 'rm '+img_name+' '+cbar_name
	os.system(cmd3)
	
	
if(imgsize == 'HD'):
	hdim = Image.new("RGB", (1920,1080), color='#FFFFFF')
	imgw = '1920'
	imgh = '1080'
	
	im1 = Image.open("temporary_map.png")
	bbox = (1,1,1535,738)
	im1 = im1.crop(bbox)
	osize = im1.size
	new_size = (osize[0]+2,osize[1]+2)
	im1new = Image.new("RGB", new_size)
	im1new.paste(im1, ((new_size[0]-osize[0])/2, (new_size[1]-osize[1])/2))
		
	hdim.paste(im1new, (192,107))
	
	draw = ImageDraw.Draw(hdim)
	fntpath = '/usr/local/share/fonts/truetype/msttcorefonts/Trebuchet_MS.ttf'
	fnt1 = ImageFont.truetype(fntpath, 14)
	xpos = 1662 - ((len(labeldate)*8)-9)/2
	draw.text((xpos,815), labeldate, (0,0,0), font=fnt1)

	
	#Add the colorbar
	cbar_orig = Image.open('temporary_cbar.png')
	bbox = (1,1,972,43)
	cbar_orig = cbar_orig.crop(bbox)
	old_size = cbar_orig.size
	new_size = (old_size[0]+2,old_size[1]+2)
	cbar_im = Image.new("RGB", new_size)
	cbar_im.paste(cbar_orig, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
	hdim.paste(cbar_im, (474,866))


	fnt4 = ImageFont.truetype(fntpath, 47)
	text2 = "less"
	draw.text((515,905), text2, (0,0,0), font=fnt4)
	text3 = "more"
	draw.text((1300,905), text3, (0,0,0), font=fnt4)
	
	draw.polygon([(500,946), (485,936), (500,926)], fill="black", outline="black")
	draw.polygon([(1420,946), (1435,936), (1420,926)], fill="black", outline="black")
	
	fnt5 = ImageFont.truetype(fntpath, 36)
	text2 = "precipitation"
	draw.text((858,915), text2, (0,0,0), font=fnt5)

	
	img_path = '../Images/Precipitation/'+imgsize+'/'
	img_name = 'clmdivprecip--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.png'
	pngfile = img_path+img_name
	print "Saving "+pngfile
	hdim.save(pngfile)


if(imgsize == 'HDSD'):
	hdim = Image.new("RGB", (1920,1080), color='#FFFFFF')
	imgw = '1920'
	imgh = '1080'
	
	im1 = Image.open("temporary_map.png")
	bbox = (1,1,1152,702)
	im1 = im1.crop(bbox)
	osize = im1.size
	new_size = (osize[0]+2,osize[1]+2)
	im1new = Image.new("RGB", new_size)
	im1new.paste(im1, ((new_size[0]-osize[0])/2, (new_size[1]-osize[1])/2))
		
	hdim.paste(im1new, (384,107))
	
	draw = ImageDraw.Draw(hdim)
	fntpath = '/usr/local/share/fonts/truetype/msttcorefonts/Trebuchet_MS.ttf'
	fnt1 = ImageFont.truetype(fntpath, 14)
	xpos = 1470 - ((len(labeldate)*8)-9)/2
	draw.text((xpos,785), labeldate, (0,0,0), font=fnt1)	
	
	#Add the colorbar
	cbar_orig = Image.open('temporary_cbar.png')
	bbox = (1,1,972,43)
	cbar_orig = cbar_orig.crop(bbox)
	old_size = cbar_orig.size
	new_size = (old_size[0]+2,old_size[1]+2)
	cbar_im = Image.new("RGB", new_size)
	cbar_im.paste(cbar_orig, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
	hdim.paste(cbar_im, (474,830))
		
	fnt4 = ImageFont.truetype(fntpath, 47)
	text2 = "less"
	draw.text((515,870), text2, (0,0,0), font=fnt4)
	text3 = "more"
	draw.text((1300,870), text3, (0,0,0), font=fnt4)
	
	fnt5 = ImageFont.truetype(fntpath, 36)
	text2 = "precipitation"
	draw.text((856,880), text2, (0,0,0), font=fnt5)
	
	draw.polygon([(500,911), (485,901), (500,891)], fill="black", outline="black")
	draw.polygon([(1420,911), (1435,901), (1420,891)], fill="black", outline="black")
	
	img_path = '../Images/Precipitation/'+imgsize+'/'
	img_name = 'clmdivprecip--'+imgw+'x'+imgh+'--'+yyyy+'-'+mm+'-00.png'
	pngfile = img_path+img_name
	print "Saving "+pngfile
	hdim.save(pngfile)