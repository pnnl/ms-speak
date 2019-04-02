/*
https://docs.oracle.com/javase/tutorial/uiswing/examples/components/index.html
 */ 

import java.io.*;  // File etc
import java.beans.*; //Property change stuff
import javax.swing.*;
import javax.swing.event.*;
import javax.swing.border.Border;
//import javax.swing.filechooser.*;
import java.awt.*;
import java.awt.event.*;
import org.ini4j.*;

class BizRuleEditor extends JDialog 
					implements PropertyChangeListener{ // ActionListener
    private static final long serialVersionUID = 3L;
	private JSlider minSlider;
	private JSlider maxSlider;
    private IdsEditor dlgParent;
    private JOptionPane optionPane; // standard dialog box

    final JLabel minString = new JLabel("Minimum Value:");
    final JLabel maxString = new JLabel("Maximum Value:");
    final JLabel currSlideValue = new JLabel("Current Value:", SwingConstants.CENTER);
    final Component space = Box.createRigidArea(new Dimension(2, 10)); // invisible, empty space 
    //final JLabel space = new JLabel("----", SwingConstants.CENTER);

    final int TIME_TYPE = 0;
    final int TEMP_TYPE = 1;
    final int REQ_TYPE = 2;
    private int sliderType = TIME_TYPE;
    private int minVal = 0;
    private int maxVal = 0;
    private int minTemp = 0;
    private int maxTemp = 0;
    private int minHour = 0;
    private int maxHour = 0;
    private int numReq = 0;
    private boolean initDlg = true;
    private boolean bHasCfgLoc = true;
    public Wini BizRulesIni; 
    public  Wini IdsCfgIni; 
	public String CfgLocation = "";
	public String LogLocation = "";
	public String BizRulesCfg = "";
	public String BizRulesLog = "";

	public BizRuleEditor(Frame aFrame, IdsEditor parent) {
        super(aFrame, true);
        dlgParent = parent;

        setTitle("Business Rule Editor");
        currSlideValue.setVisible(false);

        minSlider = new JSlider(0, 100, 0);
        minSlider.setMinorTickSpacing(5);
        minSlider.setMajorTickSpacing(10);
        minSlider.setPaintTicks(true);
        minSlider.setPaintLabels(true);

		try {

	    	//System.out.println("user.dir: " + System.getProperty("user.dir"));		
			
   			File f = new File("Ids.cfg");
			if(!f.exists()){
				f.createNewFile();
			}
			IdsCfgIni = new Wini(f);
			CfgLocation = getIniValueS( IdsCfgIni, "Settings", "ConfigLocation" );
			if( CfgLocation == null ){
				CfgLocation = System.getProperty("user.dir");
				bHasCfgLoc = false;
			}
			else if( CfgLocation.isBlank() || CfgLocation.isEmpty() ){
		    	System.out.println("ERROR: Cfg File Location Not Set Properly.");
				System.exit(-1);
				return;
			}
			if( !bHasCfgLoc )
				setIniValue( IdsCfgIni, "Settings", "ConfigLocation", CfgLocation );

			//f.close(); Streams can be opened and closed, files cannot.
			// java.io.File doesn't represent an open file, it represents a path in the filesystem.
			
			// File.separator is either / or \ t
			BizRulesCfg = CfgLocation + File.separator + "BizRules.cfg";
	    	//System.out.println("BizRulesCfg: " + BizRulesCfg);
			f = new File(BizRulesCfg);
			if(!f.exists()){
				f.createNewFile();
			}
			BizRulesIni = new Wini(f);
			
			BizRulesLog = getIniValueS( BizRulesIni, "Settings", "LogFile" );
			if( BizRulesLog == null ){
				LogLocation = System.getProperty("user.dir");
				BizRulesLog = LogLocation + File.separator + "srv_msp.log";
				setIniValue( BizRulesIni, "Settings", "LogFile", BizRulesLog );
			}
		}
		catch(FileNotFoundException e) {
	    	System.out.println("Cfg File Not Found @: " + CfgLocation);
			System.exit(-1);
			return;
		}
		catch(IOException e) {
	    	System.out.println("ERROR accessing File: " + BizRulesCfg);
		  	e.printStackTrace();
			System.exit(-1);
			return;
   		}

        minSlider.addChangeListener((ChangeEvent event) -> {
        	minVal = minSlider.getValue();
            if( !initDlg ) {
	            currSlideValue.setVisible(true);
	            currSlideValue.setText( Integer.toString(minVal) );
            }
        });
        
        maxSlider = new JSlider(0, 100, 0);
        maxSlider.setMinorTickSpacing(5);
        maxSlider.setMajorTickSpacing(10);
        maxSlider.setPaintTicks(true);
        maxSlider.setPaintLabels(true);
        
        maxSlider.addChangeListener((ChangeEvent event) -> {
        	maxVal = maxSlider.getValue();
            if( initDlg ) {
	            initDlg = false;
            }
            else {
	            currSlideValue.setVisible(true);
	            currSlideValue.setText( Integer.toString(maxVal) );
            }
        });

        //Create an array of the text and components to be displayed.
        Object[] array = {minString, minSlider, space, maxString, maxSlider, currSlideValue};
 
		//Create the JOptionPane:
        UIManager.put("OptionPane.minimumSize",new Dimension(400,300)); 
        //JOptionPane(Object message, int messageType, int optionType, Icon icon, Object[] options, Object initialValue
        optionPane = new JOptionPane(array,
                                    JOptionPane.PLAIN_MESSAGE,
                                    JOptionPane.OK_CANCEL_OPTION,
                                    null,
                                    null,
                                    null);
        //Make this dialog display it.
        setContentPane(optionPane);
        //Handle window closing correctly.
        setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
        addWindowListener(new WindowAdapter() {
                public void windowClosing(WindowEvent we) {
                /*
                 * Instead of directly closing the window,
                 * we're going to change the JOptionPane's
                 * value property.
                 */
                	//Integer integer = Integer.valueOf(JOptionPane.CLOSED_OPTION);
                    //optionPane.setValue(new Integer(JOptionPane.CLOSED_OPTION));
                    optionPane.setValue(Integer.valueOf(JOptionPane.CLOSED_OPTION));
            }
        });

        //Register an event handler that reacts to option pane state changes.
        optionPane.addPropertyChangeListener(this);
	}
    /** getIniValue */
    public int getIniValue(Wini inifile, String sectionID, String key) {
    	try {
        	int val = inifile.get(sectionID, key, int.class);
        	return val; // returns 0 if section/key doesn't exist
    	}
		catch(Exception e) {
		  	e.printStackTrace();
    		System.out.println("Error Getting Ini Value, Section: '" + sectionID
        			+ "', Key: '" + key + "'");
	    	return 0;
	    }
    }
    /** getIniValue */
    public String getIniValueS(Wini inifile, String sectionID, String key) {
    	try {
    		String val = inifile.get(sectionID, key, String.class);
        	return val; 
    	}
		catch(Exception e) {
		  	e.printStackTrace();
    		System.out.println("Error Getting Ini String, Section: '" + sectionID
    			+ "', Key: '" + key + "'");
	    	return null;
	    }
    }
    
    /** setIniValue */
    public int setIniValue(Wini inifile, String sectionID, String key, int val) {
    	try{
    		//System.out.println("Setting Ini Section: " + sectionID
    		//	+ "Key: " + key
			//	+ "Value: " + val );	
	    	inifile.put(sectionID, key, val);
	    	inifile.store();
	    	return 1;
	    }
		catch(IOException e) {
		  	e.printStackTrace();
    		System.out.println("Error Setting Ini Section: '" + sectionID
    			+ "', Key: '" + key
				+ "', Value: '" + val + "'");
	    	return 0;
   		}
     }         
    /** setIniValue */
    public int setIniValue(Wini inifile, String sectionID, String key, String val) {
    	try{
	    	inifile.put(sectionID, key, val);
	    	inifile.store();
	    	return 1;
	    }
		catch(IOException e) {
		  	e.printStackTrace();
    		System.out.println("Error Setting Ini Section: '" + sectionID
        			+ "', Key: '" + key
    				+ "', Value: '" + val + "'");
	    	return 0;
   		}
     }
    
    /** ConfigureSliders */
    public void ConfigureSliders(String type, String sectionID) {
    	minString.setVisible(true);
        minSlider.setVisible(true);
        maxString.setVisible(true);
        maxSlider.setVisible(true);
        currSlideValue.setVisible(false);
        initDlg = true;
        
    	//System.out.println("ConfigureSliders Ini Section: " + sectionID);
 
        if( type.equals( "Time" ) ){
			minHour = getIniValue( BizRulesIni, sectionID, "minHour" );
			maxHour = getIniValue( BizRulesIni, sectionID, "maxHour" );
        	sliderType = TIME_TYPE;
        	//System.out.printf("Configure for Time.\n");
        	minString.setText("Start Hour:(" + Integer.toString(minHour) + ")" );
        	minSlider.setMinimum(0);
        	minSlider.setValue(minHour);
        	minSlider.setMaximum(23);
            minSlider.setMinorTickSpacing(1);
            minSlider.setMajorTickSpacing(0);

        	maxString.setText("End Hour:(" + Integer.toString(maxHour) + ")" );
        	maxSlider.setMinimum(0);
         	maxSlider.setValue(maxHour);
        	maxSlider.setMaximum(23);
        	maxSlider.setMinorTickSpacing(1);
            maxSlider.setMajorTickSpacing(0);
        }
        else if( type.equals( "Temperature" )){
			minTemp = getIniValue( BizRulesIni, sectionID, "minTemp" );
			maxTemp = getIniValue( BizRulesIni, sectionID, "maxTemp" );
        	sliderType = TEMP_TYPE;
        	//System.out.printf("Configure for Temp.\n");
        	minString.setText("Minimum Temperature:(" + Integer.toString(minTemp) + ")" );
         	minSlider.setMinimum(32);
        	minSlider.setValue(minTemp);
        	minSlider.setMaximum(64);
            minSlider.setMinorTickSpacing(2);
            minSlider.setMajorTickSpacing(0);
        	
           	maxString.setText("Maximum Temperature:(" + Integer.toString(maxTemp) + ")" );
         	maxSlider.setMinimum(74);
         	maxSlider.setValue(maxTemp);
         	maxSlider.setMaximum(100);
         	maxSlider.setMinorTickSpacing(2);
            maxSlider.setMajorTickSpacing(0);
       }
        else if( type.equals( "Requests" )){
			numReq = getIniValue( BizRulesIni, sectionID, "numReq" );
        	sliderType = REQ_TYPE;
        	//System.out.printf("Configure for Requests.\n");
        	minString.setVisible(false);
        	minSlider.setVisible(false);
        	maxString.setText("Maximum # of Request per day:(" + Integer.toString(numReq) + ")" );
        	maxSlider.setMinimum(0);
        	maxSlider.setValue(numReq);
        	maxSlider.setMaximum(100);
        	maxSlider.setMinorTickSpacing(5);
        	maxSlider.setMajorTickSpacing(10);
    	}
    	else{
            System.out.printf("Invalid Configuration Option.\n");
            minString.setText("Invalid Configuration Option!");
            minSlider.setVisible(false);
            maxString.setVisible(false);
            maxSlider.setVisible(false);
    	}
    }
    
    /** This method reacts to state changes in the option pane(i.e., dialog SET button press). */
    public void propertyChange(PropertyChangeEvent e) {
        String prop = e.getPropertyName();

        if (isVisible()
        		&& (e.getSource() == optionPane)
        		&& (JOptionPane.VALUE_PROPERTY.equals(prop) ||
        				JOptionPane.INPUT_VALUE_PROPERTY.equals(prop))) {

            /* getValue returns the value the user has selected. UNINITIALIZED_VALUE implies the user has not yet
			 * made a choice, null means the user closed the window with out choosing anything. Otherwise the 
			 * returned value will be one of the options defined in this object,
             */
        	Object selectedValue = optionPane.getValue();

            if (selectedValue == JOptionPane.UNINITIALIZED_VALUE) {
                //ignore reset
                return;
            }

            optionPane.setValue(JOptionPane.UNINITIALIZED_VALUE);
            int retVal = ((Integer)selectedValue).intValue();
            currSlideValue.setText("");

        	//System.out.println("Selected Method '" + dlgParent.cfgdMethod + "' for Endpoint '" + dlgParent.cfgdEp + "'");
        	//String sectionID = dlgParent.cfgdEp + "_" + dlgParent.cfgdMethod;
        	String sectionID = dlgParent.cfgdEp + dlgParent.cfgdMethod;
           	//System.out.println("Ini Section: " + sectionID);
            switch (retVal) {            
	            case JOptionPane.OK_OPTION:
	                //System.out.printf("Dialog returned OK\n");
	                switch (sliderType) {
			            case TIME_TYPE:
			            	if( minVal >= maxVal ) {
				                currSlideValue.setText("Start Hour: " + minVal + " must be before End Hour: " + maxVal);
			            	}
			            	else {
			            		minHour = minVal;
			            		maxHour = maxVal;
			            		setIniValue( BizRulesIni, sectionID, "minHour", minHour );
			            		setIniValue( BizRulesIni, sectionID, "maxHour", maxHour );
			                    dlgParent.setLabel("Time Window for method '" + dlgParent.cfgdMethod + "' set to " + minHour + ":00 to " + maxHour + ":00." );
				                clearAndHide();
		            		}
			                break;
			            case TEMP_TYPE:
			            	if( minVal >= maxVal ) {
				                currSlideValue.setText("Start Temp: " + maxVal + " must be lower then End Temp: " + maxVal);
			            	}
			            	else {
			            		minTemp = minVal;
			            		maxTemp = maxVal;
			            		setIniValue( BizRulesIni, sectionID, "minTemp", minTemp );
			            		setIniValue( BizRulesIni, sectionID, "maxTemp", maxTemp );
			                    dlgParent.setLabel("Temperature Range for method '" + dlgParent.cfgdMethod + "' set to between " + minTemp + " and " + maxTemp + " degrees." );
				                clearAndHide();
			            	}
			                break;
			            case REQ_TYPE:
			            	numReq = maxVal;
			            	setIniValue( BizRulesIni, sectionID, "numReq", numReq );
		                    dlgParent.setLabel("Maximum Daily Requests for method '" + dlgParent.cfgdMethod + "' set to " + numReq + "." );
			                clearAndHide();
			                break;
			            default:
			                dlgParent.setLabel("Invalid Max Slider Value: " + maxVal);
	                		clearAndHide();
			                break;   
	                }	                
	                break;
	            case JOptionPane.CANCEL_OPTION:
	                dlgParent.setLabel("Operation Cancelled.");
	                clearAndHide();
	                break;
	            case JOptionPane.CLOSED_OPTION:
	                dlgParent.setLabel("Operation Cancelled.");
	                clearAndHide();
	                break;
	            default:
	                dlgParent.setLabel("Error: Dialog returned OTHER: %s\n");
	                                  //,optionPane.getValue());
	                clearAndHide();
	                break;   
            }
        }
    }

    /** This method clears the dialog and hides it. */
    public void clearAndHide() {
        setVisible(false);
    }            
} // BizRuleEditor

public class IdsEditor extends JPanel {
    private static final long serialVersionUID = 2L;
	private static final String newline = "\n";
	
	// chm - try sizing..
	private static final int PREF_W = 600;
	private static final int PREF_H = 300;
	
	
    JTextArea IdsLogPane;
    JTextArea LogLogPane;
    //Specify the look and feel to use.  Valid values:
    //null (use the default), "Metal", "System", "Motif", "GTK+"
    final static String LOOKANDFEEL = null;
    public String cfgdMethod = "";
    public String cfgdEp = "";
    
    JLabel label;
    ImageIcon icon;// = createImageIcon("resources/middle.gif");
    JFrame topFrame;
    String BizRuleTabTip = "Configure Business Rules";
    String NetWorkTabTip = "Configure Network";
    String LoggingTabTip = "Configure Logging";
    String IdsTabTip = "Configure IDS";
    BizRuleEditor bizRuleDlg;

    /** Creates the GUI shown inside the frame's content pane. */
    public IdsEditor(JFrame frame, boolean isDebug) {
        super(new BorderLayout());
    	/*String imgdir = "./";
    	if(isDebug) {
	    	System.out.println("Running in Debugger.");
	    	imgdir = "src/";
    	}
    	else {
			;//System.out.println("NOT Running in Debugger.");
    	}
        this.topFrame = frame;
        String img = imgdir + "resources/web.png";
       	File imageCheck = new File(img);
    	if(imageCheck.exists()) 
    	    ;//System.out.println("Image file found!");
    	else {
    	    System.out.println("Image file not found: "+img);
    	    System.out.println("Current Working Directory = " + System.getProperty("user.dir"));
    	    System.exit(-1);
    	    return;
    	}
    	try {
            var webIcon = new ImageIcon(img);
            this.topFrame.setIconImage(webIcon.getImage()); //  from JFrame
    	} catch (Exception ex) {
    		System.out.println(ex);
    	}
    	icon = createImageIcon(imgdir + "resources/middle.gif");
        */

        bizRuleDlg = new BizRuleEditor(frame, this);
        bizRuleDlg.pack();

        //Create the components.
        JPanel bizTabPanel = createBizRulesTab();
        //JPanel netTabPanel = createNetTab();
        JPanel idsTabPanel = createIdsTab();
        JPanel logTabPanel = createLogTab();
        label = new JLabel("Click the \"Set\" button"
                           + " to bring up the Corresponding Business Rule Editor.",
                           JLabel.CENTER);

        //Lay them out.
        Border padding = BorderFactory.createEmptyBorder(20,20,5,20);
        bizTabPanel.setBorder(padding);
        idsTabPanel.setBorder(padding);
        logTabPanel.setBorder(padding);
        //netTabPanel.setBorder(padding);

        JTabbedPane tabbedPane = new JTabbedPane();
        tabbedPane.addTab("Business Rules", null, bizTabPanel, BizRuleTabTip); //tooltip text
        tabbedPane.addTab("IDS", null, idsTabPanel,IdsTabTip);
        tabbedPane.addTab("Logging", null, logTabPanel, LoggingTabTip);
        //tabbedPane.addTab("Networking", null, netTabPanel, NetWorkTabTip);
        tabbedPane.addChangeListener(new ChangeListener() {
        	public void stateChanged(ChangeEvent e) {
        		//System.out.println("Tab: " + tabbedPane.getSelectedIndex());
 		    	switch(tabbedPane.getSelectedIndex())
		    	{
			    	case 0 :
			    		label.setText("Click the \"Set\" button"
			    				+ " to bring up the Corresponding Business Rule Editor.");
			    		break;
			    	case 1 :
       					label.setText("View or Specify Configuration File");
			    		break;
			    	case 2 :
       					label.setText("Click the \"Configure\" button"
                           + " to bring up the Logging Editor.");
			    		break;
			    	case 3 :
       					label.setText("Click the \"Configure\" button"
                           + " to bring up the Network Editor.");
			    		break;
			    }
        	}
	    });
        add(tabbedPane, BorderLayout.CENTER);
        add(label, BorderLayout.PAGE_END);
        label.setBorder(BorderFactory.createEmptyBorder(10,10,10,10));
    }

 // chm - try sizing..
    @Override
    public Dimension getPreferredSize() {
       return new Dimension(PREF_W, PREF_H);
    }
    
    /** Sets the text displayed at the bottom of the frame. */
    void setLabel(String newText) {
        label.setText(newText);
    }

    /** Returns an ImageIcon, or null if the path was invalid. */
    protected static ImageIcon createImageIcon(String path) {
        java.net.URL imgURL = IdsEditor.class.getResource(path);
        if (imgURL != null) {
            return new ImageIcon(imgURL);
        } else {
            System.err.println("Couldn't find file: " + path);
   	    	System.out.println("Current Working Directory = " + System.getProperty("user.dir"));
            return null;
        }
    }
    /*
     * Endpoint - Endpoint Name:
     * 	CB - Customer Billing
     *  CD - Connect Disconnect
     *  MR - Meter Reading
     *  OD - Outage Detection
     */
    /** Creates the panel shown by the first tab. */
    @SuppressWarnings("unchecked")
	private JPanel createBizRulesTab() {
        final int numButtons = 3;
        final int idxBizGroups = 0;
        final int idxEndPoints = 1;
        final int idxMethods = 2;
        final int numDropsies = idxMethods+1;

        JRadioButton[] radioButtons = new JRadioButton[numButtons];
		JComboBox<String>[] dropdowns = new JComboBox[numDropsies];
        String[] cmbolabels= {"Process Groups", "Endpoints", "Methods"};
        String[] bizgrps = new String[3];//= {"Metering Management", "Customer Billing", "Outage Management"};
        final int idxMetering = 0;
        final int idxCustomer = 1;
        final int idxOutage = 2;
        bizgrps[idxMetering] = "Metering Management";
        bizgrps[idxCustomer] = "Customer Billing";
        bizgrps[idxOutage] = "Outage Management";

        String[] MeteringEPs={"CD_Server", "MR_Server"};
        final int idxCD = 0;
        final int idxMR = 1;
        String[] CDMethods= {"GetCDSupportedMeters", "InitiateConnectDisconnect",
        					 "IsCDSupported", "SetCDDevicesDisabled", "SetCDDevicesEnabled"};
        String[] MRMethods= {"GetLatestMeterReadings", "GetMeterReadingsByBillingCycle",
        					 "GetEndDeviceEventsByMeterIDs"};

        String[] CustomerEPs={"CB_Server", "MDM_Server", "PG_Server"};
        final int idxCB = 0;
        final int idxMDM = 1;
        final int idxPG = 2;
        String[] CBMethods= {"ChangeCustomerData", "ChangeMeterData", "ChangeStreetLightData"};
        String[] MDMMethods= {"InitiateBillingDeterminants"};
        String[] PGMethods= {"ChangePaymentTransactions", "ChangeRecurringPaymentConfiguration", "ProcessPaymentTransactions"};
 
        String[] OutageEPs={"OD_Server"};
        final int idxOD = 0;
        String[] ODMethods= {"GetMeterIDsByEndDeviceStateTypes", "InitiateEndDevicePings"};

        final DefaultComboBoxModel<String> MeteringEPModel = new DefaultComboBoxModel<String>(MeteringEPs);
        final DefaultComboBoxModel<String> CDMethodModel = new DefaultComboBoxModel<String>(CDMethods);
        final DefaultComboBoxModel<String> MRMethodModel = new DefaultComboBoxModel<String>(MRMethods);

        final DefaultComboBoxModel<String> CustomerEPModel = new DefaultComboBoxModel<String>(CustomerEPs);
        final DefaultComboBoxModel<String> CBMethodModel = new DefaultComboBoxModel<String>(CBMethods);
        final DefaultComboBoxModel<String> MDMMethodModel = new DefaultComboBoxModel<String>(MDMMethods);
        final DefaultComboBoxModel<String> PGMethodModel = new DefaultComboBoxModel<String>(PGMethods);

        final DefaultComboBoxModel<String> OutageEPModel = new DefaultComboBoxModel<String>(OutageEPs);
        final DefaultComboBoxModel<String> ODMethodModel = new DefaultComboBoxModel<String>(ODMethods);
		
        final ButtonGroup group = new ButtonGroup();

        final JButton cfgButton = new JButton("Set");

        final String timeWinCommand = "timeWin";
        final String tempWinCommand = "tempWin";
        final String maxReqCommand  = "maxReq";
        
        radioButtons[0] = new JRadioButton("Time Window");
        radioButtons[0].setActionCommand(timeWinCommand);

        radioButtons[1] = new JRadioButton("Temperature Window");
        radioButtons[1].setActionCommand(tempWinCommand);

        radioButtons[2] = new JRadioButton("Maximum Requests");
        radioButtons[2].setActionCommand(maxReqCommand);

        for (int i = 0; i < numButtons; i++) {
            group.add(radioButtons[i]);
        }
        radioButtons[0].setSelected(true);
       
        dropdowns[idxBizGroups] = new JComboBox<String>(bizgrps);
        dropdowns[idxEndPoints] = new JComboBox<String>();
        dropdowns[idxMethods] = new JComboBox<String>();
        for (int i = 0; i < numDropsies; i++) {
        	dropdowns[i].setEditable(false);
        }
        // Handle BizGroup selection, populate with corresponding Endpoints
		dropdowns[idxBizGroups].setSelectedIndex(-1);
        //Alternatively, upon selection in the first combo you can rebuild the items in the 
        //second one manually, ie: using JComboBox methods removeAllItems() and addItem().
		dropdowns[idxBizGroups].addActionListener (new ActionListener () {
		    public void actionPerformed(ActionEvent e) {
		        if (bizgrps[idxMetering].equals(dropdowns[idxBizGroups].getSelectedItem())){
		            dropdowns[idxEndPoints].setModel(MeteringEPModel);    
		        } else if (bizgrps[idxCustomer].equals(dropdowns[idxBizGroups].getSelectedItem())){
		            dropdowns[idxEndPoints].setModel(CustomerEPModel);    
		        } else {// idxOutage
		            dropdowns[idxEndPoints].setModel(OutageEPModel);    
		        }
		        dropdowns[idxEndPoints].setEnabled(true);
		        dropdowns[idxEndPoints].setSelectedIndex(0);
		    }
		});
		
		// Handle Endpoint selection, populate with corresponding Methods
		dropdowns[idxEndPoints].addActionListener (new ActionListener () {
		    public void actionPerformed(ActionEvent e) {
		    	int bizIdx = dropdowns[idxBizGroups].getSelectedIndex();
		    	boolean bErr = false; 
		    	switch(bizIdx)
		    	{
			    	case idxMetering :
				        if (MeteringEPs[idxCD].equals(dropdowns[idxEndPoints].getSelectedItem())){
				            dropdowns[idxMethods].setModel(CDMethodModel);    
				        } else if (MeteringEPs[idxMR].equals(dropdowns[idxEndPoints].getSelectedItem())){
				            dropdowns[idxMethods].setModel(MRMethodModel);    
				        } else {
				        	setLabel("Meter Endpoint selection Error.");
				        	bErr = true;
				        }
			    		break;		    	
			    	case idxCustomer :
				        if (CustomerEPs[idxCB].equals(dropdowns[idxEndPoints].getSelectedItem())){
				            dropdowns[idxMethods].setModel(CBMethodModel);    
				        } else if (CustomerEPs[idxMDM].equals(dropdowns[idxEndPoints].getSelectedItem())){
				            dropdowns[idxMethods].setModel(MDMMethodModel);    
				        } else if (CustomerEPs[idxPG].equals(dropdowns[idxEndPoints].getSelectedItem())){
				            dropdowns[idxMethods].setModel(PGMethodModel);    
				        } else {
				        	setLabel("Customer Endpoint selection Error.");    
				        	bErr = true;
				        }
				        break;		    	
			    	case idxOutage :
				        if (OutageEPs[idxOD].equals(dropdowns[idxEndPoints].getSelectedItem())){
				            dropdowns[idxMethods].setModel(ODMethodModel);    
				        } else {
				        	setLabel("Outage Endpoint selection Error.");    
				        	bErr = true;
				        }
			    		break;		    	
			    	default:
			    		break;
		    	}
		    	if( !bErr )
		    	{
			        dropdowns[idxMethods].setEnabled(true);
			        dropdowns[idxMethods].setSelectedIndex(0);
			        cfgButton.setEnabled(true);
	
					int epIdx = dropdowns[idxEndPoints].getSelectedIndex();
					if( epIdx != -1)
						cfgdEp = dropdowns[idxEndPoints].getSelectedItem().toString();
	            	//System.out.println("Selected Endpoint: " + cfgdEp);
		        	//setLabel("Selected Endpoint: " + cfgdEp);
		    	}
		    }
		});

		// Handle method selection, save current method name
		dropdowns[idxMethods].addActionListener (new ActionListener () {
			public void actionPerformed(ActionEvent e) {
				int methIdx = dropdowns[idxMethods].getSelectedIndex();
				if( methIdx != -1)
					cfgdMethod = dropdowns[idxMethods].getSelectedItem().toString();
			}
		});

		
		// Handle 'Set' button
        cfgButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
            	//System.out.println("Selected Method '" + cfgdMethod + "' for Endpoint '" + cfgdEp + "'");
                String command = group.getSelection().getActionCommand();
                if (command == timeWinCommand)
                {
                	bizRuleDlg.ConfigureSliders( "Time", cfgdEp + cfgdMethod );
                	bizRuleDlg.setTitle("Time Constraint Configuration");
                    //setLabel("Time Window Set.");
                }
                else if (command == tempWinCommand)
                {
               		bizRuleDlg.ConfigureSliders( "Temperature", cfgdEp + cfgdMethod );
                	bizRuleDlg.setTitle("Temperature Constraint Configuration");
                } else if (command == maxReqCommand)
                {
               		bizRuleDlg.ConfigureSliders( "Requests", cfgdEp + cfgdMethod );
                	bizRuleDlg.setTitle("Maximum Daily Request Configuration");
                }
                bizRuleDlg.setLocationRelativeTo(topFrame);
                bizRuleDlg.setVisible(true);
                return;
            }
        });

        return createBizPanel(radioButtons, cfgButton, dropdowns, cmbolabels);
    }

    /**
     * Used by createBizRulesTab
     * to create a pane containing a description, a single column of radio buttons, 
     * a single row of combo boxes and the set button.
		https://docs.oracle.com/javase/tutorial/uiswing/layout/groupExample.html 
        https://docs.oracle.com/javase/tutorial/uiswing/layout/group.html
     */
    private JPanel createBizPanel(JRadioButton[] radioButtons, JButton setButton, 
    						  JComboBox<String>[] dropdowns, String[] cmbolabels) {
        int numChoices = radioButtons.length;
        JPanel radioPanel = new JPanel();
		radioPanel.setBorder(BorderFactory.createTitledBorder("Business Rules:"));
        radioPanel.setLayout(new BoxLayout(radioPanel, BoxLayout.PAGE_AXIS));// LINE_AXIS
        for (int i = 0; i < numChoices; i++) {
            radioPanel.add(radioButtons[i]);
        }

        JLabel label1 = new JLabel(cmbolabels[0]);
        JLabel label2 = new JLabel(cmbolabels[1]);
        JLabel label3 = new JLabel(cmbolabels[2]);

		JPanel topPanel;
        topPanel = new JPanel();
        topPanel.setLayout(new BoxLayout(topPanel, BoxLayout.LINE_AXIS));// X_AXIS
        boolean MULTICOLORED = false; // false;
        if (MULTICOLORED) {
            topPanel.setOpaque(true);
            topPanel.setBackground(new Color(255, 0, 0));
        	topPanel.setBorder(BorderFactory.createEmptyBorder(5,5,5,5));
       }
 		topPanel.add(radioPanel);   	
    	topPanel.add(Box.createRigidArea(new Dimension(30, 0))); // invisible, empty space    
		setButton.setPreferredSize(new Dimension(120, 40));
		setButton.setMaximumSize(new Dimension(120, 40));
		setButton.setMinimumSize(new Dimension(120, 40));
		setButton.setEnabled(false);
		topPanel.add(setButton);

        JPanel cmbPanel = new JPanel();
        GroupLayout layout = new GroupLayout(cmbPanel);
        layout.setAutoCreateGaps(true);
        layout.setAutoCreateContainerGaps(false); // no border gaps so aligns with combo panel
        
        cmbPanel.setLayout(layout);
        dropdowns[1].setEnabled(false);
        dropdowns[2].setEnabled(false);
		// addComponent(Component component, int min, int pref, int min)
        layout.setHorizontalGroup(layout.createSequentialGroup()
         		.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
        				.addComponent(label1, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        				.addComponent(dropdowns[0], 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
         		.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
        				.addComponent(label2, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        				.addComponent(dropdowns[1], 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
         		.addGroup(layout.createParallelGroup(GroupLayout.Alignment.LEADING)
        				.addComponent(label3, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        				.addComponent(dropdowns[2], 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        		);
		layout.setVerticalGroup(layout.createSequentialGroup()
		      .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
		           .addComponent(label1)
		           .addComponent(label2)
		           .addComponent(label3))
		      .addGroup(layout.createParallelGroup(GroupLayout.Alignment.BASELINE)
		           .addComponent(dropdowns[0])
		           .addComponent(dropdowns[1])
		           .addComponent(dropdowns[2]))
		);
		
		Dimension cmb1sz = dropdowns[0].getPreferredSize();
		dropdowns[1].setPreferredSize(cmb1sz);
		dropdowns[2].setPreferredSize(cmb1sz);
		//dropdowns[1].setMaximumSize(new Dimension(120, 40));
		//dropdowns[1].setMinimumSize(new Dimension(120, 40));
		
		JPanel bizPane;
        bizPane = new JPanel();
        bizPane.setLayout(new BoxLayout(bizPane, BoxLayout.Y_AXIS));
		bizPane.add(topPanel);
		bizPane.add(cmbPanel);
        return bizPane;
    }

    /** Creates the net panel */
    private JPanel createNetTab() {
        final int numButtons = 2;
        JRadioButton[] radioButtons = new JRadioButton[numButtons];
        final ButtonGroup group = new ButtonGroup();

        JButton cfgButton = null;

        final String netOption1 = "netOption1";
        final String netOption2 = "netOption2";

        radioButtons[0] = new JRadioButton("Net Configuration Option 1");
        radioButtons[0].setActionCommand(netOption1);

        radioButtons[1] = new JRadioButton("Net Configuration Option 2");
        radioButtons[1].setActionCommand(netOption2);

        for (int i = 0; i < numButtons; i++) {
            group.add(radioButtons[i]);
        }
        radioButtons[0].setSelected(true);

        cfgButton = new JButton("Configure");
 		cfgButton.setPreferredSize(new Dimension(40, 40));
		cfgButton.setMaximumSize(new Dimension(40, 40));
		cfgButton.setMinimumSize(new Dimension(40, 40));
        cfgButton.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
        		String command = group.getSelection().getActionCommand();
        		if (command == netOption1) {
        			JOptionPane optionPane = new JOptionPane(new JLabel("Under Construction",JLabel.CENTER));
        			JDialog dialog = optionPane.createDialog("Net Option 1");
        			dialog.setModal(true);
        			dialog.setVisible(true);  		
        			//JOptionPane.showMessageDialog(topFrame,	"TBD.",
        			//		"Net Option 1",JOptionPane.PLAIN_MESSAGE);
        		} else if (command == netOption2) {
         			JOptionPane optionPane = new JOptionPane(new JLabel("Under Construction",JLabel.CENTER));
        			JDialog dialog = optionPane.createDialog("Net Option 2");
        			dialog.setModal(true);
        			dialog.setVisible(true);  		
        		}
        	}
        });
        return createNetPanel(NetWorkTabTip + ":", radioButtons, cfgButton);
    }
 
    private JPanel createNetPanel(String description, JRadioButton[] radioButtons, JButton showButton)
    {

		int numChoices = radioButtons.length;
		JPanel radioPanel = new JPanel();
		JLabel label = new JLabel(description);
		
		radioPanel.setLayout(new BoxLayout(radioPanel, BoxLayout.PAGE_AXIS));
		radioPanel.add(label);
		
		for (int i = 0; i < numChoices; i++) {
			radioPanel.add(radioButtons[i]);
		}
		
		JPanel pane = new JPanel(new BorderLayout());
		pane.add(radioPanel, BorderLayout.PAGE_START);
		pane.add(showButton, BorderLayout.PAGE_END);
		return pane;
    }
 
    /*
     * Creates the IDS pane
     */
    private JPanel createIdsTab() {
        //JButton cfgButton = null;
        final JButton selectButton = new JButton("Select Configuration File Location...");
        final JButton viewButton = new JButton("View Configuration File");
 
        //Create the IdsLogPane first, because the action listeners
        //need to refer to it.
        IdsLogPane = new JTextArea(5,20);
        IdsLogPane.setMargin(new Insets(5,5,5,5));
        IdsLogPane.setEditable(false);
        JScrollPane logareaScrollPane = new JScrollPane(IdsLogPane);

        //Create a file chooser
        //fc = new JFileChooser();
        //System.out.println("Working Directory = " +  System.getProperty("user.dir"));
        //fc = new JFileChooser(System.getProperty(bizRuleDlg.CfgLocation));
        //Uncomment one of the following lines to try a different
        //file selection mode.  The first allows just directories
        //to be selected (and, at least in the Java look and feel,
        //shown).  The second allows both files and directories
        //to be selected.  If you leave these lines commented out,
        //then the default mode (FILES_ONLY) will be used.
        //
        //fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
        //fc.setFileSelectionMode(JFileChooser.FILES_AND_DIRECTORIES);
        selectButton.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
        		JFileChooser fc;
                fc = new JFileChooser(bizRuleDlg.CfgLocation);
                fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
                fc.setDialogTitle("Select Configuration File Folder");
                int returnVal = fc.showOpenDialog(IdsEditor.this);
                if (returnVal == JFileChooser.APPROVE_OPTION){
                	String temp = fc.getSelectedFile().getAbsolutePath();
                	if( !bizRuleDlg.CfgLocation.equalsIgnoreCase(temp) ) {
                    	bizRuleDlg.CfgLocation = temp;
                    	bizRuleDlg.BizRulesCfg = bizRuleDlg.CfgLocation + File.separator + "BizRules.cfg";
                    	bizRuleDlg.setIniValue( bizRuleDlg.IdsCfgIni, "Settings", "ConfigLocation", 
                    							bizRuleDlg.CfgLocation );

                		try {
                    		File f = new File(bizRuleDlg.BizRulesCfg);
                			if(!f.exists()){
                				f.createNewFile();
                			}
                			bizRuleDlg.BizRulesIni = new Wini(f);
                		}
                		catch(Exception ex) {
                	    	System.out.println("ERROR Creating Business Rule File: " + bizRuleDlg.BizRulesCfg);
                		  	ex.printStackTrace();
                			System.exit(-1);
                			return;
                   		}
                    	IdsLogPane.append("\nIni file directory set to: " + bizRuleDlg.CfgLocation);
                	}
                	else {
                		IdsLogPane.append("\nIni file directory still: " + bizRuleDlg.CfgLocation);
                	}
                } else {
                    IdsLogPane.append("\nOperation cancelled by user." + newline);
                }
             };
        });

        viewButton.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
                int returnVal = JFileChooser.APPROVE_OPTION;
                if (returnVal == JFileChooser.APPROVE_OPTION) {
                    File file = new File(bizRuleDlg.BizRulesCfg);
                    IdsLogPane.setText("");
                	IdsLogPane.append("Ini file: " + bizRuleDlg.BizRulesCfg + ".\n");
                    try {
                    	StringBuffer buffer;
                	    buffer = new StringBuffer();
                	    FileReader reader=new FileReader(file);
                        int i=1;
                        while(i!=-1)
                        {
                            i=reader.read();
                            if( i != -1 ) {
	                            char ch=(char) i;
	                            buffer.append(ch);
                            }
                        }
                        reader.close();
                        IdsLogPane.append(buffer.toString());
                    } catch (FileNotFoundException ex) {
                        System.err.println("FileNotFoundException.");
                        ex.printStackTrace();
                    } catch (IOException ex) {
                        System.err.println("IOException.");
                        ex.printStackTrace();
                    }
                } else {
                    IdsLogPane.append("Operation cancelled by user." + newline);
                }
             };
        });
        return createIdsPanel(IdsTabTip + ":", selectButton, viewButton, logareaScrollPane);
    }
 
    private JPanel createIdsPanel(String description, JButton selectButton, JButton viewButton, JScrollPane logPane)
    {

        JPanel buttonPanel = new JPanel(); //use FlowLayout
        buttonPanel.add(selectButton);
        buttonPanel.add(viewButton);
    	
		JPanel pane = new JPanel(new BorderLayout());
		//pane.add(showButton, BorderLayout.PAGE_END);
		pane.add(buttonPanel, BorderLayout.PAGE_START);
		pane.add(logPane, BorderLayout.CENTER);

		return pane;
    }

     /*
      * Creates the logging panel
      */
    private JPanel createLogTab() {
        final JButton selectButton = new JButton("Select Log File Location...");
        final JButton viewButton = new JButton("View Log File");
 
        LogLogPane = new JTextArea(5,20);
        LogLogPane.setMargin(new Insets(5,5,5,5));
        LogLogPane.setEditable(false);
        JScrollPane logScrollPane = new JScrollPane(LogLogPane);

        selectButton.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
        		JFileChooser fc;
                fc = new JFileChooser(bizRuleDlg.LogLocation);
                fc.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
                fc.setDialogTitle("Select Log File Folder");
                int returnVal = fc.showOpenDialog(IdsEditor.this);
                if (returnVal == JFileChooser.APPROVE_OPTION){
                	String temp = fc.getSelectedFile().getAbsolutePath();
                	if( !bizRuleDlg.LogLocation.equalsIgnoreCase(temp) ) {
                    	bizRuleDlg.LogLocation = temp;
                    	bizRuleDlg.BizRulesLog = bizRuleDlg.LogLocation + File.separator + "srv_msp.log";
                    	bizRuleDlg.setIniValue( bizRuleDlg.BizRulesIni, "Settings", "LogFile", 
                    							bizRuleDlg.BizRulesLog );
                    	LogLogPane.append("\nLog file set to: " + bizRuleDlg.BizRulesLog);
                	}
                	else {
                		LogLogPane.append("\nLog file still: " + bizRuleDlg.BizRulesLog);
                	}
                } else {
                    LogLogPane.append("\nOperation cancelled by user." + newline);
                }
             };
        });

        viewButton.addActionListener(new ActionListener() {
        	public void actionPerformed(ActionEvent e) {
                int returnVal = JFileChooser.APPROVE_OPTION;
                if (returnVal == JFileChooser.APPROVE_OPTION) {
                    File file = new File(bizRuleDlg.BizRulesLog);
                    LogLogPane.setText("");
                	LogLogPane.append("Log file: " + bizRuleDlg.BizRulesLog + ".\n");
                    try {
                    	StringBuffer buffer;
                	    buffer = new StringBuffer();
                	    FileReader reader=new FileReader(file);
                        int i=1;
                        while(i!=-1)
                        {
                            i=reader.read();
                            if( i != -1 ) {
	                            char ch=(char) i;
	                            buffer.append(ch);
                            }
                        }
                        reader.close();
                        LogLogPane.append(buffer.toString());
                    } catch (FileNotFoundException ex) {
                        //System.err.println("FileNotFoundException.");
                        //ex.printStackTrace();
                        LogLogPane.append("Log file has not yet been created.\n");
                    } catch (IOException ex) {
                        System.err.println("IOException.");
                        ex.printStackTrace();
                    }
                } else {
                    LogLogPane.append("Operation cancelled by user." + newline);
                }
             };
        });
        return createLogPanel(IdsTabTip + ":", selectButton, viewButton, logScrollPane);
    }
 
    private JPanel createLogPanel(String description, JButton selectButton, JButton viewButton, JScrollPane logPane)
    {

        JPanel buttonPanel = new JPanel(); //use FlowLayout
        buttonPanel.add(selectButton);
        buttonPanel.add(viewButton);
    	
		JPanel pane = new JPanel(new BorderLayout());
		//pane.add(showButton, BorderLayout.PAGE_END);
		pane.add(buttonPanel, BorderLayout.PAGE_START);
		pane.add(logPane, BorderLayout.CENTER);

		return pane;
    }

	private static void initLookAndFeel() {
        String lookAndFeel = null;

        if (LOOKANDFEEL != null) {
            if (LOOKANDFEEL.equals("Metal")) {
                lookAndFeel = UIManager.getCrossPlatformLookAndFeelClassName();
            } else if (LOOKANDFEEL.equals("System")) {
                lookAndFeel = UIManager.getSystemLookAndFeelClassName();
            } else if (LOOKANDFEEL.equals("Motif")) {
                lookAndFeel = "com.sun.java.swing.plaf.motif.MotifLookAndFeel";
            } else if (LOOKANDFEEL.equals("GTK+")) { //new in 1.4.2
                lookAndFeel = "com.sun.java.swing.plaf.gtk.GTKLookAndFeel";
            } else {
                System.err.println("Unexpected value of LOOKANDFEEL specified: "
                                   + LOOKANDFEEL);
                lookAndFeel = UIManager.getCrossPlatformLookAndFeelClassName();
            }

            try {
                UIManager.setLookAndFeel(lookAndFeel);
            } catch (ClassNotFoundException e) {
                System.err.println("Couldn't find class for specified look and feel:"
                                   + lookAndFeel);
                System.err.println("Did you include the L&F library in the class path?");
                System.err.println("Using the default look and feel.");
            } catch (UnsupportedLookAndFeelException e) {
                System.err.println("Can't use the specified look and feel ("
                                   + lookAndFeel
                                   + ") on this platform.");
                System.err.println("Using the default look and feel.");
            } catch (Exception e) {
                System.err.println("Couldn't get specified look and feel ("
                                   + lookAndFeel
                                   + "), for some reason.");
                System.err.println("Using the default look and feel.");
                e.printStackTrace();
            }
        }
    }
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
	    boolean isDebug = java.lang.management.ManagementFactory.getRuntimeMXBean().
	    		getInputArguments().toString().indexOf("jdwp") >= 0;
        //Set the look and feel.
        initLookAndFeel();
        
        //Create and set up the window.
        JFrame frame = new JFrame("MultiSpeak Intrusion Detection Configurator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        //Create and set up the content pane.
        IdsEditor idsEditor = new IdsEditor(frame,isDebug);
        idsEditor.setOpaque(true); //content panes must be opaque
        frame.setContentPane(idsEditor);
        //frame.getContentPane().add(mainPanel);
        frame.pack();
        frame.setLocationByPlatform(true);
        frame.setVisible(true);
        
    }

    public static void main(String[] args) {
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                createAndShowGUI();
            }
        });
    }

}
