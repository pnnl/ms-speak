
public enum JReturn { 
	SUCCESS(0), FAIL(1), INIT_FAIL(2), INITXSD_FAIL(3), VALID8_FAIL(4), EXCEPTION(5); 
	private int value; 
	private JReturn(int value) 
	{
		this.value = value; 
	}
	public int value() 
	{
		return( this.value ); 
	}
};
