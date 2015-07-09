with    ada_io;        use     ada_io;
with    random_integer;


procedure bank is

  -- These 2 constants can be altered to change
  --  the behavior of the simulation
  number_of_tellers : constant integer := 4;
  number_of_customers : constant integer := 5;

  -- These 2 ranges can be altered to change
  --  the behavior of the simulation
  subtype transaction_time_range is integer range 1 .. 10;
  subtype time_between_visits_range is integer range 1 .. 100;

  -- Global types
  subtype money is integer range 0 .. integer'last;
  type status is ( success, insufficient_funds, bad_cust_id );
  subtype cust_id is integer range 0 .. number_of_customers;

  subtype teller_id is character;
  last_teller_id : teller_id := character'pred('A');

  -- Task specifications

  task type customer;           -- Requestor task type, no entries
  task type teller is
    -- Entries to do simple transactions and return status
    entry deposit ( id : cust_id; val : in  money; stat : out status );
    entry withdraw( id : cust_id; val : in  money; stat : out status );
    entry balance ( id : cust_id; val : out money; stat : out status );
  end teller;

  -- Arrays of tasks
  tellers : array( 1 .. number_of_tellers ) of teller;
  customers : array ( 1 .. number_of_customers ) of customer;

  task accounts_manager is
    -- Opens accounts, establishes new customer id's
    entry new_account( new_id : out cust_id );
  end accounts_manager;

  task bank_database is
    -- Maintains bank's internal data about open accounts and balances
    entry enter_cust_id ( id : cust_id );
    entry verify_cust_id( id : cust_id; legal  : out boolean );
    entry deposit       ( id : cust_id; amount : in  money   );
    entry withdraw      ( id : cust_id; amount : in  money   );
    entry balance       ( id : cust_id; amount : out money   );
  end bank_database;

  function next_teller_id return teller_id is
  begin
    last_teller_id := character'succ( last_teller_id );
    return last_teller_id;
  end;

  procedure put_secs( secs : integer ) is
  begin
    put( secs, 2 );  put( " second" );
    if secs = 1 then
      put( ' ' );
    else
      put( 's' );
    end if;
  end;

  task body teller is
    current_balance : money;
    valid   : boolean;
    last_id : cust_id;
    del     : integer;
    tel_id  : teller_id;

    function random_transaction_time return integer is
      length : constant integer := transaction_time_range'last -
				   transaction_time_range'first + 1;
    begin
      return (random_integer.next mod length) + transaction_time_range'first;
    end;

  begin
    put( "Teller - activation done" );  new_line;
    tel_id := next_teller_id;
    loop
      select                    -- Wait for any transaction request
	accept deposit( id : cust_id; val : in money; stat : out status ) do
	  last_id := id;
	  bank_database.verify_cust_id( id, valid );
	  if not valid then
	    stat := bad_cust_id;
	  else
	    bank_database.deposit( id, val );
	    stat := success;
	  end if;
	end deposit;
      or
	accept withdraw( id : cust_id; val : in money; stat : out status ) do
	  last_id := id;
	  bank_database.verify_cust_id( id, valid );
	  if not valid then
	    stat := bad_cust_id;
	  else
	    bank_database.balance( id, current_balance );
	    if current_balance < val then
	      stat := insufficient_funds;
	      put( "Account #" ); put( integer(id) ); put( " -" );
	      put( integer(val), 6 ); put( " = insufficient funds" ); new_line;
	    else
	      bank_database.withdraw( id, val );
	      stat := success;
	    end if;
	  end if;
	end withdraw;
      or
	accept balance( id : cust_id; val : out money; stat : out status ) do
	  last_id := id;
	  bank_database.verify_cust_id( id, valid );
	  if not valid then
	    stat := bad_cust_id;
	  else
	    bank_database.balance( id, val );
	    stat := success;
	  end if;
	end balance;
      end select;
      del := random_transaction_time;
      put( "Teller   " ); put( tel_id );
      put( " waits " ); put_secs( del );
      put( " after handling account #" );
      put( last_id ); new_line;
      delay duration(del);
      put( "Teller   " ); put( tel_id );
      put( " wait done" ); new_line;
    end loop;                   -- Simulate transaction time
  end teller;

  task body customer is
    -- Local type
    type transaction is ( deposit, withdraw, balance );

    subtype money_range is money range 1 .. 1000;

    -- Local variables
    id : cust_id;
    amount : money;
    stat : status;
    del : integer;

    function random_transaction return transaction is
      length : constant integer := transaction'pos(transaction'last) -
				   transaction'pos(transaction'first) + 1;
    begin
      return transaction'val( (random_integer.next mod length) +
			      transaction'pos(transaction'first) );
    end;

    function random_teller return integer is
    begin
      return (random_integer.next mod number_of_tellers) + 1;
    end;

    function random_amount return money is
      length : constant integer := money_range'last - money_range'first + 1;
    begin
      return money_range'val( (random_integer.next mod length) +
			      money_range'pos(money_range'first) );
    end;

    function random_time_between_visits return integer is
      length : constant integer := time_between_visits_range'last -
				   time_between_visits_range'first + 1;
    begin
      return (random_integer.next mod length) + time_between_visits_range'first;
    end;

  begin
    put( "Customer - activation done" );  new_line;
    accounts_manager.new_account( id );                 -- Get new cust id
    loop
      del := random_time_between_visits;
      put( "Account #" ); put( id );
      put( " waits " ); put_secs( del );  new_line;
      delay duration(del);
      put( "Account #" ); put( id );
      put( " wait done" ); new_line;
      case random_transaction is        -- Pick random transaction
	when deposit =>
	  tellers(random_teller).deposit ( id, random_amount, stat );
	when withdraw =>
	  tellers(random_teller).withdraw( id, random_amount, stat );
	when balance =>
	  tellers(random_teller).balance ( id, amount, stat );
      end case;
    end loop;
  end customer;

  task body accounts_manager is
    next : cust_id := 0;
  begin
    put( "Accounts_manager - activation done" );  new_line;
    next := 0;
    loop
      accept new_account( new_id : out cust_id ) do
	new_id := next;
	bank_database.enter_cust_id( next );
	next := next + 1;
      end new_account;
    end loop;
  end accounts_manager;

  task body bank_database is
    -- In real situations, more elaborate data structures are needed
    balances : array(cust_id) of money;
    valid_id : array(cust_id) of boolean := (others => false);
  begin
    put( "Bank_database - activation done" );  new_line;
    for vind in valid_id'range loop
      valid_id(vind) := false;
    end loop;
    loop
      select
	accept enter_cust_id( id : cust_id ) do
	  valid_id(id) := true;
	  balances(id) := 0;
	  put( "Account #" );  put( id );  put( " is now open" ); new_line;
	end enter_cust_id;
      or
	accept verify_cust_id( id : cust_id; legal : out boolean ) do
	  legal := valid_id(id);
	  put( "Account #" );  put( id );
	  if valid_id(id) then
	    put( " is valid" );
	  else
	    put( " is not valid" );
	  end if;
	  new_line;
	end verify_cust_id;
      or
	accept deposit( id : cust_id; amount : in money ) do
	  balances(id) := balances(id) + amount;
	  put( "Account #" );  put( id );
	  put( " +" ); put( integer(amount), 6 );
	  put( " = " );  put( integer(balances(id)), 5 ); new_line;
	end deposit;
      or
	accept withdraw( id : cust_id; amount : in money ) do
	  balances(id) := balances(id) - amount;
	  put( "Account #" );  put( id );
	  put( " -" ); put( integer(amount), 6 );
	  put( " = " );  put( integer(balances(id)), 5 ); new_line;
	end withdraw;
      or
	accept balance( id : cust_id; amount : out money ) do
	  amount := balances(id);
	  put( "Account #" );  put( id );
	  put( " balance = " );  put( integer(balances(id)), 5 ); new_line;
	end balance;
      end select;
    end loop;
  end bank_database;

begin   -- Main body of bank simulation
  -- Activation of customer and teller task collections
  --  and band_database and accounts_manager tasks occurs here.
  null;
  -- This program runs forever
  -- Procedure bank_simulation is completed but not terminated
end bank;
