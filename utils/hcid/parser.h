/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     K_OPTIONS = 258,
     K_DEVICE = 259,
     K_AUTOINIT = 260,
     K_SECURITY = 261,
     K_PAIRING = 262,
     K_OFFMODE = 263,
     K_DEVICEID = 264,
     K_PTYPE = 265,
     K_NAME = 266,
     K_CLASS = 267,
     K_VOICE = 268,
     K_PAGETO = 269,
     K_LM = 270,
     K_LP = 271,
     K_ISCAN = 272,
     K_PSCAN = 273,
     K_DISCOVTO = 274,
     K_PASSKEY = 275,
     K_YES = 276,
     K_NO = 277,
     WORD = 278,
     PATH = 279,
     STRING = 280,
     LIST = 281,
     HCI = 282,
     BDADDR = 283,
     ID = 284,
     NUM = 285
   };
#endif
/* Tokens.  */
#define K_OPTIONS 258
#define K_DEVICE 259
#define K_AUTOINIT 260
#define K_SECURITY 261
#define K_PAIRING 262
#define K_OFFMODE 263
#define K_DEVICEID 264
#define K_PTYPE 265
#define K_NAME 266
#define K_CLASS 267
#define K_VOICE 268
#define K_PAGETO 269
#define K_LM 270
#define K_LP 271
#define K_ISCAN 272
#define K_PSCAN 273
#define K_DISCOVTO 274
#define K_PASSKEY 275
#define K_YES 276
#define K_NO 277
#define WORD 278
#define PATH 279
#define STRING 280
#define LIST 281
#define HCI 282
#define BDADDR 283
#define ID 284
#define NUM 285




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 59 "parser.y"
{
	char *str;
	long  num;
}
/* Line 1489 of yacc.c.  */
#line 114 "parser.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

