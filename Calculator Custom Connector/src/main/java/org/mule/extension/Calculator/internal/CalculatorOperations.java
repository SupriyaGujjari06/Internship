package org.mule.extension.Calculator.internal;

import static org.mule.runtime.extension.api.annotation.param.MediaType.ANY;

import org.mule.runtime.extension.api.annotation.param.MediaType;
import org.mule.runtime.extension.api.annotation.param.Config;
import org.mule.runtime.extension.api.annotation.param.Connection;


/**
 * This class is a container for operations, every public method in this class will be taken as an extension operation.
 */
public class CalculatorOperations {

  /**
   * Example of an operation that uses the configuration and a connection instance to perform some action.
   */


  /**
   * Example of a simple operation that receives a string parameter and returns a new string message that will be set on the payload.
   */
  @MediaType(value = ANY, strict = false)
  public int Calculator(int n1,int n2,String operator) {
	  if(operator.equals("add"))
		  return (n1+n2);
	  else if(operator.equals("sub"))
          return (n1-n2);
	  else if(operator.equals("mul"))
		  return (n1*n2);
	  else
		  return (n1/n2);
	  
  }

  /**
   * Private Methods are not exposed as operations
   */
 
}
