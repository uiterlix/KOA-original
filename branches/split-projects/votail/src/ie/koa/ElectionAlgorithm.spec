 package ie.koa;

/**
 * This is a Java Modeling Language (JML) design specification of the vote counting 
 * algorithm for elections to Dail Eireann.
 * 
 * @author Dermot Cochran
 * @copyright Systems Research Group and University College Dublin, Ireland.
 * @reviewer Joe Kiniry
 * 
 * @design This JML specification and associated Java code is intended
 * to be checkable using ESC/Java2 (the Extended Static Checker for 
 * Java, version 2).
 * 
 * @see <a href="http://www.irishstatutebook.ie/1992_23.html">Part XIX of the 
 * Electoral Act, 1992</a>
 * @see Requirements for this specification are taken from 
 * <a href="http://www.cev.ie/htm/tenders/pdf/1_2.pdf">Department of 
 * Environment and Local Government, Commentary on Count 
 * Rules, sections 3-16, pages 12-65</a>
 * @see <a href="http://secure.ucd.ie/products/opensource/KOA/">The KOA Remote 
 * Voting System</a>
 * @see <a href="http://secure.ucd.ie/products/opensource/ESCJava2/">ESCJava/2 
 * Homepage</a>
 * @see <a href="http://www.jmlspecs.org/">JML Homepage</a>
 */

public class ElectionAlgorithm {
	
  /**  
   * Abstract State Machine for Election Algorithm.
   * @design 
   * The election count algorithm is modeled as an abstract state machine with state
   * values and transitions between those states. The normal path is: 
   * <p>
   * EMPTY --> SETUP --> PRELOAD --> LOADING --> PRECOUNT --> 
   * COUNTING --> FINISHED --> REPORT 
   * 
   */
  
   /** Start state */
   public static final byte EMPTY;
   /** Set up candidate list */
   public static final byte SETUP;
   /** Ready to load ballots */
   public static final byte PRELOAD;
   /** Load all valid ballots */
   public static final byte LOADING;
   /** Ready to count votes */
   public static final byte PRECOUNT;
   /** Count the votes */
   public static final byte COUNTING;
   /** Finished counting */
   public static final byte FINISHED;
   /** Declare election result */
   public static final byte REPORT;
 
   
  /*@ public model byte state;
    @ public invariant EMPTY < SETUP;
    @ public invariant SETUP < PRELOAD;
    @ public invariant PRELOAD < LOADING;
    @ public invariant LOADING < PRECOUNT;
    @ public invariant PRECOUNT < COUNTING;
    @ public invariant COUNTING < FINISHED;
    @ public invariant FINISHED < REPORT;
    @ public initially state == EMPTY;
    @ public constraint \old (state) <= state;
    @ public invariant (state == EMPTY) || (state == SETUP) || (state == PRELOAD) ||
    @   (state == LOADING) || (state == PRECOUNT) || (state == COUNTING) ||
    @   (state == FINISHED) || (state == REPORT);
    @*/
	
  /** List of decisions made */
  /*@ public model Decision[] decisionsMade;
    @ public invariant (\forall int i; 0 <= i && i < numberOfDecisions;  
    @   decisionsMade[i].decisionTaken != Decision.NODECISION &&
    @   decisionsMade[i].atCountNumber < countNumber && 
    @   (\exists int k; 0 <= k && k < totalCandidates;
    @      decisionsMade[i].candidateID == candidateList[k].getCandidateID()));
    @*/
	
  /** Number of decisions made */
  /*@ public model int numberOfDecisions;
    @ public initially numberOfDecisions == 0;
    @ public invariant 0 <= numberOfDecisions;
    @ public constraint \old (numberOfDecisions) <= numberOfDecisions;
    @ public constraint (state != COUNTING) ==> 
    @   numberOfDecisions == \old (numberOfDecisions);
    @*/
	
  /** List of details for each candidate. 
   * @constraint There are no duplicates in the list of candidate IDs and, once the 
   * counting starts, there must be a ballot paper associated with each vote
   * held by a candidate.
   */
  //@ public model non_null ie.koa.Candidate[] candidateList;
  /*@ public invariant (state == PRELOAD || state == LOADING || state == PRECOUNT) 
    @   ==> 
    @   (\forall int i; 0 <= i && i < totalCandidates;
    @   candidateList[i].getStatus() == Candidate.CONTINUING &&
    @   candidateList[i].getTotalVote() == 0 &&
    @   candidateList[i].getOriginalVote() == 0);
    @
    @ public invariant (state == PRELOAD || state == LOADING || state == PRECOUNT ||
    @   state == COUNTING || state == FINISHED || state == REPORT)
    @   ==>
    @   (\forall int i, j; 
    @     0 <= i && i < totalCandidates && i < j && j < totalCandidates;
    @     candidateList[i].getCandidateID() != candidateList[j].getCandidateID());
    @
    @ public invariant (state == PRELOAD || state == LOADING || state == PRECOUNT ||
    @   state == COUNTING || state == FINISHED || state == REPORT)
    @   ==>
    @   (\forall int i; 
    @     0 <= i && i < totalCandidates;
    @     candidateList[i].getCandidateID() != Ballot.NONTRANSFERABLE);
    @
    @ protected invariant (state == COUNTING || state == FINISHED || state == REPORT)
    @   ==> (\forall int i; 0 <= i && i < totalCandidates;
    @   candidateList[i].getTotalVote() == 
    @   getNumberOfVotes (candidateList[i].getCandidateID()));
    @*/
	
  /** List of contents of each ballot paper that will be counted. */
  //@ public model non_null ie.koa.Ballot[] ballotsToCount;
  /*@ public invariant (state >= PRECOUNT)
    @  ==>
    @  (\forall int i, j; 
    @     0 <= i && i < totalVotes && i < j && j < totalVotes;
    @     ballotsToCount[i].getBallotID() != ballotsToCount[j].getBallotID());
    @*/
	
  /** Total number of candidates for election */
  //@ public model int totalCandidates;
  //@ public invariant 0 <= totalCandidates;
  //@ public invariant totalCandidates <= candidateList.length;
  /*@ public constraint (state >= LOADING) ==> 
    @   totalCandidates == \old (totalCandidates);
    @ protected invariant (state == FINISHED) ==> totalCandidates == 
    @   numberElected + numberEliminated;
    @ public invariant (state == COUNTING) ==> 1 <= totalCandidates;
    @*/
	
  /** Number of candidates elected so far */
  //@ public model int numberElected;
  //@ public invariant 0 <= numberElected;
  //@ public invariant numberElected <= seats;
  /*@ public invariant (state <= PRECOUNT) ==> numberElected == 0;
    @ protected invariant (COUNTING <= state && state <= REPORT)
    @   ==> numberElected == (\num_of int i; 0 <= i && i < totalCandidates;
    @       isElected(candidateList[i]));
    @ public invariant (state == FINISHED || state == REPORT) ==> 
    @   numberElected == seats;
    @ public constraint (state == COUNTING) ==> 
    @   \old(numberElected) <= numberElected;
    @*/
	
	
  /** Number of candidates excluded from election so far */
  //@ protected model int numberEliminated;
  //@ protected invariant 0 <= numberEliminated;
  //@ protected invariant numberEliminated <= totalCandidates - seats;
  /*@ protected invariant (state == COUNTING || state == FINISHED || state == REPORT)
    @   ==> numberEliminated == (\num_of int i; 0 <= i && i < totalCandidates;
    @       candidateList[i].getStatus() == Candidate.ELIMINATED);
    @*/
	
  /** Number of seats to be filled in this election */
  //@ public model int seats;
  //@ public invariant 0 <= seats;
  //@ public invariant seats <= totalSeats;
  /*@ public constraint (state == LOADING || state == COUNTING) ==> 
    @   seats == \old (seats);
    @ public invariant (state == COUNTING) ==> 1 <= seats;
    @*/
	
  /** Total number of seats in this constituency
   * @design The consitution and laws of Ireland do not allow less than three or 
   *   more than five seats in each Dail constituency, but this could change in 
   *   future and is not an essential part of the specification.
   */
  //@ public model int totalSeats;
  //@ public invariant 0 <= totalSeats;
  /*@ public constraint (state == LOADING || state == COUNTING) ==> 
    @   totalSeats == \old (totalSeats);
    @*/
	
  /** Total number of valid votes in this election 
   * @design There is a theoretical maximum number of votes because there
   *   must be at least one seat for every thirty thousand electors, and therefore
   *   a maximum of 150,000 votes in a five seater constituency, but this also 
   *   could change and is not an essential part of the specification.  The Java 
   *   primitive type <code>int</code> has a maximum value of over two billion
   *   which should be sufficient for anything less than a worldwide election.
   */
  //@ public model int totalVotes;
  //@ public invariant 0 <= totalVotes;
  //@ public invariant totalVotes <= ballotsToCount.length;
  /*@ public invariant (state == EMPTY || state == SETUP || state == PRELOAD) 
	@   ==> totalVotes == 0;
    @ public constraint (state == LOADING) 
    @   ==> \old (totalVotes) <= totalVotes;
    @ public constraint (state == PRECOUNT || state == COUNTING || 
    @   state == FINISHED || state == REPORT) 
    @   ==> totalVotes == \old (totalVotes);
    @*/
	
  /** Number of votes so far which did not have a transfer to
   * a continuing candidate */
  //@ public model int nonTransferableVotes;
  //@ public invariant 0 <= nonTransferableVotes;
  //@ public invariant nonTransferableVotes <= totalVotes;
  /*@ public invariant (state == COUNTING || state == FINISHED || state == REPORT)
    @   ==> nonTransferableVotes == (\num_of int i; 0 <= i && i < totalVotes;
    @   ballotsToCount[i].candidateID == Ballot.NONTRANSFERABLE);
    @*/
	
  /** Minimum number of votes needed to guarantee election */
  //@ public model int quota;
  //@ public invariant 0 <= quota;
  //@ public invariant quota <= totalVotes;
  /** @see requirement 3, section 3, item 3, page 13 */
  /*@ public invariant (PRECOUNT < state) ==> 
    @   quota == 1 + (totalVotes / (seats + 1));
    @*/
	
  /** Minimum number of votes needed to save deposit unless elected */
  //@ public model int depositSavingThreshold;
  //@ public invariant 0 <= depositSavingThreshold;
  //@ public invariant depositSavingThreshold <= totalVotes;
  /** @see requirement 6, section 3, item 3, page 13 */
  /*@ invariant (PRECOUNT < state) ==> depositSavingThreshold == 
    @   (((totalVotes / (totalSeats + 1)) + 1) / 4) + 1;
    @*/
	
  /** Number of rounds of counting so far */
  //@ public model int countNumber;
  //@ public initially countNumber == 0;
  //@ public invariant 0 <= countNumber;
  //@ public invariant countNumber < Candidate.MAXCOUNT;
  //@ public constraint (state == COUNTING) ==> \old(countNumber) <= countNumber;
  /*@ public constraint (state == COUNTING) ==> 
    @   countNumber <= \old (countNumber) + 1;
    @*/
	
  /** Number of candidates with surplus votes */
  //@ public model int numberOfSurpluses;
  //@ public invariant 0 <= numberOfSurpluses;
  //@ public invariant numberOfSurpluses <= numberElected;
	
  /** Total number of undistributed surplus votes */
  //@ public model int sumOfSurpluses;
  //@ public invariant 0 <= sumOfSurpluses;
  //@ public invariant sumOfSurpluses <= totalVotes;
  /*@ invariant (state == COUNTING) ==> sumOfSurpluses == (\sum int i; 0 <= i && 
	@   i < totalCandidates; getSurplus(candidateList[i])); 
	@*/
	    
  /** Number of seats which remain to be filled */
  //@ public model int remainingSeats; 
  //@ public invariant 0 <= remainingSeats;
  //@ public invariant remainingSeats <= seats;
  //@ public invariant (state <= PRECOUNT) ==> remainingSeats == seats;
  /*@ public invariant (state == FINISHED || state == REPORT) ==> 
	@   remainingSeats == 0;
	@ public invariant (state == COUNTING) ==> 
	@   remainingSeats == (seats - numberElected);
	@*/
	
  /** Number of candidates neither elected nor excluded from election */
  //@ public model int numberOfContinuingCandidates;
  //@ public invariant 0 <= numberOfContinuingCandidates;
  //@ public invariant numberOfContinuingCandidates <= totalCandidates;
  //@ public invariant (state == FINISHED) ==> numberOfContinuingCandidates == 0;
  /*@ invariant (state == COUNTING) ==> numberOfContinuingCandidates == 
	@   (totalCandidates - numberElected) - numberEliminated;
	@*/
  /** There must be at least one continuing candidate for each remaining seat
   * @see requirement 11, section 4, item 4, page 16
   */
  /*@ invariant (state == COUNTING) ==>
    @   remainingSeats <= numberOfContinuingCandidates;
    @*/
	
  /** The lowest non-zero number of votes held by a continuing candidate 
   * @see requirement 13, section 4, item 4, page 17
   * */
  //@ public model int lowestContinuingVote;
  //@ public invariant 0 < lowestContinuingVote;
  /*@ public invariant  
    @   (\exists int k; 0 <= k && k < totalCandidates;  
	@   candidateList[k].getStatus() == Candidate.CONTINUING &&
	@   0 < candidateList[k].getTotalVote())
    @   ==> lowestContinuingVote == 
	@   (\min int i; 0 <= i && i < totalCandidates && 
	@   candidateList[i].getStatus() == Candidate.CONTINUING &&
	@   0 < candidateList[i].getTotalVote();
	@   candidateList[i].getTotalVote());
	@*/
 	
  /** The second lowest non-zero number of votes held by a continuing candidate */
  //@ public model int nextHighestVote;
  //@ public invariant lowestContinuingVote < nextHighestVote;
  /*@ public invariant  
    @   (\exists int k; 0 <= k && k < totalCandidates;  
	@   candidateList[k].getStatus() == Candidate.CONTINUING &&
	@   lowestContinuingVote < candidateList[k].getTotalVote()) 
	@   ==> nextHighestVote == 
    @   (\min int i; 0 <= i && i < totalCandidates && 
    @   candidateList[i].getStatus() == Candidate.CONTINUING &&
    @   lowestContinuingVote < candidateList[i].getTotalVote(); 
    @   candidateList[i].getTotalVote()); 
    @*/
	
  /** The highest number of votes held by a continuing candidate */
  //@ public model int highestContinuingVote;
  //@ public invariant highestContinuingVote < quota;
  /*@ public invariant (0 < numberOfContinuingCandidates)
    @   ==> highestContinuingVote == 
    @   (\max int i; 0 < i && i < totalCandidates && 
    @   candidateList[i].getStatus() == Candidate.CONTINUING; 
    @   candidateList[i].getTotalVote());   
    @*/
	
  /** Highest available surplus for distribution */
  //@ public model int highestSurplus;
  //@ public invariant 0 <= highestSurplus;
  //@ public invariant highestSurplus <= sumOfSurpluses;
  /*@ invariant (state == COUNTING) ==> highestSurplus ==
    @   (\max int i; 0 < i && i < totalCandidates; getSurplus (candidateList[i]));
    @*/
	
  /** Sum of continuing votes other than the highest */
  //@ public model int sumOfOtherContinuingVotes;
  //@ public invariant 0 <= sumOfOtherContinuingVotes;
  //@ public invariant sumOfOtherContinuingVotes <= totalVotes;
  /*@ invariant (state == COUNTING) ==> sumOfOtherContinuingVotes ==
	@   (\sum int i; 0 <= i && i < totalCandidates && 
	@   candidateList[i].getStatus() == Candidate.CONTINUING 
	@   && candidateList[i].getTotalVote() < highestContinuingVote; 
	@   candidateList[i].getTotalVote());
	@*/
	
  /** Number of candidates with equal highest continuing votes */
  //@ public model int numberOfEqualHighestContinuing;
  //@ public invariant 0 <= numberOfEqualHighestContinuing;
  /*@ public invariant 
    @   numberOfEqualHighestContinuing <= numberOfContinuingCandidates;
    @ public invariant (state == COUNTING) ==> numberOfEqualHighestContinuing == 
    @   (\num_of int i; 0 <= i && i < totalCandidates && 
    @   candidateList[i].getStatus() == Candidate.CONTINUING; 
    @   candidateList[i].getTotalVote() == highestContinuingVote);
    @*/
	
  /** Number of candidates with equal lowest non-zero votes */
  //@ public model int numberOfEqualLowestContinuing;
  //@ public invariant 0 <= numberOfEqualLowestContinuing;
  /*@ public invariant 
    @   numberOfEqualLowestContinuing <= numberOfContinuingCandidates; 
    @ public invariant (state == COUNTING) ==> numberOfEqualLowestContinuing == 
    @   (\num_of int i; 0 <= i && i < totalCandidates && 
    @   candidateList[i].getStatus() == Candidate.CONTINUING; 
    @   candidateList[i].getTotalVote() == lowestContinuingVote);
	@*/
  
	
  /** 
   * Determine if the candidate has received enough votes for election
   * 
   * @param candidate This candidate
   * @return True if the candidate has at least a quota of votes
   * @see "http://www.cev.ie/htm/tenders/pdf/1_1.pdf, page 79, paragraph 120 (2)"
   */
  /*@ requires candidate != null;
    @ requires countNumber >= 1;
    @ requires state == COUNTING;
    @ ensures \result == (candidate.getTotalVote() >= quota);
    @*/
  protected /*@ pure @*/ boolean hasQuota (ie.koa.Candidate candidate);

	
  /** 
   * Determine if the candidate has been elected
   * 
   * @design It is possible for a candidate without having reached the quota
   *   to be elected in the final round of counting by virtue of being the
   *   highest continuing candidate when one seat remains.
   *   
   * @see requirement 4, section 13, item 3, page 13
   * 
   * 
   * <p> The quota is the minimum number of votes needed for election, except 
   * when any of the following shortcuts apply.
   * <ul>
   * <li>The number of continuing candidates is equal to the number of remaining
   * seats.
   * <li>The number of continuing candidates is one more than the number of 
   * remaining seats.
   * <li>There is one remaining seat.
   * </ul>
   * 
   * @see <a href="http://www.cev.ie/htm/tenders/pdf/1_1.pdf">Department of Environment and Local Government, Electronic Vote Counting System, Appendix E</a>
   * @see <a href="http://www.cev.ie/htm/tenders/pdf/1_2.pdf">Department of Environment and Local Government, Count Requirements and Commentary on Count Rules, sections 3-14</a>
   * @see <a href="http://www.irishstatutebook.ie/1992_23.html">Sections 48, 118 and 124 of the Electoral Act, 1992</a>
   * 
   * @param candidate This candidate
   * @return True if the candidate has been elected
   */
  /*@ requires candidate != null;
    @ requires countNumber >= 1;
    @ requires state == COUNTING;
    @ ensures (\result == true) <==> 
    @   (candidate.getStatus() == Candidate.ELECTED || hasQuota(candidate));
    @*/
  protected /*@ pure @*/ boolean isElected (ie.koa.Candidate candidate);
	
	
  /** 
   * Determine how many surplus votes a candidate has.
   * 
   * The surplus is the maximum number of votes available for transfer
   * @see requirement 5, section 3, item 3, page 13
   *  
   * @param candidate The candidate record
   * @return The undistributed surplus for that candidate, or zero if the 
   * candidate has less than a quota of votes
   */
  /*@ requires state == COUNTING;
    @ requires candidate != null;
    @ requires 0 <= countNumber;
    @ ensures (hasQuota(candidate) == true) ==> \result == 
    @ (candidate.getTotalVote() - quota);
    @ ensures (hasQuota(candidate) == false) ==> \result == 0;
    @ ensures \result >= 0;
    @*/
  protected /*@ pure @*/ int getSurplus (ie.koa.Candidate candidate);
	
  /** 
   * Determines if a candidate has saved his or her deposit.
   * 
   * @design The deposit saving threshold is one plus one quarter of the full 
   * quota.<p>
   *   It is possible for a candidate without the deposit saving threshold
   *   to be elected in the final round of counting by virtue of being the
   *   highest continuing candidate when one seat remains.  This could happen,
   *   for example, if the majority of ballots contained only first preferences.
   *   
   * @see requirement 7, section 13, item 3, page 13
   * 
   * @param candidate This candidate
   * @return <code>true</code> if candidate has had enough votes to save deposit 
   * or has been elected
   */
  /*@ requires (state == COUNTING) || (state == FINISHED) || (state == REPORT);
    @ ensures \result == (candidate.getOriginalVote() >= depositSavingThreshold) ||
    @   (isElected (candidate) == true);
    @*/
  protected /*@ pure @*/ boolean isDepositSaved (/*@ non_null @*/ ie.koa.Candidate candidate);

	
  /** 
   * Distribution of surplus votes
   * 
   * @param candidateWithSurplus The candidate whose surplus is to be distributed
   * @design The highest surplus must be distributed if the total surplus 
   *   could save the deposit of a candidate or change the relative position 
   *   of the two lowest continuing candidates, or would be enough to elect the
   *   highest continuing candidate.
   * @see requirements 14-18, section 5, item 2, page 18
   * @see requirement 8, section 4, item 2, page 15
   */
  /*@ requires getSurplus (candidateWithSurplus) > 0;
    @ requires state == COUNTING;
    @ requires numberOfContinuingCandidates > remainingSeats;
    @ requires (numberOfContinuingCandidates > remainingSeats + 1) ||
    @   (sumOfSurpluses + lowestContinuingVote > nextHighestVote) ||
    @   (numberOfEqualLowestContinuing > 1);
    @ requires remainingSeats > 0;
    @ requires (remainingSeats > 1) ||
    @   ((highestContinuingVote < sumOfOtherContinuingVotes + sumOfSurpluses) &&
    @   (numberOfEqualHighestContinuing == 1));
    @ requires getSurplus (candidateWithSurplus) == highestSurplus;
    @ requires (sumOfSurpluses + highestContinuingVote >= quota) ||
    @   (sumOfSurpluses + lowestContinuingVote > nextHighestVote) ||
    @   (numberOfEqualLowestContinuing > 1) ||
    @   ((sumOfSurpluses + lowestContinuingVote >= depositSavingThreshold) &&
    @      (lowestContinuingVote < depositSavingThreshold));
    @ ensures getSurplus (candidateWithSurplus) == 0;
    @*/
  /** @see requirement 9, section 4, item 3, page 16 */
  /*@ ensures countNumber == \old (countNumber) + 1;
    @ ensures (state == COUNTING) || (state == FINISHED);
    @*/
  /** @see requirement 2, section 3, item 3, page 12 */
  /*@
    @ ensures totalVotes == nonTransferableVotes + 
    @   (\sum int i; 0 <= i && i < totalCandidates; 
    @   candidateList[i].getTotalVote());
    @*/
  protected void distributeSurplus(/*@ non_null @*/ 
                                ie.koa.Candidate candidateWithSurplus);
	
	
  /** 
   * Elimination of one or more candidates and transfer of votes
   * 
   * @param candidate This candidate
   * 
   * @design More than one candidate could be eliminated in the same round if the
   *   combined vote held by the group is not enough to elect a candidate or to
   *   save a deposit, and if there are no surplus votes available for distribution.
   * 
   * @see requirement 10, section 4, item 4, page 16
   * @see requirement 12, section 4, item 4, page 16
   */
  /*@ requires 1 <= numberToEliminate;
    @ requires numberToEliminate <= numberOfContinuingCandidates; 
    @ requires (\forall int i;
    @          0 <= i && i < numberToEliminate;
    @          candidatesToEliminate[i].getTotalVote() == 0 ||
    @          depositSavingThreshold <= candidatesToEliminate[i].getTotalVote() ||
    @          candidatesToEliminate[i].getTotalVote() + 
    @          sumOfSurpluses + (\sum int j;
    @            0 <= j && j != i && j < numberToEliminate;
    @            candidatesToEliminate[i].getTotalVote()) < depositSavingThreshold);
    @ requires (\forall int i;
    @          0 <= i && i < numberToEliminate;
    @          candidatesToEliminate[i].getStatus() == Candidate.CONTINUING);
    @ requires sumOfSurpluses + (\sum int i;
    @          0 <= i && i < numberToEliminate;
    @          candidatesToEliminate[i].getTotalVote()) < quota;
    @ requires remainingSeats < numberOfContinuingCandidates;
    @ requires (state == COUNTING);
    @ ensures (\forall int i;
    @          0 <= i && i < numberToEliminate;
    @          candidatesToEliminate[i].getStatus() == Candidate.ELIMINATED &&
    @          candidatesToEliminate[i].getTotalVote() == 0);
    @ ensures numberEliminated == \old (numberEliminated) + numberToEliminate;
    @ ensures remainingSeats <= numberOfContinuingCandidates;
    @ ensures numberElected <= seats;
    @ ensures \old(lowestContinuingVote) <= lowestContinuingVote;
    @*/
  protected void eliminateCandidates(
		  /*@ non_null @*/ Candidate[] candidatesToEliminate,
		  int numberToEliminate);
	
	
  /** 
   * Declare election results
   */
  /*@ requires state == FINISHED;
    @ assignable state;
    @ ensures state == REPORT;
    @*/
  public ElectionResults report();

	
  /**
   * Set up candidate details and number of seats
   */
  /*@ requires state == EMPTY;
    @ ensures state == PRELOAD;
    @ ensures totalCandidates == electionDetails.numberOfCandidates;
    @ ensures seats == electionDetails.numberOfSeatsInThisElection;
    @ ensures totalSeats == electionDetails.totalNumberOfSeats;
    @ assignable state, seats, totalSeats, totalCandidates, candidateList;
    @*/
  public void setup (ElectionDetails electionDetails);
	
	
  /** Loads all valid ballot papers */
  // @constraint All ballot papers must be assigned to a valid candidate ID
  /*@ requires state == PRELOAD;
    @ assignable state, totalVotes, ballotsToCount, quota, depositSavingThreshold;
    @ ensures state == PRECOUNT;
    @ ensures totalVotes == ballotBox.numberOfBallots;
    @ ensures (\forall int i; 0 <= i && i < totalVotes;
    @   (\exists int j; 0 <= j && j < totalCandidates;
    @      ballotsToCount[j].isAssignedTo(candidateList[i].getCandidateID())));
    @*/
  public void load(BallotBox ballotBox);
	
	
  /**
   * Count the votes.
   *
   * @design This is the method that starts the counting process.
   * @see requirement 1, section 3, item 2, page 12
   */
  /*@ public normal_behavior 
    @   requires remainingSeats == seats;
    @   requires numberElected == 0;
    @   requires nonTransferableVotes == 0;
    @   requires state == PRECOUNT;
    @   requires numberOfContinuingCandidates == totalCandidates;
    @   requires countNumber == 0;
    @   ensures state == FINISHED;
    @   assignable state, countNumber, numberElected,
    @   numberOfContinuingCandidates, remainingSeats, numberOfSurpluses, candidateList,
    @   sumOfSurpluses, highestContinuingVote, lowestContinuingVote,
    @   nextHighestVote, nonTransferableVotes, ballotsToCount, 
    @   numberOfContinuingCandidates;
    @   ensures remainingSeats == 0;
    @   ensures numberElected == seats;
    @   ensures numberOfContinuingCandidates == 0;
    @   ensures countNumber >= 0;
    @ also
    @   protected normal_behavior
    @   requires numberEliminated == 0; 
    @   assignable numberEliminated;
    @   ensures numberEliminated == totalCandidates - numberElected;
    @*/
  public void count();
  
  /**
   * Get the status of the algorithm in progress
   */
  /*@ ensures \result == state;
    @*/
  public /*@ pure @*/ byte getStatus();
  
  /**
   * Gets the current number of votes for this candidate ID
   * 
   * @design This method an also be used to check the number of nontransferable 
   * votes.
   * 
   * @param candidateID Candidate ID for which to check the votes.
   * @return Number of votes currently assigned to this candidate
   */
  /*@ requires (state == COUNTING || state == FINISHED || state == REPORT);
    @ requires 0 < candidateID || candidateID == Ballot.NONTRANSFERABLE;
    @ ensures \result== (\num_of int j; 0 <= j && j < totalVotes;
    @     ballotsToCount[j].isAssignedTo(candidateID));
    @*/
  protected /*@ pure @*/ int getNumberOfVotes (int candidateID);
  
  /**
   * Gets the potential number of transfers from one candidate to another.
   * 
   * @design This method is needed to get the proportions to use when transfering
   * surplus votes.  If the candidate was elected on the first count then all
   * votes are examined, otherwise only the last set of votes received are examined.
   * 
   * @see requirement 19, section 7, item 2, page 23
   * 
   * @param fromCandidate Candidate ID from which to check the transfers
   * @param toCandidateID Candidate ID to check for receipt of transfered votes
   * @return Number of votes potentially transferable from this candidate to that
   *   candidate
   */
  /*@ requires (state == COUNTING);
    @ requires 0 < toCandidateID;
    @ requires toCandidateID != Ballot.NONTRANSFERABLE;
    @ ensures \result== (\num_of int j; 0 <= j && j < totalVotes;
    @   (ballotsToCount[j].isAssignedTo(fromCandidate.getCandidateID())) &&
    @   (ballotsToCount[j].getCountNumberAtLastTransfer() ==
    @   fromCandidate.getLastSetAddedCountNumber()) && 
    @   (getNextContinuingPreference(ballotsToCount[j]) == toCandidateID));
    @*/
  protected /*@ pure @*/ int getPotentialTransfers (
		  /*@ non_null @*/ Candidate fromCandidate, int toCandidateID);
  
  /**
   * Get the maximum number of votes transferable to continuing candidates.
   * 
   * @see requirement 20, section 7, item 2, page 24
   * 
   * @param fromCandidate Candidate from which to check the transfers
   * @return Number of votes potentially transferable from this candidate
   */
  /*@ requires (state == COUNTING);
    @ ensures \result == (\sum int i; 0 <= i && i < totalCandidates;
    @   getPotentialTransfers (fromCandidate, candidateList[i].getCandidateID()));
    @*/
  protected /*@ pure @*/ int getTotalTransferableVotes (
		  /*@ non_null @*/ Candidate fromCandidate); 
  
  /**
   * Gets the next preference continuing candidate.
   * 
   * @design This is the _nearest_ next preference i.e.
   * filter the list of preferences to contain continuing candidates and then
   * get the next preference to a continuing candidate, if any.
   * 
   * @param ballot Ballot paper from which to get the next preference
   * 
   * @return Candidate ID of next continuing candidate or NONTRANSFERABLE
   */
  /*@ requires state == COUNTING;
    @ ensures (\result == Ballot.NONTRANSFERABLE) <=!=>
    @   (\exists int k; 1 <= k && k <= ballot.remainingPreferences(); 
    @     (\result == ballot.getNextPreference(k)) &&
    @     (\forall int i; 1 <= i && i < k;
    @       isContinuingCandidateID(ballot.getNextPreference(i)) == false)
    @   );
    @*/
  protected /*@ pure @*/ int getNextContinuingPreference(/*@ non_null @*/ Ballot ballot);
  
  /**
   * Determine actual number of votes to transfer to this candidate, excluding
   * rounding up of fractional transfers
   * 
   * @see requirement 21, section 7, item 3.1, page 24
   * @see requirement 22, section 7, item 3.2, page 25
   * 
   * @design The votes in a surplus are transfered in proportion to
   *   the number of transfers available throughout the candidates ballot stack.
   *   The calculations are made using integer values because there is no concept
   *   of fractional votes or fractional transfer of votes, in the existing manual
   *   counting system.  If not all transferable votes are accounted for the
   *   highest remainders for each continuing candidate need to be examined.
   * 
   * @param fromCandidate Candidate from which to count the transfers
   * @param toCandidate Continuing candidate eligible to receive votes
   * @return Number of votes to be transfered, excluding fractional transfers
   */
  /*@ requires (state == COUNTING);
    @ requires (fromCandidate.getStatus() == Candidate.ELECTED) ||
    @   (fromCandidate.getStatus() == Candidate.ELIMINATED);
    @ requires toCandidate.getStatus() == Candidate.CONTINUING;
    @ ensures ((fromCandidate.getStatus() == Candidate.ELECTED) && 
    @   (getSurplus(fromCandidate) < getTotalTransferableVotes(fromCandidate)))
    @   ==>
    @   (\result == 
    @               (getSurplus (fromCandidate) * 
    @               getPotentialTransfers (fromCandidate, 
    @                                     toCandidate.getCandidateID()) /
    @               getTotalTransferableVotes (fromCandidate)));
    @ ensures ((fromCandidate.getStatus() == Candidate.ELIMINATED) ||
    @   (getTotalTransferableVotes(fromCandidate) <= getSurplus (fromCandidate)))
    @    ==>
    @   (\result == 
    @     (\num_of int j; 0 <= j && j < totalVotes;
    @     ballotsToCount[j].isAssignedTo(fromCandidate.getCandidateID()) &&
    @     getNextContinuingPreference(ballotsToCount[j]) == 
    @     toCandidate.getCandidateID()));
    @*/
  protected /*@ pure @*/ int getActualTransfers (
		  /*@ non_null @*/ Candidate fromCandidate, 
		  /*@ non_null @*/ Candidate toCandidate);
  
  /**
   * Determine the rounded value of a fractional transfer.
   * 
   * @design This depends on the shortfall and the relative size of the 
   * other fractional transfers.
   * 
   * @see requirements 23-25, section 7, item 3.2, page 25
   *
   * @param fromCandidate
   *        Elected candidate from which to distribute surplus
   *        
   * @param toCandidate
   *        Continuing candidate potentially eligible to receive transfers
   *        
   * @return <code>1</code> if the fractional vote is to be rounded up
   *         <code>0</code> if the fractional vote is to be rounded down
   */
  /*@ requires state == COUNTING;
    @ requires isElected (fromCandidate); 
    @ requires toCandidate.getStatus() == ie.koa.Candidate.CONTINUING;
    @ requires getSurplus(fromCandidate) < 
    @   getTotalTransferableVotes(fromCandidate);
    @ ensures (getCandidateOrderByHighestRemainder 
    @   (fromCandidate, toCandidate) <=
    @   getTransferShortfall (fromCandidate))
    @   ==> \result == 1;
    @ ensures (getCandidateOrderByHighestRemainder 
    @   (fromCandidate, toCandidate) >
    @   getTransferShortfall (fromCandidate))
    @   ==> \result == 0;
    @*/
  protected /*@ pure @*/ int getRoundedFractionalValue (
		  /*@ non_null @*/ Candidate fromCandidate, 
		  /*@ non_null @*/ Candidate toCandidate);
  
  /**
   * Determine the number of continuing candidates with a higher remainder in
   * their transfer quotient, or deemed to have a higher remainder.
   * 
   * @design There must be a strict ordering of candidates for the purpose of
   * allocating the transfer shortfall.  If two or more candidates have equal
   * remainders then use the number of transfers they are about to receive and if 
   * the number of transfers are equal then look at the number of votes already
   * receieved.
   * 
   * @param fromCandidate
   *        Elected candidate from which to distribute surplus
   *        
   * @param toCandidate
   *        Continuing candidate potentially eligible to receive transfers
   *        
   * @return The number of continuing candidates with a higher quotient remainder
   *   than this candidate
   */
  /*@ requires state == COUNTING;
    @ requires isElected (fromCandidate); 
    @ requires toCandidate.getStatus() == ie.koa.Candidate.CONTINUING;
    @ requires getSurplus(fromCandidate) < getTotalTransferableVotes(fromCandidate);
    @ ensures \result == (\num_of int i; i <= 0 && i < totalCandidates &&
    @   candidateList[i].getCandidateID() != toCandidate.getCandidateID() &&
    @   candidateList[i].getStatus() == ie.koa.Candidate.CONTINUING;
    @   (getTransferRemainder(fromCandidate, candidateList[i]) > 
    @      getTransferRemainder(fromCandidate, toCandidate)) ||
    @   ((getTransferRemainder(fromCandidate, candidateList[i]) == 
    @      getTransferRemainder(fromCandidate, toCandidate)) &&
    @   (getActualTransfers(fromCandidate, candidateList[i]) >
    @   getActualTransfers(fromCandidate, toCandidate))) ||
    @   ((((getTransferRemainder(fromCandidate, candidateList[i]) == 
    @      getTransferRemainder(fromCandidate, toCandidate)) &&
    @   (getActualTransfers(fromCandidate, candidateList[i]) ==
    @   getActualTransfers(fromCandidate, toCandidate)))) &&
    @   isHigherThan (candidateList[i], toCandidate)));
    @*/
  protected /*@ pure @*/ int getCandidateOrderByHighestRemainder (
		  /*@ non_null @*/ Candidate fromCandidate, 
		  /*@ non_null @*/ Candidate toCandidate);
  
  /**
   * Determine if one continuing candidate is higher than another, for the purpose
   * of resolving remainders of transfer quotients.
   * 
   * @design This is determined by finding the earliest round of counting in which
   * these candidates had unequal votes.  If both candidates are equal at all counts
   * then random numbers are used to draw lots.
   * 
   * @see <a href="http://www.cev.ie/htm/tenders/pdf/1_2.pdf">Department of 
   * Environment and Local Government, Count Requirements and  Commentary on Count 
   * Rules, section 7, page 25</a>
   * 
   * @param firstCandidate
   *        The first of the two candidates to be compared
   * 
   * @param secondCandidate
   *        The second of the two candidates to be compared
   * 
   * @return <code>true</code> if first candidate is deemed to have received more
   *   votes than the second.
   */
  /*@ requires firstCandidate.getStatus() == Candidate.CONTINUING;
    @ requires secondCandidate.getStatus() == Candidate.CONTINUING;
    @ ensures \result == (\exists int i; 0 <= i && i < countNumber;
    @   (firstCandidate.getVoteAtCount(i) > secondCandidate.getVoteAtCount(i)) &&
    @   (\forall int j; 0 <= j && j < i;
    @   firstCandidate.getVoteAtCount(j) == secondCandidate.getVoteAtCount(j))) ||
    @   ((randomSelection (firstCandidate, secondCandidate) == 
    @     firstCandidate.getCandidateID()) && 
    @     (\forall int k; 0 <= k && k < countNumber;
    @     firstCandidate.getVoteAtCount(k) == secondCandidate.getVoteAtCount(k)));
    @*/
  protected /*@ pure @*/ boolean isHigherThan (
		  /*@ non_null @*/ Candidate firstCandidate,
		  /*@ non_null @*/ Candidate secondCandidate);
  
  /**
   * Draw lots to choose between two continuing candidates.
   * 
   * @design The offical guidelines suggest that the returning officer 
   * be asked to draw lots each time a random selection is required.  This
   * is simulated by having random numbers assigned to the candidates, so that
   * process of drawing lots is repeatable for testing purposes. <p> This means that
   * the count results are deterministic for any given set of random numbers.
   * 
   * @param firstCandidate
   *        The first of the two candidates to be compared
   * 
   * @param secondCandidate
   *        The second of the two candidates to be compared
   *        
   * @return The candidate ID of the chosen candidate
   */
  /*@ requires state == COUNTING;
    @ requires firstCandidate.getStatus() == Candidate.CONTINUING;
    @ requires secondCandidate.getStatus() == Candidate.CONTINUING;
    @ requires firstCandidate.randomNumber != secondCandidate.randomNumber;
    @ ensures (\result == firstCandidate.candidateID) <==>
    @   (firstCandidate.randomNumber < secondCandidate.randomNumber);
    @ ensures (\result == secondCandidate.candidateID) <==>
    @   (secondCandidate.randomNumber < firstCandidate.randomNumber);
    @*/
  protected /*@ pure @*/ int randomSelection (
		  /*@ non_null @*/ Candidate firstCandidate,
		  /*@ non_null @*/ Candidate secondCandidate);
  
  
  
  
  /**
   * Determine the indivisble remainder after integer division by the transfer 
   * factor for surpluses.
   * 
   * @design This can all be done with integer arithmetic; no need to use
   * floating point numbers, which could introduce rounding errors.
   * 
   * @param fromCandidate Elected candidate from which to count the transfers
   * @param toCandidate Continuing candidate eligible to receive votes
   * 
   * @return The size of the quotient remainder 
   */
  /*@ requires state == COUNTING;
    @ requires isElected (fromCandidate); 
    @ requires toCandidate.getStatus() == ie.koa.Candidate.CONTINUING;
    @ requires getSurplus(fromCandidate) < getTotalTransferableVotes(fromCandidate);
    @ requires 0 <= getTransferShortfall (fromCandidate);
    @ ensures \result == 
    @   getPotentialTransfers(fromCandidate, toCandidate.getCandidateID()) -
    @   ((getActualTransfers(fromCandidate, toCandidate) * 
    @     getTotalTransferableVotes (fromCandidate)) /
    @     getSurplus(fromCandidate)); 
    @*/
  protected /*@ pure @*/ int getTransferRemainder (
		  /*@ non_null @*/ Candidate fromCandidate, 
		  /*@ non_null @*/ Candidate toCandidate); 
  
  /**
   * Determine shortfall between sum of transfers rounded down and the size of
   * surplus.
   * 
   * @param fromCandidate
   *        Elected candidate from which to distribute surplus
   *        
   * @return The shortfall between the sum of the transfers and the size of surplus
   */
  /*@ protected normal_behavior
    @   requires state == COUNTING;
    @   requires isElected (fromCandidate); 
    @   requires getSurplus(fromCandidate) < getTotalTransferableVotes(fromCandidate);
    @   ensures \result == getSurplus (fromCandidate) - 
    @     (\sum int i; 0 <= i && i < totalCandidates &&
    @     candidateList[i].getStatus() == Candidate.CONTINUING;
    @     getActualTransfers (fromCandidate, candidateList[i]));
    @*/
  protected /*@ pure @*/ int getTransferShortfall (
		  /*@ non_null @*/ Candidate fromCandidate);
  
  /**
   * Determine if a candidate ID beints to a continuing candidate.
   * 
   * @param candidateID
   *        The ID of candidate for which to check the status
   *        
   * @return <code>true</code> if this candidate ID matches that of a
   *         caontinuing candidate
   */
  /*@ requires 0 < candidateID;
    @ ensures \result == (\exists int i;
    @   0 <= i && i < totalCandidates;
    @   candidateID == candidateList[i].getCandidateID() &&
    @   candidateList[i].getStatus() == Candidate.CONTINUING);
    */
  public /*@ pure @*/ boolean isContinuingCandidateID (int candidateID);
  
  /**
   * List each ballot ID in order by random number used to show how the votes have
   * been mixed and numbered.
   * 
   * @param ballot Ballot for which to get order of
   * @return Order of this ballot in numbered list of ballots
   */
  /*@
    @ requires state == REPORT;
    @ ensures 1 <= \result;
    @ ensures \result <= ballotsToCount.length;
    @ ensures (\forall Ballot a, b; a != null && b != null;
    @   (getOrder (a) < getOrder (b)) <==> (b.isAfter(a)));
    @*/
  protected /*@ pure @*/ int getOrder(/*@ non_null @*/ Ballot ballot);
  
  /**
   * List each candidate ID in order by random number to show how lots would be have
   * been chosen.
   * 
   * @param candidate Candidate for which to get the order of
   * @return Order of this candidate for use when lots are chosen
   */
  /*@
    @ requires state == REPORT;
    @ ensures 1 <= \result;
    @ ensures \result <= candidateList.length;
    @ ensures (\forall Candidate c, d; c != null && d != null;
    @   (getOrder (c) < getOrder (d)) <==> (d.isAfter(c)));
    @*/
  protected /*@ pure @*/ int getOrder(/*@ non_null @*/ Candidate candidate);
  
  /**
   * Transfer votes from one candidate to another.
   * @param fromCandidate Elected or excluded candidate 
   * @param toCandidate Continuing candidate
   * @param numberOfVotes Number of votes to be transfered
   */
  /*@ requires fromCandidate.getStatus() != Candidate.CONTINUING;
    @ requires toCandidate.getStatus() == Candidate.CONTINUING;
    @ requires numberOfVotes == getActualTransfers (fromCandidate, toCandidate) +
    @   getRoundedFractionalValue (fromCandidate, toCandidate);
    @ ensures fromCandidate.getTotalVote() == 
    @   \old (fromCandidate.getTotalVote()) - numberOfVotes;
    @ ensures toCandidate.getTotalVote() ==
    @   \old (toCandidate.getTotalVote()) + numberOfVotes;
    @*/
  protected void transferVotes(
		  /*@ non_null @*/ Candidate fromCandidate,
		  /*@ non_null @*/ Candidate toCandidate,
		  int numberOfVotes);
  
  /**
   * Update list of decision events.
   */
  /*@ requires state == COUNTING;
    @ ensures (\forall int i; 0 <= i && i < totalCandidates;
    @   isElected (candidateList[i]) ==> (\exists int k;
    @     0 <= k && k < numberOfDecisions;
    @     (decisionsMade[k].candidateID == candidateList[i].getCandidateID()) &&
    @     ((decisionsMade[k].decisionTaken == Decision.ELECTBYQUOTA) ||
    @       (decisionsMade[k].decisionTaken == Decision.DEEMELECTED))) &&
    @   (\forall int n; 0 <= n && n < numberOfDecisions;
    	@      (decisionsMade[n].candidateID  == candidateList[i].getCandidateID())
    	@      ==> (decisionsMade[n].decisionTaken != Decision.EXCLUDE))
    @   );
    @*/
  protected void updateDecisions();
}