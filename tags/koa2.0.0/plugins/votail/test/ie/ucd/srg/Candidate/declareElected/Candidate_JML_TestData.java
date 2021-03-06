/*******************************************************************************
 * Copyright (c) 2001, 2004 IBM Corporation and others.
 * All rights reserved. This program and the accompanying materials
 * are made available under the terms of the Eclipse Public License v1.0
 * which accompanies this distribution, and is available at
 * http://www.eclipse.org/legal/epl-v10.html
 * 
 * Contributors:
 *     IBM Corporation - initial API and implementation
 *******************************************************************************/
// This file was generated by jmlunit on Mon Apr 23 16:48:42 IST 2007.

package ie.koa;

import java.util.Random;

/** Supply test data for the JML and JUnit based testing of 
 *  Candidate.
 *
 *  <p>Test data is supplied by overriding methods in this class.  See
 *  the JML documentation and the comments below about how to do this.
 *
 *  <p>This class is also the place to override the <kbd>setUp()</kbd>
 *  and <kbd>tearDown()</kbd> methods if your testing needs some
 *  actions to be taken before and after each test is executed.
 *
 *  <p>This class is never rewritten by jmlunit.
 */
public abstract class Candidate_JML_TestData
    extends junit.framework.TestCase
{
    /** Initialize this class. */
    public Candidate_JML_TestData(java.lang.String name) {
        super(name);
    }

    /** Return the overall test suite for accumulating tests; the
     * result will hold every test that will be run.  This factory
     * method can be altered to provide filtering of test suites, as
     * they are added to this overall test suite, based on various
     * criteria.  The test driver will first call the method
     * addTestSuite to add a test suite formed from custom programmed
     * test methods (named testX for some X), which you can add to
     * this class; this initial test suite will also include a method
     * to check that the code being tested was compiled with jmlc.
     * After that, for each method to be tested, a test suite
     * containing tests for that method will be added to this overall
     * test suite, using the addTest method.  Test suites added for a
     * method will have some subtype of TestSuite and that method's
     * name as their name. So, if you want to control the overall
     * suite of tests for testing some method, e.g., to limit the
     * number of tests for each method, return a special-purpose
     * subclass of {@link junit.framework.TestSuite} in which you override the
     * addTest method.
     * @see junit.framework.TestSuite
     */
    //@ assignable objectState;
    //@ ensures \result != null;
    public junit.framework.TestSuite overallTestSuite() {
        return new junit.framework.TestSuite("Overall tests for Candidate");
    }

    /** Return an empty test suite for accumulating tests for the
     * named method.  This factory method can be altered to provide
     * filtering or limiting of the tests for the named method, as
     * they are added to the test suite for this method.  The driver
     * will add individual tests using the addTest method.  So, if you
     * want to filter individual tests, return a subclass of TestSuite
     * in which you override the addTest method.
     * @param methodName The method the tests in this suite are for.
     * @see junit.framework.TestSuite
     * @see org.jmlspecs.jmlunit.strategies.LimitedTestSuite
     */
    //@ assignable objectState;
    //@ ensures \result != null;
    public junit.framework.TestSuite emptyTestSuiteFor
        (java.lang.String methodName)
    {
        return new junit.framework.TestSuite(methodName);
    }

    // TEST DATA SUPPLY SECTION

    // You should edit the following code to supply test data.  In the
    // skeleton originally supplied below, the jmlunit tool made a
    // guess as to a minimal strategy for generating test data for
    // each type of object used as a receiver, and each type used as
    // an argument.  There is a library of strategies for generating
    // test data in org.jmlspecs.jmlunit.strategies, which are used in
    // the tool's guesses.  See the documentation for JML and in
    // particular for the org.jmlspecs.jmlunit.strategies package for
    // a general discussion of how to do this.  (This package's
    // documentation is available through the JML.html file in the top
    // of the JML release, and also in the package.html file that
    // ships with the package.)
    //
    // In the code below, you can change the strategies from those
    // that were guessed by the jmlunit tool, and you can also define
    // new ones to suit your needs.  You can also delete any useless
    // sample test data that has been generated for you to show you
    // the pattern of how to add your own test data.  The only
    // requirement is that you implement the methods below.
    //
    // If you change the type being tested in a way that introduces
    // new types of arguments for some methods, then you will have to
    // introduce (by hand) definitions that are similar to the ones
    // below, because jmlunit never rewrites this file.

    /** Return a new, freshly allocated indefinite iterator that
     * produces test data of type 
     * int
     * for testing the method named by the String methodName in
     * a loop that encloses loopsThisSurrounds many other loops.
     * @param methodName name of the method for which this
     *                      test data will be used.
     * @param loopsThisSurrounds number of loops that the test
     *                           contains inside this one.
     */
    //@ requires methodName != null && loopsThisSurrounds >= 0;
    //@ ensures \fresh(\result);
    protected org.jmlspecs.jmlunit.strategies.IntIterator
        vintIter
        (java.lang.String methodName, int loopsThisSurrounds)
    {
        return vintStrategy.intIterator();
    }

    /** The strategy for generating test data of type
     * int. */
    private org.jmlspecs.jmlunit.strategies.IntStrategyType
        vintStrategy
        = new org.jmlspecs.jmlunit.strategies.IntStrategy()
            {
                protected int[] addData() {
                    return new int[] {
                        // replace this comment with test data if desired
                    };
                }
            };

    /** Return a new, freshly allocated indefinite iterator that
     * produces test data of type 
     * long
     * for testing the method named by the String methodName in
     * a loop that encloses loopsThisSurrounds many other loops.
     * @param methodName name of the method for which this
     *                      test data will be used.
     * @param loopsThisSurrounds number of loops that the test
     *                           contains inside this one.
     */
    //@ requires methodName != null && loopsThisSurrounds >= 0;
    //@ ensures \fresh(\result);
    protected org.jmlspecs.jmlunit.strategies.LongIterator
        vlongIter
        (java.lang.String methodName, int loopsThisSurrounds)
    {
        return vlongStrategy.longIterator();
    }

    /** The strategy for generating test data of type
     * long. */
    private org.jmlspecs.jmlunit.strategies.LongStrategyType
        vlongStrategy
        = new org.jmlspecs.jmlunit.strategies.LongStrategy()
            {   Candidate candidate = new Candidate();
                long MAX_VALUE;
                protected long[] addData() {
                    return new long[] {
			0,1,candidate.MAXCOUNT-1,candidate.MAXCOUNT,MAX_VALUE-1,MAX_VALUE
                // replace this comment with test data if desired
                    };
                }
            };

    /** Return a new, freshly allocated indefinite iterator that
     * produces test data of type 
     * ie.koa.Candidate
     * for testing the method named by the String methodName in
     * a loop that encloses loopsThisSurrounds many other loops.
     * @param methodName name of the method for which this
     *                      test data will be used.
     * @param loopsThisSurrounds number of loops that the test
     *                           contains inside this one.
     */
    //@ requires methodName != null && loopsThisSurrounds >= 0;
    //@ ensures \fresh(\result);
    protected org.jmlspecs.jmlunit.strategies.IndefiniteIterator
        vie_koa_CandidateIter
        (java.lang.String methodName, int loopsThisSurrounds)
    {
        return vie_koa_CandidateStrategy.iterator();
    }

    /** The strategy for generating test data of type
     * ie.koa.Candidate. */
    private org.jmlspecs.jmlunit.strategies.StrategyType
        vie_koa_CandidateStrategy
        = new org.jmlspecs.jmlunit.strategies.NewObjectAbstractStrategy()
            {
                Candidate candidate = new Candidate();
		Candidate candidate2 = new Candidate();
		Candidate candidate3 = new Candidate();
		Candidate candidate4 = new Candidate();
		Candidate candidate5 = new Candidate();
		Candidate candidate6 = new Candidate();
		Candidate candidate7 = new Candidate();
		Candidate candidate8 = new Candidate();
	            protected Object make(int n) {
                    switch (n) {
		        case(1):  return candidate;
                        case(2):  candidate.setCandidateID(10);
			          return candidate;
		        case(3):  candidate.declareElected();
			          return candidate;
		        case(4):  return candidate.getState();
		        case(5):  candidate2.setCandidateID(11);
			          return candidate2;
		        case(6):  candidate2.declareElected();
			          return candidate2; 
                        case(7):  return candidate2.getState();
		        case(8):  candidate3.setCandidateID(12);
			          return candidate3;
		        case(9):  candidate3.declareElected();
			          return candidate3;
                        case(10): return candidate3.getState();
		        case(11): candidate4.setCandidateID(983);
			          return candidate4;
		        case(12): candidate4.declareElected();
                                  return candidate4; 
                        case(13): return candidate4.getState();
		        case(14): candidate5.setCandidateID(1);
			          return candidate5;
		        case(15): candidate5.declareElected();
			          return candidate5;
                        case(16): return candidate5.getState(); 
		        case(17): candidate6.setCandidateID(17636);
			          return candidate6;
		        case(18): candidate6.declareElected(); 
			          return candidate6;
                        case(19): return candidate6.getState();
		        case(20): candidate7.setCandidateID(2147483646);
			          return candidate7;
		        case(21): candidate7.declareElected();
                                  return candidate7;
                        case(22): return candidate7.getState(); 
		        case(23): candidate8.setCandidateID(2147483647);
			          return candidate8;
		        case(24): candidate8.declareElected(); 
			          return candidate8;
                        case(25): return candidate8.getState();
		           
                        		       
                        // replace this comment with test data if desired
                    default:
                        break;
                    }
                    throw new java.util.NoSuchElementException();
                }
            };
}
