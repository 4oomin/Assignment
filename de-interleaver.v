module DE_interleavr(Q,D,clk,rst_n);
output	[11:0]	Q;
input	[11:0]	D;
input		clk,rst_n;

wire	[10:0]  ptr_a,ptr_b,ptr_c,ptr_d,ptr_e,ptr_f;
wire 		wen_a,wen_b,wen_c,wen_d,wen_e,wen_f;
wire		csn_a,csn_b,csn_c,csn_d,csn_e,csn_f;
wire	[3:0]	mux;
wire	[11:0]	q_a,q_b,q_c,q_d,q_e,q_f;

ctrl	 u0( .ptr_a(ptr_a),.ptr_b(ptr_b),.ptr_c(ptr_c),.ptr_d(ptr_d),.ptr_e(ptr_e),.ptr_f(ptr_f),
	     .wen_a(wen_a),.wen_b(wen_b),.wen_c(wen_c),.wen_d(wen_d),.wen_e(wen_e),.wen_f(wen_f),
	     .csn_a(csn_a),.csn_b(csn_b),.csn_c(csn_c),.csn_d(csn_d),.csn_e(csn_e),.csn_f(csn_f),
	     .mux(mux),.clk(clk),.rst_n(rst_n));

SRAM_4	  u1( .q_a(q_a),.q_b(q_b),.q_c(q_c),.q_d(q_d),.q_e(q_e),.q_f(q_f),
	     .ptr_a(ptr_a),.ptr_b(ptr_b),.ptr_c(ptr_c),.ptr_d(ptr_d),.ptr_e(ptr_e),.ptr_f(ptr_f),
	     .wen_a(wen_a),.wen_b(wen_b),.wen_c(wen_c),.wen_d(wen_d),.wen_e(wen_e),.wen_f(wen_f),
	     .csn_a(csn_a),.csn_b(csn_b),.csn_c(csn_c),.csn_d(csn_d),.csn_e(csn_e),.csn_f(csn_f),
	     .d(D),.clk(clk),.rst_n(rst_n));


mux_out	  u2( .out(Q),.mux(mux),.q_a(q_a),.q_b(q_b),.q_c(q_c),.q_d(q_d),.q_e(q_e),.q_f(q_f));



endmodule



module ctrl( ptr_a,ptr_b,ptr_c,ptr_d,ptr_e,ptr_f,
	     wen_a,wen_b,wen_c,wen_d,wen_e,wen_f,
	     csn_a,csn_b,csn_c,csn_d,csn_e,csn_f,
	     mux,clk,rst_n);

input 		clk,rst_n;
output	[10:0]  ptr_a,ptr_b,ptr_c,ptr_d,ptr_e,ptr_f;
output 		wen_a,wen_b,wen_c,wen_d,wen_e,wen_f;
output		csn_a,csn_b,csn_c,csn_d,csn_e,csn_f;
output	[3:0]	mux;

reg	[3:0]   mux;
reg 	[14:0]  ptr;////////////////////////////////////////////////////////////
reg 	[2:0]   cycle;
always@(negedge clk )begin
		if(rst_n == 1'b1)begin
			mux<=4'd11;
			ptr<=15'd18431;///////////////////////////////////////////////////////////////////
			cycle<=3'd0 ;
		end else begin
			if(mux>=4'd11) mux <=4'd0;
			else mux<=mux+4'd1;
			/*if(ptr>=15'd18431) ptr <=15'd0;
			else ptr<=ptr +15'd1;*/
		end
		//if(ptr ==15'd0) cycle <= cycle + 3'd1;////////////////////////////////////////////////////////////
end

reg	[10:0]  ptr_a,ptr_b,ptr_c,ptr_d,ptr_e,ptr_f;
reg 		wen_a,wen_b,wen_c,wen_d,wen_e,wen_f;
reg		csn_a,csn_b,csn_c,csn_d,csn_e,csn_f;


always @(*)begin
		case(mux)
			4'd0:begin
				wen_a<=1'b0;
				csn_a<=1'b0;		
			  end
			4'd1:begin
				if(ptr_a == 11'd1535) ptr_a = 11'd0;
				else ptr_a=ptr_a+11'd1;
				wen_a<=1;
				csn_a<=0;
			  end

			4'd2:begin
				wen_b<=1'b0;
				csn_b<=1'b0;	
			  end
			4'd3:begin
				if(ptr_b == 11'd1535) ptr_b = 11'd0;
				else ptr_b=ptr_b+11'd1;
				wen_b<=1;
				csn_b<=0;
			  end
			
			4'd4:begin
				wen_c=1'b0;
				csn_c=1'b0;
				
			  end
			4'd5:begin
				if(ptr_c == 11'd1535) ptr_c = 11'd0;
				else ptr_c=ptr_c+11'd1;
				wen_c<=1'b1;
				csn_c<=1'b0;

			  end
			4'd6:begin
				wen_d=1'b0;
				csn_d=1'b0;
				
			  end
			4'd7:begin
				if(ptr_d == 11'd1535) ptr_d = 11'd0;
				else ptr_d=ptr_d+11'd1;
				wen_d<=1'b1;
				csn_d<=1'b0;
			  end
			4'd8:begin
				wen_e=1'b0;
				csn_e=1'b0;
				
			  end
			4'd9:begin
				if(ptr_e == 11'd1535) ptr_e = 11'd0;
				else ptr_e=ptr_e+11'd1;
				wen_e<=1'b1;
				csn_e<=1'b0;
			  end
			4'd10:begin
				wen_f=1'b0;
				csn_f=1'b0;
				
			  end
			4'd11:begin
				if(ptr_f == 11'd1535) ptr_f = 11'd0;
				else ptr_f=ptr_f+11'd1;
				wen_f<=1'b1;
				csn_f<=1'b0;
			  end
			default:begin
				   csn_a<=1'b1;
				   csn_b<=1'b1;
				   csn_d<=1'b1;
				   csn_d<=1'b1;
				   csn_e<=1'b1;
				   csn_f<=1'b1;
				end
		endcase
		
	
end

always @(*)begin
	case(cycle)
		3'd0:begin
			ptr_a=11'd0;
			ptr_b=11'd768;
			ptr_c=11'd1280;
			ptr_d=11'd256;
			ptr_e=11'd1024;
			ptr_f=11'd512;
		  end
		3'd1:begin
			ptr_a=11'd0;
			ptr_b=11'd0;
			ptr_c=11'd1024;
			ptr_d=11'd512;
			ptr_e=11'd512;
			ptr_f=11'd1024;
		  end
		3'd2:begin
			ptr_a=11'd0;
			ptr_b=11'd768;
			ptr_c=11'd768;
			ptr_d=11'd768;
			ptr_e=11'd0;
			ptr_f=11'd0;
		  end
		3'd3:begin
			ptr_a=11'd0;
			ptr_b=11'd0;
			ptr_c=11'd512;
			ptr_d=11'd1024;
			ptr_e=11'd1024;
			ptr_f=11'd512;
		  end
		3'd4:begin
			ptr_a=11'd0;
			ptr_b=11'd768;
			ptr_c=11'd256;
			ptr_d=11'd1280;
			ptr_e=11'd512;
			ptr_f=11'd1024;
		  end
		3'd5:begin
			ptr_a=11'd0;
			ptr_b=11'd0;
			ptr_c=11'd0;
			ptr_d=11'd0;
			ptr_e=11'd0;
			ptr_f=11'd0;
		  end
		
	endcase
end

endmodule

module mux_out(out,mux,q_a,q_b,q_c,q_d,q_e,q_f);
output	[11:0]	out;
input	[3:0]	mux;
input	[11:0]	q_a,q_b,q_c,q_d,q_e,q_f;

reg	[11:0]	out;
always@(*)begin
	case(mux)
		4'd0:out<=q_a;
		4'd2:out<=q_b;
		4'd4:out<=q_c;
		4'd6:out<=q_d;
		4'd8:out<=q_e;
		4'd10:out<=q_f;
		default:out<=out;
	endcase
end
endmodule


module SRAM_4(q_a,q_b,q_c,q_d,q_e,q_f,
	      ptr_a,ptr_b,ptr_c,ptr_d,ptr_e,ptr_f,
	      wen_a,wen_b,wen_c,wen_d,wen_e,wen_f,
	      csn_a,csn_b,csn_c,csn_d,csn_e,csn_f,
	      d,clk,rst_n);

output	[11:0]	q_a,q_b,q_c,q_d,q_e,q_f;

input	[10:0]  ptr_a,ptr_b,ptr_c,ptr_d,ptr_e,ptr_f;
input 		wen_a,wen_b,wen_c,wen_d,wen_e,wen_f;
input		csn_a,csn_b,csn_c,csn_d,csn_e,csn_f;
input	[11:0]  d;
input		clk,rst_n;


SRAM1536x12 u0
(
 .NWRT(wen_a),
 .DIN(d),
 .RA(ptr_a[10:3]),
 .CA(ptr_a[2:0]),
 .NCE(csn_a),
 .CK(clk),
 .DO(q_a) 
 );

SRAM1536x12 u1
(
 .NWRT(wen_b),
 .DIN(d),
 .RA(ptr_b[10:3]),
 .CA(ptr_b[2:0]),
 .NCE(csn_b),
 .CK(clk),
 .DO(q_b) 
 );

SRAM1536x12 u2
(
 .NWRT(wen_c),
 .DIN(d),
 .RA(ptr_c[10:3]),
 .CA(ptr_c[2:0]),
 .NCE(csn_c),
 .CK(clk),
 .DO(q_c) 
 );

SRAM1536x12 u3
(
 .NWRT(wen_d),
 .DIN(d),
 .RA(ptr_d[10:3]),
 .CA(ptr_d[2:0]),
 .NCE(csn_d),
 .CK(clk),
 .DO(q_d) 
 );

SRAM1536x12 u4
(
 .NWRT(wen_e),
 .DIN(d),
 .RA(ptr_e[10:3]),
 .CA(ptr_e[2:0]),
 .NCE(csn_e),
 .CK(clk),
 .DO(q_e) 
 );

SRAM1536x12 u5
(
 .NWRT(wen_f),
 .DIN(d),
 .RA(ptr_f[10:3]),
 .CA(ptr_f[2:0]),
 .NCE(csn_f),
 .CK(clk),
 .DO(q_f)  
 );

endmodule


// RAM Model
//  CSN : Chip Select Neg
//  WEN : Write Enable Neg
//  WEN=0, CSN=0: 00 WRITE
//  WEN=1, CSN=0: 10 READ 
//  WEN=1, CSN=1: 11 STOP 

//`define STIMULUS

module SRAM1536x12
    #(	parameter ADDRESSSIZE = 11,
	parameter ADDRESSBITSIZE = 1536,		    
        parameter WORDSIZE = 12)
(
 input NWRT,
 input [WORDSIZE-1:0] DIN,
 input [8-1:0] RA,
 input [3-1:0] CA,
 input NCE,
 input CK,
 output [WORDSIZE-1:0] DO 
 );

wire   [WORDSIZE-1:0] wDO;

spsram_hd_1536x12m6 SRAM_syn
(
.CK	(CK		),
.CSN	(NCE		),
.WEN	(NWRT		),
.OEN	(1'b0		),
.A	({RA,CA}	),
.DI	(DIN    	),
.DOUT	(wDO		));

assign DO = wDO ; 

endmodule

/*`ifdef STIMULUS*/

module spsram_hd_1536x12m6 
    #(	parameter ADDRESSSIZE = 11,
	parameter ADDRESSBITSIZE = 1536,		    
        parameter WORDSIZE = 12)
(
 input                      CK,
 input                      CSN,
 input                      WEN,
 input                      OEN,
 input [ADDRESSSIZE-1:0]    A,
 input [WORDSIZE-1:0]       DI,
 output [WORDSIZE-1:0]      DOUT
 );

 wire [WORDSIZE-1:0] wDOUT ;

SRAM SRAM1536x12 ( CK, DI, A, WEN, CSN, wDOUT );

assign DOUT = wDOUT ; 

endmodule



module SRAM
    #(	parameter ADDRESSSIZE = 11,
	parameter ADDRESSBITSIZE = 1536,		    
        parameter WORDSIZE = 12)
(
 input iClk,
 input [WORDSIZE-1:0] D,
 input [ADDRESSSIZE-1:0] A,
 input WEN, CSN, 
 output reg [WORDSIZE-1:0] Q
 );

	reg [WORDSIZE-1:0] Mem [0:ADDRESSBITSIZE-1];
	reg [WORDSIZE-1:0] Mem_in ;

	always @(*) begin
	Mem_in = Mem[A] ;
	end

	always @(posedge iClk )    begin

		if (!CSN && !WEN)  
		Mem[A] <= D;
		else if (!CSN && WEN)
		Q <= Mem_in;
		else
		Q <= Q;
	end

endmodule