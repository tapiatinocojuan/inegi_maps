# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 739,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Interfaz graficadora de agebs" ), wx.VERTICAL )
		
		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_comboBox7Choices = []
		self.m_comboBox7 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox7Choices, 0 )
		bSizer14.Add( self.m_comboBox7, 1, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"AGEE", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer14.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer14, 1, wx.EXPAND, 5 )
		
		bSizer141 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_comboBox71Choices = []
		self.m_comboBox71 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox71Choices, 0 )
		bSizer141.Add( self.m_comboBox71, 1, wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"AGEM", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		bSizer141.Add( self.m_staticText91, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer141, 1, wx.EXPAND, 5 )
		
		bSizer1411 = wx.BoxSizer( wx.HORIZONTAL )
		
		m_comboBox711Choices = []
		self.m_comboBox711 = wx.ComboBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Combo!", wx.DefaultPosition, wx.DefaultSize, m_comboBox711Choices, 0 )
		bSizer1411.Add( self.m_comboBox711, 1, wx.ALL, 5 )
		
		self.m_staticText911 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Localidad", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText911.Wrap( -1 )
		bSizer1411.Add( self.m_staticText911, 0, wx.ALL, 5 )
		
		
		sbSizer1.Add( bSizer1411, 1, wx.EXPAND, 5 )
		
		self.m_button3 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Crear kml", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		self.SetSizer( sbSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_comboBox7.Bind( wx.EVT_COMBOBOX, self.on_agee_select )
		self.m_comboBox71.Bind( wx.EVT_COMBOBOX, self.on_agem_select )
		self.m_button3.Bind( wx.EVT_BUTTON, self.create_kml )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def on_agee_select( self, event ):
		event.Skip()
	
	def on_agem_select( self, event ):
		event.Skip()
	
	def create_kml( self, event ):
		event.Skip()
	

